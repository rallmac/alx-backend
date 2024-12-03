function createPushNotificationsJobs(jobs, queue) {
  // Validate input
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Process each job
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    // Handle job creation
    job
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    // Save the job to the queue
    job.save();
  });
}

export default createPushNotificationsJobs;
