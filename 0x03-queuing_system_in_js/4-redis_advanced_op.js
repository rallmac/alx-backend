import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Listen for the `connect` event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the `error` event
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Store a hash using `hset`
const hashKey = 'HolbertonSchools';
client.hset(hashKey, 'Portland', '50', redis.print);
client.hset(hashKey, 'Seattle', '80', redis.print);
client.hset(hashKey, 'New York', '20', redis.print);
client.hset(hashKey, 'Bogota', '20', redis.print);
client.hset(hashKey, 'Cali', '40', redis.print);
client.hset(hashKey, 'Paris', '2', redis.print);

// Display the hash using `hgetall`
client.hgetall(hashKey, (err, reply) => {
  if (err) {
    console.error(`Error fetching hash ${hashKey}: ${err.message}`);
    return;
  }
  console.log(reply);
});
