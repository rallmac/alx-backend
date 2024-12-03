import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// Handle connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Publish messages to the channel
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
};

// Send messages
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
