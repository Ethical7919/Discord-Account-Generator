from concurrent.futures import ThreadPoolExecutor
from httpx_socks import SyncProxyTransport
from random import choice
from string import ascii_letters
from httpx import Client
from HCaptcha import Bypass
from time import sleep, time
import os
import requests

os.system('cls; clear')

_0, __0, _______0, _____0, ________0 = 0, open("proxies.txt", encoding='utf-8').readlines(), 60, ThreadPoolExecutor(max_workers=int(100000)), 500
___0 = "" #Invite Code
____0 = 2500
_________0 = "" #Username
__________0 = 2

def _O():
    global _0, __0
    try:
        _ = __0[_0]
        _0 += 1
    except:
        _, _0 = __0[0], 0
    return _.replace('\n','')

def __O(_0):
    return ''.join(choice(ascii_letters)for _ in range(_0))

def ___O(X, OO_):
    global __X0, __X1
    X_ = Bypass()
    print("HCaptcha Bypassed")
    while True:
        if OO_ <= int(time()):
            break
        sleep(0.5)
    while True:
        try:
            __0__ = Client(base_url='https://discord.com', headers={"Host":"discord.com","user-agent":f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57","accept-encoding":"gzip","accept-language":"en-US","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC4xMTAgU2FmYXJpLzUzNy4zNiBFZGcvOTYuMC4xMDU0LjU3IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjExMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg0NzEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"})
            _0_0_ = __0__.get("/api/v9/experiments",timeout=18).json()["fingerprint"]
            print(_0_0_)
            with Client(transport=SyncProxyTransport.from_url(f'socks4://{_O()}')) as _00:
                _ = _00.post("https://discord.com/api/v9/auth/register", timeout=19, headers={"Host":"discord.com", "Connection":"keep-alive", "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": _0_0_, "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/register", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"}, json={"fingerprint": _0_0_, "username":f"{_________0} | {__O(int(__________0))}", "invite": X, "consent": True, "gift_code_sku_id": None, "captcha_key": X_}).json()
            ______0 = open("tokens.txt", "a")
            ______0.write(f'{_["token"]}\n')
            ______0.close()
            return _["token"]
        except:
            pass

def ____O(OO_):
    print(___O(___0, OO_))

___OO = int(time()+int(_______0))
print(f"Starting in {_______0} seconds or more than that, please wait")
for _ in range (____0):
    _____0.submit(____O, ___OO)
    if _ == ________0:
        sleep(10);________0 += 500
