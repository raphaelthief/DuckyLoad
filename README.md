# DuckyLoad

![DuckyLoader](https://github.com/raphaelthief/DuckyLoad/blob/main/Pictures/Main.JPG "DuckyLoader")

## Diclaimer :
This RubberDucky payload generator is provided for educational purposes only.
The use of this software to perform malicious or illegal actions is strictly prohibited.
The author of this program takes no responsibility for any damage resulting from the use of this software.
The user is solely responsible for their actions and is encouraged to abide by the laws and regulations in their jurisdiction.

## Usages purposes :
The interest of this program is primarily aimed at red team or pentesting activities on device security where the code will be injected using Rubber Ducky techniques. The primary goal of this program is to facilitate payload generation by customizing certain information and functionalities while maintaining a library of these payloads.

## Aviable payloads :
For the vast majority of scripts, you can choose between normal execution or invoking admin rights (runas)

![DuckyLoader](https://github.com/raphaelthief/DuckyLoad/blob/main/Pictures/Menu.JPG "DuckyLoader")

- Windows payloads
	- Stealers
		- Webbrowsers stealer
		- Files stealer
		- FileZilla stealer
		- Wifi creds stealer
		- PC infos stealer
		- Files + Wbbrowsers + Wifi creds stealer
	- Backdoors
		- Set open port
		- Open wifi host
		- Reverse shell - Powershell
		- Reverse shell - Python
	- Droppers
		- Download & execute
		- Folder exception (Windows Defender) + Download + Execute
		- UAC Bypass (msconfig exploit) + Folder exception (Windows Defender) + Download & execute 
		- Drop & decode base64 executable
	- OS access
		- Pannel evasion (Kiosk evasion)
		- Windows keypad
		- Start cmd
		- Start powershell
		- Start registry
		- Start Task scheduler
	- Fun
		- Rick roll cmd
		- Launch webpage

![DuckyLoader](https://github.com/raphaelthief/DuckyLoad/blob/main/Pictures/Exemple.JPG "DuckyLoader")
## Description : 
DuckyLoader is a Rubber Ducky script generator. The generated .txt format is compatible and tested for use with FlipperZero. The particularity of Ducky Loader is that it employs an all-in-one methodology with automatic error handling through the command prompt, resulting in faster and more reliable execution.

### Exemple :
Usually, in most scripts, you have the following execution format :

```
Command 1
ENTER
DELAY 250
Command 2
ENTER
DELAY 250
etc ...
```

The main challenge and subtlety of Rubber Ducky scripts lie in the execution delays between commands. Here, all scripts minimize these constraints to the maximum extent, where only the command writing time matters. This significantly reduces the code injection duration :

```
DELAY 250
GUI r
DELAY 500
STRING cmd
ENTER
DELAY 1000
STRING command 1 & command 2 & command 3 & command 4 & etc... & exit
ENTER
```

"&" will execute the next command regardless of whether the previous one failed.
"&&" will execute the next command only if the previous command succeeded.

## Notes :
You can use these combinations knowingly to create a single command that will execute with delay management directly handled by cmd.
Avoid directly using PowerShell but prefer the use of cmd for executing attacks. I believe, based on my analysis and personal perception of use cases, that PowerShell is more sensitive in terms of Windows detection systems than cmd. The majority of attack scripts directly execute PowerShell commands via the PowerShell interface, and I think it's preferable to invoke PowerShell from cmd. Of course, these observations are subjective.

Another point of observation that you should take into consideration:
Reducing the execution window size might seem like a good idea; however, I've noticed code execution errors with such minimized windows. That's why I've chosen to leave the execution windows at a default size to prioritize successful execution, which will last no longer than 15 seconds. In the context of physical intrusion, these 15 seconds might seem like an eternity, but in reality, it's nothing, and it's a perfectly acceptable delay.
