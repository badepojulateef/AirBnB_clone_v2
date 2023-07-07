#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))
        archize_size = os.stat(res).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, archize_size))
    except Exception:
        archive_path = None
    return archive_path
