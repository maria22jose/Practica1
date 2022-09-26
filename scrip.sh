(sudo nmap -sP -n 192.168.240.0/24| grep -B 2 82:70 | grep report | cut -d " " -f 5
>emi.txt)
cat -n emi.txt 

