#===============================================================================
import subprocess
#===============================================================================


#===============================================================================

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
def get_cont():
    out = run('docker ps')
    for line in out.split('\n'):
        if '0.0.0.0' in line:
            con_id = line.split()[0].strip()
            print(f'docker logs {con_id}')
            print(f'docker exec {con_id} pgrep -a python')
            print(f'docker exec -it {con_id} /bin/bash')
#===============================================================================
def get_images():
    out = run('docker images')
    for line in out.split('\n'):
        if 'name' in line:
            con_id = line.split()[2].strip()
            run(f'docker run -v /root/docker/hft.license/xox:/xox -d -p 8080:80 {con_id}')
#===============================================================================
if __name__ == "__main__":
    run('rm -rf /root/docker/hft.license/xox/hft.license')
    get_images()
    get_cont()
