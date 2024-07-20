
import threading, signal
import os, sys, git
from time import sleep
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def start_script():
    os.execv(sys.executable, ['python'] + sys.argv)

def update_from_repo():
    repo = git.Repo('./')
    repo.remotes.origin.pull()
    start_script()

def exit_after_response():
    update_from_repo()
    os.kill(os.getpid(), signal.SIGINT)

@app.route("/restart")
def restart():
    threading.Thread(target=exit_after_response).start()
    return "working.."

if __name__ == "__main__":
    sleep(2)
    app.run(host='0.0.0.0', port = 80)