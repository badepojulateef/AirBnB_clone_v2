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
    generates a .tgz archive from the contents
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


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    Args:
        archive_path (str) - The path to the archived static files
    """
    if not path.exists(archive_path):
        return False

    file_path = path.basename(archive_path)  # web_static_20170314233357.tgz
    file_name = filename[:-4]  # web_static_20170314233357
    directory_path = "/data/web_static/releases/{}/".format(file_name)
    # /data/web_static/releases/web_static_20170314233357/

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the target directory
        run("sudo mkdir -p {}".format(directory_path))

        # Uncompress the archive to the folder
        run("sudo tar -xzf /tmp/{} -C {}".format(file_path, directory_path))

        # Delete the archive from the web server
        run("sudo rm -rf /tmp/{}".format(file_path))

        run("sudo mv {}web_static/*".format(directory_path, directory_path))

        # Delete the extra web_static directory
        run("rm -rf {}web_static".format(directory_path))

        # Delete the symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(directory_path))

        return True
    except Exception as e:
        False


    def deploy():
        """
        Creates and distributes an archive to your web servers
        """
        try:
            packed_files = do_pack()
            if packed_files is None:
                return False
            return do_deploy(packed_files)
        except Exception as e:
            return False
