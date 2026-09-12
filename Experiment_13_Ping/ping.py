import os
import subprocess
import platform

def custom_ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '4', host]
    
    with open("output.txt", "w") as f:
        f.write(f"Executing Ping to {host}...\n\n")
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            f.write(output)
        except subprocess.CalledProcessError as e:
            f.write(f"Ping failed:\n{e.output}")
        except Exception as e:
            f.write(f"Error:\n{str(e)}")

custom_ping("127.0.0.1")
