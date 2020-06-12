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


#Handles game from loading teams from file
#Up until gaining credits

all_players = []
#Load Home Team
h_team={"name":"hometeam","points":0,"r_points":0,"r_pref":"","Medicial":-1,"Mentor":-1,"Marketeer":-1,"Lights":0,"Fan_Exp":0,"Fan_Cap":0,"Coach_Cost":0,"tac1_pref":0,"tac2_pref":0,"tac3_pref":0}
#Load Players
h_path = input("Home Team File: ")
h_load = open(h_path,"r+")
for x in h_load:
	xi = x.split(':')
	if xi[0] == "medic":
		h_team["Medical"] = int(xi[8])
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "mentor":
		h_team["Mentor"] = int(xi[8])
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "marketeer":
		h_team["Markteer"] = int(xi[8])
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "medic":
		h_team["Medical"] = int(xi[8])
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "stadium":
		h_team["Fan_Exp"] = int(xi[1])
		h_team["Fan_Cap"] = int(xi[2])
	elif xi[0] == "name":
		h_team["name"] = xi[1].rstrip()
	elif xi[0] == "tac1_pref":
		h_team["tac1_pref"] = int(xi[1])
	elif xi[0] == "tac2_pref":
		h_team["tac2_pref"] = int(xi[1])
	elif xi[0] == "tac3_pref":
		h_team["tac3_pref"] = int(xi[1])
	elif xi[0] == "roster-player":
		new_player={"name":xi[1],"team":"home",
		"s_int":int(xi[2]),"s_acc":int(xi[3]),"s_eva":int(xi[4]),"s_pot":int(xi[5]),"s_fit":int(xi[6]),"s_ego":int(xi[7]),"s_kno":int(xi[8]),
		"per":xi[9],"drug":xi[10],
		"r_init":0,"r_shts":0,"r_hit":0,
		"c_pos":"","tac1":xi[11],"tac2":xi[12],"tac3":xi[13],
		"exp":0,"fat":0,
		"inj":int(xi[14]),"g_ht":0,"g_ph":0,"g_fc":0,"g_st":0,"g_rd":0,"g_cost":int(xi[22]),
		"c_ht":int(xi[16]),"c_ph":int(xi[17]),"c_fc":int(xi[18]),"c_st":int(xi[15]),"c_rd":int(xi[19])}
		all_players.append(new_player)

#Load Away Team
a_team={"name":"awayteam","points":0,"r_points":0,"r_pref":"","Medicial":-1,"Mentor":-1,"Marketeer":-1,"Lights":0,"Fan_Exp":0,"Fan_Cap":0,"Coach_Cost":0,"tac1_pref":0,"tac2_pref":0,"tac3_pref":0}
#Load Players
a_path = input("Away Team File: ")
a_load = open(a_path,"r+")

for x in a_load:
	xi = x.split(':')
	if xi[0] == "medic":
		a_team["Medical"] = int(xi[8])
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "mentor":
		a_team["Mentor"] = int(xi[8])
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "marketeer":
		a_team["Markteer"] = int(xi[8])
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "medic":
		a_team["Medical"] = int(xi[8])
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "stadium":
		a_team["Fan_Exp"] = int(xi[1])
		a_team["Fan_Cap"] = int(xi[2])
	elif xi[0] == "name":
		a_team["name"] = xi[1].rstrip()
	elif xi[0] == "tac1_pref":
		a_team["tac1_pref"] = int(xi[1])
	elif xi[0] == "tac2_pref":
		a_team["tac2_pref"] = int(xi[1])
	elif xi[0] == "tac3_pref":
		a_team["tac3_pref"] = int(xi[1])
	elif xi[0] == "roster-player":
		new_player={"name":xi[1],"team":"away",
		"s_int":int(xi[2]),"s_acc":int(xi[3]),"s_eva":int(xi[4]),"s_pot":int(xi[5]),"s_fit":int(xi[6]),"s_ego":int(xi[7]),"s_kno":int(xi[8]),
		"per":xi[9],"drug":xi[10],
		"r_init":0,"r_shts":0,"r_hit":0,
		"c_pos":"","tac1":xi[11],"tac2":xi[12],"tac3":xi[13],
		"exp":0,"fat":0,
		"inj":int(xi[14]),"g_ht":0,"g_ph":0,"g_fc":0,"g_st":0,"g_rd":0,"g_cost":int(xi[22]),
		"c_ht":int(xi[16]),"c_ph":int(xi[17]),"c_fc":int(xi[18]),"c_st":int(xi[15]),"c_rd":int(xi[19])}
		all_players.append(new_player)
