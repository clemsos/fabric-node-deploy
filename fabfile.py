#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from settings import *
from fabric.contrib import files
import os

SETTINGS = {
     'host': '18f-hub',
    'port': env.port,
    'home': HOME_DIR,
    'log': os.path.join(LOG_DIR, 'build.log'),
    'branch': 'master'
}

# env.use_ssh_config = True


def uptime():
    """ Show number of active connections on the server """
    run('uptime')

def remote_info():
    """ Get name and info of remote host """
    run('uname -a')

def local_info():
    """ Get name and info of local host """
    local('uname -a')

def update_code_from_git():
    """ Download latest version of the code from git """
    if not files.exists(HOME_DIR):
        with cd(HOME_DIR):
            run("git clone %s" % MAIN_GITHUB_REP )
    with cd(REMOTE_REPO_DIR):
        run("git pull")

def update_requirements():
    """ Update external dependencies on host """
    with cd(REMOTE_REPO_DIR):
        cmd = ['npm install']
        # cmd += ['--requirement %s' %  os.path.join(CODE_DIR,'requirements.txt')]
        run(' '.join(cmd))

def start():
  fabric.api.run(
    "cd %s && forever start -l %s -a deploy/hookshot.js -p %i -b %s -c \"%s\""
    % (REMOTE_REPO_DIR, LOG, SETTINGS['port'], SETTINGS['branch'], COMMAND)
  )

def stop():
  fabric.api.run(
    "cd %s && forever stop deploy/hookshot.js -p %i -b %s -c \"%s\""
    % (REMOTE_REPO_DIR, SETTINGS['port'], SETTINGS['branch'], COMMAND)
  )

def restart():
  fabric.api.run(
    "cd %s && forever restart deploy/hookshot.js -p %i -b %s -c \"%s\""
    % (REMOTE_REPO_DIR, SETTINGS['port'], SETTINGS['branch'], COMMAND)
  )

def init():
    """ Init setup of the project """
    pass

def deploy():
    """ Update the project """
    update_code_from_git()
    update_requirements()
