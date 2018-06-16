"""
"""
import os
import signal
import subprocess
import sys


def get_processes_by_username(username):
    output = ''
    try:
        ps = subprocess.Popen(('ps', '-ef'), stdout=subprocess.PIPE)
        output = subprocess.check_output(('grep', username), stdin=ps.stdout)
        ps.wait()
    except subprocess.CalledProcessError as e:
        print e.output

    return output


def kill_process(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        return 0
    except OSError:
        return 1


def main():
    while True:
        output = ''
        print 'Type username to show his processes!'
        output = get_processes_by_username(raw_input())
        print output
        if output == '':
            print 'Nothing found!'
            break

        print 'Type pid to kill process!'
        errno = kill_process(int(raw_input()))
        if errno == 0:
            print 'Process terminated!'

        else:
            print 'Error! Process cannon be terminated!'


if __name__ == '__main__':
    main()
