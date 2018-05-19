#!python
# -*- coding: utf-8 -*-#
"""
Varibles in alfred.

Author : Bhishan Poudel
Date   : May 19, 2018
"""
# Imports
import json
import sys


data = {'valid': 'true', 'title':'Bash',
        'arg':'bash','quicklookurl':'~/Dropbox/Help/bash.sh',
        'icon': {'path':'bash.png'}}
json.dump(data, sys.stdout)

"""
Required:


{"items": [
{
    "valid": true,
    "uid": "",
    "title": "Bash",
    "arg": "bash",
    "subtitle": "",
    "quicklookurl": "~/Dropbox/Help/bash.sh",
    "icon": {
        "path": "bash.png"
    }
}
]}
"""