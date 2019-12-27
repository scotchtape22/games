#!/bin/python
#Team planner for WCLT
#Reads a contract proposal for a player and gives their result

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
print("---------------")
prop_type = input("Proposed contract type: ")

expected = (pd[2]+pd[3]+pd[4]+pd[5]+pd[6]+pd[7])*100
favor = 0
