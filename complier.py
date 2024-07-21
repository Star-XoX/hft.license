#===============================================================================
'to copy/paste default python startups lol'
#===============================================================================
import os, subprocess
from shutil import rmtree as rm, copytree as cp
#===============================================================================
dir_path = os.path.dirname(os.path.realpath(__file__)) 
react_folder = f'{dir_path}/dist/XoX/react' 
build_folder = f'{dir_path}/react/build' 
#===============================================================================
def run(cmd: str, args: list = None, cwd: str = None, wait: bool = True) -> str:
    ''' 
        to exec a command to the terminal
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
        cwd = cwd
    )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ return output
    if args: 
        out = terminal.communicate(os.linesep.join(args))[0].strip()
        if out[1] != '': return out[1].strip()
        else: return out[0].strip()
    elif wait: 
        out = terminal.communicate()
        if out[1] != '': return out[1].strip()
        else: return out[0].strip()
    else: 
        return None
#===============================================================================
def main(script_name):
    'nick clean out .jpath and all configs'
    py2exe = ' '.join([
        f'pyinstaller {script_name}',
        '--noconfirm',
        '--onefile'
        # '--add-data "react/build/*;react/build"',
        # '--add-data "binary/*;binary"'
    ])
    resp = run(py2exe)
    print(resp)
    # rm(react_folder)
    # os.mkdir(react_folder)
    # cp(build_folder, f'{react_folder}/build')
    # run('start https://localhost:25000')
#===============================================================================
script_name = 'script.py'
main(script_name)
#===============================================================================
  
