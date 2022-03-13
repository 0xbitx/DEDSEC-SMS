#coded by oxbit

import os

print("")
print("""
██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗    ███████╗███╗   ███╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔════╝████╗ ████║██╔════╝
██║  █0xbit██╗  ██║  ██║███████╗█████╗  ██║         ███████╗██╔████╔██║███████╗
██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║         ╚════██║██║╚██╔╝██║╚════██║
██████╔╝███████╗██████╔╝███████║███████╗╚██████╗    ███████║██║ ╚═╝ ██║███████║
╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝    ╚══════╝╚═╝     ╚═╝╚══════╝""")
print("       [*] DEDSEC SMS IS A FREE SMS TOOL WITH 1 FREE TEXT A DAY [*]")
print("                       [*] SEND ANONYMOUS SMS [*]                  ")
print("")
print("[*]--------------------------------------------------------------------[*]")
print (" [*1 1 - SEND\n [*] 2 - EXIT")
print("[*]--------------------------------------------------------------------[*]")


def sent():
	print("[*] Example: +639773543755 [*]")
	phonenumber = input("NUMBER: ")
	print("[*] Your message [*]")
	sms = input("MESSAGE: ")
	os.system('''curl -# -X POST https://textbelt.com/text --data-urlencode phone='''+phonenumber+'''  --data-urlencode message="''' +sms+ ''''" -d key=textbelt''')


while True:
	opt = input("CMD: ")
	if opt == "1":
		sent()
	if opt == "2":
		os.close()
