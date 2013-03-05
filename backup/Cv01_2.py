#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# syky CV01

import time

def pow3(x):
  return x*x*x

def acuTime():
	print("Prave je :    " + str(time.localtime()[2]) +"."+ str(time.localtime()[1])+"."+ str(time.localtime()[0]) + "  " + str(time.localtime()[3])+":" + str(time.localtime()[4]))

def hi(jmeno):
	print('Ahoj %s' %jmeno)
	return 0

def rek():
	jmeno = ''
	jmeno = dinput("Zadej jmeno: ")
	if jmeno== '':
		print("Nezadal jsi jmeno")
		time.sleep(2)
		rek();
	else:
		hi(jmeno)

if __name__ == "__main__":
	jmeno = ''
	jmeno = input("Zadej jmeno: ")
	if jmeno == '':
		print("Nezadal jsi jmeno")
		time.sleep(2)
		rek()
	else:
		hi(jmeno)
