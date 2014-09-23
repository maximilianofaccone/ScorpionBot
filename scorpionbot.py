#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
import string
import urllib2
import random

from google import search
from bs4 import BeautifulSoup
from time import sleep
from commands import getoutput
from urllib import urlopen
from re import search, sub

HOST="irc.freenode.net"
PORT=6667
NICK="ScorpionBot"
PASS="scorpion15563"
IDENT="ScorpionBot"
REALNAME="Dark Scorpion"
CHAN="#puppy-latino"
readbuffer=""
track = ''
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("PASS %s\r\n" % PASS)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
#s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Hello There!"))
#s.send("PRIVMSG %s :%s\r\n" % (CHAN, "I am a bot"))

away = []
woman = False

def send_msg(msg):
        s.send("PRIVMSG %s :%s" % (CHAN, msg))

while 1:
#        new_track = getoutput('deadbeef --nowplaying "%a - %t - %b"').split('\n')[1]

#       if track != new_track:
#               track = new_track
#               s.send("PRIVMSG "+ CHAN +" :Escuchando %s\n" % track)

        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )
        for line in temp:
                #print line
                line=string.rstrip(line)
                line=line.split(CHAN + ' :')
                username = line[0].split('!')[0].split(':')[1]

#PING y saludo de bienvenida
                if line[0].find("PING") != -1:
                        pingid = line[0].split()[1]
                        s.send("PONG %s\r\n" % pingid)

                elif line[0].find('JOIN') != -1:
                        if username != NICK and username.find(HOST) == -1:
                                sleep(5)
                                send_msg("Bienvenid@ %s Cuidado con los trolls, roccos y tenochslb que hay en la sala.\n" % username)

                if len(line) > 1:
                  
		  if 'florinda' in line[1].split():
                    send_msg("Vamonos tesoro, no te juntes con esta chusma\n")
                    sleep(2)
                    send_msg("Si mami. Chusma, chusma prfff\n")

#                 if line[1].find('http') != -1:
#		    for u in line[1].split():
#                   d = search('(.+://)(www.)?([^/]+)(.*)', u)
#                   url = u
#                   response = urllib2.urlopen(url)
#                   html = response.read()
#
#                                 soup = BeautifulSoup(html)
#                                 title = soup.html.head.title
#                                 print title.contents
                                              
#                                 send_msg("%s\n" % (title.contents).encode('utf8'))
					      

                  if  line[1] == '$about':
                    send_msg("Max_Escorpion presenta, ScorpionBot, un trollbot creado por Maximiliano Faccone\n")

                  if  line[1] == '$ version':
                    send_msg("ScorpionBot 1.0.5 (c) 2014 Maximiliano Faccone\n")

                  if  line[1] == '$regreso' :
                    print username
                    if not username in away:
                      send_msg("Arrivederci %s \n" % username)
                      away.append(username)
                      print away

                  if line[1] == '$hevuelto' :
                    if username in away:
                      send_msg("%s ha vuelto. Ya podemos dejar de trollearlo.\n" % username)
                      away.remove(username)

                  for l in line[1].split():
                    if l in away != -1 and username != 'ScorpionBot':
                      send_msg("%s no esta. Vamos a trollearlo\n" % l)

#Saludo $hi
                  if  line[1] == '$hi' or line[1] == '$HI':
                    send_msg("Bienvenidos %s\n" % username) 
								
		  if  line[1] == '$frase':
		    lines = open("data/fortunes", "r").readlines()
		    link = lines[random.randint(0, len(lines)-1)]
	            send_msg("%s\n" % link)
		    print link
	            	
		  if line[1] == '$faptime':
		    send_msg("Scorpion BOT presenta:\n")
		    sleep(2)
		    send_msg("Una producción de Rocco_\n")
		    sleep(2)
	            send_msg("F A P T I M E !\n")
		    sleep(2)
		    lines = open("data/faptime", "r").readlines()
		    link = lines[random.randint(0, len(lines)-1)]
		    send_msg("%s\n" % link)
#guardar historial
		  vartmp = str(line[1])
		  vartmp2 = username + ": " + vartmp.decode("utf8")
		  vartmp3 = username + ": " + str(line[1])
		  print vartmp2
		  historial = open('history/history', 'a')
		  historial.write(vartmp3)
                  historial.write('\n')
		  historial.close()


	          #for res in search(searchgg, lang='es', stop=3):
		    #print res
                    #send_msg("%s\n" % url.encode("utf8"))
			