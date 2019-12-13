#!/bin/python
#WORLD CHAMPIONSHIP LAZER TAG
#Single Game Debugger
import random

def die_roll(chk,player,team):
	the_roll = random.randint(0,99)
	if chk == "int":
		the_result = player["s_int"] - the_roll
		if player["drug"] == "cocaine":
			the_result = the_result*1.25
		elif player["drug"] == "marijuana":
			the_result = the_result*.8		
		if player["per"] == "aggressive":
			the_result = the_result*1.25
		elif player["per"] == "cautious":
			the_result = the_result*.8	
		if player["c_pos"] == "skirmisher":
			the_result = the_result*2
		elif player["c_pos"] == "guard":
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
		if player["c_pos"] == "battleline":
			the_result = the_result*2
		elif player["c_pos"] == "skirmisher":
			the_result = the_result*.5
	elif chk == "eva":
		the_result = player["s_eva"] - the_roll
		if player["drug"] == "marijuana":
			the_result = the_result*1.25
		elif player["drug"] == "adderall":
			the_result = the_result*.8		
		if player["per"] == "cautious":
			the_result = the_result*1.25
		elif player["per"] == "stoic":
			the_result = the_result*.8	
		if player["c_pos"] == "guard":
			the_result = the_result*2
		elif player["c_pos"] == "battleline":
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
		game_log(player["name"]+" made a highlighut play!")
		team["Lights"] = team["Lights"] + 1
	#50+ earns exp, -25 earns fatigute
	if the_result > 49 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" learned something!")
		player["exp"] = player["exp"] + 1
	elif the_result < -25 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" may have injured himself!")
		player["fat"] = player["fat"] + 1


def game_log(msg):
	#Will write to a file eventually
	print(msg)
	sleep 2


#Handles game from loading teams from file
#Up until gaining credits

