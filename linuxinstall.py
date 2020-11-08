import request, os

def Kaliinsttaler():
print(f'[!] Please Wait Load Data..')
os.system(pkg update -y ')
os.system('pkg upgrade -y ')
os.system('pkg install wget -y ')
os.system('pkg install openssh -y ')
os.system('pkg install bash-y ')
os.system('pkg install openssl')
os.system('pkg install proot -y ')
os.system('hash -r ')
os.system('wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh ')
os.system('bash kali.sh)


print("-=[LinuxInstaller]=-
				[Menu]
				[1].Y
				[2].N
				")
menu = input('Y/n : ')


if menu == '1':
 Kaliinsttaler()
elif menu == '2':
 print('Exit')
sys.exit()
else:
print('[?] command not found..')
sys.exit()
