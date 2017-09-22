#!/usr/local/bin/python3.4

import sys
import os
import time


def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def main():
    while 1:
        write_stdout('READY\n')
        line = sys.stdin.readline()
        headers = dict([x.split(':') for x in line.split()])
        data = sys.stdin.read(int(headers['len']))
        if data == "process_state_stoping":
            time.sleep(15)
        write_stdout('RESULT 2\nOK')


if __name__ == '__main__':
    main()