#Be sure to close files at the end

#Save starting preferences for tactics
h_t1_s = h_team["tac1_pref"]
h_t2_s = h_team["tac2_pref"]
h_t3_s = h_team["tac3_pref"]

a_t1_s = a_team["tac1_pref"]
a_t2_s = a_team["tac2_pref"]
a_t3_s = a_team["tac3_pref"]

clock = 1
half = 1
ot = 0
# If this is a playoff game, change ot = 2
game_log("Match Begins!","t",0)

while (clock <= 16 and half <=2) or ot == 1:
	#Choose tactics by building rolls
	a_tac_range = a_team["tac1_pref"]+a_team["tac2_pref"]+a_team["tac3_pref"]
	h_tac_range = h_team["tac1_pref"]+h_team["tac2_pref"]+h_team["tac3_pref"]

	# Based on roll range, set tactic
	a_tac_roll = random.randint(0,a_tac_range)
	if a_tac_roll < a_team["tac1_pref"]:
		for p in all_players:
			if p["team"] == "away":
				p["c_pos"] = p["tac1"]
		a_team["r_pref"] = "tac1"
		# game_log("Away team chose tactic 1","t",0)
	elif a_tac_roll < a_team["tac1_pref"]+a_team["tac2_pref"] and a_tac_roll > a_team["tac1_pref"]:
		for p in all_players:
			if p["team"] == "away":
				p["c_pos"] = p["tac2"]
		a_team["r_pref"] = "tac2"
		# game_log("Away team chose tactic 2","t",0)
	else:
		for p in all_players:
			if p["team"] == "away":
				p["c_pos"] = p["tac3"]
		a_team["r_pref"] = "tac3"
		# game_log("Away team chose tactic 3","t",0)

	h_tac_roll = random.randint(0,h_tac_range)
	if h_tac_roll < h_team["tac1_pref"]:
		for p in all_players:
			if p["team"] == "home":
				p["c_pos"] = p["tac1"]
		h_team["r_pref"] = "tac1"
		# game_log("Home team chose tactic 1","t",0)
	elif h_tac_roll < h_team["tac1_pref"]+h_team["tac2_pref"] and h_tac_roll > h_team["tac1_pref"]:
		for p in all_players:
			if p["team"] == "home":
				p["c_pos"] = p["tac2"]
		h_team["r_pref"] = "tac2"
		# game_log("Home team chose tactic 2","t",0)
	else:
		for p in all_players:
			if p["team"] == "home":
				p["c_pos"] = p["tac3"]
		h_team["r_pref"] = "tac3"
		# game_log("Home team chose tactic 3","t",0)

	#Roll initative for all players
	for p in all_players:
		# Reset from the previous round
		p["r_shts"] = 0
		p["r_hit"] = 0
		p["r_init"] = -1000
		if p["c_pos"] == "bench":
			continue
		else:
			p["g_rd"] = p["g_rd"] + 1
			if p["team"]=="home":
				p["r_init"]=die_roll("int",p,h_team)
			elif p["team"]=="away":
				p["r_init"]=die_roll("int",p,a_team)
			#Count shots
			if p["c_pos"] != "ambush":
				p["r_shts"] = p["r_shts"] + 1
				if p["c_pos"] == "freefire":
					p["r_shts"] = p["r_shts"] + 1
				if p["per"] == "ambitious":
					p["r_shts"] = p["r_shts"] + 1				


	#Sort all players
	all_players = sorted(all_players, key=itemgetter('r_init'), reverse=True)

	#Shooting
	shots_remaining = 0
	for s in all_players:
		shots_remaining = shots_remaining + s["r_shts"]

	active = 0
	#print(shots_remaining)
	while shots_remaining > 0:
		# print(all_players[active]['name']+" is up to "+all_players[active]['c_pos']+" , shots remaining "+str(all_players[active]['r_shts'])+" , times hit "+str(all_players[active]['r_hit']))
		if all_players[active]["r_shts"] > 0:
			# print("player is acting")
			all_players[active]["r_shts"] = all_players[active]["r_shts"] - 1
			stealing = 1
			#Check action
			if all_players[active]["c_pos"] == "steal":
				#Look for ambush
				for ambu in all_players:
					if ambu["team"] != all_players[active]["team"] and ambu["c_pos"] == "ambush" and ambu["r_hit"] == 0:
						ambu["g_st"] = ambu["g_st"] + 1
						if ambu["team"] == "home":
							ambush = die_roll("acc",ambu,h_team)
							dodge = die_roll("eva",all_players[active],a_team)
							if ambush > dodge:
								game_log(ambu["name"]+" defends their flag from "+all_players[active]["name"]+"!","t",0)
								h_team["r_points"] = h_team["r_points"] + 1
								ambu["g_ph"] = ambu["g_ph"] + 1
								all_players[active]["g_ht"] = all_players[active]["g_ht"] + 1
								stealing = 0
								break
						elif ambu["team"] == "away":
							ambush = die_roll("acc",ambu,a_team)
							dodge = die_roll("eva",all_players[active],h_team)
							if ambush > dodge:
								game_log(ambu["name"]+" defends their flag from "+all_players[active]["name"]+"!","t",0)
								a_team["r_points"] = a_team["r_points"] + 1
								all_players[active]["g_ht"] = all_players[active]["g_ht"] + 1
								ambu["g_ph"] = ambu["g_ph"] + 1
								stealing = 0
								break
				#If unhit, steal!
				if stealing == 1:
					game_log(all_players[active]["name"]+" has stolen the enemy flag and ended the round!","t",0)
					if all_players[active]["team"] == "home":
						h_team["r_points"] = h_team["r_points"] + 4
						all_players[active]["g_fc"] = all_players[active]["g_fc"] + 1
					elif all_players[active]["team"] == "away":
						a_team["r_points"] = a_team["r_points"] + 4
						all_players[active]["g_fc"] = all_players[active]["g_fc"] + 1
					break
			else:
				#Else, find targets
				# print("Looking for target")
				target = len(all_players) - 1
				while target > 0:
					if all_players[target]["team"] != all_players[active]["team"] and all_players[target]["c_pos"] != "bench" and all_players[target]["r_hit"] == 0:
						#Shoot at the target!
						all_players[active]["g_st"] = all_players[active]["g_st"] + 1
						stealing = 0
						if all_players[active]["team"] == "home":
							attack = die_roll("acc",all_players[active],h_team)
							dodge = die_roll("eva",all_players[target],a_team)
							if attack > dodge:
								game_log(all_players[active]["name"]+" hits "+all_players[target]["name"]+"!","t",0)
								h_team["r_points"] = h_team["r_points"] + 1
								all_players[active]["g_ph"] = all_players[active]["g_ph"] + 1
								all_players[target]["r_hit"] = 1
								all_players[target]["g_ht"] = all_players[target]["g_ht"] + 1
								break
							else:
								game_log(all_players[active]["name"]+" misses "+all_players[target]["name"]+"!","t",0)								
								break
						if all_players[active]["team"] == "away":
							attack = die_roll("acc",all_players[active],a_team)
							dodge = die_roll("eva",all_players[target],h_team)
							if attack > dodge:
								game_log(all_players[active]["name"]+" hits "+all_players[target]["name"]+"!","t",0)
								a_team["r_points"] = a_team["r_points"] + 1
								all_players[active]["g_ph"] = all_players[active]["g_ph"] + 1
								all_players[target]["r_hit"] = 1
								all_players[target]["g_ht"] = all_players[target]["g_ht"] + 1
								break
							else:
								game_log(all_players[active]["name"]+" misses "+all_players[target]["name"]+"!","t",0)								
								break
					target = target - 1					

				#If you can't find a target, take the flag
				if stealing == 1:
					game_log(all_players[active]["name"]+" has stolen the unprotected enemy flag and ended the round!","t",0)
					if all_players[active]["team"] == "home":
						game_log("The away team had no players to protect the flag","t",0)
						h_team["r_points"] = h_team["r_points"] + 4
					elif all_players[active]["team"] == "away":
						game_log("The home team had no players to protect the flag","t",0)
						a_team["r_points"] = a_team["r_points"] + 4
					break

		#Count remaining shots
		#print("end of shooting round")
		shots_remaining = 0
		for s in all_players:
			if s["r_hit"] == 1:
				s["r_shts"] = 0
			shots_remaining = shots_remaining + s["r_shts"]

		if shots_remaining == 0:
			game_log("No shots remaining","l",0)
			break
		#Choose next
		if active == len(all_players) - 1:
			active = 0
		else:
			active = active + 1

		#If not

	# Advance add in points, change preferences:
	# +1 if you won the round with this tactic
	# -1 down to 1 if you lost the round with this tactic
	# No change for ties

	if h_team["r_points"] > a_team["r_points"]:
		if h_team["r_pref"] == "tac1":
			h_team["tac1_pref"] = h_team["tac1_pref"] + 1
		elif h_team["r_pref"] == "tac2":
			h_team["tac2_pref"] = h_team["tac2_pref"] + 1
		elif h_team["r_pref"] == "tac3":
			h_team["tac3_pref"] = h_team["tac3_pref"] + 1
		if a_team["r_pref"] == "tac1" and a_team["tac1_pref"] > 1:
			a_team["tac1_pref"] = a_team["tac1_pref"] - 1
		elif a_team["r_pref"] == "tac2" and a_team["tac2_pref"] > 1:
			a_team["tac2_pref"] = a_team["tac2_pref"] - 1
		elif a_team["r_pref"] == "tac3" and a_team["tac3_pref"] > 1:
			a_team["tac3_pref"] = a_team["tac3_pref"] - 1
	elif h_team["r_points"] < a_team["r_points"]:
		if a_team["r_pref"] == "tac1":
			a_team["tac1_pref"] = a_team["tac1_pref"] + 1
		elif a_team["r_pref"] == "tac2":
			a_team["tac2_pref"] = a_team["tac2_pref"] + 1
		elif a_team["r_pref"] == "tac3":
			a_team["tac3_pref"] = a_team["tac3_pref"] + 1
		if h_team["r_pref"] == "tac1" and h_team["tac1_pref"] > 1:
			h_team["tac1_pref"] = h_team["tac1_pref"] - 1
		elif h_team["r_pref"] == "tac2" and h_team["tac2_pref"] > 1:
			h_team["tac2_pref"] = h_team["tac2_pref"] - 1
		elif h_team["r_pref"] == "tac3" and h_team["tac3_pref"] > 1:
			h_team["tac3_pref"] = h_team["tac3_pref"] - 1

	# Add the round score into the total, reset
	h_team["points"] = h_team["points"] + h_team["r_points"] 
	h_team["r_points"] = 0
	a_team["points"] = a_team["points"] + a_team["r_points"] 
	a_team["r_points"] = 0

	#Clock Advance
	game_log("==============================","f",0)
	game_log("end of round "+str(clock)+"- half "+str(half),"t",0)
	game_log(h_team["name"]+": "+str(h_team["points"]),"t",0)
	game_log(a_team["name"]+": "+str(a_team["points"]),"t",0)
	game_log("==============================","f",0)
	clock = clock + 1

	if clock == 17 and half == 1:
		game_log("HALF TIME!","t",0)
		half = 2
		clock = 1
		# Halftime adjustments - +4 to the highest total, -2 down to 1 for the lowest, don't touch ties
	
	#Code for overtime halfs would be good to.
	if clock == 17 and half == 2 and ot == 2:
		if h_team["points"] == a_team["points"]:
			game_log("OVERTIME.","t",0)
			ot = 1
	if ot == 1:
		if h_team["points"] != a_team["points"]:
			ot = 0
			



