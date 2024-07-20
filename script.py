# 333
import threading, signal
import os, sys, git
import subprocess
from time import sleep
from flask import Flask, request, jsonify
from traceback import format_exc as catch
import logging
import __main__
from os import getcwd
from os.path import dirname, realpath, normpath, expanduser
#===============================================================================
if hasattr(__main__, '__file__'):
    dir_path = dirname(realpath(__main__.__file__))
else:
    dir_path = getcwd()

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def hello():
    return '{"status": "nick was not here"}'

def start_script():
    os.execv(sys.executable, ['python'] + sys.argv)

def update_from_repo():
    # repo = git.Repo('./')
    # repo.remotes.origin.pull()
    start_script()

def exit_after_response():
    sleep(2)
    # update_from_repo()
    logging.info("Sending signal to stop container")
    os.kill(1, signal.SIGUSR1)
    logging.info("after")
    # try:
    #     os.kill(os.getpid(), signal.SIGINT)
    # except:
    #     logging.info('failed1')
    # logging.info('after1')
    # try:
    #     os.kill(os.getpid(), 9)
    # except:
    #     logging.info('failed2')
    # logging.info('after2')
    # try:
    #     sys.exit() 
    # except:
    #     logging.info('failed3')
    # logging.info('after3')
    # try:
    #     quit() 
    # except:
    #     logging.info('failed4')


def exit_after_response1():
    sleep(2)
    # update_from_repo()
    logging.info("Sending signal to stop container prep")
    try:
        os.kill(os.getpid(), signal.SIGINT)
    except:
        logging.info('failed1')
    logging.info('after1')
    try:
        os.kill(os.getpid(), 9)
    except:
        logging.info('failed2')
    logging.info('after2')
    try:
        sys.exit() 
    except:
        logging.info('failed3')
    logging.info('after3')
    try:
        quit() 
    except:
        logging.info('failed4')




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

@app.route("/cmd", methods=["POST"])
def custom():
    cmd = request.get_json()["cmd"]
    try:
        

        # output = subprocess.check_output(cmd, shell=True, text=True)
        output = run(cmd, cwd= dir_path)
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)})


@app.route("/restart")
def restart():
    logging.info('goin under 2')
    os.system('nohup python3 -u /xox/hft.license/other.py > /xox/hft.license/out.other &')

    # os.system('nohup python -u other.py > out.other &')
    threading.Thread(target=exit_after_response).start()
    return "working.."

@app.route("/restart1")
def restart1():
    logging.info('goin under 1')
    # os.system('nohup python -u other.py > out.other &')
    os.system('nohup python3 -u /xox/hft.license/other.py > /xox/hft.license/out.other &')


    threading.Thread(target=exit_after_response1).start()
    return "working.."

if __name__ == "__main__":
    for itry in range(33):
        sleep(2)
        try:
            app.run(host='0.0.0.0', port = 80)
        except:
            logging.info(catch())
    
    # logging.info(sys.executable)
    # logging.info(sys.argv)
    # os.execv(sys.executable, ['python'] + sys.argv)