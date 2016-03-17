#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

HOME_DIR = "/home/"
MAIN_GITHUB_REP = "https://github.com/clemsos/app.junkware.io.git"
APP_NAME = "app.junkware.io"

LOG_DIR=os.path.join("/var/log/", APP_NAME)
CODE_DIR=os.path.join(HOME_DIR, APP_NAME)

def staging():
    """ Staging server credentials """
    env.hosts = ['127.0.0.1']
    env.user  = 'clemsos'
    env.remote_admin  = 'root'
    env.port="2022"
    env.mongo_user = "root"

def prod():
    """ Staging server credentials """
    env.hosts = ['127.0.0.1']
    env.user  = 'clemsos'
    env.remote_admin  = 'root'
    env.port="2022"
    env.mongo_user = "root"
