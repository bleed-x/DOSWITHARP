#We will DOS a victim with ARP poisening on the other systems that exist in a network
#################################################################################


#This is the main module that we will use to craete a packets and send them
from scapy.all import *

#This is a module that we use to interact with python interpreter
import sys

#This is a module that we use to interact with the operation system that python is running on it
import os

#This is a module that  we use to get information like IP address from network adapter
import netifaces as lp

#This is a module that we use to create a more thread to use them in poisening operation
import threading

#This is a module that we use to create a delay time in exection of python code
import time





#The alive systems addressess will store is in this file
result=open("/root/Desktop/ipaddress.txt" , 'w+') #create a writeable file
result2=open("/root/Desktop/macaddress.txt" , 'w+') #create a writeable file 

alivesys=[] #It is a list variable that we will use to store the alive systems IP address in the network
sysmac=[]   #It is a list variable that we will use to store the MAC address of the Alive systems in network



	
	
	













