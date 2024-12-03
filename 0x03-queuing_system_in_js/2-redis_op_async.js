import redis from 'redis';
import { promisify } from 'util';

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

// Promisify the `get` method to use with async/await
const getAsync = promisify(client.get).bind(client);

// Function to set a value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print); // redis.print logs the reply (e.g., "Reply: OK")
}

// Async function to display the value of a key in Redis
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

// Call the functions
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
