import os
import sys
from github import Github


class use:
    g = Github("aakhashgv@gmail.com", "Hsahkaavg0")
    name = "temp"


def createRepository():
    for repo in use.g.get_user().get_repos():
        print(repo.name)
    new = use.g.get_user().create_repo(use.name)
    print("repo created: ", use.name)


def addFiles():
    repo = use.g.get_repo("Phenox11/temp")
    repo.create_file("Readme.md", "init commit", "contents")


def folder():
    print("what type is it? \n 1. Home \n 2. School \n 3. Portfolio")
    input1 = input()
    print(input1)
    func_dict = {
        "home": os.chdir("/home/jagelta/Documents/Projects/Home/"),
        "school": os.chdir("/home/jagelta/Documents/Projects/School/"),
        "porfolio": os.chdir("/home/jagelta/Documents/Projects/Portfolio/"),
    }
    os.system("git clone https://github.com/Phenox11/$1.git")
    os.system("git remote add origin https://github.com/Phenox11/$1.git")


def invd():
    print("Invalid Input")
    folder()


if __name__ == "__main__":
    createRepository()
    addFiles()
    folder()
