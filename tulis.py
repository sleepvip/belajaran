###Belajar Bot Tulis
import requests
from bs4 import BeautifulSoup
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Bot Menulis \033[1;36;40m]\033[0;37;40m')
tulisan = input('\033[1;36;40m[\033[1;33;40m Tulisan \033[1;36;40m]\033[0;37;40m > ')
url = 'https://tools.zone-xsec.com/api/nulis.php?q={}'.format(tulisan)
r = requests.get(url)
Results = BeautifulSoup(r.text, 'html.parser')
print('\n\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Hasil Tulisan \033[1;36;40m]\033[0;37;40m')
print(Results)
print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Hasil Tulisan Di Simpan Di Link Web Image \033[1;36;40m]\033[0;37;40m')