#################END OF GAME#################

#Final
game_log("==============================","f",0)
game_log("FINAL SCORE:","t",0)
game_log(h_team["name"]+": "+str(h_team["points"]),"t",0)
game_log(a_team["name"]+": "+str(a_team["points"]),"t",0)
game_log("==============================","f",0)


#Sort players for better stat view
#Stats
game_log("==============================","f",0)
game_log("FINAL STATS - "+h_team["name"]+":","t",0)
game_log("Player\t\t\t\tHits\tShots\tFlags\tShooting %\tPoints Earned\tHits Taken\tHit +/-","t",0)
for p in all_players:
	if p['team'] == "home":
		try:
			sp = p["g_ph"]/p["g_st"]
		except:
			sp = "NA"
		pp = p["g_ph"]+(p["g_fc"]*4)
		ppm = pp - p["g_ht"]
		game_log(p["name"]+":\t\t"+str(p["g_ph"])+"\t"+str(p["g_st"])+"\t"+str(p["g_fc"])+"\t"+str(sp)+"\t"+str(pp)+"\t"+str(p["g_ht"])+"\t"+str(ppm),"t",0)
game_log("==============================","f",0)
game_log("FINAL STATS - "+a_team["name"]+":","t",0)
game_log("Player\t\t\t\tHits\tShots\tFlags\tShooting %\tPoints Earned\tHits Taken\tHit +/-","t",0)
for p in all_players:
	if p['team'] == "away":
		try:
			sp = p["g_ph"]/p["g_st"]
		except:
			sp = "NA"
		pp = p["g_ph"]+(p["g_fc"]*4)
		ppm = pp - p["g_ht"]
		game_log(p["name"]+":\t\t"+str(p["g_ph"])+"\t"+str(p["g_st"])+"\t"+str(p["g_fc"])+"\t"+str(sp)+"\t"+str(pp)+"\t"+str(p["g_ht"])+"\t"+str(ppm),"t",0)
