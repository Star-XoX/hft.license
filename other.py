


# 333
import threading, signal
import os, sys, git
import subprocess
from time import sleep
from flask import Flask, request, jsonify
from traceback import format_exc as catch

import __main__
from os import getcwd
from os.path import dirname, realpath, normpath, expanduser
#===============================================================================
if hasattr(__main__, '__file__'):
    dir_path = dirname(realpath(__main__.__file__))
else:
    dir_path = getcwd()
#===============================================================================
def run(cmd: str, args: list = None, cwd: str = None, wait: bool = True, exe = None) -> str:
    ''' 
        to exec a command in the terminal
        >>> --------------------------------------------------------------------
        cmd: (str) = 'sudo apt-get upgrade'
        args: (list) = ['Y']
        cwd: (str) = '~/XoX'
        wait: (bool) = False
        >>> --------------------------------------------------------------------
        try: run('apt-get upgrade', ['Y'], wait = False)
        >>> -------------------------------------------------------------------- 
        return str || None || raise ValueError
    '''
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ excute the give code
    terminal = subprocess.Popen(
        cmd, 
        shell = True,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True,
        cwd = cwd,
        executable = exe,
    )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ return output
    try:
        if args: 
                out = terminal.communicate(os.linesep.join(args))[0].strip()
                if out[1] != '': 
                    return out[1].strip()
                else: 
                    return out[0].strip()
        elif wait: 
            out = terminal.communicate()
            if out[1] != '': 
                return out[1].strip()
            else: 
                return out[0].strip()
    except: pass
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ return output
    return None
#===============================================================================
if __name__ == "__main__":
    for itry in range(5):
        cmd = 'pgrep -a python'
        output = run(cmd, cwd= dir_path)
        if 'script.py' in output:
            sleep(3)
            continue
        os.system('./start.sh')
        