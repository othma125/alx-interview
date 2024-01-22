#!/usr/bin/python3
'''A script that generates random HTTP request logs.
'''
from random import randint, choice, random
from sys import stdout
import datetime
from time import sleep


for i in range(10000):
    sleep(random())
    stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
        randint(1, 255),
        randint(1, 255),
        randint(1, 255),
        randint(1, 255),
        datetime.datetime.now(),
        '/projects/1216',
        'HTTP/1.1',
        choice([200, 301, 400, 401, 403, 404, 405, 500]),
        randint(1, 1024)
    ))
    stdout.flush()
