import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Handle connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors
subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel
const channel = 'holberton school channel';
subscriber.subscribe(channel);

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  }
});
