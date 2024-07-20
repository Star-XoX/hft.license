
import os
from time import sleep
import logging

import subprocess
logging.basicConfig(level=logging.INFO)

logging.info('Starting init.py')
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

# out = run('git clone --progress https://github.com/Star-XoX/hft.license.git', cwd = '/xox')
# logging.info(out)

# out = run('python3 -m venv /venv', cwd = '/xox/hft.license')
# logging.info(out)

# Set the PATH environment variable
# os.environ['PATH'] = '/xox/hft.license/venv/bin:' + os.environ['PATH']

# out = run('pip3 install -r /xox/hft.license/requirements.txt')
# logging.info(out)

# Run the Python script
# CMD ["python", "script.py"]

# /xox/hft.license

os.system('nohup python3 -u ./script.py > ./out.script &')

# os.system("""trap 'kill ${!}; echo "Killed by backgrounded process"; exit 1' USR1""")


# os.system('./start.sh')
logging.info('Started script.py')

while True:
    sleep(2222)