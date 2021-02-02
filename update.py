#!/usr/bin/env python3


import git


repo = git.Repo('key-randomizer')
repo.remotes.upstream.pull('main')
