#!/bin/python
#Turn processor for l33t
#v0.0.2
import random

def list_victims(pa):
	#List all players with a number
	choice = 0
	for p in pa:
		s = choice + " - " + p["name"]
		print(s)
		choice = choice + 1
	target = input("Chose Target: ")
	return target
#Load player from file eventually
#lf = open('load','w')

#Creates an array of players like so:
p1 = {"name":"","action":"","target":"","action_m":"","target_m":"","role":"","gang":"","gov":"","cp":0,"account":0,"limit":0,"kin":"","transactions":[],"whispers":[],"investments":[]}

pa = [p1,]
broadcasts = []

pool = 10
limit = 6

#Assign actions
for p in pa:
	#Must be reasonable
	r = 0
	while r == 0:
		print("Action for "+p)
		if p["role"] == "pleb" or p["role"] == "cartel":
			print("H-Hide")
			print("Z-Zap")
			print("S-Secure")
			print("F-Follow")
			print("D-DoS")
			print("M-Mine")
		if p["gov"] == "admin":
			print("C-Consolidate Power")
			print("I-Investigation")
		if p["role"] == "ghost":
			print("H-Hide")
			print("N-Haunt")
		if p["role"] == "Blackhat":
			print("E-Engineer")
		ac = input("Choice: ")
		if ac = 'H':
			p["action"] = "hide"
			break
		elif ac = 'Z'
			p["target"] = list_victims(pa)
			p["action"] = "zap"
			break
		elif ac = 'S'
			p["target"] = list_victims(pa)
			p["action"] = "secure"
			break
		elif ac = 'F'
			p["target"] = list_victims(pa)
			break
		elif ac = 'D'
			p["target"] = list_victims(pa)
			p["action"] = "dos"
			break
		elif ac = 'M':
			p["action"] = "mine"
			if p["role"] == "leader":
				p["target"] = input("amount to mine: ")
		elif ac = 'C':
			if p["account"] < 15:
				continue
			else:
				p["action"] = "consolidate"
				break
		elif ac = 'N':
			p["target"] = list_victims(pa)
			p["action"] = "haunt"
			break
		elif ac = 'I':
			p["target"] = list_victims(pa)
			p["action"] = "investigate"
			break
		elif ac = 'E':
			if p["account"] < 10:
				continue
			else:
				target_a = list_victims(pa)
				target_b = list_victims(pa)
				target_c = target_a+"-"+target_b
				p["target"] = target_c
				p["action"] = "engineer"
				break
		print("Error - Invalid Choice")

#Moderator chooses second order
for p in pa:
	#Must be reasonable
	if p["gov"] == "mod":
		r = 0
		while r == 0:
			print("Action for "+p)
			if p["role"] == "pleb" or p["role"] == "cartel":
				print("H-Hide")
				print("Z-Zap")
				print("S-Secure")
				print("F-Follow")
				print("D-DoS")
				print("M-Mine")
			if p["gov"] == "admin":
				print("C-Consolidate Power")
				print("I-Investigation")
			if p["role"] == "ghost":
				print("H-Hide")
				print("N-Haunt")
			if p["role"] == "Blackhat":
				print("E-Engineer")
			ac = input("Choice: ")
			if ac = 'H':
				p["action"] = "hide"
				break
			elif ac = 'Z'
				p["target"] = list_victims(pa)
				p["action"] = "zap"
				break
			elif ac = 'S'
				p["target"] = list_victims(pa)
				p["action"] = "secure"
				break
			elif ac = 'F'
				p["target"] = list_victims(pa)
				break
			elif ac = 'D'
				p["target"] = list_victims(pa)
				p["action"] = "dos"
				break
			elif ac = 'M':
				p["action"] = "mine"
				if p["role"] == "leader":
					p["target"] = input("amount to mine: ")
			elif ac = 'C':
				if p["account"] < 15:
					continue
				else:
					p["action"] = "consolidate"
					break
			elif ac = 'N':
				p["target"] = list_victims(pa)
				p["action"] = "haunt"
				break
			elif ac = 'I':
				p["target"] = list_victims(pa)
				p["action"] = "investigate"
				break
			elif ac = 'E':
				if p["account"] < 10:
					continue
				else:
					target_a = list_victims(pa)
					target_b = list_victims(pa)
					target_c = target_a+"-"+target_b
					p["target"] = target_c
					p["action"] = "engineer"
					break
			print("Error - Invalid Choice")
