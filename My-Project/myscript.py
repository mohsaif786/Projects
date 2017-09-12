#!/usr/bin/python
try:
    f = open('testfile')
except Exception:
    print('sorry this file does not exist')
