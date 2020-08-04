# Automatic Git User SignIn
Run the python script and follow prompts to switch git users on a shared computer and to clock in!

Make sure you have an ssh key configured.

Run this script when different users use the same computer!

# setup

In order to use this projects full functionality you need to go through a few first steps when using on a new computer.
1. Download python from: https://www.python.org/downloads/ if using Windows.
2. Download the <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">ChromeDriver</a> and stick chromedriver.exe into your users bin folder. Make sure bin is in the environment variables path.
 - Example `C:\Users\MPLEX\bin` contains chromedriver.exe
 - Search for environment variables and click on "edit the system environment variables"
 - Click "Environment variables" and under System variables make sure `C:\Users\MPLEX\bin` is in `PATH` (Could be `Path`). Click edit to add or see if it exists.
3. Within the cloned repository open command prompt
 - run `pip install selenium`


# How to Use

From within the mainfiles of project core or another git project open command prompt and run some of the following commands.
This assumes this repository is cloned or copied into its own folder within the mainfiles of your project.

When you first enter the office and you want to switch git users AND sign in. 
- Run `python Automatic-Git-User-SignIn\startMyWorkday.py`

To switch git users without signing in:
- Run `python Automatic-Git-User-SignIn\switchUsers.py`

To clock out at the end of the day/clock in without switching users:
- Run `python Automatic-Git-User-SignIn\quickClock.py`

To commit and push all current git changes:
- Run `python Automatic-Git-User-SignIn\quickCommit.py`