all_players = []
#Load Home Team
h_team={"name":"hometeam","points":0,"Medicial":-1,"Mentor":-1,"Marketeer":-1,"Lights":0,"Fan_Exp":0,"Fan_Cap":0,"Coach_Cost":0}
#Load Players
for x in h_load:
	xi = x.split()
	if xi[0] == "medic":
		h_team["Medical"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + xi[15]
	elif xi[0] == "mentor":
		h_team["Mentor"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + xi[15]
	elif xi[0] == "marketeer":
		h_team["Markteer"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + xi[15]
	elif xi[0] == "medic":
		h_team["Medical"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + xi[15]
	elif xi[0] = "stadium":
		h_team["Fan_Exp"] = xi[1]
		h_team["Fan_Cap"] = xi[2]
	elif xi[0] == "roster-player":
		new_player={"name":xi[0],"team":"home",
		"s_int":xi[1],"s_acc":xi[2],"s_eva":xi[3],"s_pot":xi[4],"s_fit":xi[5],"s_ego":xi[6],"s_kno":xi[7],
		"per":xi[8],"drug":xi[9],
		"r_init":0,"r_shts":0,"r_hit":0,
		"c_pos":"","w_pos":xi[10],"sw_pos":xi[11],"l_pos":xi[12],"sl_pos":xi[13],
		"exp":0,"fat":0,
		"inj":xi[14],"g_ht":0,"g_ph":0,"g_fc":0,"g_st":0,"g_cost":xi[14]}
		all_players.append(new_player)

#Load Away Team
a_team={"name":"hometeam","points":0,"Medicial":-1,"Mentor":-1,"Marketeer":-1,"Lights":0,"Fan_Exp":0,"Fan_Cap":0,"Coach_Cost":0}
#Load Players
for x in a_load:
	xi = x.split()
	if xi[0] == "medic":
		a_team["Medical"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + xi[15]
	elif xi[0] == "mentor":
		a_team["Mentor"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + xi[15]
	elif xi[0] == "marketeer":
		a_team["Markteer"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + xi[15]
	elif xi[0] == "medic":
		a_team["Medical"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + xi[15]
	elif xi[0] = "stadium":
		a_team["Fan_Exp"] = xi[1]
		a_team["Fan_Cap"] = xi[2]
	elif xi[0] == "roster-player":
		new_player={"name":xi[0],"team":"away",
		"s_int":xi[1],"s_acc":xi[2],"s_eva":xi[3],"s_pot":xi[4],"s_fit":xi[5],"s_ego":xi[6],"s_kno":xi[7],
		"per":xi[8],"drug":xi[9],
		"r_init":0,"r_shts":0,"r_hit":0,
		"c_pos":"","w_pos":xi[10],"sw_pos":xi[11],"l_pos":xi[12],"sl_pos":xi[13],
		"exp":0,"fat":0,
		"inj":xi[14],"g_ht":0,"g_ph":0,"g_fc":0,"g_st":0,"g_cost":xi[14]}
		all_players.append(new_player)
#Be sure to close files!

clock = 1
game_log("Match Begins!")

while clock < 21:
	#Figure out the game state and set the actions and reset round info
	if a_team["Points"]+10 < h_team["Points"]:
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["w_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["l_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
		#Home team winning by wide margin
		#Away team winning by wide margin
	elif a_team["Points"] > h_team["Points"]+10:
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["l_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["w_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
	elif a_team["Points"] < h_team["Points"]:
		#Home team winning by small margin
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["sw_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["sl_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
	elif a_team["Points"] > h_team["Points"]:
		#Away team winning by small margin
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["sl_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["sw_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000

	#Roll initative for all players
	for p in all_players:
		if p["c_pos"] == "bench":
			continue
		else:
			if p["team"]="home"
				p["r_init"]=die_roll("int",p,h_team)
			elif p["team"]="away"
				p["r_init"]=die_roll("int",p,a_team)

	#Count shots
	for p in all_players:
		if p["c_pos"] == "bench" or p["c_pos"] != "ambush":
			continue
		p["r_shts"] = p["r_shts"] + 1
		if p["c_pos"] == "fteam":
			p["r_shts"] = p["r_shts"] + 1
		if p["per"] == "ambitious":
			p["r_shts"] = p["r_shts"] + 1

	#Sort all players

	#Shooting
	shots_remaining = 0
	for s in all_players:
		shots_remaining = shots_remaining + s["r_shts"]

	active = 0

	while shots_remaining > 0:
		if all_players[active]["r_shts"] > 1:
			all_players[active]["r_shts"] = all_players[active]["r_shts"] - 1
			stealing = 1
			#Check action
			if all_players[active]["c_pos"] == "steal":
				#Look for ambush
				for ambu in all_players:
					if ambu["team"] != all_players[active]["team"] and ambu["c_pos"] == "ambush" and ambu["r_hit"] == 0:
						ambu["g_st"] = ambu["g_st"] + 1
						if ambu[team] == "home":
							ambush = die_roll("acc",ambu,h_team)
							dodge = die_roll("eva",all_players[active],a_team)
							if ambush > dodge:
								game_log(ambu["name"]+" defends their flag from "+all_players[active]["name"]+"!")
								h_team["points"] = h_team["points"] + 1
								ambu["g_ph"] = ambu["g_ph"] + 1
								stealing = 0
						elif ambu[team] == "away":
							ambush = die_roll("acc",ambu,a_team)
							dodge = die_roll("eva",all_players[active],t_team)
							if ambush > dodge:
								game_log(ambu["name"]+" defends their flag from "+all_players[active]["name"]+"!")
								a_team["points"] = a_team["points"] + 1
								ambu["g_ph"] = ambu["g_ph"] + 1
								stealing = 0
				#If unhit, steal!
				if stealing == 1:
					game_log(all_players[active]["name"]+" has stolen the enemy flag and ended the round!")
					if all_players[active]["team"] == "home"
						h_team["points"] = h_team["points"] + 4
						all_players[active]["g_fc"] = all_players[active]["g_fc"] + 1
					elif all_players[active]["team"] == "away"
						a_team["points"] = a_team["points"] + 4
						all_players[active]["g_fc"] = all_players[active]["g_fc"] + 1
					break
			else:
				#Else, find targets
				target = len(all_players) - 1
				while target > 0:
					if all_players[target]["team"] != all_players[active]["team"] and all_players[target]["c_pos"] != "bench" and all_players[target]["r_hit"] == 0:
						#Shoot at the target!
						all_players[target]["g_st"] = all_players[target]["g_st"] + 1
						stealing = 0
						if all_players[active]["team"] == "home":
							attack = die_roll("acc",all_players[active],h_team)
							dodge = die_roll("eva",all_players[target],a_team)
							if attack > dodge:
								game_log(all_players[active]["name"]+" hits "+all_players[target]["name"]+"!")
								h_team["points"] = h_team["points"] + 1
								all_players[active]["g_ph"] = all_players[active]["g_ph"] + 1
								all_players[target]["r_hit"] = 1
								break
							else:
								game_log(all_players[active]["name"]+" misses "+all_players[target]["name"]+"!")								
								break
						if all_players[active]["team"] == "away":
							attack = die_roll("acc",all_players[active],a_team)
							dodge = die_roll("eva",all_players[target],h_team)
							if attack > dodge:
								game_log(all_players[active]["name"]+" hits "+all_players[target]["name"]+"!")
								a_team["points"] = a_team["points"] + 1
								all_players[active]["g_ph"] = all_players[active]["g_ph"] + 1
								all_players[target]["r_hit"] = 1
								break
							else:
								game_log(all_players[active]["name"]+" misses "+all_players[target]["name"]+"!")								
								break
					target = target - 1					

				#If you can't find a target, take the flag
				if stealing == 1:
					game_log(all_players[active]["name"]+" has stolen the unprotected enemy flag and ended the round!")
					if all_players[active]["team"] == "home"
						game_log("The away team had no players to protect the flag")
						h_team["points"] = h_team["points"] + 4
					elif all_players[active]["team"] == "away"
						game_log("The home team had no players to protect the flag")
						a_team["points"] = a_team["points"] + 4
					break

		#Count remaining shots
		for s in all_players:
			if s[r_hit] == 1:
				s["r_shts"] = 0
			shots_remaining = shots_remaining + s["r_shts"]
		if shots_remaining == 0:
			game_log("No shots remaining")
			break
		#Choose next
		if active == len(all_players) - 1:
			active = 0
		else:
			active = active + 1

		#If not 
	#Clock Advance
	game_log("end of round "+clock)
	game_log("Home: "+h_home["points"])
	game_log("Away: "+a_home["points"])
	clock = clock + 1



#################END OF GAME#################

#Final
game_log("FINAL SCORE:")
game_log("Home: "+h_home["points"])
game_log("Away: "+a_home["points"])

#Sort players for better stat view
#Stats
game_log("FINAL STATS:")
game_log("Player\t\tHits\tShots\tFlags\tShooting %\tPoints Earned\tHits Taken\tHit +/-")
for p in all_players:
	try:
		sp = p["g_ph"]/p["g_st"]
	else:
		sp = "NA"
	pp = p["g_ph"]+(p["g_fc"]*4)
	ppm = p["g_ht"]+(p["g_fc"]*4)
	game_log(p["name"]+":\t"+p["g_ph"]+"\t"+p["g_st"]+"\t"+p["g_fc"]+"\t"+sp+"\t"+pp+"\t"+p["g_ht"]+"\t"+ppm)

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
			h_gamecost = h_gamecost + p["g_cost"]
			if p["drug"] != "none":
				h_gamecost = h_gamecost + 1000
		if p["team"] == "away":
			a_gamecost = a_gamecost + p["g_cost"]
			if p["drug"] != "none":
				a_gamecost = a_gamecost + 1000

#Net totals
a_net = a_cashtot - a_gamecost
h_net = h_cashtot - h_gamecost

game_log("The away team earned "+a_net)
game_log("The home team earned "+h_net)


# Level Ups
for p in players:
	lurs = 0
	if p["team"] == "home"
		luas = p["exp"]
		while luas > 0:
			lu_att = die_roll("pot",p,h_team)
			if lu_att > 0:
				lurs = lurs + 1
			luas = luas - 1
	if p["team"] == "away"
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
	"s_int":x[1],"s_acc":x[2],"s_eva":x[3],"s_pot":x[4],"s_fit":x[5],"s_ego":x[6],"s_kno":x[7],
		lu_set = ["int","int","int","acc","acc","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "stoic":
		lu_set = ["int","acc","acc","acc","acc","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "cautious":
		lu_set = ["int","int","acc","eva","eva","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "ambitious":
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","ego","ego","kno"]
	elif p["per"] == "eager":
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","kno","kno","kno"]
	else:
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","ego","kno","kno"]
	while lurs > 0:
		this_lvl = random.choice(lu_set)
		if this_lvl = "int":
			p["s_int"] = p["s_int"] + 1
			game_log(p["name"]+" leveled up initiative!")
		elif this_lvl = "acc":
			p["s_acc"] = p["s_acc"] + 1
			game_log(p["name"]+" leveled up accuracy!")
		elif this_lvl = "eva":
			p["s_eva"] = p["s_eva"] + 1
			game_log(p["name"]+" leveled up evasion!")
		elif this_lvl = "fit":
			p["s_fit"] = p["s_fit"] + 1
			game_log(p["name"]+" leveled up fitness!")
		elif this_lvl = "ego":
			p["s_ego"] = p["s_ego"] + 1
			game_log(p["name"]+" leveled up ego!")
		elif this_lvl = "kno":
			p["s_kno"] = p["s_kno"] + 1
			game_log(p["name"]+" leveled up knowledge!")
		lurs = lurs - 1

#Injuries
for p in players:
	inrc = 0
	if p["team"] == "home"
		inrk = p["fat"]
		while inrk > 0:
			lu_att = die_roll("fit",p,h_team)
			if lu_att > 0:
				inrc = inrc + 1
			inrk = inrk - 1
	if p["team"] == "away"
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
	game_log(p["name"] + " is injured for "+total_in+" games")
	p["inj"] = p["inj"] + total_in

#Save
#Add to all time stats?
