#!/usr/bin/python3

import requests
def serverCall():
    URL = "http://nrs-projects.humboldt.edu/~bjm23/Hackathon/python_function.php"
    machine='SH130c'
    PARAM = {'name':machine}
    r = requests.get(url = URL, params = PARAM)
