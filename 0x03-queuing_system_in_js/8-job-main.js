import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Create a queue
const queue = kue.createQueue();

// Sample jobs list
const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

// Add jobs to the queue
createPushNotificationsJobs(list, queue);
