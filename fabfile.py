from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['sse_groundup@assu-web.stanford.edu']

def prepare_deploy():
    local("python manage.py test groundup")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")
    
def deploy():
    code_dir = '/home/sse/groundup/website'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone groundup@assu-web.stanford.edu:/home/sse/groundup/website.git %s" % code_dir)
            
    with cd(code_dir):
        run("git pull")
        
    
    