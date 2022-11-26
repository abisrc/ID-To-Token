import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.RED + """
        888 888b.    88888 .d88b.    88888 .d88b. 8  dP 8888 8b  8 
         8  8   8      8   8P  Y8      8   8P  Y8 8wdP  8www 8Ybm8 
         8  8   8      8   8b  d8      8   8b  d8 88Yb  8    8  "8 
        888 888P'      8   `Y88P'      8   `Y88P' 8  Yb 8888 8   8 
                              github.com/abisrc
""" + Fore.RED)
print(banner)
userid = input(" $ User ID:  ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n $ Token First Part: {encodedStr}')
os.system('pause >nul')
