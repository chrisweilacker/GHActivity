from github import Github
import os, config, shutil, sys, math, random, time, subprocess

shouldRun = random.randint(1,100)
#Only run 57% of the time...i.e 4 out of 7 days
if shouldRun<42:
    print('no push today')
    sys.exit()

g = Github(config.token)

#Commit between 1 and 3 commits today.
numberCommits = random.randint(1,3)
print('got into GitHub')
repo = g.get_user().get_repo('epochTimeRepo')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('pwd')
#Create tempDir
if os.path.exists('tempDir'):
    shutil.rmtree(os.path.abspath('tempDir'))
os.mkdir('tempDir')

#create clone
os.chdir('tempDir')

if repo:
    os.system('git clone ' + repo.clone_url)
else:
    print('repo doesnt exist')
    sys.exit()

dirList = os.listdir()
os.chdir(dirList[0])
os.system('git checkout master')
for i in range(numberCommits):
    file = open("README.md", "w")
    d = time.time()
    text = f'# EPOCH TIME REPO \n This repo was a simple test of how to get Epoch time written in multiple languages \n Current Epoch Time is {d}'
    file.write(text)
    file.close()
    os.system('git add README.md')
    os.system(f'git commit -m "Updated current Epoch to {d}"')
    os.system(f'sleep {random.randint(6, 18)}')

os.system('git push origin master --force-with-lease')
print('Check your GitHub to see if it was updated')






