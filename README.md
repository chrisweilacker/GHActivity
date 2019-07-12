### Github Activity ###
This script adds some activity to each of your latest 4 public repos that you own creating activity Monday - Friday for a better Github Activity display to place on your portfolio website especially for those that do lots of coding via classes etc that are not being pushed up to GitHub.

Only works on Mac OS X+ if you are on windows can update the GHActivity.sh portion as needed to have it run on schedule(shouldnt be too difficult).
1. Install Python3 and Pip3/Anaconda if you dont have it already.
2. Run pip3 install PyGithub or conda install -c conda-forge pygithub depending on your setup
3. Add your GitHub API key to config.py as well as your username.
4. Update the path in GHActivity.sh to the full path to GHActivity.py
5. Run the GHActivity.sh once to add a cron job that will run every morning Monday - Friday at 11AM.