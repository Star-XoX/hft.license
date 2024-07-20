
import os, sys, git


def update_from_repo():
    repo = git.Repo('./')
    repo.remotes.origin.pull()

update_from_repo()

# nick 11