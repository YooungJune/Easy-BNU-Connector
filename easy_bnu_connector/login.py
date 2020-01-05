'''
Author: GasinAn
'''
# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
try:
    import tkinter
except:
    import Tkinter as tkinter
try:
    import _thread
except:
    import thread as _thread

from requests import request
from bs4 import BeautifulSoup

from methods import methods


BROWSERS = {'MicrosoftEdge.exe', 'iexplorer.exe', 'chrome.exe',
            '360chrome.exe', 'liebao.exe'}
BNU_STUDENT_CONNECT_COMMAND = 'netsh wlan connect BNU-Student'
BNU_CONNECT_COMMAND = 'netsh wlan connect BNU'
BNU_URL = 'http://www.bnu.edu.cn'
GET_CHALLENGE_URL = '/cgi-bin/get_challenge'
SRUN_PORTAL_URL = '/cgi-bin/srun_portal'
ENC = 'srun_bx1'
NUM = '200'
TYPE = '1'


def ban_browsers_come_out():
    while True:
        for browser in BROWSERS:
            if os.system('taskkill /im '+browser+' /f') is 0:
                return 0

def login():
    try:
        r = request('GET', BNU_URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        r = request('GET', soup.a['href'])
        srun_portal_pc_url = r.url[:21]
        soup = BeautifulSoup(r.text, 'html.parser')
        ip = soup.find(id='user_ip')['value']
        ac_id = soup.find(id='ac_id')['value']

        username = e_username.get()
        password = e_password.get()
        params = {'callback': 'jQuery', 'username': username, 'ip': ip}
        r = request('GET', srun_portal_pc_url+GET_CHALLENGE_URL, params=params)

        token = r.text[21:85]
        d = {'username': username,
            'password': password,
            'ip': ip,
            'acid': ac_id,
            'enc_ver': ENC}
        json_d = str(d).replace(chr(39), chr(34)).replace(' ', '')
        i = '{SRBX1}'+methods.base64_encode(methods.xEncode(json_d, token))
        hmd5 = methods.md5(password, token)
        chkstr = token+username
        chkstr += token+hmd5
        chkstr += token+ac_id
        chkstr += token+ip
        chkstr += token+NUM
        chkstr += token+TYPE
        chkstr += token+i
        password = '{MD5}'+hmd5
        params = {'callback': 'jQuery',
                'action': 'login',
                'username': username,
                'password': password,
                'ac_id': ac_id,
                'ip': ip,
                'chksum': methods.sha1(chkstr),
                'info': i,
                'n': NUM,
                'type': TYPE,
                'os': 'Windows+10',
                'name': 'Windows',
                'double_stack': '0'}

        r = request('GET', srun_portal_pc_url+SRUN_PORTAL_URL, params=params)
        if r.text[61:72] == 'login_error':
            if r.text[94] == 'P':
                text_title.set('用户名或密码错误')
            elif r.text[94] == 'U':
                text_title.set('用户不存在')
            else:
                text_title.set('登录失败')
        else:
            text_title.set('登录成功')

    except TypeError:
        text_title.set('用户已在线')
    except:
        text_title.set('无法连接校园网')

gui = tkinter.Tk()
gui.title('')
gui.geometry('+500+250')
text_title = tkinter.StringVar()
l_title = tkinter.Label(gui, textvariable=text_title)
l_title.grid(row=0, columnspan=2)
l_username = tkinter.Label(gui, text='用户名')
l_username.grid(row=1, column=0)
e_username = tkinter.Entry(gui)
e_username.grid(row=1, column=1)
l_password = tkinter.Label(gui, text='密码')
l_password.grid(row=2, column=0)
e_password = tkinter.Entry(gui, show='A')
e_password.grid(row=2, column=1)
b_login = tkinter.Button(gui, text='登录', command=login)
b_login.grid(row=3, columnspan=2)

if os.system(BNU_STUDENT_CONNECT_COMMAND) is 0:
    text_title.set('BNU-Student')
elif os.system(BNU_CONNECT_COMMAND) is 0:
    text_title.set('BNU')
else:
    text_title.set('无法连接校园网')
_thread.start_new_thread(ban_browsers_come_out, ())
gui.mainloop()