#!/bin/python
import random

#WCLT Player creation
#Make leagues for Germany, Russia, and Japan?

loc_data = open("data_lists/locations.txt","r")
locations = loc_data.readlines()
loc_data.close()
for l in locations:
	l = l.rstrip()

dispos = ["aggressive","reactive","stoic","ambitious","eager"]

fn_data = open("data_lists/firstnames.txt","r")
f_name = fn_data.readlines()
fn_data.close()
for l in f_name:
	l = l.rstrip()

ln_data = open("data_lists/lastnames.txt","r")
l_name = ln_data.readlines()
ln_data.close()
for l in l_name:
	l = l.rstrip()


create = input("How many players? ")
create = int(create)
while create > 0:
	my_dispo = random.choice(dispos)
	my_int = random.randint(40,70)
	my_acc = random.randint(40,70)
	my_eva = random.randint(40,70)
	my_pot = random.randint(30,80)
	my_fit = random.randint(40,70)
	my_ego = random.randint(0,20)
	my_kno = random.randint(10,30)
	my_name = random.choice(f_name).rstrip()+" "+random.choice(l_name).rstrip()
	my_home = random.choice(locations)
	my_age = random.randint(16,20)

	#Change the output to match the format in the team template, which should eventually match the sql output
	print(my_name+":"+str(my_int) +":"+str(my_acc) +":"+str(my_eva)+":"+str(my_pot)+":"+str(my_fit)+":"+str(my_kno)+":"+str(my_kno)+":"+my_dispo+":NA:bench:bench:bench:0:0:0:0:0:0:"+my_home.rstrip()+":"+str(my_age)+":0:0:"+"NA")

	create = create - 1
#ROSTER:NAME:INT:ACC:EVA:POT:FIT:EGO:KNO:PERSONALITY:DRUG:TAC1:TAC2:TAC3:INJ:Hits-Taken:Players-Hit:Flags-Captured:Rounds-Played:Hometown:Age:GAME_COST:CONTRACT_LENGTH:CONTRACT_TYPE