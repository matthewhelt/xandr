# Xandr Coding Test Submission

## Usage

   * Ensure no other services are using port 5000 for this test (use <code>netstat -ltnp | grep -w '5000'</code> to determine if docker has already bound the port)
   * Clone this repo into a directory
   * In that directory, run this command <code>sudo docker build -t test .</code>
   * You will now have a docker image named <code>test:latest</code> if the previous command is successfull, it's time to start the container
   * Start up command is <code>docker run -d -p 5000:5000 test</code>, you may need to use sudo
   * If no errors have been encountered, the service should now be running locally on port 5000.
   
## Test

  * GET request to <code>localhost:5000/</code> should return a JSON object with all the employee records
  * GET request to <code>localhost:5000/1</code> should return a JSON object with the single employee record with ID 1
  * PUT request to <code>localhost:5000/1</code> should increase the field 'salary' by 5% which should be immediately reflected in any subsequent GET request
  * Note that PUT request must include the ID in the URL
  
## Caveats & ToDo

  * The state of the Employee object does not persist, restarting the app will lose all changes. Next steps would be to include a persistence layer
  * Utilization of other HTTP verbs or URL schema is not implemented and will result in service errors, these errors are not handled
