#!/bin/python
#Team planner for WCLT
#Takes a team file, and opens it up, allows players to view player data and set game plan?

f_path = input("Load Team File: ")
f_load = open(f_path,"r+")
f_data = f_load.readlines()

print("G-Set Game Plan")
print("C-Change Coaches")
print("S-Upgrade Stadium")
print("V-View Team")
p_choice = input("Action? ")



if p_choice == "G"
for rp in f_data:
	rpd = rp_split(":")
	if rpd[0] == "roster-player":
		overall = (int(rpd[2])+int(rpd[3])+int(rpd[4])+int(rpd[5])+int(rpd[6])+int(rpd[7]))/7
		print("Game plan for "+rpd[1])
		print("Initiative:"+rpd[2])
		print("Accuracy:"+rpd[3])
		print("Evasion:"+rpd[4])
		print("Fitness:"+rpd[5])
		print("Potential:"+rpd[6])
		print("Overall:"+Overall)
		#Choose druge
		print("A-Adderall")
		print("C-Cocaine")
		print("G-Set Game Plan")
		print("G-Set Game Plan")
		print("N-None")
		c_drug=input("Drug Choice: ")

