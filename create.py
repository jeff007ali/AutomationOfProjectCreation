import sys
import os
from github import Github

workspace_path = "Downloads/myScrap/pyLab_myLab/"

username = "" #Assign your github username
password = "" #Assign your github password

def create():
    folderName = str(sys.argv[1])
    try:
        os.mkdir(workspace_path + folderName)
    except OSError:
        print ("Creation of the directory {} failed".format(folderName))
    else:
        print ("Successfully created the directory : {}".format(folderName))

    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Successfully created repository : {}".format(folderName))


if __name__ == "__main__":
    create()
