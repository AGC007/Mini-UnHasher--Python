#~~~~~~~~~~~ Code By AGC007 ~~~~~~~~~~~~#

#pip install requests
#~~ Github : AGC007\

#~START

#~LIB :

from requests.structures import CaseInsensitiveDict
from urllib import response
import requests
import string
import json
import os

#~Data :

USER_Hash = ""
Hash = ""

#~Function :

def Mini_UnHasher(USER_Hash):
   
    try:
   
        Hash = USER_Hash

        REQ = requests.get("http://www.nitrxgen.net/md5db/"+ Hash + ".json")
        JSONR = json.loads(REQ.text)

        if(REQ.status_code == 200) or (JSONR['result']['found'] == 'True'):
            Text_Decode = JSONR['result']['pass']
            print("Text Decode :" , Text_Decode)
        else:
            print("ER > Code :", REQ.status_code) 

    except: 
            print('ER') 

#~Main :

print("""
==========================================================
========= Mini-UnHasher [v1-Software] By AGC007™ =========
=====================  Version: 1.0  =====================
=================== Developer: +AGC007+ ==================
==========================================================

----------------------------------------------------------""")

USER_Hash = input("\nPlease Enter Hash : ")
Mini_UnHasher(USER_Hash)


#~END

#~~~~~~~~~~~ Code By AGC007 ~~~~~~~~~~~~#



