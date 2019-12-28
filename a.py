import os
import sys
from github import Github
from git import Repo


class use:
    g = Github("aakhashgv@gmail.com", "Hsahkaavg0")
    name = sys.argv[1]


def createRepository():
    # for repo in use.g.get_user().get_repos():
     #   print(repo.name)
    new = use.g.get_user().create_repo(use.name)
    print("repo created: ", use.name)


def addFiles():
    repo = use.g.get_repo("Phenox11/"+use.name)
    repo.create_file("Readme.md", "init commit", "content")


def folder():
    print("what type is it? \n 1. Home \n 2. School \n 3. Portfolio")
    input1 = input()

    if int(input1) == 1:
        Repo.clone_from("https://github.com/Phenox11/"+use.name +
                        ".git", "/home/jagelta/Documents/Projects/Home/"+use.name)
    elif int(input1) == 2:
        Repo.clone_from("https://github.com/Phenox11/"+use.name+".git",
                        "/home/jagelta/Documents/Projects/School/"+use.name)
    elif int(input1) == 3:
        Repo.clone_from("https://github.com/Phenox11/"+use.name+".git",
                        "/home/jagelta/Documents/Projects/Portfolio/"+use.name)
    else:
        invd()


def invd():
    print("Invalid Input")
    folder()


if __name__ == "__main__":
    createRepository()
    addFiles()
    folder()
