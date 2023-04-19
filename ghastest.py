from github import PyGithub
import os

# create a Github instance using an access token
g = Github(os.environ['GITHUB_ACCESS_TOKEN'])

# get the organization object
org_name = "my-org"
org = g.get_organization(org_name)

# iterate through all repositories in the organization
for repo in org.get_repos():

    # enable secret scanning for the repository
    try:
        repo.enable_secret_scanning()
        print(f"Enabled secret scanning for {repo.full_name}")
    except Exception as e:
        print(f"Error enabling secret scanning for {repo.full_name}: {e}")
