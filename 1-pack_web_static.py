#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents
"""
import os
from fabric.api import local
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['107.22.142.218']


def do_pack():
    """
    Compresses the web_static directory into a .tgz file.

    Returns:
        str: Path to the created archive on success, None on failure.
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)
        local("tar -czvf {} web_static".format(archive_path))
        if os.path.exists(archive_path):
            return archive_path
        else:
            return None
    except Exception as e:
        return None