game_log("==============================","f",0)
game_log("Tactic Preferences","f",0)
game_log(h_team["tac1_pref"],"f",0)
game_log(h_team["tac2_pref"],"f",0)
game_log(h_team["tac3_pref"],"f",0)
game_log(a_team["tac1_pref"],"f",0)
game_log(a_team["tac2_pref"],"f",0)
game_log(a_team["tac3_pref"],"f",0)
game_log("==============================","f",0)

# Money Earned
# Roll for gaining credits
# Credit maximum is determined by the fanbase size
# Credit minimum is determined by the fan experience
# Earn attempts at cash based on
# 90s rolled (Highlight Reel Plays)
# 10 for winning
# A number of bonus dice based on the marketeers knowledge
# D100 - KNO
# For each, roll a die based on fanbase tier:
# 1-5 for D4-D12
# Sum is the amount of credits earned
# Fan experience denotes a minimum level earned
# Pay players, staff, facilities, and drugs used

a_cashtot = 0
h_cashtot = 0
a_gamecost = 0
h_gamecost = 0

if h_team["points"] > a_team["points"]:
	h_cashrolls = 20+h_team["Lights"]

	if h_team["Marketeer"] != -1:
		h_cashrolls = h_cashrolls + (h_team["Marketeer"] - random.randint(0,99))

	if h_team["Fan_Cap"] == 1:
		h_cashtot = h_cashrolls * random.randint(1,4)
	elif h_team["Fan_Cap"] == 2:
		h_cashtot = h_cashrolls * random.randint(1,6)
	elif h_team["Fan_Cap"] == 3:
		h_cashtot = h_cashrolls * random.randint(1,8)
	elif h_team["Fan_Cap"] == 4:
		h_cashtot = h_cashrolls * random.randint(1,10)
	elif h_team["Fan_Cap"] == 5:
		h_cashtot = h_cashrolls * random.randint(1,12)

	a_cashrolls = a_team["Lights"]

	if a_team["Marketeer"] != -1:
		a_cashrolls = a_cashrolls + (a_team["Marketeer"] - random.randint(0,99))

	if a_team["Fan_Cap"] == 1:
		a_cashtot = a_cashrolls * random.randint(1,4)
	elif a_team["Fan_Cap"] == 2:
		a_cashtot = a_cashrolls * random.randint(1,6)
	elif a_team["Fan_Cap"] == 3:
		a_cashtot = a_cashrolls * random.randint(1,8)
	elif a_team["Fan_Cap"] == 4:
		a_cashtot = a_cashrolls * random.randint(1,10)
	elif a_team["Fan_Cap"] == 5:
		a_cashtot = a_cashrolls * random.randint(1,12)

