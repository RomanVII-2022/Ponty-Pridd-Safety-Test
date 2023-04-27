## Running the Selenium Script

### Step 1: Activate the Virtual Enviroment
1. Navigate into the PontySafety directory.
2. Write the following command to activate the virtual environment.

        . virtual/bin/activate

3. If the virtual environment is activated you will see (virtual) at the beginning of every line on the command line.

### Step 2: Install all Dependencies
1. Ensure that you are in the PontySafety directory.
2. Run the following command to install all the dependencies in your virtual environment.

        python3 -m pip install -r requirements.txt

3. To verify that all the dependencies have been installed run the following command.

        pip freeze

4. The output of the above command should be the same as the data in the **requirements.txt** file.

### Step 3: Open Your Chrome Browser in Debug Mode.
1. Navigate into Documents and create a folder. You can name it anything. For this example we will name it **chromeprofile**.
2. Navigate into the directory where **google-chrome** is.
3. To check the directory run the folowing command.

        which google-chrome

4. Run the following command. Replace **username** with the username you're logged in as.

        google-chrome --remote-debugging-port=9898 --user-data-dir='/home/username/Documents/chromeprofile'

5. A fresh chrome window should pop-up.

### Step 4: Running Your First TestCase.
1. Switch back to the terminal you had activated the virtual environment and downloaded dependencies.
2. Ensure that you are in the PontySafety directory.
3. Run the following command to test all the test cases in the login page.

        pytest -s -v testCases/test_001_login.py

4. The test cases should automatically start running on the chrome window you opened in debug mode.

> To run the other test cases replace the last part of the previous command with the name of the file you want to run. 

5. To run all the testcases together enter the following command.

        pytest -s -v testCases


        