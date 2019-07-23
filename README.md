### Github Activity ###
This script adds activity to an 'epochTimeRepo' in order to create activity on your activity log.
NOTE: USE AT YOUR OWN RISK

Only works on Mac OS X+ if you are on windows can figure out how to run it on a sechule (shouldnt be too difficult).
1. Install Python3 and Pip3/Anaconda if you dont have it already.
2. Run pip3 install PyGithub or conda install -c conda-forge pygithub depending on your setup
3. Add your GitHub API key to a config.py file as well as your GitHub username use config.example.py to see the setup.
4. Update the path in the .plist file to the full path to GHActivity.py as well as the full path to your python installation you can use type -a python3 to find this. Also update your username and paths to wherever you want the output log/error log file to be.
5. Create a repository named epochTimeRepo
6. Copy the .plist file to ~/Library/LaunchAgents
7. run the command launchctl load ~/Library/LaunchAgents/com.gieson.launcha.GGHActivity.plist
8. Check the log file to make sure that the script ran.  Also check your repository a new README.md file should have been added and at least one commit should have been made unless you got unlucky and was the 3/7 days that it doesnt update your commits.  if a popup asking for your user password comes up for Git to access your key file select always allow.