elif h_team["points"] < a_team["points"]:
	h_cashrolls = h_team["Lights"]

	if h_team["Marketeer"] != -1:
		h_cashrolls = h_cashrolls + (h_team["Marketeer"] - random.randint(0,99))

	if h_team["Fan_Cap"] == 1:
		h_cashtot = h_cashrolls * random.randint(1,4)
	elif h_team["Fan_Cap"] == 2:
		h_cashtot = h_cashrolls * random.randint(1,6)
	elif h_team["Fan_Cap"] == 3:
		h_cashtot = h_cashrolls * random.randint(1,8)
	elif h_team["Fan_Cap"] == 4:
		h_cashtot = h_cashrolls * random.randint(1,10)
	elif h_team["Fan_Cap"] == 5:
		h_cashtot = h_cashrolls * random.randint(1,12)

	a_cashrolls = 20+a_team["Lights"]

	if a_team["Marketeer"] != -1:
		a_cashrolls = a_cashrolls + (a_team["Marketeer"] - random.randint(0,99))

	if a_team["Fan_Cap"] == 1:
		a_cashtot = a_cashrolls * random.randint(1,4)
	elif a_team["Fan_Cap"] == 2:
		a_cashtot = a_cashrolls * random.randint(1,6)
	elif a_team["Fan_Cap"] == 3:
		a_cashtot = a_cashrolls * random.randint(1,8)
	elif a_team["Fan_Cap"] == 4:
		a_cashtot = a_cashrolls * random.randint(1,10)
	elif a_team["Fan_Cap"] == 5:
		a_cashtot = a_cashrolls * random.randint(1,12)
