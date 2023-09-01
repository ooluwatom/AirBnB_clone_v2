#!/usr/bin/python3
"""Python script to Compress web static package
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress directory

    Return: path to archive on success; None on fail
    """
    # To get current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    # To create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # To check if archiving was successful
    if result.succeeded:
        return archive_path
    return None
