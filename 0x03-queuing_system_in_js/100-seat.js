import express from 'express';
import kue from 'kue';
import { promisify } from 'util';
import redis from 'redis';

// Initialize Redis client
const client = redis.createClient();
const reserveSeat = promisify(client.set).bind(client);
const getCurrentAvailableSeats = promisify(client.get).bind(client);

// Initialize Kue queue
const queue = kue.createQueue();

// Express app
const app = express();
const PORT = 1245;

let reservationEnabled = true;

// Initialize available seats
const initializeSeats = async () => {
  await reserveSeat('available_seats', 50);
};
initializeSeats();

// Route: Get available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats('available_seats');
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route: Reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route: Process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats('available_seats');
    const seatsLeft = parseInt(currentSeats, 10) - 1;

    if (seatsLeft < 0) {
      done(new Error('Not enough seats available'));
    } else {
      await reserveSeat('available_seats', seatsLeft);

      if (seatsLeft === 0) {
        reservationEnabled = false;
      }

      done();
    }
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