# Else tie
else:
	h_cashrolls = h_team["Lights"]

	if h_team["Marketeer"] != -1:
		h_cashrolls = h_cashrolls + (h_team["Marketeer"] - random.randint(0,99))

	if h_team["Fan_Cap"] == 1:
		h_cashtot = h_cashrolls * random.randint(1,4)
	elif h_team["Fan_Cap"] == 2:
		h_cashtot = h_cashrolls * random.randint(1,6)
	elif h_team["Fan_Cap"] == 3:
		h_cashtot = h_cashrolls * random.randint(1,8)
	elif h_team["Fan_Cap"] == 4:
		h_cashtot = h_cashrolls * random.randint(1,10)
	elif h_team["Fan_Cap"] == 5:
		h_cashtot = h_cashrolls * random.randint(1,12)

	a_cashrolls = a_team["Lights"]

	if a_team["Marketeer"] != -1:
		a_cashrolls = a_cashrolls + (a_team["Marketeer"] - random.randint(0,99))

	if a_team["Fan_Cap"] == 1:
		a_cashtot = a_cashrolls * random.randint(1,4)
	elif a_team["Fan_Cap"] == 2:
		a_cashtot = a_cashrolls * random.randint(1,6)
	elif a_team["Fan_Cap"] == 3:
		a_cashtot = a_cashrolls * random.randint(1,8)
	elif a_team["Fan_Cap"] == 4:
		a_cashtot = a_cashrolls * random.randint(1,10)
	elif a_team["Fan_Cap"] == 5:
		a_cashtot = a_cashrolls * random.randint(1,12)

