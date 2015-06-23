#!/usr/bin/env python



import re
import os

#Author : Aditya Choudhary 

#DES = os.getcwd()	# gives dir. of teminal, from which script is run
DES = os.path.dirname(os.path.abspath(__file__))	# gives dir. of script

pattern1 = '"_'
pattern2 = 'Id'

subst1 = '"'
subst2 = '_id'

with open(DES+"/"+"Tags_2c.json",'w') as new_file:
	with open(DES+"/"+"Tags_2.json") as old_file:
		for line in old_file:
			s= line
			#s.replace(pattern1,subst1)
			#line.replace(pattern2,subst2)
			#print line
			line = re.sub(pattern2,subst2,line)
			line = re.sub(pattern1,subst1,line)
			#print line
			new_file.write(line)

#close(old_file)
