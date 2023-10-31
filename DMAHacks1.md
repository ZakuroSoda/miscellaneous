## Methods-to-Bypass-Corporate-Device-Management
1. Windows Recovery Env Command Prompt
2. .\Administrator
3. Linux Dual Boot

## Dual-Booting a Lenovo ThinkPad L13 Gen 2 issued by the Ministry of Education with Mobile Device Management software
(MDM not DMA, kids)

### Section 1: Creating the OEM boot drive
Step 1: Go to Lenovo Support and sign in with a Lenovo Account or create one for free
Step 2: Request for a digital recovery drive by filling in the form
Step 3: Download the Lenovo recovery media creator and sign in with your credentials
Step 4: Choose your request at the home page and select your USB drive at the next page
Step 5: Press yes yes yes until everything is done
Conclusion: You now have Lenovo recovery media for Lenovo model 20VH/20VJ

### Section 2: Creating the Microsoft Windows boot drive
Step 1: Get the Windows Recovery Media Creator from Microsoft’s webpage
Step 2: Open the executable file and select the applicable options and click yes yes yes until you have a drive
Conclusion: You now have generic recovery media for all Microsoft Windows PCs

### Section 3: Installing the Non-MDM (colloquially known as DMA) partition
Step 1: Plug the USB drive created in Section 1 into your laptop while off
Step 2: Turn on your computer and SPAM the F12 key until you get the boot options menu
Step 3: Click on your recovery drive and press yes yes yes until you have a clean copy of Windows (tainted by Lenovo bloatware but it’s better than not having drivers at all cough cough Microsoft)
Step 4: In OOBE, you will be required to sign into the students.edu.sg organisation. To circumvent this, indicate that you will be logging in via a smart key, then press Shift+F10 or Shift+Fn+F10 and type in netsh wlan disconnect (or unplug ethernet). Then, proceed with creating a local account.
Conclusion: You have set up an installation of Windows without MOE malware (but Lenovo nonsense)

### Section 4: Preparation to install MDM (also known as DMA)
Step 1: Open diskmgmt.msc by typing into the search bar
Step 2: Select your main partition and select shrink in the right click menu
Step 3: Shrink by 30-100GB
Conclusion: You have created unallocated space for your MOE malware partition (also known as DMA, rightly MDM)

### Section 5: Installation of malware
Step 1: Plug in the recovery drive you have created in Section 2 to your computer while it is turned off
Step 2: Turn your laptop on and again, SPAM F12 and choose the thumb drive
Step 3: You will observe that Lenovo is shot so Microsoft does not carry their display drivers. Do not worry because you can’t do shit about it. 
Step 4: Choose an advance install and select your unallocated space (it’s foolproof so don’t tell me you can’t do it) and install
Step 5: Your computer will restart and you can set up MOE Malware as usual (just use MOE credentials)
Step 6: To ensure your brand new Government-Sanctioned Malware is functional SPAM the sync button in settings and keep the laptop on for two hours (only continue when you see that you can two finger scroll (stupid Lenovo) and you have company portal installed
Conclusion: Welcome to MalwareOS

### Section 6: Quality-of-Life improvement
Step 1: Go to start menu of MalwareOS and do a shift restart
Step 2: Select use another operating system
Step 3: Click change defaults and make the default operating system what it is not currently (idgaf about changing names at this point) and set the timer to 5seconds
Conclusion: You have a dual booted system but you can’t use WSL or Huawei drivers. Sucks to be you.