#!/bin/python
#WORLD CHAMPIONSHIP LAZER TAG
#Single Game Debugger
import random
import time
from operator import itemgetter


def die_roll(chk,player,team):
	the_roll = random.randint(0,99)
	#Debug log roll
	if chk == "int":
		the_result = player["s_int"] - the_roll
		if player["drug"] == "cocaine":
			the_result = the_result*1.25
		elif player["drug"] == "marijuana":
			the_result = the_result*.8		
		if player["per"] == "aggressive":
			the_result = the_result*1.25
		elif player["per"] == "reactive":
			the_result = the_result*.8	
		if player["c_pos"] == "charge":
			the_result = the_result*2
		elif player["c_pos"] == "skirmish":
			the_result = the_result*.5
	elif chk == "acc":
		the_result = player["s_acc"] - the_roll
		if player["drug"] == "adderall":
			the_result = the_result*1.25
		elif player["drug"] == "cocaine":
			the_result = the_result*.8		
		if player["per"] == "stoic":
			the_result = the_result*1.25
		elif player["per"] == "aggressive":
			the_result = the_result*.8	
		if player["c_pos"] == "snipe":
			the_result = the_result*2
		elif player["c_pos"] == "charge":
			the_result = the_result*.5
	elif chk == "eva":
		the_result = player["s_eva"] - the_roll
		if player["drug"] == "marijuana":
			the_result = the_result*1.25
		elif player["drug"] == "adderall":
			the_result = the_result*.8		
		if player["per"] == "reactive":
			the_result = the_result*1.25
		elif player["per"] == "stoic":
			the_result = the_result*.8	
		if player["c_pos"] == "skirmish":
			the_result = the_result*2
		elif player["c_pos"] == "snipe":
			the_result = the_result*.5
	elif chk == "pot":
		the_result = player["s_eva"] - the_roll
		if player["per"] == "ambitious":
			the_result = the_result+20
		if the_result < 0 and team["Mentor"] != -1:
			the_result = random.randint(0,99) - team["Mentor"]
	elif chk == "fit":
		the_result = player["s_eva"] - the_roll
		if player["drug"] == "steroid":
			the_result = the_result+20
		if the_result < 0 and team["Medical"] != -1:
			the_result = random.randint(0,99) - team["Medical"]
	# Check for results
	# Round result
	round(the_result)
	if p["inj"] > 0:
		the_result = the_result - 50
	#If 90+, a light was generated
	if the_result > 89 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" made a highlight play!","l",0)
		team["Lights"] = team["Lights"] + 1
	#50+ earns exp, -50 earns fatigute
	if the_result > 49 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" learned something!","l",0)
		player["exp"] = player["exp"] + 1
	elif the_result < -49 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" may have injured himself!","l",0)
		player["fat"] = player["fat"] + 1
	game_log(player['name']+" rolled a "+str(the_result)+" for "+chk,"l",0)
	return the_result


def game_log(msg,tier,d_flag):
	#Will write to a file eventually
	#Tiers: d - debug,l - log only, t - terminal and log, f - format (screen only)
	#Don't show die rolls to screen?
	if tier == 't':
		print(msg)
		time.sleep(1)
		l_load = open("game_log.txt","a")
		l_load.write(msg+"\n")
		l_load.close()	
		return
	elif tier == 'l':
		l_load = open("game_log.txt","a")
		l_load.write(msg+"\n")
		l_load.close()
		return
	elif tier == 'd':
		if d_flag == 1:
			print(msg)
			l_load = open("game_debug.txt","a")
			l_load.write(msg+"\n")
			l_load.close()
	elif tier == 'f':
		print(msg)
		time.sleep(1)	
		return
