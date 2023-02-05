import subprocess as s

def killProcess(pid):
    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
