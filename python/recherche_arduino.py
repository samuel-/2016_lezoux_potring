#!/usr/bin/env python
#-*- coding: utf-8 -*-
####################
# Potring 2.0 <potringpotring@gmail.com>
# voir http://www.museomix.org/prototypes/potring/
# copyright (c) 04/2017 Samuel Braikeh <samuel.braikeh@gmail.com>
# license GNU GPL v.2
####################
# mets j.ring à jour selon l'état des contacteurs
####################

from time import sleep
from collections import deque, defaultdict
from operator import itemgetter
from settings import *

import sys
import msvcrt
import serial
import time

###############
ARDUINO = True
CLAVIER = not ARDUINO
###############
###############

Potiers0 = deque(maxlen=20)
Potiers1 = deque(maxlen=20)

def recherche_interupt():
    
 #   print arduino.read_until('\n')
    #ajouter les valeurs reçues par l'arduino
    
    
    
    
    Potiers0.append(tmp0)
    Potiers1.append(tmp1)
    OldPotier0 = max_occurrences(list(Potiers0))[0]
    OldPotier1 = max_occurrences(list(Potiers1))[0]
    if j.ring[0]!=OldPotier0 : j.remplir(0,OldPotier0)
    if j.ring[1]!=OldPotier1 : j.remplir(1,OldPotier1)
##############################
def max_occurrences(seq):
    c = defaultdict(int)
    for item in seq:
        c[item] += 1
    return max(c.iteritems(), key=itemgetter(1))
##############################
def chercher(MAIN=False):
	if ARDUINO : chercher_arduino(MAIN)
	elif CLAVIER : chercher_clavier(MAIN)
##############################
##############################
def chercher_arduino(MAIN):
	ser = serial.Serial('COM3', 9600, timeout=1, parity='N')
	print ("wait...")
	time.sleep(1)

	while j.jeu_go:
		try:
			line = ser.readline()
			print line
			if ('010F4CAB739A' in line):
				j.remplir(0,-1)
				j.remplir(1,-1)
				j.remplir(0,0)
				j.remplir(1,1)					
			if ('010F4CA8658F' in line):
				j.remplir(0,-1)
				j.remplir(1,-1)
				j.remplir(0,1)
				j.remplir(1,2)
		except ser.SerialTimeoutException:
			print('Data could not be read')
			time.sleep(0.1)
def chercher_clavier(MAIN):
	while j.jeu_go:
		print "test avant"
		oo=msvcrt.getch()
		#oo=sys.stdin.read(1)
		print "test"
		if oo=="a":
			if j.ring[0]==-1:j.remplir(0,0)
			elif j.ring[0]==0:j.remplir(0,-1)
		elif oo=="z":
			if j.ring[0]==-1:j.remplir(0,1)
			elif j.ring[0]==1:j.remplir(0,-1)
		elif oo=="e":
			if j.ring[0]==-1:j.remplir(0,2)
			elif j.ring[0]==2:j.remplir(0,-1)
		elif oo=="i":
			if j.ring[1]==-1:j.remplir(1,0)
			elif j.ring[1]==0:j.remplir(1,-1)
		elif oo=="o":
			if j.ring[1]==-1:j.remplir(1,1)
			elif j.ring[1]==1:j.remplir(1,-1)
		elif oo=="p":
			if j.ring[1]==-1:j.remplir(1,2)
			elif j.ring[1]==2:j.remplir(1,-1)
		if MAIN :
			print " potier0 : "+str(j.ring[0])+"        potier1 : "+str(j.ring[1])
			if oo=="q":break
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
####################
if __name__ == '__main__':
	j.jeu_go = True
	chercher(MAIN=True)
