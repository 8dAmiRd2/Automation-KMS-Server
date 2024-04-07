import subprocess ,os
print("""
      _____________KMS-Automation________________
     |              Creator AMIR                 |
     |Have Good day!                             |
     |GitHub ID:8dAmiRd2                         |
     |Email : amiboy2200@gmail.com               |
     |____________↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑____________|
             Function 1 = Active windows offline
             Function 2 = Active Office product Offline
             Function 0 = Exit the Automation
             """)
#Active the Windows:
def Windows():
      result = subprocess.run("slmgr /skms " + IP,shell=True, stdout=subprocess.PIPE)
      result = subprocess.run("slmgr /ato",shell=True, stdout=subprocess.PIPE)
      print("Your Systeam has been Activated Successfully.")
#Active The Office:
def Office():
      result = subprocess.run("cd C:\Program Files\Microsoft Office\Office16",shell=True, stdout=subprocess.PIPE)
      result = subprocess.run("cscript ospp.vbs /sethst:" + IP,shell=True, stdout=subprocess.PIPE)
      result = subprocess.run("cscript ospp.vbs /act",shell=True, stdout=subprocess.PIPE)
      print("Your Office has been Activated Successfully.")
def ping_server():
      response = os.system("ping -n 1 "+IP)
      if response == 0:
            print(f"server {IP} is up and running...")
            return True
      elif response == 1:
            print(f"Server {IP} is down...")
            exit()
while True:
      user = input ("Choose your Function: ")
      if user == "0":
            break
      IP = input("Please Enter your KMS-Server IP(H.H.H.H): ")
      if user == '1':
            print("[+]Checking connection  to the Server...")
            ping_server()
            Windows()
      elif user =='2':
            print("[+]Checking connection  to the Server...")
            ping_server()
            Office()
