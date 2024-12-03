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

// Function to set a value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print); // redis.print logs the reply (e.g., "Reply: OK")
}

// Function to display the value of a key in Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
      return;
    }
    console.log(reply);
  });
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
