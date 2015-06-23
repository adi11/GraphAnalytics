#!/usr/bin/env python



import re
import os

#Author : Aditya Choudhary 

#DES = os.getcwd()	# gives dir. of teminal, from which script is run
DES = os.path.dirname(os.path.abspath(__file__))	# gives dir. of script

pattern1 = 'Tags="&lt;(.*)&gt;'
pattern2 = 'Id="[0-9]+"'
pattern3 = '/>'

#subst1 = ""
#subst2 = 'Type= \"Tag\" />'
subst3 = 'PostId="'

edgel = ['id','outV','type','inV','label']
count=0
#q = re.search('Tags="&lt;(.*)&gt;',t)

with open(DES+"/"+"Edges_1.xml",'w') as e_file:
	with open(DES+"/"+"Posts_1.xml",'w') as new_file:
		with open(DES+"/"+"Posts.xml") as old_file:
			for line in old_file:
			
				t = line
				#for getting Id and adding PostId 
				
				sbg2 = re.findall(r"[0-9]+",t)
				if sbg2:
					line = re.sub(pattern3,subst3+sbg2[0]+'" '+pattern3,line)
				new_file.write(line)	
				#for seperating tags
				subgroup = re.search(pattern1,t)
				if subgroup:
					st = subgroup.group(1)
					lis = re.findall(r"[\w'-]+",st) 
					# lis = ['data-mining', 'gt', 'lt', 'definitions']
			
					for i,val in enumerate(lis):
						if('lt' != val and 'gt' != val):
							print count,val
							ne = '<edge '+edgel[0]+'="'+str(count)+'" '
							ne+= edgel[1]+'="'+val+'" '
							ne+= edgel[2]+'="edge" ' 
							ne+= edgel[3]+'="'+sbg2[0]+'" '
							ne+= edgel[4]+'="tag" />\n'
							count+=1
							e_file.write(ne)
			
			