#Carry out actions
for p in pa:
	if p["action"] == "zap":
		#Pay
		if p["role"]
		p['account'] = p['account'] - 3
		s = 1
		#Look for blocker or a bounce
		for b in pa:
			if b['action'] == "secure":
				if b["target"] == p["target"]:
					b["whispers"].append("You caught "+p["name"]+" attacking "+b["target"]+"!")
					p["whispers"].append("Your zap was thwarted by "+b["name"]+"!")
					for f in pa:
						if f["action"] == "follow":
							if f["target"] == p["name"]:
								f["whispers"].append(p["name"]+" attempted to zap "+p["target"]+" but it was blocked by "+b["name"])
							elif f["target"] == b["name"]:
								f["whispers"].append(b["name"]+" blocked a zap by "+p["name"]+" aimed at "+p["target"])								
					s = 0
			elif b['name'] == p["target"]:
				if b["action"] == "zap":
					if b["target"] == p["name"]:
						p["whispers"].append("Your zap was countered by "+b["name"]+"!")
						for f in pa:
							if f["action"] == "follow":
							f["target"] == p["name"]:
							f["whispers"].append(p["name"]+" traded zapps with "+p["target"])
						s = 0
		#If succesful, bonk the dude!
		if s == 1:
			for t in pa:
				if t["name"] == target:
					t["whispers"].append("You've been zapped!")
					t["account"] == 0
			for f in pa:
				if f["action"] == "follow":
					f["target"] == p["name"]:
						f["whispers"].append(p["name"]+" zapped at "+p["target"])

	elif p["action"] == "block":
		#Block is covered in the zap action, just take their credits and inform the follower
		p['account'] = p['account'] - 3
		for f in pa:
			if f["action"] == "follow":
				f["target"] == p["name"]:
					f["whispers"].append(p["name"]+" was blocking "+p["target"])

	elif p["action"] == "hide":
		for f in pa:
			if f["action"] == "follow":
				if f["target"] == p["name"]:
					if p["role"] == ghost
						f["whispers"].append(p["name"]+" is a ghost, how are you following them?")
					else:
						f["whispers"].append(p["name"]+" was in hiding this round")

	elif p["action"] == "dos":
		for b in pa:
			if b["name"] == p["target"]:
				b["limit"] = b["limit"] + 1
		for f in pa:
			if f["action"] == "follow":
				if f["target"] == p["name"]:
					f["whispers"].append(p["name"]+" was mining this round.")

	elif p["action"] == "haunt":
		for b in pa:
			if b["name"] == p["target"]:
				b["limit"] = b["limit"] + 2
		for f in pa:
			if f["action"] == "follow":
				if f["target"] == p["name"]:
					f["whispers"].append(p["name"]+" is a ghost, how are you following them?")

	elif p["action"] == "mine":
		for f in pa:
			if f["action"] == "follow":
				if f["target"] == p["name"]:
					f["whispers"].append(p["name"]+" was mining this round.")

	elif p["action"] == "consolidate":
		p['account'] = p['account'] - 15
		for f in pa:
			if f["action"] == "follow":
				if f["target"] == p["name"]:
					f["whispers"].append(p["name"]+" is consolidating power!")

	elif p["action"] == "investigation":
		broadcasts.append(p["name"]+ " is investigating "+p["target"])
		for t in pa:
			if t["name"] == p["target"]:
				p["whispers"].append(t["name"]+" Report:")
				p["whispers"].append("Account:"+t["account"])
				p["whispers"].append("Action:"+t["action"]+" "+t["target"])
				p["whispers"].append("Investments:"+t["investments"])

	elif p["action"]