#See how fan experience saves them
#Calculate game cost:
	a_gamecost = a_team["Coach_Cost"]
	h_gamecost = h_team["Coach_Cost"]
	for p in all_players:
		if p["team"] == "home":
			h_gamecost = h_gamecost + int(p["g_cost"])
			if p["drug"] != "none":
				h_gamecost = h_gamecost + 1000
		if p["team"] == "away":
			a_gamecost = a_gamecost + int(p["g_cost"])
			if p["drug"] != "none":
				a_gamecost = a_gamecost + 1000

#Net totals
a_net = int(a_cashtot) - int(a_gamecost)
h_net = int(h_cashtot) - int(h_gamecost)

game_log("The away team earned "+str(a_net),"l",0)
game_log("The home team earned "+str(h_net),"l",0)


# Level Ups
for p in all_players:
	lurs = 0
	if p["team"] == "home":
		luas = p["exp"]
		while luas > 0:
			lu_att = die_roll("pot",p,h_team)
			if lu_att > 0:
				lurs = lurs + 1
			luas = luas - 1
	if p["team"] == "away":
		luas = p["exp"]
		while luas > 0:
			lu_att = die_roll("pot",p,a_team)
			if lu_att > 0:
				lurs = lurs + 1
			luas = luas - 1
	if lurs == 0:
		break
	#Set levelup set
	if p["per"] == "aggressive":
		lu_set = ["int","int","int","acc","acc","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "stoic":
		lu_set = ["int","acc","acc","acc","acc","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "reactive":
		lu_set = ["int","int","acc","eva","eva","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "ambitious":
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","ego","ego","kno"]
	elif p["per"] == "eager":
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","kno","kno","kno"]
	else:
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","ego","kno","kno"]
	while lurs > 0:
		this_lvl = random.choice(lu_set)
		if this_lvl == "int":
			p["s_int"] = p["s_int"] + 1
			if p["s_int"] > 99:
				p["s_int"] = 99
			game_log(p["name"]+" leveled up initiative!","l",0)
		elif this_lvl == "acc":
			p["s_acc"] = p["s_acc"] + 1
			if p["s_acc"] > 99:
				p["s_acc"] = 99
			game_log(p["name"]+" leveled up accuracy!","l",0)
		elif this_lvl == "eva":
			p["s_eva"] = p["s_eva"] + 1
			if p["s_eva"] > 99:
				p["s_eva"] = 99
			game_log(p["name"]+" leveled up evasion!","l",0)
		elif this_lvl == "fit":
			p["s_fit"] = p["s_fit"] + 1
			if p["s_fit"] > 99:
				p["s_fit"] = 99
			game_log(p["name"]+" leveled up fitness!","l",0)
		elif this_lvl == "ego":
			p["s_ego"] = p["s_ego"] + 1
			if p["s_ego"] > 99:
				p["s_ego"] = 99
			game_log(p["name"]+" leveled up ego!","l",0)
		elif this_lvl == "kno":
			p["s_kno"] = p["s_kno"] + 1
			if p["s_kno"] > 99:
				p["s_kno"] = 99
			game_log(p["name"]+" leveled up knowledge!","l",0)
		lurs = lurs - 1

#Injuries
for p in all_players:
	continue
	#THIS IS TO STOP IT FOR TESTING! RENABLE THIS LATER!
	inrc = 0
	if p["team"] == "home":
		inrk = p["fat"]
		while inrk > 0:
			lu_att = die_roll("fit",p,h_team)
			if lu_att > 0:
				inrc = inrc + 1
			inrk = inrk - 1
	if p["team"] == "away":
		inrk = p["fat"]
		while inrk > 0:
			lu_att = die_roll("fit",p,a_team)
			if lu_att > 0:
				inrc = inrc + 1
			inrk = inrk - 1
	if inrc == 0:
		break
	total_in = 0
	while inrc > 0:
		#Roll assuming D10 for now
		total_in = total_in + random.randint(1,10)
		inrc = inrc - 1
	game_log(p["name"] + " is injured for "+str(total_in)+" games","l",0)
	p["inj"] = p["inj"] + total_in

#Stats
for p in all_players:
	p["c_ht"] = p["c_ht"] + p["g_ht"]
	p["c_ph"] = p["c_ph"] + p["g_ph"]
	p["c_fc"] = p["c_fc"] + p["g_fc"]
	p["c_st"] = p["c_st"] + p["g_st"]
	p["c_rd"] = p["c_rd"] + p["g_rd"]

#Save Question?
a_load.close()
h_load.close()
sv_choice = input("Save Results?(Y/n): ")
if sv_choice == "Y":
	h_load = open(h_path,"r")
	h_data = h_load.readlines()
	h_load.close()
	h_load = open(h_path,"w")
	for x in h_data:
		xi = x.split(":")
		if xi[0] == "treasure":
			new_treasure = int(xi[1]) + h_net
			new_line = "tresaure:"+str(new_treasure)
			h_load.write(new_line)
		if xi[0] == "roster-player":
			#Find the player in all players that matches
			for p in all_players:
				if p["name"] == xi[1] and p["team"] == "home":
					updated_player = "roster-player:"+p["name"]+":"+str(p["s_int"])+":"+str(p["s_acc"])+":"+str(p["s_eva"])+":"+str(p["s_pot"])+":"+str(p["s_fit"])+":"+str(p["s_ego"])+":"+str(p["s_kno"])+":"+p["per"]+":"+p["drug"]+":"+p["tac1"]+":"+p["tac2"]+":"+p["tac3"]+":"+str(p["inj"])+":"+str(p["c_st"])+":"+str(p["c_ht"])+":"+str(p["c_ph"])+":"+str(p["c_fc"])+":"+str(p["c_rd"])+":"+xi[20]+":"+xi[21]+":"+xi[22]+":"+xi[23]+":"+xi[24]
					h_load.write(updated_player)

		else:
			h_load.write(x)

	a_load = open(a_path,"r")
	a_data = a_load.readlines()
	a_load.close()
	a_load = open(a_path,"w")
	for x in a_data:
		xi = x.split(":")
		if xi[0] == "treasure":
			new_treasure = int(xi[1]) + a_net
			new_line = "tresaure:"+str(new_treasure)
			a_load.write(new_line)
		if xi[0] == "roster-player":
			#Find the player in all players that matches
			for p in all_players:
				if p["name"] == xi[1] and p["team"] == "away":
					updated_player = "roster-player:"+p["name"]+":"+str(p["s_int"])+":"+str(p["s_acc"])+":"+str(p["s_eva"])+":"+str(p["s_pot"])+":"+str(p["s_fit"])+":"+str(p["s_ego"])+":"+str(p["s_kno"])+":"+p["per"]+":"+p["drug"]+":"+p["tac1"]+":"+p["tac2"]+":"+p["tac3"]+":"+str(p["inj"])+":"+str(p["c_st"])+":"+str(p["c_ht"])+":"+str(p["c_ph"])+":"+str(p["c_fc"])+":"+str(p["c_rd"])+":"+xi[20]+":"+xi[21]+":"+xi[22]+":"+xi[23]+":"+xi[24]
					a_load.write(updated_player)


		else:
			a_load.write(x)
