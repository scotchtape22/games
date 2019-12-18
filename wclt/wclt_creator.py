#!/bin/python
import random

#WCLT Player creation
#Make leagues for Germany, Russia, and Japan?

locations = ["Milwaukee","Chicago","Champagn","St.Paul","Duluth","Miami","Detroit","Seattle","Brooklyn","Montreal","Vancouver","Havanna","Atlanta","Toronto","Mexico City","Vera Cruz","Austin","South Beach","Cleveland","Toledo","Hollywood","Minneapolis","Qubec City","Portland","Roswell","Boston","New Orleans","Silicon Valley","Chicago","Denver"]
dispos = ["aggressive","reactive","determined"]
f_name = ["Skip","Captain","Knack","Flash","Beef","Blast","Butch","Dic","Austin","Gordon","Archie","William","Sid","Justin","Wanye","Bobby","Guy","Lucky","Luc","Manly","Doug","Sergei","Vlad","Dimitri","CJ","Red","Dustin","Yooper","Igor","Christoff","Paul","Mordecai","Tommy","Isaac","Eli","Mario","Jonny","Gary","Lightening","no-name","Jeremy","Sarge","Phinneas","Billy","Ezikial","Remy","Sarah","Benny","Robert","Bolt","Butch","Peter","Blast","Paul","Annabelle","Dirk","Marie","Slab","Flint","Soph","Bert","Lazer","Blendin","Mable","Dipper","Wendy","Trigger","Squid","Missy","Ted","Rufus","Sanic"]
l_name = ["85","Sexbang","Sung","Danger","Macklin","Thunderfist","MeOuch","Soos","Cordaroy","Pines","Phobos","Booteh","Beefcake","Starlite","Calumet","Mariucci","Abney","MacInnis","Hancock","Sandusky","Ontanogan","L\'Anse","Chassel","Portage","Superior","Erie","Huron","Alsance","McAllister","Sherpa","Soo","Sweney","Manistique","Gould","Allegheny","Hamilton","Mississauga","Kingston","Sudbury","Monongahela","Charelston","Parker","Walters","Bennett","St.Croix","Wausau","Hodag","Kewaskum","Menomonee","Brunswick","Essen","Calhammer","Carmel","Llopis","Dortmund","Mercer","Lutsen","Finlandia","Cloquet","Nitro","Ashland","Fargo","Butte","Vamboldt","Newport","Bozeman","Whitehall","Linden","Baraga","Turku","Dresden","Niagara","Zodd","Domski","Parros","Inronstag","McHugeLarge","Metropolous","Deadlift","Vanderhuge","York","Young","Hardcheese","Kim","Orr","Myre","Bombey","Horton","Roy","Marshfield","Lom","Rhinelander","McMan","Cooles","Krieger","Carlton","Primm","Maple","Evergreen","River","Duluth","St.Paul","Muskeegon","Houghton","Arbor","LaThrill","Hawk","Great","Thatcher","Thrash","Hall","Shock","Hoth","House","Plante","Jones","Two-Point-0","Penn","Temple","Briggs","Norsemen","Flake","Burre","Su","Greenberg","LaFlamme","Black","Federov","Blitz","MacIntyre","Parks","Dawson","Johnson","Sully","Ortega","Fedorchek","Cox","Steele","Mccrosscheq","Mac","James","Slapshot","Henrei","McMan","Moser","Survivor","Sisu","Dogmeat","McTravis","Dooblekill","Deadeye","Beefboi","Mann","Wyld","Stallions"]




create = input("How many players? ")
create = int(create)
while create > 0:
	my_dispo = random.choice(dispos)
	my_dis = random.randint(1,2)
	my_rea = random.randint(1,2)
	my_acc = random.randint(1,2)
	my_eva = random.randint(1,2)
	my_dur = random.randint(2,3)
	my_pot = random.randint(2,5)
	my_name = random.choice(f_name) + " " + random.choice(l_name)
	my_home = random.choice(locations)
	my_age = random.randint(16,20)
	my_ego = random.randint(0,2)

	print(my_name + ":" + my_home + ":" + str(my_age) + ":" + str(my_ego) + ":" + my_dispo + ":" + str(my_dis) + ":" + str(my_rea)  + ":" + str(my_acc)  + ":" + str(my_eva) + ":" + str(my_dur) + ":" + str(my_pot))

	create = create - 1