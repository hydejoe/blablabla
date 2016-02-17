# -*- coding=utf-8 -*-
#每间隔10分钟获取一次ip
#并将ip地址写入f_path路径
#
#
import requests,time
f_path='/you/log/path' #change me,example:'/home/user/log.txt'
ip=''
def check_ip():
    try:
        r=requests.get('http://1212.ip138.com/ic.asp',timeout=5)
    except requests.exceptions.ConnectTimeout:
        file_edit('Timeout')
    else:
        file_edit(r.text)

def file_edit(s):
    Time=time.strftime("%H:%M")
    if s=='Timeout':
        with open(f_path,'a') as f:
            f.write('\n'+'Timeout on '+Time)
    else:
        msg=s_to_ip(s)
        if msg=='No change':
            with open(f_path,'a') as f:
                f.write(' '+Time)
        else:
            with open(f_path,'a') as f:
                f.write('\n'+ip+' on '+Time)

def s_to_ip(s):
    global ip
    s1=s.split('[')
    s2=s1[1].split(']')
    if s2[0]==ip:
        msg='No change'
    else:
        ip=s2[0]
        msg=s2[0]
    return msg

def loop():
    while 1:
        print 'checking'
        check_ip()
        print 'check finished'
        time.sleep(600)

if __name__=='__main__':
    loop()
