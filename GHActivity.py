from github import Github
import os
import config

g = Github(config.token)
repoList = []
numberRepos = 3

for repo in g.get_user().get_repos():
    # Get the repos clone url for only repo's that you are the owner
    if repo.owner.email == config.email:
        #Add repo to list 
        repoList.append(repo.clone_url)
    if len(repoList) == numberRepos:
        break




