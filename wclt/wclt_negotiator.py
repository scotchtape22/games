#!/bin/python
#Team planner for WCLT
#Reads a contract proposal for a player and gives their result
import random

#Enter Player
#Player array - pd
#ROSTER:NAME:INT:ACC:EVA:POT:FIT:EGO:KNO:PERSONALITY:DRUG:WIN:S_WIN:LOSE:S_LOSE:INJ:Hits-Taken:Players-Hit:Flags-Captured:Rounds-Played:Hometown:GAME_COST:CONTRACT_LENGTH:CONTRACT_TYPE

#Enter Contract Data:
prop_gamt = input("Proposed pay per game: ")
prop_term = input("Proposed contract length (seasons): ")
print("---------------")
print("F-Franchise")
print("P-Pro")
print("T-Two-Way")
print("M-Minor League")
print("C-Coach")
print("---------------")
prop_type = input("Proposed contract type: ")
prop_loc = input("Team Location: ")
#Error check plz

expected = (pd[2]+pd[3]+pd[4]+pd[5]+pd[6]+pd[7])*100

expected = expected - (500*prop_term)

if pd[age] < 25:
	if prop_type == "P" or prop_type == "F":
		expected = expected - 1000
	elif prop_type == "C":
		expected = expected + 8000
elif pd[age] > 24 and pd[age] < 36:
	if prop_type == "M" or prop_type == "T":
		expected = expected + 5000
	elif prop_type == "C":
		expected = expected + 4000
elif pd[age] > 35 and pd[age] < 44:
	if prop_type == "C":
		expected = expected - 2000
	else:
		expected = expected + 3000
else:
	expected = expected+6000

if pd[8] == "eager":
	expected = expected - 1000

if prop_type == "F":
	expected = expected - 1000

if pd[hometown] == prop_loc:
	expected = expected - 2000


if expected <= prop_gamt:
	print(pd[1]=" has accepted the contract")
else:
	big_roll = expected+(prop_gamt/2)
	big_roll = round(big_roll,0)
	random.randint(1,big_roll)
	if big_roll > expected:
		print(pd[1]=" has accepted the contract")
	else:
		print(pd[1]=" has rejected the contract")
