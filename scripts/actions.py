#-*- coding: utf-8 -*-  
#coding=utf-8 
#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------
Gold = ("Gold", "4e8046ba-759b-428c-917f-7e9268a5af90") #The GUID from markers.o8g
Power = ("Power", "d115ea96-ed05-4bf7-ba22-a34c8675c676") #The GUID from markers.o8g
STR_Up = ("STR_Up", "7898d5a0-1d59-42b2-bbfb-5051cc420cd8") #The GUID from markers.o8g
Burn = ("Burn", "c272aa0c-f283-4ff5-b545-a5a3f150e6da") #The GUID from markers.o8g
TokenRed = ("TokenRed", "6238a357-41b7-4bca-b394-925fc1b2caf8") #The GUID from markers.o8g
TokenBlue = ("TokenBlue", "99452bc7-d95b-4c54-8577-41d98dd3e30b") #The GUID from markers.o8g
MilitaryColor = "#ae0603" #A shade of red from the Military Icon
IntrigueColor = "#006b34" #A shade of green from the Intrigue Icon
PowerColor = "#1a4d8f" #A shade of blue from the Power Icon
WaitColor = "#5c3521" # Grey
PlayColor = "#ffA6f7" # Yellow
miljudgecolor = "#000000" # black
milsavecolor = "#ff0000" # red
saveactioncolor = "#6aa84f" # green
countereventcolor = "#c0ff3e" #
usedplotcolor = "#99ffff"
sacrificecolor = "#a0522d"
interruptcolor = "#ffd700"
leavecolor = "#b03060"
leaveandabilitycolor = "#20124d"
leaveonlycolor = "#e06666"
abilitycolor = "#a32f5b"
Stealthcolor = "#ffffff"
cantchallengecolor = "#fffacd"
GameURL = "http://octgn.gamersjudgement.com/wordpress/agot2/"
FAQ_URL = "https://images-cdn.fantasyflightgames.com/filer_public/03/43/034309e6-c3a2-4575-8062-32ede5798ef8/gt01_rules-reference-web.pdf"
#add
MilitaryIcon = ("MilitaryIcon", "7e9610d4-c06d-437d-a5e6-100000000001")
IntrigueIcon = ("IntrigueIcon", "0cabfb36-01b4-46c4-bb2a-42889fb63e8b")
PowerIcon = ("PowerIcon", "a6b9db40-b0ad-4b22-b049-5837c4ece904")
mdict = dict(
	strup=("STR_Up", "7898d5a0-1d59-42b2-bbfb-5051cc420cd8"),
	powicon=("PowerIcon", "a6b9db40-b0ad-4b22-b049-5837c4ece904"),
	inticon=("IntrigueIcon", "0cabfb36-01b4-46c4-bb2a-42889fb63e8b"),
	milicon=("MilitaryIcon", "7e9610d4-c06d-437d-a5e6-100000000001"),
	burnicon=("Burn", "c272aa0c-f283-4ff5-b545-a5a3f150e6da"),
	tkred=("TokenRed","6238a357-41b7-4bca-b394-925fc1b2caf8"))
debugMode = True
countusedplot = 0
Heartsbaneused = 0
countmil = 1
challengetype = 0
winplayer = []
attacker = []
defender = []
unopposed = 0
otherplayer = []
mjfinish = 0
savepoint = 0
claimtmp = 0
timerIsRunning = False
savetarget = []
inserttarget = []
interruptpass = 0
interruptpasstmp = 0
interruptcancelplayer = []
saveactionplayer = []
interruptcancelcard = []
interruptcancellastcard = []
interruptcanceledcard = []
reducegold = 0
interruptcancelok = 1
interruptlib = {}
interruptlibtmp = {}
mainpass = ""
selectplayer = []
sessionpass = ""
selectedcard = []
stealthcount = 0
cardkilllist = []
smcount = 1
kbcount = 1
recount = 1
abilityattach = {}
leavecardtype = []
leavetablecard = []
reactionattach = {}
actionattach = {}
reactioncardlimit = {}
actioncardlimit = {}
keywordattach = []
intertreaction = 0
isinsertreaction = 0
interruptreaction = []
nextcardtmp = []
cardtoaction = []
dwtmpcard = []
plotcard = []

savetargettmp = []
inserttargettmp = []
interruptcancelcardtmp = []
interruptcancelplayertmp = []
interruptcanceledcardtmp = []
interruptcancellastcardtmp = []
interruptlibtmp = {}
interruptcanceloktmp = 1
saveactionplayertmp = []
mainpasstmp = ""
insertreactioncard = []

listattach = []
import re
import time


#---------------------------------------------------------------------------
# Table group actions
#---------------------------------------------------------------------------
def googleDriveWebsite(group, x = 0, y = 0):
	mute()

	openUrl("{}".format(GameURL))
	
def faqWebsite(group, x = 0, y = 0):
	mute()
	
	openUrl("{}".format(FAQ_URL))
	
def flipCoin(group, x = 0, y = 0):
	mute()
	n = rnd(1, 2)
	if n == 1:
		notify("**{} flips heads.**".format(me))
	else:
		notify("**{} flips tails.**".format(me))
		
def sixSided(group, x = 0, y = 0):
	mute()
	n = rnd(1,6)
	notify("**{} rolls a {} on a 6-sided die.**".format(me, n))
	
def twelveSided(group, x = 0, y = 0):
	mute()
	n = rnd(1,12)
	notify("**{} rolls a {} on a 12-sided die.**".format(me, n))
	
def xSided(group, x = 0, y = 0):
	mute()
	sides = askInteger("Roll a how many sided die? (minimum 3)", 3)
	if sides == None: return
	elif sides < 3:
		whisper("Please choose a number greater than or equal to 3.")
		return
	else:
		n = rnd(1,sides)
		notify("**{} rolls a {} on a {}-sided die.**".format(me, n, sides))

def cancelAllHighlight(group, x = 0, y = 0):
	mute()
	for card in group:
		card.target(False)
		if card.controller == me:
			card.highlight = None

def turnDone(group, x = 0, y = 0):
	mute()
	notify("**{} is done.**".format(me))

def restoreAll(group, x = 0, y = 0): 
	mute()
	myCards = (card for card in table
				if card.controller == me)
	for card in myCards:
		if card.isFaceUp:
			card.orientation &= ~Rot90
			card.highlight = None
			card.target(False)
	notify("{} stands all their cards.".format(me))

def announceMil(group, x = 0, y = 0):
	mute()
	global countmil
	global attacker
	global challengetype
	global selectedcard
	global sessionpass
	global stealthcount
	stealth = ""
	stealthcount = 0
	if sessionpass != "milselectok":
		notify("**{} declares a MIL challenge.**".format(me))
		list = []
		for card in table:
			card.highlight = None
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0:
				list.append(card)
		if len(list) == 0:
			whisper("No more card can eclares a MIL challenge.")
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 character to attack."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = MilitaryColor
			if c.model != "a8854084-67e5-4955-89db-3d9cb1337789":
				if c.model == "09903f79-6155-4a63-9b52-e10fb2e69898":
					for cards in table:
						if cards.model == "99a12a9c-6e83-43bd-8947-0cc47ffcd02a" and cards.controller == me:
							attach = eval(getGlobalVariable("attachmodify"))
							if attach.has_key(cards._id):
								if attach(cards._id) == c._id and countmil == 1:
									c.orientation = 0
								else:c.orientation = 1
				elif c.model != "09903f79-6155-4a63-9b52-e10fb2e69898":c.orientation = 1
				if re.search(r'stealth',c.keywords,re.I):   #stealth
					stealth = "0"
					stealthcount += 1
					if c.model == afterchallengereacion['Ghost'][1]:setGlobalVariable("cantchallenge", "1")
		notify("**{} declares MIL attackers.**".format(me))
		if getGlobalVariable("automode") == "1":
			attacker = me
			challengetype = 1
			remoteCall(otherplayer, "getattacker", [attacker,challengetype])
			sessionpass = ""
			selectedcard = []
			setGlobalVariable("selectmode", "0")
		if stealth == "0":
			if checktablestealthcount(0) > 0:
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						if checktablestealthcount(0) <= stealthcount:
							stealthcount = checktablestealthcount(0)
							selectstealth(table)
							return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":
			if getGlobalVariable("mainstep") == "0":setGlobalVariable("mainstep", "1")
			checkafterchallengereacioncard(1)
			b = str(int(me.getGlobalVariable("milcount"))+1)
			me.setGlobalVariable("milcount",b)
		countmil += 1
	else:
		whisper("You must declare at least 1 character to attack.")

def announceInt(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global stealthcount
	global selectedcard
	global sessionpass
	stealth = ""
	stealthcount = 0
	if sessionpass != "intselectok":
		notify("**{} declares an INT challenge.**".format(me))
		list = []
		for card in table:
			card.highlight = None
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 character to attack."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
				stealthcount += 1
		notify("**{} declares INT attackers.**".format(me))
		if getGlobalVariable("automode") == "1":
			attacker = me
			challengetype = 2
			remoteCall(otherplayer, "getattacker", [attacker,challengetype])
			sessionpass = ""
			selectedcard = []
			setGlobalVariable("selectmode", "0")
		if stealth == "0":
			if checktablestealthcount(0) > 0:
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						if checktablestealthcount(0) <= stealthcount:
							stealthcount = checktablestealthcount(0)
							selectstealth(table)
							return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":
			setGlobalVariable("mainstep", "1")
			checkafterchallengereacioncard(1)
			b = str(int(me.getGlobalVariable("intcount"))+1)
			me.setGlobalVariable("intcount",b)
	else:
		whisper("You must declare at least 1 character to attack.")

def announcePow(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global stealthcount
	global selectedcard
	global sessionpass
	stealth = ""
	stealthcount = 0
	if sessionpass != "powselectok":
		notify("**{} declares a POW challenge.**".format(me))
		list = []
		for card in table:
			card.highlight = None
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Power == "Yes" or card.markers[PowerIcon] > 0) and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 character to attack."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
				stealthcount += 1
		notify("**{} declares POW attackers.**".format(me))
		if getGlobalVariable("automode") == "1":
			attacker = me
			challengetype = 3
			remoteCall(otherplayer, "getattacker", [attacker,challengetype])
			sessionpass = ""
			selectedcard = []
			setGlobalVariable("selectmode", "0")
		if stealth == "0":
			if checktablestealthcount(0) > 0:
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						if checktablestealthcount(0) <= stealthcount:
							stealthcount = checktablestealthcount(0)
							selectstealth(table)
							return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":
			setGlobalVariable("mainstep", "1")
			checkafterchallengereacioncard(1)
			b = str(int(me.getGlobalVariable("powcount"))+1)
			me.setGlobalVariable("powcount",b)
	else:
		whisper("You must declare at least 1 character to attack.")

def holdOn(group, x = 0, y = 0):
	mute()
	notify("**Please wait.  {} has an action/question.**".format(me))

def announceOpp(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global defender
	global sessionpass
	if getGlobalVariable("automode") == "1":
		setGlobalVariable("mainstep", "3")
		if attacker == me:
			notify("You already are a attacker.")
			return
		if attacker != []:
			notify("**{} responds: Opposed/Defend.**".format(me))
			if challengetype == 1:
				choiceList = ['Military', 'No defenders']
				colorList = ['#ae0603' ,'#D8D8D8']
				choice = askChoice("Opposed or defend?", choiceList,colorList)
				if choice == 1:
					if getGlobalVariable("automode") != "1":
						defMil(table)
					else:
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "1")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
						sessionpass = "mildefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					notify("{} declares no defenders.".format(me))
					defender = me
					remoteCall(otherplayer, "getdefender", [me])
					challengeaction(1)
			if challengetype == 2:
				choiceList = ['Intrigue', 'No defenders']
				colorList = ['#006b34' ,'#D8D8D8']
				choice = askChoice("Opposed or defend?", choiceList,colorList)
				if choice == 1:
					if getGlobalVariable("automode") != "1":
						defInt(table)
					else:
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "1")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
						sessionpass = "intdefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					if getGlobalVariable("automode") == "1":
						c = 0
						for card in table:
							if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0 and card.highlight != IntrigueColor:
								card.highlight = IntrigueColor
								card.orientation = 1
								c = 1
						if c == 0:notify("{} declares no defenders.".format(me))
						else:
							setGlobalVariable("bedefend","")
							notify("**{} declares INT defenders.**".format(me))
					else:
						notify("{} declares no defenders.".format(me))
					defender = me
					remoteCall(otherplayer, "getdefender", [me])
					challengeaction(1)
			if challengetype == 3:
				choiceList = ['Power', 'No defenders']
				colorList = ['#1a4d8f','#D8D8D8']
				choice = askChoice("Opposed or defend?", choiceList,colorList)
				if choice == 1:
					if getGlobalVariable("automode") != "1":
						defPow(table)
					else:
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and (card.Power == "Yes" or card.markers[PowerIcon] > 0) and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "1")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
						sessionpass = "powdefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					notify("{} declares no defenders.".format(me))
					defender = me
					remoteCall(otherplayer, "getdefender", [me])
					challengeaction(1)
			else:return
		else:notify("No challenge happened.")
	else:
		notify("**{} responds: Opposed/Defend.**".format(me))
		choiceList = ['Military', 'Intrigue', 'Power', 'No defenders']
		colorList = ['#ae0603' ,'#006b34','#1a4d8f','#D8D8D8']
		choice = askChoice("Which challenge do you want to defend?", choiceList,colorList)
		if choice == 1:
			defMil(table)
		elif choice == 2:
			defInt(table)
		elif choice == 3:
			defPow(table)
		elif choice == 4:
			notify("{} declares no defenders.".format(me))
		else:return
		
def defMil(group, x = 0, y = 0):
	mute()
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "mildefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares characters to defend."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = MilitaryColor
			c.orientation = 1
		notify("**{} declares MIL defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	if getGlobalVariable("automode") == "1":
		setGlobalVariable("selectmode", "0")
		defender = me
		remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		challengeaction(1)

def defInt(group, x = 0, y = 0):
	mute()
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "intdefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares characters to defend."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
		if getGlobalVariable("automode") == "1":
			for card in table:
				if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0 and card.highlight != IntrigueColor:
					card.highlight = IntrigueColor
					card.orientation = 1
			setGlobalVariable("bedefend","")
		notify("**{} declares INT defenders.**".format(me))
	else:
		if getGlobalVariable("automode") == "1":
			c = 0
			for card in table:
				if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0 and card.highlight != IntrigueColor:
					card.highlight = IntrigueColor
					card.orientation = 1
					c = 1
			if c == 0:notify("{} declares no defenders.".format(me))
			else:
				setGlobalVariable("bedefend","")
				notify("**{} declares INT defenders.**".format(me))
	if getGlobalVariable("automode") == "1":
		setGlobalVariable("selectmode", "0")
		defender = me
		remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		challengeaction(1)

def defPow(group, x = 0, y = 0):
	mute()
	global defender
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "powdefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Power == "Yes" or card.markers[PowerIcon] > 0) and card.orientation == 0:
				list.append(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares characters to defend."
		dlg.min = 1
		dlg.max = len(list)
		cards = dlg.show()
	else:cards = selectedcard
	if cards != None and cards != []:
		for c in cards:
			if getGlobalVariable("automode") != "1":
				c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
		notify("**{} declares POW defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	if getGlobalVariable("automode") == "1":
		defender = me
		remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		challengeaction(1)
		
def scoop(group, x = 0, y = 0):
	mute()
	
	if not confirm("Scoop your side of the table?"): return
	
	var = me.getGlobalVariable("setupOk")
	var="0"
	me.setGlobalVariable("setupOk", var)
	me.counters['Gold'].value = 0  #reset all counters
	me.counters['Power'].value = 0
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("turn", "0")
	
	for c in me.hand: 
		if not c.Type == "Faction" and not c.Type == "Agenda":
			c.moveTo(me.Deck)			
	for c in me.piles['Discard Pile']: c.moveTo(me.Deck)
	for c in me.piles['Dead Pile']: c.moveTo(me.Deck)

	myCards = (card for card in table
        	if card.owner == me)

	for card in myCards:
		if card.Type == "Faction": 
			card.moveTo(me.hand)
		elif card.Type == "Agenda":
			card.moveTo(me.hand)
		elif card.Type == "Plot": 
			card.moveTo(me.piles['Plot Deck'])
		else: 
			card.moveTo(me.Deck)

	notify("{} scoops their side of the table.".format(me))

#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------

	
def kneel(card, x = 0, y = 0):
	mute()
	# if (card.model == "f97ccf1a-5b0d-490f-9968-78330e92171c" or card.model == "4c8a114e-106c-4460-846b-28f73914fc11") and card.orientation == 0:
	# 	if not confirm("Do you want to use {}'s ability?".format(card.name)): return
	# 	attach = card.name+str(card.position)
	# 	for cards in table:
	# 		f = cards.name+str(cards.position)
	# 		if attachmodify != {}:
	# 			if f == attachmodify[attach]:
	# 				if card.model == "4c8a114e-106c-4460-846b-28f73914fc11":#just for Heartsbane
	# 					global Heartsbaneused
	# 					cards.markers[STR_Up] += 3
	# 					card.orientation ^= Rot90
	# 					Heartsbaneused = 1	
	# 					return
	# 				if cards.orientation != 0:
	# 					cards.orientation ^= Rot90
	# 					card.orientation ^= Rot90
	# 				else:
	# 					notify("{} is standing, you cannot stand it.".format(cards))
	# 					return
	# else:notify("{} s already knelt.".format(card))
	# if card.model not in ("f97ccf1a-5b0d-490f-9968-78330e92171c" ,"4c8a114e-106c-4460-846b-28f73914fc11"):		
	card.orientation ^= Rot90
	if card.orientation & Rot90 == Rot90:
		notify('{} kneels {}.'.format(me, card.name))
	else:
		notify('{} stands {}.'.format(me, card.name))

def flipcard(card, x = 0, y = 0):
	mute()
	if card.isFaceUp:
		notify("{} turns {} face down.".format(me, card))
		card.isFaceUp = False
		card.orientation &= ~Rot90
	else:
		card.isFaceUp = True
		notify("{} turns {} face up.".format(me, card))
		#duplicate
		if len(me.piles['Plot Deck']) == 7:
			uniquecards = []
			uniquecardsinex = []
			for u in table:
				if u.name == card.name and u.filter == None and u.index != card.index:
					if u.name not in uniquecards:
						if u.controller == me and u.unique == "Yes":
							uniquecards.append(u.name)
							uniquecardsinex.append(u.index)
							cx, cy = u.position
			if uniquecards != []:
				if card.name == uniquecards[0] and card.index not in uniquecardsinex and card.controller == me:
					if me.isInverted:x,y = attachat(cx-8,cy-8,table)
					else:x,y = attachat(cx+8,cy+8,table)
					if me.isInverted: 
						card.moveToTable(x,y)
					else:
						card.moveToTable(x,y)
					notify("{} plays {}'s duplicate.".format(me,card))
					card.sendToBack()
					card.filter = "#005c3521"

def addGold(card, x = 0, y = 0):
	mute()
	notify("{} adds a Gold to {}.".format(me, card))
	card.markers[Gold] += 1
	me.counters['Gold'].value += 1
    
def addPower(card, x = 0, y = 0):
    mute()
    notify("{} adds a Power to {}.".format(me, card))
    card.markers[Power] += 1
    me.counters['Power'].value += 1
	
def addSTR_Up(card, x = 0, y = 0):
	mute()
	card.markers[STR_Up] += 1
	
def addBurn(card, x = 0, y = 0):
	mute()
	card.markers[Burn] += 1

def addRedToken(card, x = 0, y = 0):
	mute()
	card.markers[TokenRed] += 1
	
def addBlueToken(card, x = 0, y = 0):
	mute()
	card.markers[TokenBlue] += 1
    
def subGold(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Gold to {}.".format(me, card))
    card.markers[Gold] -= 1
    me.counters['Gold'].value -= 1
    
def subPower(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Power to {}.".format(me, card))
    card.markers[Power] -= 1 
    me.counters['Power'].value -= 1
	
def subSTR_Up(card, x = 0, y = 0):
    mute()
    card.markers[STR_Up] -= 1
	
def subBurn(card, x = 0, y = 0):
    mute()
    card.markers[Burn] -= 1
	
def subRedToken(card, x = 0, y = 0):
    mute()
    card.markers[TokenRed] -= 1
	
def subBlueToken(card, x = 0, y = 0):
    mute()
    card.markers[TokenBlue] -= 1
	
def addMilitaryHighlight(card, x = 0, y = 0):
	mute()
	card.highlight = MilitaryColor
	card.target(False)
	
def addIntrigueHighlight(card, x = 0, y = 0):
	mute()
	card.highlight = IntrigueColor
	card.target(False)
	
def addPowerHighlight(card, x = 0, y = 0):
	mute()
	card.highlight = PowerColor
	card.target(False)

def cancelHighlight (card, x = 0, y = 0):
	mute()
	card.highlight = None
	card.target(False)

def addhousepow(ok = 1):
	for count in range(0,ok):
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == me:
				addPower(housecard)

def subhousepow(ok = 1):
	for count in range(0,ok):
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == me:
				subPower(housecard)


	
#---------------------------
#movement actions
#---------------------------

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

def randomDiscard(group=me.hand):
	mute()
	card = group.random()
	if card == None: return
	card.moveTo(me.piles['Discard pile'])
	notify("{} randomly discards {}.".format(me, card))
 
def discardMany(group):
	count = 0
	discAmount = None
	
	mute()
	if len(group) == 0: return
	if discAmount == None: discAmount = askInteger("Randomly discard how many cards?", 2)
	if discAmount == None: return
	
	for index in range(0,discAmount):
		card = group.random()
		if card == None: break
		card.moveTo(me.piles['Discard pile'])
		count += 1
		notify("{} randomly discards {}.".format(me,card))
	notify("{} randomly discards {} cards.".format(me, count))

def mulligan(group):
	count = None
	draw = None
	mute()
	
	if not confirm("Are you sure you want to Mulligan?"): return False
	if draw == None: draw = askInteger("How many cards would you like to draw for your Mulligan?", len(me.hand))
	if draw == None: return True
	
	for card in group:
		card.moveToBottom(me.deck)
			
	me.deck.shuffle()
		
	for card in me.deck.top(draw):
		card.moveTo(me.hand)
	notify("{} mulligans and draws {} new cards.".format(me, draw))
	
	return True

#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------

def shuffle(group):

	group.shuffle()

def draw(group):
	mute()
	if len(group) == 0: return
	group[0].moveTo(me.hand)
	notify("{} draws a card.".format(me))
	
def drawRandom(group):
	mute()
	
	card = group.random()
	if card == None: return
	card.moveTo(me.hand)
	notify("{} randomly draws a plot card.".format(me))

def drawMany(group):
	drawAmount = None
	
	mute()
	if len(group) == 0: return
	if drawAmount == None: drawAmount = askInteger("Draw how many cards?", 2)
	if drawAmount == None: return
	
	if len(group) < drawAmount:
		drawAmount = len(group)
	
	for card in group.top(drawAmount):
		card.moveTo(me.hand)
	notify("{} draws {} cards.".format(me, drawAmount))
 
def discardManyFromTop(group):
	count = 0
	discAmount = None
	
	mute()
	if len(group) == 0: return
	if discAmount == None: discAmount = askInteger("Discard how many from top?", 4)
	if discAmount == None: return
	
	for index in range(0,discAmount):
		card = group.top()
		card.moveTo(me.piles['Discard pile'])
		count += 1
		if len(group) == 0: break
	notify("{} discards {} cards from the top of their Deck.".format(me, count))
	
def reshuffle(group):
	count = None
	
	mute()
	if len(group) == 0: return
	if not confirm("Are you sure you want to reshuffle the {} back into your Deck?".format(group.name)): return
	
	myDeck = me.deck
	for card in group:
		card.moveTo(myDeck)
	myDeck.shuffle()
	notify("{} shuffles thier {} back into their deck.".format(me, group.name))
	
def moveOneRandom(group):
	mute()
	if len(group) == 0: return
	if not confirm("Are you sure you want to move one random card from your {} to your Hand?".format(group.name)): return
	
	card = group.random()
	if card == None: return
	card.moveTo(me.hand)
	notify("{} randomly moves {} from their discard to their hand.".format(me, card))

#---------------------------------------------------------------------------
# New actions
#---------------------------------------------------------------------------
# New Table group actions
#---------------------------------------------------------------------------
def setup(group, x = 0, y = 0):
	mute()
	global winplayer
	global attacker
	global defender
	global unopposed
	global challengetype
	global otherplayer
	if not confirm("Confirm to setup?"): return
	var = me.getGlobalVariable("setupOk")
	if var != "0":
		whisper("You already did your Setup")
		return
	if len(me.hand) == 0:
		whisper("You need to load a deck first") 
		return
	var="1"
	me.setGlobalVariable("setupOk", var)
	notify("**{} has started setup, please wait**".format(me))
	for c in me.hand: 
		if c.Type == "Faction":
			if me.isInverted: 
				c.moveToTable(-320,-100)			
			else:
				c.moveToTable(-320,10)
		if c.Type == "Agenda":
			if me.isInverted: 
				c.moveToTable(-240,-100)			
			else:
				c.moveToTable(-240,10)
	me.deck.shuffle()
	for card in me.deck.top(7):
		card.moveTo(me.hand)
	if me.isInverted: 
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,-200)
	else:
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,110)
	# if confirm ("Need the quickbar?"):
	# 	if me.isInverted: 
	# 		table.create("342dd044-b0f7-4eef-a021-5b755397f9d4",-280,-50)
	# 		table.create("6a34f431-c468-4d31-8d8c-51aac6a66f89",-320,-50)
	# 		table.create("338370f8-3952-46a7-a3b9-a462a326e7bb",-360,-50)
	# 		table.create("9936a519-785c-4058-b060-4ca0a01258ea",-280,-90)
	# 		table.create("91e2e6b3-9929-4365-93b2-3d143a20e6ff",-280,-130)
	# 		table.create("c237b30d-6511-4646-a93a-49b63ff4aa22",-320,-130)
	# 		table.create("d6ac416d-0956-403f-a1bc-ed6e8c5ba4a9",-360,-130)
	# 		table.create("dac3d665-1af7-427e-9f50-36d77b93513c",-280,-170)
	# 		table.create("08e6fe74-098f-4429-9076-71235a67c9b0",-280,-210)
	# 		table.create("be7113f0-d44a-4923-bbc2-a2b3ad4cd948",-400,-50)
	# 		table.create("7e3783d4-150a-46dd-8bd7-ef3680744d8c",-400,-90)
	# 	else:
	# 		table.create("342dd044-b0f7-4eef-a021-5b755397f9d4",300,20)
	# 		table.create("6a34f431-c468-4d31-8d8c-51aac6a66f89",340,20)
	# 		table.create("338370f8-3952-46a7-a3b9-a462a326e7bb",380,20)
	# 		table.create("9936a519-785c-4058-b060-4ca0a01258ea",300,60)
	# 		table.create("91e2e6b3-9929-4365-93b2-3d143a20e6ff",300,100)
	# 		table.create("c237b30d-6511-4646-a93a-49b63ff4aa22",340,100)
	# 		table.create("d6ac416d-0956-403f-a1bc-ed6e8c5ba4a9",380,100)
	# 		table.create("dac3d665-1af7-427e-9f50-36d77b93513c",300,140)
	# 		table.create("08e6fe74-098f-4429-9076-71235a67c9b0",300,180)
	# 		table.create("be7113f0-d44a-4923-bbc2-a2b3ad4cd948",420,20)
	# 		table.create("7e3783d4-150a-46dd-8bd7-ef3680744d8c",420,60)
	notify("**{} is ready to setup**".format(me))
	if me._id == 1:
		if me.isInverted: 
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",380,-100)
		else:
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",-400,0)
	if getGlobalVariable("numplayer") == "2":
		n = rnd(1, 2)
		if n == 1:
			notify("**Seven Gods decide {} is the firstplayer.**".format(getGlobalVariable("AID")))
		else:
			setGlobalVariable("firstplay","False")
			f = (card for card in table  
					if card.name == "1st Player Token")
			for card in f:
				if card.controller == me:
					moveFP(card)
				else:
					remoteCall(players[1], "moveFP", card)
			notify("**Seven Gods decide {} is the firstplayer.**".format(getGlobalVariable("BID")))
	for person in players:
		if person != me:
			otherplayer = person
			remoteCall(players[1], "getotherplayer", me)
	winplayer = []
	attacker = []
	defender = []
	unopposed = 0
	challengetype = 0
	placesetupcards()

def placesetupcards():
	mute()
	list = []
	for p in me.hand:list.append(p)
	dlg=cardDlg(list)
	dlg.title = "Choose your setup cards."
	dlg.text = "You may place up to 8 gold cost worth cards as setup cards. To mulligan, close the window without choosing any cards."
	dlg.min = 0
	dlg.max = len(list)
	cards = dlg.show()
	uniquecards = [] #Duplicates
	cost = 0
	limit = 0
	countcards = 20
	countcardss = 20
	place = "OK"
	if cards != None:
		for placecard in cards:
			if placecard.unique != "Yes":
				cost += int(placecard.cost)
			elif placecard.unique == "Yes" and placecard.name not in uniquecards:
				uniquecards.append(placecard.name)
				cost += int(placecard.cost)
			if re.search(r'limit',placecard.keywords,re.I):   #keyword limit
				limit += 1
			if placecard.type == "Event":
				confirm("You may only place character, location, and attachment cards.")
				place = "NOTOK"
			if placecard.type == "Attachment":
				if not confirm("Each attachment must be attached to a valid target under its owner’s control."):
					place = "NOTOK"
		if cost > 8:
			confirm("You may only place up to 8 gold cost.")
			place = "NOTOK"
		if limit > 1:
			confirm("You may only place up 1 limited card.")
			place = "NOTOK"
		if place == "NOTOK":
			placesetupcards()
		if place == "OK":
			for card in cards:
				if me.isInverted:
					card.moveToTable(countcardss,-100,True)
					countcardss=countcardss+80
				else:
					card.moveToTable(countcards,10,True)
					countcards=countcards+80
				card.peek()
			for drawcard in me.deck.top(7-len(me.hand)):
				drawcard.moveTo(me.hand)
			notify("{} is ready to begin.".format(me))
			me.setGlobalVariable("setupOk","3")
			if len(players) == 1:
				remoteCall(me, "proccessetupcard", [table])
			else:
				if me.getGlobalVariable("setupOk") == players[1].getGlobalVariable("setupOk") == "3":
					remoteCall(me, "proccessetupcard", [1])
	else:
		if me.getGlobalVariable("setupOk") == "2":
			placesetupcards()
		else:
			isMulligan = mulligan(me.hand)
			if(isMulligan):
				me.setGlobalVariable("setupOk","2")
			placesetupcards()

def proccessetupcard(count):
	mute()
	global listattach
	for card in table:
		if not card.isFaceUp and card.controller == me:
			flipcard(card)
			if card.type == "Attachment" and card.filter == None:
				listattach.append(card)
	if len(listattach) > 0:
		me.setGlobalVariable("setupOk","4")
		attatchcard(listattach)
	else:
		reordertable(table)
	if count == 1:remoteCall(players[1], "proccessetupcard", [2])

def attatchcard(listattach):
	mute()
	global sessionpass
	for card in table:
		card.target(False)
	targetTuple = ([card._id for card in table if card.Type in "Character" and card.controller == me], me._id)
	me.setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	sessionpass = "attatchcardselect"
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	whisper("Please select a target for {}".format(listattach[0]))

def reordertable(group, x = 0, y = 0):
	mute()
	countcards = 20
	countcard = 20
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if card.type == "Character" and card.controller == me and card.filter == None:
			if me.isInverted:
				card.moveToTable(countcards,-100,True)
			else:
				card.moveToTable(countcards,10,True)
			countcards=countcards+80
		if card.type == "Location" and card.controller == me and card.filter == None:
			if me.isInverted:
				card.moveToTable(countcard,-220,True)
			else:
				card.moveToTable(countcard,120,True)
			countcard=countcard+80
		list = []
		list2 = []
		list3 = []
		for d in attach:
			if attach[d] == card._id:
				list.append(d)
		for dcard in table:
			if dcard.name == card.name and dcard.filter == WaitColor and dcard.controller == me:
				list2.append(dcard._id)
		list.reverse()
		for cardatt in table:
			for listcard in table:
				if cardatt.controller == me and cardatt.name == listcard.name and  listcard._id in (list) and cardatt.filter == WaitColor:
					list3.append(cardatt)
		i = 12			
		if len(list) > 0:
			for cardindex in list:
				for carda in table:
					if carda._id == cardindex:
						x1,y1 = card.position
						if me.isInverted:carda.moveToTable(x1-i,y1-i)
						else:carda.moveToTable(x1+i,y1+i)
						carda.sendToBack()
						x2,y2 = carda.position
						i+=12
						k = 12
						for cardattd in list3:
							if cardattd.name == carda.name:
								if me.isInverted:cardattd.moveToTable(x2-k,y2+k)
								else:cardattd.moveToTable(x2+k,y2-k)
								cardattd.sendToBack()
								k+=12
		i = 12
		if card.unique == "Yes":
			if len(list2) > 0:
				for cardindex in list2:
					for carda in table:
						if carda._id == cardindex:
							x1,y1 = card.position
							carda.moveToTable(x1-i,y1-i)
							carda.sendToBack()
							i+=12
	notify("{} finished setup phase".format(me))
	me.setGlobalVariable("setupOk","5")
	# if me.getGlobalVariable("setupOk") == players[1].getGlobalVariable("setupOk") == "5":
	# 	notify("Plot phase start")
	# 	remoteCall(me, "revealplot", [table])
	# 	remoteCall(players[1], "revealplot", [table])

def endturn(group, x = 0, y = 0): 
	count = 0
	discAmount = None
	mute()
	if not confirm("Are you sure to end this turn?"): return
	myCards = (card for card in table  #restore all cards
			if card.controller == me)
	for card in myCards:
		if card.isFaceUp:
			card.orientation &= ~Rot90
			card.highlight = None
			card.target(False)
	me.counters['Gold'].value = 0  #reset gold counters
	goldcard = (card for card in table
			if card.controller == me)
	for card in goldcard: 
		card.markers[Gold] = 0
	getreserve(group)
	if len(me.hand) > me.counters['Reserve'].value:  #check reserve
		if discAmount == None: 
			whisper("The number of cards in {}'s hand is more than your reserve.You should discard {} cards.".format(me, len(me.hand)-me.counters['Reserve'].value))
			discAmount = askInteger("How many cards to discard?", len(me.hand)-me.counters['Reserve'].value) 
		if discAmount == None: return
		dlg = cardDlg([c for c in me.hand])
		dlg.title = "These cards are in your hand:"
		dlg.text = "Choose {} cards to discard.".format(discAmount)
		dlg.min = discAmount
		dlg.max = discAmount
		cards = dlg.show()
		if cards != None:
			for card in cards:
				card.moveTo(me.piles['Discard pile'])
				notify("{} discard {}.".format(me, card))
		else:return
	else:
		notify("Hand size is ok.")
	
	global countusedplot
	oldcountusedplot = countusedplot
	countusedplot = len(me.piles['Used Plot Pile'])
	# for card in table:
	# 	if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":#just for Dawn
	# 		attach = card.name+str(card.position)
	# 		for cards in table:
	# 			f = cards.name+str(cards.position)
	# 			if f == attachmodify[attach]:cards.markers[STR_Up] += countusedplot-oldcountusedplot
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("turn", "0")
	global countmil
	countmil = 1
	notify("{} is ready for a new turn.".format(me))

def countincome(group, x=0, y=0):
	mute()
	if me.getGlobalVariable("turn") == "0":
		uniquecards = []
		for incomecard in table:
			if incomecard.isFaceUp:
				if incomecard.goldincome and incomecard.controller == me:
					if incomecard.Unique != "Yes":
						me.counters['Gold'].value += int(incomecard.goldincome)
					elif incomecard.Unique == "Yes" and incomecard.name not in uniquecards:
						uniquecards.append(incomecard.name)
						me.counters['Gold'].value += int(incomecard.goldincome)
		plotlist = [card for card in table
						if card.controller == me and card.type == "Plot" and card.filter == None]
		plotlist.reverse()
		for plotcard in plotlist:
			me.counters['Gold'].value += int(plotcard.plotgoldincome)
			plotcard.markers[Gold] += me.counters['Gold'].value
			break
		notify("{} counts income {} gold.".format(me,me.counters['Gold'].value))
		plotlist.reverse()
		me.setGlobalVariable("turn", "1")
		return
	else:
		notify("You have already counted income.")

def getreserve(group, x=0, y=0):
	mute()
	for person in players:
		person.counters['Reserve'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		plotlist = [card for card in table
						if card.controller == person and card.type == "Plot"]
		plotlist.reverse()
		uniquecards = []
		for card in personCards:
			if card.isFaceUp:
				if card.Reserve and int(card.Reserve) > 0:
					if card.Unique != "Yes":
						person.counters['Reserve'].value += int(card.Reserve)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Reserve'].value += int(card.Reserve)	
		for card in plotlist:
			person.counters['Reserve'].value += int(card.plotReserve)
			break
		plotlist.reverse()
		notify("{}'s Reserve value is {}.".format(person,person.counters['Reserve'].value))
	return

def getInit(group, x = 0, y = 0):
	mute()
	for person in players:
		person.counters['Initiative'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		plotlist = [card for card in table
						if card.controller == person and card.type == "Plot"]
		plotlist.reverse()
		uniquecards = []
		for card in personCards:
			if card.isFaceUp:
				if card.Initiative and int(card.Initiative) != 0:
					if card.Unique != "Yes":
						person.counters['Initiative'].value += int(card.Initiative)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Initiative'].value += int(card.Initiative)	
		for card in plotlist:
			person.counters['Initiative'].value += int(card.plotInitiative)
			break
		plotlist.reverse()
		if person.counters['Initiative'].value > 0:
 			person.counters['Initiative'].value = person.counters['Initiative'].value
 		else:
 			person.counters['Initiative'].value = 0
		notify("{}'s Initiative value is {}.".format(person,person.counters['Initiative'].value))
	return

def fp(group, x = 0, y = 0):
	mute()
	getInit(table)
	recalcPower(table)
	maxInit = -1
	minPower = -1
	winners = []
	numPlayers = len(players)
	for i in range(numPlayers):
		if players[i].counters['Initiative'].value > maxInit:
			maxInit = players[i].counters['Initiative'].value
			minPower = players[i].counters['Power'].value
			winners = []
			winners.append(i)
		elif players[i].counters['Initiative'].value == maxInit:
			if minPower < 0 or players[i].counters['Power'].value < minPower:
				minPower = players[i].counters['Power'].value
				winners = []
				winners.append(i)
			elif players[i].counters['Power'].value == minPower:
				winners.append(i)
	if len(winners) == 1:
		winner = players[winners[0]]
		notify("{} wins the initiative.".format(winner))
	else:
		n = rnd(0, len(winners) - 1)
		winner = players[winners[n]]
		notify("{} randomly wins the initiative.".format(winner))
	notify("**{} decides who is the first player.**".format(winner))
	setGlobalVariable("firstplay","{}".format(winner._id))
	# if there are more than 2 players, move the FP token manually
	if numPlayers == 2:
		decidefirstplayer(table)
	return

def recalcPower(group, x = 0, y = 0):
	mute()
	index = 0
	for person in players:
		person.counters['Power'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		for card in personCards:
			if card.markers[Power] > 0:
				person.counters['Power'].value += card.markers[Power]
		notify("{} has a total of {} power.".format(person.name,person.counters['Power'].value))

def dominance(group, x=0, y=0):
	mute()
	maxSTR = 0
	winner = -1
	numPlayers = len(players)
	for i in range(numPlayers):
		person = players[i]
		person.counters['Str'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		uniquecards = []
		# exclude knelt unique characters
		for card in personCards:
			if card.isFaceUp and card.orientation == Rot90:
				if card.Strength and card.Unique == "Yes":
					if card.name not in uniquecards:
						uniquecards.append(card.name)
		personCards = (card for card in table
						if card.controller == person)
		for card in personCards:
			if card.isFaceUp:
				if card.orientation != Rot90:
					str = 0
					if card.Strength:
						if card.Unique != "Yes":
							str += int(card.Strength)
						elif card.name not in uniquecards:
							uniquecards.append(card.name)
							str += int(card.Strength)
					if card.markers[STR_Up] > 0:
						str += card.markers[STR_Up]
					if card.markers[Burn] > 0:
						str -= card.markers[Burn] * 4
					if str > 0:
						person.counters['Str'].value += str
				if card.dominance and int(card.dominance) > 0:
					if card.Unique != "Yes":
						person.counters['Str'].value += int(card.dominance)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Str'].value += int(card.dominance)
				if card.markers[Gold] > 0:
					person.counters['Str'].value += card.markers[Gold]
		if person.counters['Str'].value > maxSTR:
			maxSTR = person.counters['Str'].value
			winner = i
		elif person.counters['Str'].value == maxSTR:
			winner = -1
		notify("{}'s total for dominance is {}.".format(person,person.counters['Str'].value))
	if winner == -1:
		notify("No one wins dominance.")
	else:
		notify("{} wins the dominance.".format(players[winner]))
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == players[winner]:
				addPower(housecard)
	notify("Dominance phase over.")
	notify("Standing phase start")
	setGlobalVariable("standingphase","1")
	setTimer(me,"dominance",table)
	return

def standingphase(group, x=0, y=0):
	mute()
	myCards = (card for card in table  #restore all cards
		if card.controller == me)
	for card in myCards:
		if card.isFaceUp:
			card.orientation &= ~Rot90
			card.highlight = None
			card.target(False)
	if getGlobalVariable("standingphase") == "1":
		setGlobalVariable("standingphase","2")
		remoteCall(players[1], "standingphase", table)
		return
	if getGlobalVariable("standingphase") == "2":
		notify("Standing phase over")
		setGlobalVariable("standingphase","0")
		setGlobalVariable("taxationphase","1")
		notify("Taxation phase start")
		taxationphase(table)

def taxationphase(group, x = 0, y = 0): 
	count = 0
	discAmount = None
	mute()
	if getGlobalVariable("taxationphase") == "1" or getGlobalVariable("taxationphase") == "2":
		me.counters['Gold'].value = 0  #reset gold counters
		goldcard = (card for card in table
				if card.controller == me)
		for card in goldcard: 
			card.markers[Gold] = 0
		getreserve(group)
		if getGlobalVariable("taxationphase") == "1":setGlobalVariable("taxationphase","1.5")
		if getGlobalVariable("taxationphase") == "2":setGlobalVariable("taxationphase","2.5")
	if len(me.hand) > me.counters['Reserve'].value:  #check reserve
		if discAmount == None: 
			whisper("The number of cards in {}'s hand is more than your reserve.You should discard {} cards.".format(me, len(me.hand)-me.counters['Reserve'].value))
			discAmount = len(me.hand)-me.counters['Reserve'].value
		dlg = cardDlg([c for c in me.hand])
		dlg.title = "These cards are in your hand:"
		dlg.text = "Choose {} cards to discard.".format(discAmount)
		dlg.min = discAmount
		dlg.max = discAmount
		cards = dlg.show()
		if cards != None:
			for card in cards:
				card.moveTo(me.piles['Discard pile'])
				notify("{} discard {}.".format(me, card))
		else:
			taxationphase(table)
			return
	else:
		notify("Hand size is ok.")
	for c in table: 
		if c.Type == "Plot" and c.controller == me:
			if len(me.piles['Plot Deck']) > 0:
				c.filter = "#0099ffff"
				x, y = c.position
				if me.isInverted:c.moveToTable(x, y-20)
				else:c.moveToTable(x, y+20)
			else:
				if c.filter == usedplotcolor:
					c.moveTo(me.piles['Plot Deck'])
				else:
					c.filter = "#0099ffff"
	
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("turn", "0")
	me.setGlobalVariable("firstevent", "0")	
	me.setGlobalVariable("milcount","1")
	me.setGlobalVariable("milcountmax","1")	
	me.setGlobalVariable("intcount","1")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","1")
	me.setGlobalVariable("powcountmax","1")
	me.setGlobalVariable("active","0")

	if getGlobalVariable("taxationphase") == "1.5":
		setGlobalVariable("taxationphase","2")
		notify("{} is ready for a new turn.".format(me))
		remoteCall(players[1], "taxationphase", table)
		return
	if getGlobalVariable("taxationphase") == "2.5":
		setGlobalVariable("ignorestr", "[]")
		setGlobalVariable("addclaim","0")
		setGlobalVariable("addclaimall","0")
		setGlobalVariable("reavelplot","0")
		setGlobalVariable("drawphase","0")
		setGlobalVariable("marshalphase","0")
		setGlobalVariable("challengephase","1")
		setGlobalVariable("standingphase","0")
		setGlobalVariable("taxationphase","0")
		setGlobalVariable("action","0")
		setGlobalVariable("activeplayer","")
		notify("{} is ready for a new turn.".format(me))
		notify("Taxation phase over")
		notify("A new turn start")
		notify("Plot phase start")
		remoteCall(me, "revealplot", [table])
		remoteCall(players[1], "revealplot", [table])


def challenge(group, x=0, y=0):
	mute()
	global winplayer
	global attacker
	global defender
	global unopposed
	if getGlobalVariable("automode") == "1":
		if attacker == []:
			notify("Please announce a attacker.")
			return
		if defender == []:
			notify("Please announce a defender.")
			return
		choice = challengetype
	else:
		choiceList = ['Military', 'Intrigue', 'Power']
		choice = askChoice("To which challenge do you want to calculate? ", choiceList)
	for person in players:
		person.counters['Str'].value = 0
		ignorestr = eval(getGlobalVariable("ignorestr"))
		personCards = (card for card in table
						if card.controller == person and card._id not in ignorestr)
		uniquecards = []
		for card in personCards:
			if card.isFaceUp:
				if choice == 1 and card.highlight == MilitaryColor:
					if card.Strength and int(card.Strength) > 0:
						if card.Unique != "Yes":
							person.counters['Str'].value += int(card.Strength)
						elif card.name not in uniquecards:
							uniquecards.append(card.name)
							person.counters['Str'].value += int(card.Strength)
					if card.markers[STR_Up] > 0:
						person.counters['Str'].value += card.markers[STR_Up]
					if card.markers[Burn] > 0:
						person.counters['Str'].value -= card.markers[Burn]
				elif choice == 2 and card.highlight == IntrigueColor:
					if card.Strength and int(card.Strength) > 0:
						if card.Unique != "Yes":
							person.counters['Str'].value += int(card.Strength)
						elif card.name not in uniquecards:
							uniquecards.append(card.name)
							person.counters['Str'].value += int(card.Strength)
					if card.markers[STR_Up] > 0:
						person.counters['Str'].value += card.markers[STR_Up]
					if card.markers[Burn] > 0:
						person.counters['Str'].value -= card.markers[Burn]
				elif choice == 3 and card.highlight == PowerColor:
					if card.Strength and int(card.Strength) > 0:
						if card.Unique != "Yes":
							person.counters['Str'].value += int(card.Strength)
						elif card.name not in uniquecards:
							uniquecards.append(card.name)
							person.counters['Str'].value += int(card.Strength)
					if card.markers[STR_Up] > 0:
						person.counters['Str'].value += card.markers[STR_Up]
					if card.markers[Burn] > 0:
						person.counters['Str'].value -= card.markers[Burn]
		notify("{}'s total strength for such challenge is {}.".format(person,person.counters['Str'].value))
	winplayer = []
	#challengetype = choice
	if getGlobalVariable("automode") == "1":
		if getGlobalVariable("numplayer") == "2":
		#if otherplayer != []
			if players[0].counters['Str'].value == players[1].counters['Str'].value:
				if players[0] == attacker:
					notify("attacker {} wins this challenge.".format(players[0]))
					winplayer = attacker
					if players[1].counters['Str'].value == 0:unopposed = 1
				else:
					notify("attacker {} wins this challenge.".format(players[1]))
					winplayer = players[1]
					if players[0].counters['Str'].value == 0:unopposed = 1
			elif players[0].counters['Str'].value > players[1].counters['Str'].value:
				if players[0] == attacker:
					notify("attacker {} wins this challenge.".format(players[0]))
					winplayer = players[0]
					if players[1].counters['Str'].value == 0:unopposed = 1
				else:
					notify("defender {} wins this challenge.".format(players[0]))
					winplayer = players[0]
			else:
				if players[0] == attacker:
					notify("defender {} wins this challenge.".format(players[1]))
					winplayer = players[1]
				else:
					notify("attacker {} wins this challenge.".format(players[1]))
					winplayer = players[1]
					if players[0].counters['Str'].value == 0:unopposed = 1
			remoteCall(otherplayer, "getwinner", [winplayer,unopposed,challengetype])
			if challengetype == 2 and getGlobalVariable("winint") == "1":winplayer.setGlobalVariable("intwin", "1")
			setGlobalVariable("mainstep", "5")
			aftercalculatestand = eval(getGlobalVariable("aftercalculatestand"))
			aftercalculatedraw = eval(getGlobalVariable("aftercalculatedraw"))
			debug(aftercalculatedraw)
			for kcard in table:
				if kcard.controller == winplayer and kcard._id in aftercalculatestand and kcard.orientation == 0:
					remoteCall(winplayer, "kneel", [kcard])
					notify("{} stand {} by [Ours is the Fury].".format(winplayer,kcard))
				if kcard.controller == winplayer and kcard._id in aftercalculatedraw and len(winplayer.deck) > 0:
					remoteCall(winplayer, "draw", [winplayer.deck])
					notify("{} draw 1 card by [For the North].".format(winplayer))
			if fplay(1) == me:checkaftercalculatereacioncardforce(1)
			else:remoteCall(otherplayer, "checkaftercalculatereacioncardforce", [1])
		else:
			notify("Only supported for Joust format.")
	# global Heartsbaneused
	# for card in table:
	# 	if card.model == "4c8a114e-106c-4460-846b-28f73914fc11" and Heartsbaneused == 1:#just for Heartsbane
	# 		attach = card.name+str(card.position)
	# 		for cards in table:
	# 			f = cards.name+str(cards.position)
	# 			if f == attachmodify[attach]:
	# 				cards.markers[STR_Up] -=3
	# 				Heartsbaneused = 0

def balancechallenge(challenge,winplayer,checkcount):
	mute()
	if checkcount == 1:
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:
				notify("waiting for fp balance the challenge")  
				if confirm("Continue to balance the challenge?"): remoteCall(otherplayer, "balancechallenge", [challenge,winplayer,2])
				else:
					notify("fp want to action") 
					return
			else:
				remoteCall(otherplayer, "balancechallenge", [challenge,winplayer,1])
	if checkcount == 2:
		notify("waiting for 2ndplayer balance the challenge")
		if confirm("Continue to balance the challenge?"):
			notify("all players checkok")
			debug(winplayer)
			balancechallengefinish(challenge,winplayer)
		else:
			notify("2ndplayer want to action") 
			return

def getotherplayer(player):
	global otherplayer
	otherplayer = player

def getwinner(winner,uo,ct):
	global winplayer
	global unopposed
	global challengetype
	winplayer = winner
	unopposed = uo
	challengetype = ct

def getattacker(attackerother,ct):
	global attacker
	global challengetype
	attacker = attackerother
	challengetype = ct

def getdefender(defenderother):
	global defender
	defender = defenderother

def challengecheck(group, x=0, y=0):
	mute()
	if getGlobalVariable("automode") == "1": 
		if winplayer != []:
			balancechallenge(challengetype,winplayer,1)
		else:
			notify("No challenge happened.")
	else:
		notify("Just for automode.")

def challengeclaim(group):
	claimcount = 0
	if attacker != []:
		plotlist = [card for card in table
			if card.controller == attacker and card.type == "Plot"]
	plotlist.reverse()
	for card in plotlist:
		claimcount = int(card.PlotClaim)
		break
	plotlist.reverse()
	return claimcount

def balancechallengefinish(challenge,winplay):
	mute()
	claim = challengeclaim(table)
	notify("claim is {}.".format(claim))
	if winplayer != defender:
		setGlobalVariable("mainstep", "6")
		if unopposed != 0:
			notify("{} add 1 pow from unopposed.".format(winplay))
			if winplay == me:
				addhousepow(1)
			else:
				remoteCall(otherplayer, "addhousepow", 1)
		if claim != 0:
			setGlobalVariable("mainstep", "7")
			if challenge == 1:
				if winplay != me:
					if getGlobalVariable("automode") != "1":
						Militarychallenge(claim)
					else:
						intomil(table)
				else:
					if getGlobalVariable("automode") != "1":
						remoteCall(otherplayer, "Militarychallenge", claim)
					else:
						remoteCall(otherplayer, "intomil", [table])
			if challenge == 2:
				for count in range(0,claim):
					if winplay != me:
						randomDiscard(me.hand)
					else:
						remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
				remoteCall(winplayer, "keyword", [1])
			if challenge == 3:
				if winplay == me:
					if checkhousepow(otherplayer) >= claim:
						remoteCall(otherplayer, "subhousepow", claim)
						addhousepow(claim)
					else:
						remoteCall(otherplayer, "subhousepow", otherplayer.counters['Power'].value)
						addhousepow(otherplayer.counters['Power'].value)
				else:
					if me.counters['Power'].value >= claim:
						subhousepow(claim)
						remoteCall(otherplayer, "addhousepow", claim)
					else:
						subhousepow(me.counters['Power'].value)
						remoteCall(otherplayer, "addhousepow", me.counters['Power'].value)
				remoteCall(winplayer, "keyword", [1])
		else:remoteCall(winplayer, "keyword", [1])
	else:
		remoteCall(winplayer, "keyword", [1])

def intomil(group):
	mute()
	global sessionpass
	list = []
	claim = challengeclaim(table)
	for card in table:
		if card.type == "Character" and card.controller == me and card.filter != WaitColor:
			list.append(card)
		c = len(list)
		if c < claim:
			b = c
		else:
			b = claim
	targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.filter != WaitColor], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	sessionpass = "milkillplayerselect"
	whisper("Please select {} players to be killed".format(b))
	whisper("**selectmode**")

def challengebalanceover(count):
	mute()
	global winplayer
	global attacker
	global defender
	global unopposed
	global challengetype
	global savetarget
	global inserttarget
	global interruptcancelcard
	global interruptcancelplayer
	global interruptcanceledcard
	global interruptcancellastcard
	global interruptlib
	global interruptcancelok
	global saveactionplayer
	global interruptpass
	global cardkilllist
	global abilityattach
	global leavecardtype
	global leavetablecard
	global reactionattach
	global reactioncardlimit
	global keywordattach

	savetarget = []
	inserttarget = []
	interruptpass = 0
	interruptcancelplayer = []
	saveactionplayer = []
	interruptcancelcard = []
	interruptcancellastcard = []
	interruptcanceledcard = []
	interruptcancelok = 1
	interruptlib = {}
	cardkilllist = []
	abilityattach = {}
	leavecardtype = []
	leavetablecard = []
	if getGlobalVariable("mainstep") == "78":
		for card in table:
			card.highlight = None
			card.target(False)
		winplayer = []
		attacker = []
		defender = []
		unopposed = 0
		challengetype = 0
		reactionattach = {}
		reactioncardlimit = {}
		keywordattach = []
	if count == 1:
		remoteCall(otherplayer, "challengebalanceover", [2])
		return
	if getGlobalVariable("aftcuevent") != "-1":
		aftcuevent = getGlobalVariable("aftcuevent")
		debug(getGlobalVariable("aftcuevent"))
		setGlobalVariable("aftcuevent", "-1")
		notify("balance over")
		if int(aftcuevent) == me._id:
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
		else:reaction("aftercalculate",1)
		return
	if getGlobalVariable("chaevent") != "-1":
		chaevent = getGlobalVariable("chaevent")
		debug(getGlobalVariable("chaevent"))
		setGlobalVariable("chaevent", "-1")
		notify("balance over")
		if int(chaevent) == me._id:
			remoteCall(otherplayer, "action", ["challenge",1])
		else:action("challenge",1)
		return
	setGlobalVariable("mainstep", "0")
	notify("challenge balance over")
	challengeaction(1)


def challengeAnnounce(group, x=0, y=0):
	mute()
	cc = 0
	ccc = 1
	global sessionpass
	if attacker ==[]:
		if getGlobalVariable("automode") != "1":
			choiceList = ['Military', 'Intrigue', 'Power', 'No challenge and Pass']
			colorList = ['#ae0603' ,'#006b34','#1a4d8f','#D8D8D8']
			choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
		else:
			choiceList = []
			colorList = []
			if getGlobalVariable("winint") == "1" and me.getGlobalVariable("intwin") != "1":
				ccc = 0
				whisper("you cannot initiate a [MIL] or [POW] challenge unless won an [INT] challenge this phase.")#AGameofThrones
			if int(me.getGlobalVariable("milcount")) <= int(me.getGlobalVariable("milcountmax")) and ccc == 1:
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0:
						choiceList.append('Military')
						colorList.append('#ae0603')
						cc = 1
						break
			if int(me.getGlobalVariable("intcount")) <= int(me.getGlobalVariable("intcountmax")):
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0:
						choiceList.append('Intrigue')
						colorList.append('#006b34')
						cc = 1
						break
			if int(me.getGlobalVariable("powcount")) <= int(me.getGlobalVariable("powcountmax")) and ccc == 1:
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Power == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0:
						choiceList.append('Power')
						colorList.append('#1a4d8f')
						cc = 1
						break
			if cc == 1:
				choiceList.append('No challenge and Pass')
				colorList.append('#D8D8D8')
				choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
			else:
				if getGlobalVariable("challengephase") == "1":
					setGlobalVariable("challengephase","2")
					notify("{} has been active player".format(players[1]))
					remoteCall(players[1], "challengeAnnounce", table)
					return
				if getGlobalVariable("challengephase") == "2":
					setGlobalVariable("challengephase","0")
					remoteCall(players[1], "dominance", table)
					return
		if getGlobalVariable("automode") != "1":
			if choice == 1:announceMil(table)
			if choice == 2:announceInt(table)
			if choice == 3:announcePow(table)
			if choice == 4:notify("{} has no challenge to initiate.".format(me))
			if choice == 0:return
		else:
			if choiceList[choice-1] == 'Military':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Military == "Yes" or card.markers[MilitaryIcon] > 0) and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
				sessionpass = "milselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'Intrigue':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Intrigue == "Yes" or card.markers[IntrigueIcon] > 0) and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
				sessionpass = "intselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'Power':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and (card.Power == "Yes" or card.markers[PowerIcon] > 0) and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
				sessionpass = "powselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'No challenge and Pass':
				notify("{} has no challenge to initiate.".format(me))
				if getGlobalVariable("challengephase") == "1":
					setGlobalVariable("challengephase","2")
					setGlobalVariable("activeplayer",str(players[1]._id))
					players[1].setGlobalVariable("active","1")
					notify("{} has been active player".format(players[1]))
					remoteCall(players[1], "challengeAnnounce", table)
					return
				if getGlobalVariable("challengephase") == "2":
					setGlobalVariable("challengephase","0")
					remoteCall(players[1], "dominance", table)
					return
			else:
				notify("{} has no challenge to initiate.".format(me))
				if getGlobalVariable("challengephase") == "1":
					setGlobalVariable("challengephase","2")
					setGlobalVariable("activeplayer",str(players[1]._id))
					players[1].setGlobalVariable("active","1")
					notify("{} has been active player".format(players[1]))
					remoteCall(players[1], "challengeAnnounce", table)
					return
				if me.getGlobalVariable("active") == players[1].getGlobalVariable("active") == "1":
					setGlobalVariable("challengephase","0")
					remoteCall(players[1], "dominance", table)
					return
	else:
		notify("challenge already happened.")

def Militarychallenge(claim = 0):
	mute()
	c = 0
	list = []
	list2 = []
	discard = 0
	cards = []
	global selectedcard
	global sessionpass
	if sessionpass != "milkillplayerselectok":
		if claim == 0:return
		#cardlist = [card for card in table
			#if card.type == "Character" and card.controller == me and card.unique == "Yes"]
		#cardlist.reverse()
		for card in table:
			if card.type == "Character" and card.controller == me and card.filter != WaitColor:
				list.append(card)
		if len(list) > 0:
			dlg = cardDlg(list)
			dlg.title = "These cards are in your table:"
			dlg.text = "Declares at least 1 character to be killed.(total is {})".format(claim)
			if len(list) < claim:
				dlg.min = len(list)
				dlg.max = len(list)
			else:
				dlg.max = claim
				dlg.min = claim
			cards = dlg.show()
		if cards == []:return
	else:
		if claim == 0:
			remoteCall(winplayer, "keyword", [1])
			sessionpass = ""
			selectedcard = []
			return
		else:
			cards = selectedcard
	if cards != None and cards != []:
		for card in cards:
			card.highlight = miljudgecolor
			list2.append(card)
		if len(list2) > 0:
			miljudgementfinish(list2,claim)
			remoteCall(otherplayer, "miljudgementfinish", [list2,claim])
			sessionpass = ""
			selectedcard = []
			f = (card for card in table  
				if card.name == "1st Player Token")
			for card1 in f:
				if card1.controller == me:
					interruptevent("miljudgementfp",1)
					#setTimer(me,"miljudgementfp",table)
					#miljudgement(table,card,1,claim)
				else:
					debug("2")
					#remoteCall(otherplayer, "miljudgement", ["table",card,1,claim])
					#remoteCall(otherplayer, "setTimer", [otherplayer,"miljudgementfp",table])
					remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
			notify("waiting for fp action")
			return
	else:
		Militarychallenge(claim)
		return
	if discard != claim and c == 0:
		Militarychallenge(claim-discard)
	if discard == claim:
		remoteCall(winplayer, "keyword", [1])
	#cardlist.reverse()

def intointerruptevent(count):
	mute()
	global sessionpass
	global smcount
	sessionpass = ""
	targetTuple = ([card._id for card in mjfinishcard if card.highlight == miljudgecolor], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	sessionpass = "miljudgementselect"
	notify("**{} into selectmode**".format(me))
	smcount = count

def miljudgementfinish(mfcard,claim):
	mute()
	global mjfinish
	global mjfinishcard
	global claimtmp
	mjfinish = 1
	mjfinishcard = mfcard
	claimtmp = claim

def miljudgementfinished(mfcard,claim,count):
	mute()
	global cardkilllist
	for card in mfcard:
		if card.controller == me:
			if card.highlight == miljudgecolor:
				cardkilllist.append(card)
				#card.moveTo(me.piles['Dead pile'])
				#notify("{} killed {}.".format(me,card))
			else:
				notify("{} saved {}.".format(me,card))
	if len(cardkilllist) > 0:remoteCall(otherplayer, "getcardkilllist", [cardkilllist])
	if count == 1:
		remoteCall(otherplayer, "miljudgementfinished", [mfcard,claim,2])
	else:
		if len(cardkilllist) > 0:
			remoteCall(otherplayer, "characterkilled", [cardkilllist,1])
		else:
			remoteCall(winplayer, "keyword", [1])

def getcardkilllist(listkill):
	global cardkilllist
	cardkilllist = listkill


def revealplot(group, x = 0, y = 0):
	mute()
	plot = 0
	me.piles['Plot Deck'].addViewer(me)
	dlg=cardDlg([c for c in me.piles['Plot Deck']])
	dlg.title = "These cards are in your unused-plot pile:"
	dlg.text = "Select a plot card to reveal."
	cards = dlg.show()
	if cards != None:
		countxy = 5
		for c in table: 
			if c.Type == "Plot" and c.controller == me:
				c.filter = "#0099ffff"
				x, y = c.position
				c.moveToTable(x-countxy,y)
				plot = 1
				#if me.isInverted:c.moveToTable(x, y-30)
				#else:c.moveToTable(x, y+30)
		if len(me.piles['Plot Deck']) == 1:plot = 0
		for card in cards:
			if plot == 0:
				if me.isInverted:card.moveToTable(-110,-75,True)
				else:card.moveToTable(-110,10,True)
			else:
				if me.isInverted:card.moveToTable(x, y-20,True)
				else:card.moveToTable(x, y+20,True)
			me.setGlobalVariable("turn","1")
			if len(me.piles['Plot Deck']) == 0:
				for card in table:
						if card.Type == "Plot" and card.controller == me and card.filter == usedplotcolor:
							card.moveTo(me.piles['Plot Deck'])
			if len(players) > 1:
				if me.getGlobalVariable("turn") == players[1].getGlobalVariable("turn") == "1":
					flipplotcard(card)
					d = (card for card in table 
							if card.type == "Plot" and card.controller != me)
					for c in d:
						remoteCall(players[1], "flipplotcard", c)
					remoteCall(me, "fp", table)
			if len(players) == 1:
				flipplotcard(card)
			else:
				card.peek()
	else:
		if getGlobalVariable("automode") == "1":revealplot(table)
		else:return
		
def decidefirstplayer(group, x = 0, y = 0):
	mute()
	if getGlobalVariable("firstplay") == "{}".format(me._id):  
		askfirstplayer(table)
	else: 
		remoteCall(players[1], "askfirstplayer", table)     


def askfirstplayer(group, x = 0, y = 0):
	mute()
	colorList = ['#1a4d8f','#ae0603']
	choiceList = ['{}'.format(me.name),'{}'.format(players[1].name)]
	choice = askChoice("Decide who is First player.", choiceList,colorList)
	if choice == 1:
		notify("**{} is firstplayer.**".format(me))
		setGlobalVariable("firstplay",str(me._id))
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:    
				moveFP(card)
			else:                        
				remoteCall(players[1], "moveFP", card)
	elif choice == 2:
		notify("**{} is firstplayer.**".format(players[1]))
		setGlobalVariable("firstplay",str(players[1]._id))
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:   
				moveFP(card)
			else:                       
				remoteCall(players[1], "moveFP", card)
	else:
		return
	askfirstreveal(table)

def askfirstreveal(group, x = 0, y = 0):
	mute()
	if fplay(1) == me:
		colorList = ['#1a4d8f','#ae0603']
		choiceList = ['{}'.format(me),'{}'.format(players[1])]
		choice = askChoice("Decide who will First reveal.", choiceList,colorList)

		if choice == 1:
			notify("{} First reveal.".format(me))
			setGlobalVariable("reavelplot","1")
			reavelplot(table)
		if choice == 2:
			notify("{} First reveal.".format(players[1]))
			setGlobalVariable("reavelplot","1")
			remoteCall(players[1], "reavelplot", table)
	else:remoteCall(players[1], "askfirstreveal", table)

def reavelplot(group, x = 0, y = 0):
	mute()
	for card in table:
		if card.type == "Plot" and card.controller == me and card.filter == None:
			notify("use {}'s ability".format(card))
			plotability(card)
	# if getGlobalVariable("reavelplot") == "1":
	# 	setGlobalVariable("reavelplot","2")
	# 	remoteCall(players[1], "reavelplot", table)
	# 	return
	# if getGlobalVariable("reavelplot") == "2":
	# 	notify("plot phase over")
	# 	setGlobalVariable("reavelplot","0")
	# 	setGlobalVariable("drawphase","1")
	# 	notify("draw phase start")
	# 	drawphase(table)

def plotability(card):
	mute()
	global sessionpass
	global nextcardtmp
	global plotcard
	list10 = []
	searchok = 0
	drawcount = 0
	cards = None
	for d in plotdict:
		if card.model == plotdict[d][1] and card.controller == me:
			if plotdict[d][2] == "winint":
				setGlobalVariable("winint","1")
				notify("{} reaveled {}, A player cannot initiate a [MIL] or [POW] challenge unless he or she has won an [INT] challenge that phase.".format(me,card))#AGameofThrones
			if plotdict[d][2] == "firstll":
				me.setGlobalVariable("firstll", "1")
				notify("{} reaveled {}, Reduce the cost of the first Lord or Lady character {} marshal this round by 2.".format(me,card,me))#ANobleCause
			if plotdict[d][2] == "addmilcount":
				me.setGlobalVariable("milcountmax",str(int(me.getGlobalVariable("milcountmax"))+1))
				notify("{} reaveled {}, may initiate an additional [MIL] challenge during the challenges phase.".format(me,card,me))#AStormofSwords
			if plotdict[d][2] == "10searchatloc":
				list10 = me.deck.top(10)
				for c in list10:
					if c.Type in ("Attachment","Location"):
						searchok = 1
						break
				dlg = cardDlg(list10)
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != None and cards[0].Type in ("Attachment","Location"):
					cards[0].moveTo(me.hand)
					me.deck.shuffle()
					notify("{} reaveled {}, add {} to {} hand.".format(me,card,cards[0],me))#BuildingOrders
				else:
					if searchok == 1:
						if confirm("There is a Attachment or Location in these cards, select again？"):plotability(card)
					else:notify("search failed")
			if plotdict[d][2] == "1c1g":
				c = 0
				for e in table:
					if e.controller != me and e.type == "Character":c += 1
				plotlist = [pcard for pcard in table
						if pcard.controller == me and pcard.type == "Plot"]
				plotlist.reverse()
				for plotcard in plotlist:
					me.counters['Gold'].value += c
					plotcard.markers[Gold] += c
					break
				notify("{} reaveled {},  Gain {} gold.".format(me,card,c))#CallingtheBanners
			if plotdict[d][2] == "subclaim":
				choiceList = ['Military', 'Intrigue', 'Power']
				colorList = ['#ae0603' ,'#006b34','#1a4d8f']
				choice = askChoice("Which challenge do you want to name?", choiceList,colorList)
				if choice == 1:
					card.markers[MilitaryIcon] += 1
					players[1].setGlobalVariable("submilclaim", str(int(players[1].getGlobalVariable("submilclaim"))+1))
				if choice == 2:
					card.markers[IntrigueIcon] += 1
					players[1].setGlobalVariable("subintclaim", str(int(players[1].getGlobalVariable("subintclaim"))+1))
				if choice == 3:
					card.markers[PowerIcon] += 1
					players[1].setGlobalVariable("subpowclaim", str(int(players[1].getGlobalVariable("subpowclaim"))+1))
				if choice == 0:
					plotability(card)
					return
				notify("{} reaveled {}, reduce the claim value on the attacker's revealed plot card by 1 during {} challenges.".format(me,card,choiceList[choice-1]))#CalmOverWesteros
			if plotdict[d][2] == "discattachment":
				if checkattachment(1) > 0:
					plotcard = card
					nextcardtmp = card
					targetTuple = ([cards._id for cards in table if cards.Type == "Attachment"], me._id) 
					setGlobalVariable("tableTargets", str(targetTuple))
					setGlobalVariable("selectmode", "1")
					if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
					else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
					sessionpass = "Confiscationselect"
					notify("**{} into selectmode**".format(me))
				else:notify("There is no attachment card in table can't use {} 's ability".format(card))
			if plotdict[d][2] == "draw3":
				for count in range(0,2):
					if len(me.deck) > 0:
						draw(me.deck)
						drawcount += 1
				notify("{} reaveled {}, Draw {} cards.".format(me,card,drawcount))#CountingCoppers
			if plotdict[d][2] == "kneel":
				if checkstandplayer(table):
					plotcard = card
					nextcardtmp = card
					targetTuple = ([cards._id for cards in table if cards.Type == "Character" and card.orientation == 0], me._id) 
					setGlobalVariable("tableTargets", str(targetTuple))
					setGlobalVariable("selectmode", "1")
					if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
					else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
					sessionpass = "FilthyAccusationsselect"
					notify("**{} into selectmode**".format(me))
			if plotdict[d][2] == "discplayer":
				cards = players[1].hand.random()
				remoteCall(players[1], "HeadsonSpikes", [card,cards])



def HeadsonSpikes(card,cards):
	mute()
	if cards.type == "Character":
		cards.moveTo(me.piles['Dead pile'])
		remoteCall(players[1], "addhousepow", [2])
		notify("{} reaveled {}, {} disc {} and gain 2 power for {} faction.".format(players[1],card,me,cards,players[1]))#HeadsonSpikes
	else:
		cards.moveTo(me.piles['Discard pile'])
		notify("{} reaveled {}, {} disc {}.".format(players[1],card,me,cards))#HeadsonSpikes


def drawphase(group, x = 0, y = 0):
	mute()
	if len(me.deck) > 0:
		draw(me.deck)
	if len(me.deck) > 0:
		draw(me.deck)
	if getGlobalVariable("drawphase") == "1":
		setGlobalVariable("drawphase","2")
		remoteCall(players[1], "drawphase", table)
		return
	if getGlobalVariable("drawphase") == "2":
		notify("draw phase over")
		setGlobalVariable("drawphase","0")
		notify("marshal phase start")
		setGlobalVariable("marshalphase","1")
		me.setGlobalVariable("inmarshal","1")
		if fplay(1) == me:marshalphase(table)
		else:remoteCall(players[1], "marshalphase", table)

def marshalphase(group, x = 0, y = 0):
	mute()
	if me.getGlobalVariable("turn") == "0":countincome(table)
	choiceList = ['Marshal', 'Action', 'No action and Pass']
	colorList = ['#ae0603' ,'#006b34','#D8D8D8']
	choice = askChoice("Which pass do you want to action?", choiceList,colorList)
	if choice == 1:marshalcard(table)
	if choice == 2:marshalphase(table)
	if choice == 3:
		if getGlobalVariable("marshalphase") =="1":
			setGlobalVariable("marshalphase","2")
			players[1].setGlobalVariable("inmarshal","1")
			remoteCall(players[1], "marshalphase", table)
			return
		elif getGlobalVariable("marshalphase") =="2":
			setGlobalVariable("marshalphase","0")
			notify("marshal phase over")
			notify("challenge phase start")
			if fplay(1) == me:
				setGlobalVariable("activeplayer",str(me._id))
				me.setGlobalVariable("active","1")
			else:
				setGlobalVariable("activeplayer",str(players[1]._id))
				players[1].setGlobalVariable("active","1")
			challengeaction(1)

def marshalcard(group, x = 0, y = 0):
	mute()
	global sessionpass
	targetTuple = ([card._id for card in me.hand if card.type in ("Character","Location","Attachment")], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	sessionpass = "marshalcardselect"
	whisper("**selectmode**")			
#---------------------------------------------------------------------------
# New Table card actions
#---------------------------------------------------------------------------
def displayCardText(card, x = 0, y = 0):
	mute()
	
	notify('{} - Card Text:'.format(card))
	notify('{}'.format(card.Text))


def displayErrata(card, x = 0, y = 0):
	mute()
	
	notify('{} - ErrataText:'.format(card._id))
	notify('{} - ErrataText:'.format(card.filter))
	notify('{} - ErrataText:'.format(card.position))
	if card.ErrataText:
		notify('{}'.format(card.ErrataText))
	else:
		notify('')

def remove(card, x = 0, y = 0):
	mute()
	if card.type == "Internal":
		whisper("You can't remove {} from the game".format(card.name))
	else:
		if not confirm("Confirm to remove this card from game."): return
		card.delete()
		notify('{} removes {} from the game'.format(me, card))

def cardLookup(card, x = 0, y = 0):
	mute()
	
	if card.isFaceUp:
		webSite = ""
		webSite += "http://www.cardgamedb.com/index.php/agameofthrones2ndedition/a-game-of-thrones-2nd-edition-cards?&advanced=false&tx="
		webSite += "{}".format(card.name)
		webSite += "&txf=Name&or=name&vw=spoiler"
		openUrl("{}".format(webSite))
	else:
		whisper("Card must be face up to use this feature.")

def disc(card, x = 0, y = 0):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	if card.type == "Plot":
		card.moveTo(me.piles['Used Plot Pile'])
		notify("{} move {} to used plot pile.".format(me, card))
	elif card.type == "Faction" or card.type ==  "Agenda":
		whisper("You can't discard {} card.".format(card.type))
	elif card.type == "Internal":
		whisper("You can't discard {}.".format(card.name))
	elif card.type == "Attachment":
		for cardc in table:
			if attach.has_key(card._id):
				if attach[card._id] == cardc._id:
					del attach[card._id]
					setGlobalVariable("attachmodify",str(attach))
					debug(getGlobalVariable("attachmodify"))
					#rollback
					if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
						cardc.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
					if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and cardc.model == "df79718d-b01d-4338-8907-7b6abff58303":cardc.markers[MilitaryIcon] -= 1#096
					if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
						stradd = re.search('\+\d\sSTR', card.Text).group()
						cardc.markers[STR_Up] -= int(stradd[1])
					if re.search('\[INT]\sicon', card.Text):cardc.markers[IntrigueIcon] -= 1
					if re.search('\[POW]\sicon', card.Text):cardc.markers[PowerIcon] -= 1
					if re.search('\[MIL]\sicon', card.Text) and cardc.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardc.markers[MilitaryIcon] -= 1
		if card.highlight == sacrificecolor:
			card.highlight = None
			notify("{} sacrifice {}.".format(me, card))
		else:
			notify("{} discard {}.".format(me, card))
		card.moveTo(me.piles['Discard pile'])
		card.resetProperties()
	elif card.type == "Character":
		for d in attach:
			if attach[d] == card._id:
				for cardd in table:
					if cardd._id == d:
						if cardd.Text.find('Terminal.') == -1 and cardd.Keywords.find('Terminal.') == -1:cardd.moveTo(me.hand)
						else:cardd.moveTo(me.piles['Discard pile'])
						del attach[d]
						setGlobalVariable("attachmodify",str(attach))
						debug(getGlobalVariable("attachmodify"))
		if card.highlight == sacrificecolor:
			card.highlight = None
			notify("{} sacrifice {}.".format(me, card))
			card.moveTo(me.piles['Dead pile'])
		else:
			notify("{} discard {}.".format(me, card))
			card.moveTo(me.piles['Discard pile'])
	elif card.type == "Event":
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))
	else:
		if card.highlight == sacrificecolor:
			card.highlight = None
			notify("{} sacrifice {}.".format(me, card))
		else:
			notify("{} discard {}.".format(me, card))
		card.moveTo(me.piles['Discard pile'])

def defaultAction(card, x = 0, y = 0):
	mute()
	# Default for Done button is playerDone
	if getGlobalVariable("selectmode") == "0" and me.getGlobalVariable("setupOk") != "4":
		if card.Type == "Internal": 
			if card.name == "Done Token":
				DoneButton(card)
			if card.name == "1st Player Token":
				moveFP(card)
		elif card.Type == "Plot" and card.isFaceUp == True:
			countincome(table)
		elif len(me.piles['Plot Deck']) == 7 and card.Type == "Attachment" and card.isFaceUp == True:
			play(card)
		elif not card.isFaceUp: #Face down card - flip
			flipcard(card, x, y)
		else:
			kneel(card, x, y)

def moveFP(card):
	mute()
	global otherplayer
	for person in players:
		if person != me:
			otherplayer = person
	if person.name == getGlobalVariable("AID"):
		playera = person
	if person.name == getGlobalVariable("BID"):
		playerb = person
	if getGlobalVariable("firstplay") == str(me._id):
		if me.isInverted: 
			card.moveToTable(-400,-100)
			card.controller = me
		else:
			card.moveToTable(-400,0)
			card.controller = me
	elif getGlobalVariable("firstplay") == str(players[1]._id):
		if me.isInverted: 
			card.moveToTable(-400,0)
			card.controller = otherplayer
		else:
			card.moveToTable(-400,-100)
			card.controller = otherplayer
	else:
		return

def DoneButton(card):
	mute()
	notify("**{} is done.**".format(me))
	card.filter = None
	if len(players) > 1:
		d = (card for card in table 
				if card.name == "Done Token" and card.controller != me)
		for c in d:
			remoteCall(players[1], "addWaitHighlight", c)
	
def addWaitHighlight(card):
	mute()
	card.filter = WaitColor
	card.target(False)

def flipplotcard(card):
	mute()
	if card.isFaceUp:
		return
	else:
		card.isFaceUp = True
		notify("{} reveals {}.".format(me, card))
	me.setGlobalVariable("turn","0")
	
#------------------------------------------------------------------------------
# New Hand Actions
#------------------------------------------------------------------------------
def attachat(ax,ay,table):
	mute()
	for c in table:
		x,y = c.position
		if x == ax and y == ay:
			return attachat(x+12,y+12,table)
	return ax,ay

def play(card):
	mute()
	ambush = 0
	fll = 0
	if getGlobalVariable("selectmode") == "1":return#and sessionpass == "savecardselect":return
	c = 0
	if card.cost == "" : 
		whisper("You can't play this card")
		return
	if card.Cost == "X": cost=askInteger("How much do you want to pay to play {} ? ".format(card.name),0)
	else :
		if getGlobalVariable("ambush") == "1" and "Ambush" in card.keywords:
			cost=int(re.search('Ambush\s\(\d\).', card.keywords).group()[8])
			ambush = 1
		else:cost=int(card.Cost)
		if me.getGlobalVariable("firstevent") == "0":
			if checkpr(me) and card.type == "Event":
				cost=int(card.Cost)-1
				if cost < 0:cost = 0
				notify("You control Paxter Redwyne the first event you play Reduce the gold cost by 1.")

		if me.getGlobalVariable("inmarshal") == "1" and me.getGlobalVariable("firstll") == "1" and me.getGlobalVariable("firstcharacter") == "0":
			if card.type == "Character" and card.Traits.find('Lord') != -1 or card.Traits.find('Lady') != -1:
				cost=int(card.Cost)-2
				if cost < 0:cost = 0
				fll = 1
				notify(" the first Lord or Lady character you marshal this round by 2")


	uniquecards = []
	if len(me.piles['Plot Deck']) != 7:
		for u in table:
			if u.controller == me and u.unique == "Yes":
				uniquecards.append(u.name)
				if card.name in uniquecards: 
					cost=0
					c = 1   #Duplicates
					x,y = u.position
					break
	if c != 1:
		if card.type == "Attachment":
			global countusedplot
			countusedplot = len(me.piles['Used Plot Pile'])
			list = []
			for targetcard in table:
				if targetcard.targetedBy == me:
					if targetcard.Keywords == 'No attachments.':
						whisper("{} cannot be attached.".format(targetcard))
						targetcard.target(False)
					elif re.search(r'\[(.*) or (.*)] character only.', card.Text,re.I):
						if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
							list.append(targetcard)
							targetcard.target(False)
						else:
							whisper("{} can only be attached to [Lord or Lady] characters.".format(card))
							targetcard.target(False)
					elif re.search(r'\[(.*)] character only.', card.Text,re.I):
						chaonly = re.search(r'\[(.*)] character only.', card.Text,re.I).group(1)
						if targetcard.Faction.find(chaonly) != -1 or targetcard.Traits.find(chaonly) != -1:
							list.append(targetcard)
							targetcard.target(False)
						else:
							whisper("{} can only be attached to [{}] characters.".format(card,chaonly))
							targetcard.target(False)
					else:
						list.append(targetcard)
						targetcard.target(False)
				if len(list) == 1:cards=list
			if list == []:
				whisper("You must targeted(use Shift+mouse left button) a card which you want to attach to.")
				return
			if len(list) > 0:
				if len(list) > 1:
					dlg = cardDlg(list)
					dlg.title = "These cards can be attached:"
					dlg.text = "Choose a card to attach."
					dlg.min = 1
					dlg.max = 1
					cards = dlg.show()
				if cards != None:
					for choose in cards:
						if len(me.piles['Plot Deck']) != 7:
							reduc=askInteger("Reduce Cost by ?",0)
							if reduc == None or cost == None: return False
							if reduc>cost: reduc=cost
							cost-=reduc
							if me.counters['Gold'].value < cost :
								whisper("You don't have enough Gold to pay for {}.".format(card))
								return False
							me.counters['Gold'].value -= cost
							for incomecard in table:
								if incomecard.controller == me and incomecard.markers[Gold] > 0:
									incomecard.markers[Gold] -= cost
						cx,cy = choose.position
						if me.isInverted:x,y = attachat(cx-15,cy-15,table)
						else:x,y = attachat(cx+15,cy+15,table)
						card.moveToTable(x,y)
						attach = eval(getGlobalVariable("attachmodify"))
						if not attach.has_key(card._id):
							attach[card._id] = choose._id
						else:attach[card._id].append(choose._id)
						setGlobalVariable("attachmodify",str(attach))
						if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and choose.model == "df79718d-b01d-4338-8907-7b6abff58303":choose.markers[MilitaryIcon] += 1#096
						if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":choose.markers[STR_Up] += countusedplot
						if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', card.Text).group()
							choose.markers[STR_Up] += int(stradd[1])
						if re.search('\[INT]\sicon', card.Text):choose.markers[IntrigueIcon] += 1
						if re.search('\[POW]\sicon', card.Text):choose.markers[PowerIcon] += 1
						if re.search('\[MIL]\sicon', card.Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":choose.markers[MilitaryIcon] += 1
						card.sendToBack()
						if len(me.piles['Plot Deck']) == 7:
							notify("{} plays {} and attachs to {}.".format(me,card,choose))
						else:
							card.highlight = PlayColor
							notify("{} plays {} and attachs to {} for {} Gold (Cost reduced by {}).".format(me,card,choose,cost,reduc))
						return True
				else:
					whisper("Attachment cards must be attached to another card or game element.")
					return
		else:
			reduc=askInteger("Reduce Cost by ?",0)
			if reduc == None or cost == None: return False
			if reduc>cost: reduc=cost
			cost-=reduc
			if me.counters['Gold'].value < cost :
				whisper("You don't have enough Gold to pay for {}.".format(card))
				return		
			if card.type == "Character":
				if fll == 1:me.setGlobalVariable("firstcharacter","1")
				clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for character in clist:
						x, y = character.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x-80,y)
					else : 	card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(20,-100)			
					else:card.moveToTable(-20,0)
			elif card.Type == "Location":
				clist = [p for p in table
							if p.controller == me and p.type == "Location" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for location in clist:
						x, y = location.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x-80,y)
					else : 	card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(20,-220)			
					else:card.moveToTable(-20,120)
			elif card.type == "Event":
				if me.isInverted: card.moveToTable(150,-230)
				else: card.moveToTable(-130,130)
				if me.getGlobalVariable("firstevent") == "0":me.setGlobalVariable("firstevent", "1")
				#whisper("Select a target.")
				#checksaveevent(card)
			else:
				if me.isInverted: card.moveToTable(150,-230)
				else: card.moveToTable(-130,130)
			if card.type != "Event":
				card.highlight = PlayColor
			if ambush != 1:notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
			else:notify("{} ambush {} for {} Gold).".format(me,card,cost))
			me.counters['Gold'].value -= cost
			for incomecard in table:
				if incomecard.controller == me and incomecard.markers[Gold] > 0:
					incomecard.markers[Gold] -= cost
			return True
	else:
		if me.isInverted: 
			card.moveToTable(x-8,y-8)
		else:
			card.moveToTable(x+8,y+8)
		card.filter = "#005c3521"
		notify("{} plays {}'s duplicate.".format(me,card))
		card.sendToBack()

			
#------------------------------------------------------------------------------
# New Pile Actions
#------------------------------------------------------------------------------
def checkdeck():
	mute()
	notify (" -> Checking deck of {} ...".format(me))
	ok = True
	
	# Faction and agenda (should be in hand)
	FactionCount = 0
	AgendaCount = 0
	FactionName = ''
	AgendaName = ''
	BannerFaction = ''
	
	for card in me.hand:
		if card.type == 'Faction':
			FactionCount += 1
			FactionName = card.faction
		elif card.type == 'Agenda':
			AgendaCount += 1
			AgendaName = card.name
		else:
			ok = False
			whisper("You have a card in your hand that is not a faction or an agenda, please put it in the appropriate deck.")
			
	if FactionCount != 1:
		ok = False
		whisper("You should have exactly 1 faction card in your hand.")
	if AgendaCount > 1:
		ok = False
		whisper("You can only use 1 agenda.")
		
	if AgendaName == "Banner of the Stag":
		BannerFaction = "Baratheon"
	elif AgendaName == "Banner of the Kraken":
		BannerFaction = "Greyjoy"
	elif AgendaName == "Banner of the Lion":
		BannerFaction = "Lannister"
	elif AgendaName == "Banner of the Sun":
		BannerFaction = "Martell"
	elif AgendaName == "Banner of the Watch":
		BannerFaction = "Night's Watch"
	elif AgendaName == "Banner of the Wolf":
		BannerFaction = "Stark"
	elif AgendaName == "Banner of the Dragon":
		BannerFaction = "Targaryen"
	elif AgendaName == "Banner of the Rose":
		BannerFaction = "Tyrell"
		
	#Plot deck
	MultiplePlotName = ''
	counts = collections.defaultdict(int)
	
	if len(me.piles['Plot Deck']) != 7:
		ok = False
		whisper("Your plot deck must contain exactly 7 cards.")
		
	for card in me.piles['Plot Deck']:
		if card.type != 'Plot':
			ok = False
			whisper("Your plot deck must contain only plots.")
			
		if card.faction != 'Neutral.' and FactionName not in card.faction:
			if card.loyal == 'Yes':
				ok = False
				notify("{}'s plot deck contains a loyal card from another faction.".format(me))
			if BannerFaction == '' or BannerFaction not in card.faction:
				ok = False
				notify("{}'s plot deck contains a card from an illegal faction.".format(me))
				
		counts[card.name] += 1
		
		if counts[card.name] > 1:
			if card.decklimit == '':
					limit = 2
			else:
				limit = int(card.decklimit)
				
			if counts[card.name] > limit:
				ok = False
				notify("{} has {} copies of {} in plot deck, but {} can has only {}.".format(me, counts[card.name], card,me, limit))
				
			if MultiplePlotName == '':
				MultiplePlotName = card.name
			else:
				ok = False
				notify("{} can has several copies of only 1 plot.".format(me))
	
	#Deck
	NeutralCount = 0
	BannerCount = 0
	me.deck.addViewer(me)
	
	if len(me.deck) < 60:
		ok = False
		notify("{}'s deck must contain at least 60 cards.".format(me))
	
	for card in me.deck:
		if card.type != "Character" and card.type != "Location" and card.type != "Attachment" and card.type != "Event":
			ok = False
			notify("{}'s deck must contain only characters, locations, attachments and events.".format(me))
	
		if card.faction == 'Neutral.':
			NeutralCount += 1
		elif FactionName not in card.faction:
			if card.loyal == 'Yes':
				ok = False
				notify("{}'s deck contains a loyal card from another faction.".format(me))
			elif BannerFaction == '' or BannerFaction not in card.faction:
				ok = False
				notify("{}'s deck contains a card from an illegal faction.".format(me))
			else:
				BannerCount += 1
				
		counts[card.name] += 1
		
		if card.decklimit == '':
			limit = 3
		else:
			limit = int(card.decklimit)
		
		if counts[card.name] > limit:
			ok = False
			notify("{} has {} copies of {} in deck, but {} can has only {}.".format(me,counts[card.name], card,me, limit))
	
	if AgendaName == 'Fealty' and NeutralCount > 15:
		ok = False
		notify("{}'s agenda is Fealty, so {} can has 15 neutral cards in deck, but {} have {}.".format(me,me,me, NeutralCount))
	elif BannerFaction != '' and BannerCount < 12:
		ok = False
		notify("{}'s agenda is {}, so {} must has at least 12 {} cards in deck, but {} have only {}".format(me, AgendaName, me,BannerFaction, me,BannerCount))
	
	me.deck.removeViewer(me)
	
	if ok:
		notify("Deck of {} is OK".format(me))
	else:
		notify("Deck of {} is NOT OK".format(me))
	
def shuffleToPlot(group):
	mute()
	for card in group:
		card.moveTo(me.piles['Plot Deck'])
	notify("{} moved all used plots to their plot deck.".format(me))

def createTitles(group):
	mute()
	if len(shared.piles['Titles']) == 6:
		whisper("Melee titles are created.")
	else:
		for card in group:
			card.delete()
		group.create("feefb8d0-f4ed-4d27-b272-3b9e9ee11a5d")
		group.create("3c734e0d-d625-4553-9cf5-74051311eef5")
		group.create("f91c60a9-d506-45f3-b5de-3a51e23279d3")
		group.create("cb3a2844-1aa5-494c-9536-87b4b9bd4562")
		group.create("0ba59f59-b08c-4e8e-ab23-b5cf9e77d176")
		group.create("3b088db8-adeb-4728-9eb9-6817455da6dc")
		notify("{} created melee titles.".format(me))

def removeTitles(group):
	mute()
	card = group.random()
	if card == None: return
	card.delete()
	notify('{} removes a Title'.format(me))
	
def chooseTitle(card):
	mute()
	card.moveToTable(0,0,True)
	card.controller == me
	card.peek()
	notify('{} choose a Title'.format(me))

def movetobottom(card):
	mute()
	if len(card.group) < 2: return
	card.moveToBottom(card.group)
	notify("{} moves a card to bottom of {}'s {}'.".format(me,card.owner,card.group.name))

	
#------------------------------------------------------------------------------
# New Events
#------------------------------------------------------------------------------
def on_table_load():
	mute()
	ver = "1.4.2.0"
	log = changelog["1.4.2.0"]
	log = '\n\n>>> '.join(log)
	choice = confirm("Changes in {}:\n>>> {}\n\nSee more info?".format(ver, log))
	if choice == True:openUrl('https://github.com/TassLehoff/AGoTv2-OCTGN')


def onloaddeck(args):
	mute()
	c = len(players)
	setGlobalVariable("numplayer","{}".format(c))
	if me._id == 1:
		setGlobalVariable("AID","{}".format(me))
	else:
		setGlobalVariable("BID","{}".format(me))
	setGlobalVariable("automode","1")
	setGlobalVariable("tableTargets", "")
	setGlobalVariable("selectmode", "0")
	setGlobalVariable("insertre", "")
	setGlobalVariable("cantchallenge", "0")
	setGlobalVariable("bedefend", "")
	setGlobalVariable("aftcr", "")
	setGlobalVariable("aftcu", "")
	setGlobalVariable("aftcuevent", "-1")
	setGlobalVariable("chaevent", "-1")
	setGlobalVariable("attachmodify", "{}")
	setGlobalVariable("mainstep", "0")
	setGlobalVariable("ambush", "1")
	setGlobalVariable("aftercalculatestand", "[]")
	setGlobalVariable("aftercalculatedraw", "[]")
	setGlobalVariable("ignorestr", "[]")
	setGlobalVariable("addclaim","0")
	setGlobalVariable("addclaimall","0")
	setGlobalVariable("reavelplot","0")
	setGlobalVariable("drawphase","0")
	setGlobalVariable("marshalphase","0")
	me.setGlobalVariable("inmarshal","1")
	me.setGlobalVariable("firstevent", "0")
	me.setGlobalVariable("firstcharacter", "0")
	me.setGlobalVariable("firstll", "0")#A Noble Cause
	setGlobalVariable("challengephase","1")
	setGlobalVariable("standingphase","0")
	setGlobalVariable("taxationphase","0")
	me.setGlobalVariable("milcount","1")
	me.setGlobalVariable("milcountmax","1")
	me.setGlobalVariable("intcount","1")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","1")
	me.setGlobalVariable("powcountmax","1")
	setGlobalVariable("action","0")
	setGlobalVariable("activeplayer","")
	me.setGlobalVariable("active","0")
	setGlobalVariable("winint","0")
	me.setGlobalVariable("intwin", "0")
	me.setGlobalVariable("submilclaim", "0")
	me.setGlobalVariable("subintclaim", "0")
	me.setGlobalVariable("subpowclaim", "0")
	player = args.player
	if player==me:
		checkdeck()
		setup(table)
		
def onmoved(args):
	mute()
	index = 0
	for card in args.cards:
		attach = eval(getGlobalVariable("attachmodify"))
		if args.cards[index].type == "Character" and args.toGroups[index].name == "Table" and args.fromGroups[index].name == "Table" and card.owner == me and card.filter != WaitColor:
			list = []
			list2 = []
			list3 = []
			for d in attach:
				if attach[d] == args.cards[index]._id:
					list.append(d)
			for dcard in table:
				if dcard.name == args.cards[index].name and dcard.filter == WaitColor and dcard.controller == me:
					list2.append(dcard._id)
			list.reverse()
			for cardatt in table:
				for listcard in table:
					if cardatt.controller == me and cardatt.name == listcard.name and  listcard._id in (list) and cardatt.filter == WaitColor:
						list3.append(cardatt)
			i = 12			
			if len(list) > 0:
				for cardindex in list:
					for carda in table:
						if carda._id == cardindex:
							x1,y1 = card.position
							if me.isInverted:carda.moveToTable(x1-i,y1-i)
							else:carda.moveToTable(x1+i,y1+i)
							carda.sendToBack()
							x2,y2 = carda.position
							i+=12
							k = 12
							for cardattd in list3:
								if cardattd.name == carda.name:
									if me.isInverted:cardattd.moveToTable(x2-k,y2+k)
									else:cardattd.moveToTable(x2+k,y2-k)
									cardattd.sendToBack()
									k+=12
			i = 12
			if args.cards[index].unique == "Yes":
				if len(list2) > 0:
					for cardindex in list2:
						for carda in table:
							if carda._id == cardindex:
								x1,y1 = card.position
								carda.moveToTable(x1-i,y1-i)
								carda.sendToBack()
								i+=12
		if card.type == "Attachment" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.owner == me:
			for card in table:
				if attach.has_key(args.cards[index]._id):
					if attach[args.cards[index]._id] == card._id:
						del attach[args.cards[index]._id]
						setGlobalVariable("attachmodify",str(attach))
						debug(getGlobalVariable("attachmodify"))
					#rollback
						if args.cards[index].model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
							card.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
						if args.cards[index].model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and card.model == "df79718d-b01d-4338-8907-7b6abff58303":card.markers[MilitaryIcon] -= 1#096
						if re.search('\+\d\sSTR', args.cards[index].Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', args.cards[index].Text).group()
							card.markers[STR_Up] -= int(stradd[1])
						if re.search('\[INT]\sicon', args.cards[index].Text):card.markers[IntrigueIcon] -= 1
						if re.search('\[POW]\sicon', args.cards[index].Text):card.markers[PowerIcon] -= 1
						if re.search('\[MIL]\sicon', args.cards[index].Text) and args.cards[index].model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":card.markers[MilitaryIcon] -= 1
			args.cards[index].resetProperties()
		if args.cards[index].type == "Character" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.owner == me:
			for d in attach:
				if attach[d] == args.cards[index]._id:
					for cardd in table:
						if cardd._id == d:
							if cardd.Text.find('Terminal.') == -1 and cardd.Keywords.find('Terminal.') == -1:cardd.moveTo(me.hand)
							else:cardd.moveTo(me.piles['Discard pile'])
							del attach[d]
							setGlobalVariable("attachmodify",str(attach))
							debug(getGlobalVariable("attachmodify"))
		index += 1

def setTimer(player,actioninsert,group,x = 0,y = 0):
    global timerIsRunning
    if player != me:return
    debug(actioninsert)
    if timerIsRunning:
        whisper("You cannot start a new timer until the current one finishes!")
        return
    timerIsRunning = True
    if actioninsert == "dominance":seconds = 5
    else:seconds = 2
    #whisper("please action in {} seconds.".format(seconds%60))
    notifications = range(11) + [30] + [x*60 for x in range(seconds/60+1)][1:]
    endTime = time.time() + seconds
    notifications = [endTime - t for t in notifications if t < seconds]
    updateTimer(endTime,notifications,actioninsert)

#This function checks the timer, and then remotecalls itself if the timer has not finished
def updateTimer(endTime,notifications,actioninsert):
    mute()
    global timerIsRunning
    global interruptreactioncard
    global isinsertreaction
    global cardtoaction
    global plotcard
    list = []
    currentTime = time.time()
    if currentTime>notifications[-1]:
            timeLeft = int(endTime - notifications[-1])
            #if timeLeft > 60: whisper("{} minutes left!".format(timeLeft/60))
            #else: whisper("{} seconds left!".format(timeLeft))
            notifications.remove(notifications[-1])
    if notifications: remoteCall(me,"updateTimer",[endTime,notifications,actioninsert])
    else:
		timerIsRunning = False
		if actioninsert == "interruptcancel":
			debug(inserttarget)
			debug(savetarget)
			if sessionpass == "3playeraddstr2selectok":
				for arrowcard in cardtoaction:
					inserttarget.arrow(arrowcard)
			else:inserttarget.arrow(savetarget)
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])
		if actioninsert == "interruptcanceled":
			if interruptcancellastcard == []:
				interruptcanceledcard.arrow(inserttarget)
			else:interruptcanceledcard.arrow(interruptcancellastcard)
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(otherplayer,"interruptlibadd",[interruptpass])
			remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])
		if actioninsert == "reactionaftuok":
			selectedcard[0].arrow(cardtoaction)
			reaction("aftercalculate",1)
		if actioninsert == "keywords":
			keywordforability(2)
		if actioninsert == "dominance":
			standingphase(table)
		if actioninsert == "Confiscationselect":
			remoteCall(cardtoaction.controller,"disc",[cardtoaction])
			notify("{} reaveled {}, discard {} from play.".format(me,plotcard,cardtoaction))#Confiscation
			plotcard.target(False)
			cardtoaction = []
			plotcard = []
		if actioninsert == "FilthyAccusationsselect":
			cardtoaction.orientation == 1
			notify("{} reaveled {}, kneel {}.".format(me,plotcard,cardtoaction))#FilthyAccusations
			plotcard.target(False)
			cardtoaction = []
			plotcard = []


def interruptevent(actioninsert,interruptpasscount):
	mute()
	global interruptpass
	global savetarget
	global inserttarget
	global interruptcancelplayer
	global interruptcancelcard
	global interruptcancelok
	global interruptlib
	global interruptcanceledcard
	global interruptcancellastcard
	global saveactionplayer
	global sessionpass
	global leavecardtype
	global abilityattach
	global reactionattach
	global isinsertreaction
	global interruptreactioncard
	savetargets = []
	inserttargets = []
	interruptcards = []
	list = []
	list2 = []
	list3 = []
	list4= []
	listcancel = []
	Faction = ""
	duplicate = 0
	sourcecard = []
	duplicatecard = []
	cardtype = ""
	tmp = []
	if actioninsert == "miljudgementfp":
		debug(interruptpasscount)
		for card in mjfinishcard:
			if card.highlight == miljudgecolor:
				list2.append(card)
		if len(list2) > 0:
			if sessionpass == "":
				choiceList = ['save player', 'cancel and do not save']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intointerruptevent(interruptpasscount)
					return
				else:
					if interruptpasscount == 2:
						f = (card for card in table  
							if card.name == "1st Player Token")
						for card1 in f:
							if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
							else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
					else:
						interruptpasscount += 1
						remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					return
			if sessionpass == "miljudgementselectok":
				savetargets = selectedcard
				if savetargets == []:
					if interruptpasscount == 2:
						f = (card for card in table  
							if card.name == "1st Player Token")
						for card1 in f:
							if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
							else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
					else:
						interruptpasscount += 1
						remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					sessionpass = ""
					return
			if sessionpass == "savecardselectok":	
				inserttargets = selectedcard
				if inserttargets == []:
					if interruptpasscount == 2:
						f = (card for card in table  
						if card.name == "1st Player Token")
						for card1 in f:
							if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
							else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
					else:
						interruptpasscount += 1
						sessionpass = ""
						remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					return
				else:
					#inserttarget = inserttargets
					sessionpass = ""
					for card in inserttargets:
						if card.filter == WaitColor:
							savetarget.highlight = None
							disc(card)
							remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
							return
						else:
							if card.type == "Event":
								if play(card):cardeffect(card,"saveaction")
								else:
									remoteCall(me, "interruptevent", ["miljudgementfp",interruptpasscount])
									return
							else:cardeffect(card,"saveaction")
							interruptcancelcard = card
						interruptcancelplayer = me
						saveactionplayer = me
						inserttarget = interruptcancelcard
						#interruptlib.append(interruptcancelcard)
						remoteCall(me, "setTimer", [me,"interruptcancel",table])
			else:
				if interruptpasscount < 2:
					interruptpasscount += 1
					remoteCall(otherplayer, "interruptevent", ["miljudgementfp",interruptpasscount])
					return
				if interruptpasscount == 2 and actioninsert == "miljudgementfp":
					f = (card for card in table  
						if card.name == "1st Player Token")
					for card1 in f:
						if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
						else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
		else:
			f = (card for card in table  
				if card.name == "1st Player Token")
			for card1 in f:
				if card1.controller == me:miljudgementfinished(mjfinishcard,claimtmp,1)
				else:remoteCall(otherplayer, "miljudgementfinished", [mjfinishcard,claimtmp,1])
	if actioninsert == "interruptcancel":
		debug(interruptcancelcard)
		debug(interruptlib)
		if interruptpasscount < 2:
			choiceList = ['interrupt', 'cancel']
			colorList = ['#ae0603' ,'#006b34']
			choice = askChoice("Do you want to interrupt {}'s {} ?".format(interruptcancelplayer,interruptcancelcard.name), choiceList,colorList)
		if interruptpasscount == 2:
			choiceList = ['interrupt', 'cancel']
			colorList = ['#ae0603' ,'#006b34']
			choice = askChoice("Do you want to interrupt {}'s {} ?".format(interruptcancelplayer,interruptcancelcard.name), choiceList,colorList)
		if choice == 1:
			for c in me.hand:
				ee = 0
				for d in counterevent:
					if counterevent[d][3] == "Hand" and c.model == counterevent[d][1] and counterevent[d][4].find(interruptcancelcard.Type) != -1:
						if counterevent[d][5] == "all":
							if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
							elif counterevent[d][7] == "all":ee = 1
						elif counterevent[d][5] != "all":
							for cardunique in table:
								if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
									if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
									elif counterevent[d][7] == "all":ee = 1
				if ee == 1:listcancel.append(c)
			for c in table:
				ee = 0
				for d in counterevent:
					if counterevent[d][3] == "table" and c.model == counterevent[d][1] and c.controller == me and counterevent[d][4].find(interruptcancelcard.Type) != -1 and c.highlight == None:
						if counterevent[d][5] == "all":
							if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
							elif counterevent[d][7] == "all":ee = 1
						elif counterevent[d][5] != "all":
							for cardunique in table:
								if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
									if counterevent[d][7] == "opponent" and interruptcancelcard.controller != me:ee = 1
									elif counterevent[d][7] == "all":ee = 1
				if ee == 1:listcancel.append(c)
			dlg = cardDlg(listcancel)
			dlg.title = "These cards are you can used:"
			dlg.text = "Declares 1 card to used.  click close button if none or cancel"
			dlg.min = 1
			dlg.max = 1
			interruptcards = dlg.show()
			if interruptcards == None:
				if interruptpasscount == 2:
					if len(interruptlib) > 0 and interruptcancellastcard != []:
						e = 0
						if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
							playertmp = []
							cardtmp = []
							if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
								if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
									isinsertreaction = 1
									playertmp = interruptlib["pass"+str(interruptpass)][0].controller
									cardtmp = insertreactioncard
									e = 1
						if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
						else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
						del interruptlib["pass"+str(interruptpass)]
						remoteCall(otherplayer,"interruptlibdel",[interruptpass])
						interruptpass -= 1
						if e == 1:
							setGlobalVariable("insertre", "1")
							backupinterruptlib(1)
							remoteCall(otherplayer, "backupinterruptlib", [1])
							remoteCall(playertmp, "interruptreaction", [cardtmp,1])
							return
						if interruptpass > 0:
							e = 0
							if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
								playertmp = []
								cardtmp = []
								if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
									if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
										isinsertreaction = 1
										playertmp = interruptlib["pass"+str(interruptpass)][0].controller
										cardtmp = insertreactioncard
										e = 1
							if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
							else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
							del interruptlib["pass"+str(interruptpass)]
							remoteCall(otherplayer,"interruptlibdel",[interruptpass])
							interruptpass -= 1
							if e == 1:
								setGlobalVariable("insertre", "2")
								backupinterruptlib(1)
								remoteCall(otherplayer, "backupinterruptlib", [1])
								remoteCall(playertmp, "interruptreaction", [cardtmp,1])
								return
						if interruptpass == 0:
							notify("over,disc card")
							debug(inserttarget)
							debug(interruptcancelok)
							if mainpass == "leave":
								if interruptcancelok == 1:
									leavecardtype.append(inserttarget._id)
									remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
								else:
									remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
									else:interruptevent("characterkill",1)
							elif mainpass == "leavereaction":
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
									else:reaction("leavetable",1)
							elif mainpass == "afterchallenge":
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
									else:reaction("afterchallenge",1)
							elif mainpass == "aftercalculate":
								if interruptcancelok == 1:
									if inserttarget.type == "Event":
										if inserttarget.controller == me:disc(inserttarget)
										else:remoteCall(otherplayer, "disc", [inserttarget])
									if interruptcancelok == 1:
										remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
									else:
										for card in table:
											card.target(False)
										remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
										if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
										else:reaction("aftercalculate",1)
							elif mainpass == "challengeaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
									else:action("challenge",1)
							else:
								if interruptcancelok == 1:
									savetarget.highlight = milsavecolor
									savepassfinish(1)
								else:
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								notify("ballanceover")
								if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
								else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
						else:
							interruptcancellastcard = interruptlib["pass"+str(interruptpass)][1]
							interruptcanceledcard = interruptlib["pass"+str(interruptpass)][0]
							interruptcancelcard = interruptcanceledcard
							remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
							if interruptlib["pass"+str(interruptpass)][2] == me:remoteCall(otherplayer, "interruptevent", ["interruptcancel",1])
							else:remoteCall(me, "interruptevent", ["interruptcancel",1])
					else:
						if interruptpass > 0:
							e = 0
							if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
								playertmp = []
								cardtmp = []
								if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
									if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
										isinsertreaction = 1
										playertmp = interruptlib["pass"+str(interruptpass)][0].controller
										cardtmp = insertreactioncard
										e = 1
							if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
							else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
							del interruptlib["pass"+str(interruptpass)]
							remoteCall(otherplayer,"interruptlibdel",[interruptpass])
							interruptpass -= 1
							if e == 1:
								setGlobalVariable("insertre", "3")
								backupinterruptlib(1)
								remoteCall(otherplayer, "backupinterruptlib", [1])
								remoteCall(playertmp, "interruptreaction", [cardtmp,1])
								return
						notify("over,disc card")
						debug(interruptcancelok)
						debug(inserttarget)
						if mainpass == "leave":
							if interruptcancelok == 1:
								leavecardtype.append(inserttarget._id)
								remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
							else:
								remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
								else:interruptevent("characterkill",1)
						elif mainpass == "leavereaction":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
								else:reaction("leavetable",1)
						elif mainpass == "afterchallenge":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
								else:reaction("afterchallenge",1)
						elif mainpass == "aftercalculate":
							if interruptcancelok == 1:
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									for card in table:
											card.target(False)
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
							else:reaction("aftercalculate",1)
						elif mainpass == "challengeaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
								else:action("challenge",1)
						else:		
							if interruptcancelok == 1:
								savetarget.highlight = milsavecolor
								savepassfinish(1)
							else:
								if inserttarget.type != "Character":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
							notify("ballanceover")
							if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
							else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
				else:
					interruptpasscount += 1
					remoteCall(otherplayer, "interruptevent", ["interruptcancel",interruptpasscount])
				return
			else:
				for card in interruptcards:
					if card.type == "Event":
						if play(card):cardeffect(card,"interrupt")
						else:
							remoteCall(me, "interruptevent", ["interruptcancel",interruptpasscount])
							return
					else:cardeffect(card,"interrupt")
					interruptcancelplayer = me
					interruptcancellastcard = interruptcanceledcard
					debug(interruptcancellastcard)
					interruptcanceledcard = card
					interruptcancelcard = card
					interruptpass += 1
					interruptlib["pass"+str(interruptpass)] = (interruptcanceledcard,interruptcancellastcard,me)
					debug(interruptlib)
				if interruptcancelok == 1:interruptcancelok = 0
				else:interruptcancelok = 1
				remoteCall(me, "setTimer", [me,"interruptcanceled",table])
		if choice == 2:
			if interruptpasscount < 2:
				interruptpasscount += 1
				remoteCall(otherplayer, "interruptevent", ["interruptcancel",interruptpasscount])
				return
			if interruptpasscount == 2 and actioninsert == "interruptcancel":
				if len(interruptlib) > 0 and interruptcancellastcard != []:
					e = 0
					if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
						playertmp = []
						cardtmp = []
						if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
							if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
								isinsertreaction = 1
								playertmp = interruptlib["pass"+str(interruptpass)][0].controller
								cardtmp = insertreactioncard
								e = 1
					if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
					else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
					del interruptlib["pass"+str(interruptpass)]
					remoteCall(otherplayer,"interruptlibdel",[interruptpass])
					interruptpass -= 1
					if e == 1:
						setGlobalVariable("insertre", "1")
						backupinterruptlib(1)
						remoteCall(otherplayer, "backupinterruptlib", [1])
						remoteCall(playertmp, "interruptreaction", [cardtmp,1])
						return
					if interruptpass > 0:
						e = 0
						if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
							playertmp = []
							cardtmp = []
							if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
								if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
									isinsertreaction = 1
									playertmp = interruptlib["pass"+str(interruptpass)][0].controller
									cardtmp = insertreactioncard
									e = 1
						if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
						else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
						del interruptlib["pass"+str(interruptpass)]
						remoteCall(otherplayer,"interruptlibdel",[interruptpass])
						interruptpass -= 1
						if e == 1:
							setGlobalVariable("insertre", "2")
							backupinterruptlib(1)
							remoteCall(otherplayer, "backupinterruptlib", [1])
							remoteCall(playertmp, "interruptreaction", [cardtmp,1])
							return
					if interruptpass == 0:
						notify("over,disc card")
						debug(inserttarget)
						debug(interruptcancelok)
						if mainpass == "leave":
							if interruptcancelok == 1:
								leavecardtype.append(inserttarget._id)
								remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
							else:
								remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
								else:interruptevent("characterkill",1)
						elif mainpass == "leavereaction":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
								else:reaction("leavetable",1)
						elif mainpass == "afterchallenge":
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
								else:reaction("afterchallenge",1)
						elif mainpass == "aftercalculate":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
								else:reaction("aftercalculate",1)
						elif mainpass == "challengeaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
								else:action("challenge",1)
						else:
							if interruptcancelok == 1:
								savetarget.highlight = milsavecolor
								savepassfinish(1)
							else:
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							notify("ballanceover")
							if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
							else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
					else:
						interruptcancellastcard = interruptlib["pass"+str(interruptpass)][1]
						interruptcanceledcard = interruptlib["pass"+str(interruptpass)][0]
						interruptcancelcard = interruptcanceledcard
						remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
						if interruptlib["pass"+str(interruptpass)][2] == me:remoteCall(otherplayer, "interruptevent", ["interruptcancel",1])
						else:remoteCall(me, "interruptevent", ["interruptcancel",1])
				else:
					if interruptpass > 0:
						e = 0
						if interruptlib["pass"+str(interruptpass)][0].highlight == sacrificecolor:
							playertmp = []
							cardtmp = []
							if isinsertreaction == 0 and orientationintable(interruptlib["pass"+str(interruptpass)][0]):
								if checkinsertreaction(interruptlib["pass"+str(interruptpass)][0]):
									isinsertreaction = 1
									playertmp = interruptlib["pass"+str(interruptpass)][0].controller
									cardtmp = insertreactioncard
									e = 1
						if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
						else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
						del interruptlib["pass"+str(interruptpass)]
						remoteCall(otherplayer,"interruptlibdel",[interruptpass])
						interruptpass -= 1
						if e == 1:
							setGlobalVariable("insertre", "3")
							backupinterruptlib(1)
							remoteCall(otherplayer, "backupinterruptlib", [1])
							remoteCall(playertmp, "interruptreaction", [cardtmp,1])
							return
					notify("over,disc card")
					debug(interruptcancelok)
					debug(inserttarget)
					if mainpass == "leave":
						if interruptcancelok == 1:
							leavecardtype.append(inserttarget._id)
							remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
						else:
							remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
							else:interruptevent("characterkill",1)
					elif mainpass == "leavereaction":
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
							else:reaction("leavetable",1)
					elif mainpass == "afterchallenge":
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
							else:reaction("afterchallenge",1)
					elif mainpass == "aftercalculate":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
							else:reaction("aftercalculate",1)
					elif mainpass == "challengeaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["challenge",1])
							else:action("challenge",1)
					else:		
						if interruptcancelok == 1:
							savetarget.highlight = milsavecolor
							savepassfinish(1)
						else:
							if inserttarget.type != "Character":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
						notify("ballanceover")
						if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
						else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
	if actioninsert == "characterkill":
		debug("aaaaaa")
		debug(abilityattach)
		if len(abilityattach) > 0:
			if sessionpass == "":
				choiceList = ['interrupt', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intocharacterkill(abilityattach,interruptpasscount)
					return
				else:
					if interruptpasscount == 2:
						cardleavetable(1)
					else:
						interruptpasscount += 1
						remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
					return
			if sessionpass == "killabilityok":
				killcards = selectedcard
				if killcards == []:
					if interruptpasscount == 2:
						cardleavetable(1)
					else:
						interruptpasscount += 1
						sessionpass = ""
						remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
					return
				else:
					debug(killcards[0])
					killcard = killcards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkinterruptkill", [killcard])
		else:
			if interruptpasscount == 2:
				cardleavetable(1)
			else:
				interruptpasscount += 1
				remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
			return

def intocharacterkill(cards,count):
	mute()
	global sessionpass
	global kbcount
	sessionpass = ""
	targetTuple = ([card._id for card in table if card.controller == me and cards.has_key(card._id)], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	sessionpass = "killability"
	kbcount = count



def checkinterruptkill(killcard):
	mute()
	global interruptcancelcard
	global interruptcancelplayer
	global inserttarget
	global interruptcancelok
	global mainpass

	if checkcountercharater(killcard):
		interruptcancelcard = killcard
		interruptcancelplayer = otherplayer
		inserttarget = interruptcancelcard
		mainpass = "leave"
		interruptcancelok = 1
		remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		interruptevent("interruptcancel",2)
	else:
		remoteCall(otherplayer,"leaveforability",[killcard])
		#interruptevent("characterkill",1)


def checkcountercharater(charatercard):
	ee = 0
	for cardhand in me.hand:
		for d in counterevent:
			if cardhand.model == counterevent[d][1] and counterevent[d][4].find(charatercard.Type) != -1:
				if counterevent[d][5] == "all":
					if counterevent[d][7] == "opponent" and charatercard.controller != me:ee = 1
					elif counterevent[d][7] == "all":ee = 1
				elif counterevent[d][5] != "all":
					for cardunique in table:
						if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
							if counterevent[d][7] == "opponent" and charatercard.controller != me:ee = 1
							elif counterevent[d][7] == "all":ee = 1
	if ee == 1:return True

def savepassfinish(ok):
	for d in cardability:
		if inserttarget.model == cardability[d][1]:
			cardtype = cardability[d][2]
			break
	if inserttarget.controller == me:usecardability(inserttarget,cardtype,savetarget)
	else:remoteCall(otherplayer, "usecardability", [inserttarget,cardtype,savetarget])

def usecardability(card,cardtype,target):
	attach = eval(getGlobalVariable("attachmodify"))
	if cardtype == "Attachment" and card.type != "Attachment":
		if target.Keywords.find('No attachments.') == -1:
			cx,cy = target.position
			if me.isInverted:x,y = attachat(cx-15,cy-15,table)
			else:x,y = attachat(cx+15,cy+15,table)
			card.moveToTable(x,y)
			debug(attach)
			if not attach.has_key(card._id):
				attach[card._id] = target._id
			else:attach[card._id].append(target._id)
			setGlobalVariable("attachmodify",str(attach))
			if re.search('\+\d\sSTR', card.Text):
				stradd = re.search('\+\d\sSTR', card.Text).group()
				target.markers[STR_Up] += int(stradd[1])
			card.sendToBack()
			card.type = "Attachment"
		else:
			disc(card)
	else:
		if attach.has_key(card._id):
			if attach[card._id] == target._id:
				del attach[card._id]
				setGlobalVariable("attachmodify",str(attach))
		debug(getGlobalVariable("attachmodify"))
		disc(card)

def getinterruptpass(interruptpassn):
	global interruptpass
	interruptpass = interruptpassn

def interruptlibadd(interruptpassn):
	global interruptpass
	interruptpass = interruptpassn
	interruptlib["pass"+str(interruptpass)] = (interruptcanceledcard,interruptcancellastcard,otherplayer)

def interruptlibdel(interruptpassn):
	global interruptpass
	interruptpass = interruptpassn
	del interruptlib["pass"+str(interruptpass)]
	interruptpass -= 1

def cardeffect(card,actioninsert):
	mute()
	if actioninsert == "saveaction":
		for d in saveaction:
			if card.model == saveaction[d][1]:
				if  saveaction[d][2] == "Event":card.highlight = None
				if  saveaction[d][2] == "sacrifice":card.highlight = sacrificecolor
				if  saveaction[d][2] == "kneel":kneel(card)
	if actioninsert == "interrupt":
		for d in counterevent:
			if card.model == counterevent[d][1]:
				if  counterevent[d][2] == "sacrifice":card.highlight = sacrificecolor
				else:card.highlight = interruptcolor

def savetargetinserttarget(savetargetn,inserttargetn,interruptcancelcardn,interruptcancelplayern,interruptcancellastcardn,interruptcanceledcardn,interruptcancelokn,saveactionplayern,mainpassn):
	mute()
	global savetarget
	global inserttarget
	global interruptcancelcard
	global interruptcancelplayer
	global interruptcanceledcard
	global interruptcancellastcard
	global interruptlib
	global interruptcancelok
	global saveactionplayer
	global mainpass

	interruptcancelok = interruptcancelokn
	savetarget = savetargetn
	inserttarget = inserttargetn
	interruptcancelcard = interruptcancelcardn
	interruptcancelplayer = interruptcancelplayern
	interruptcancellastcard = interruptcancellastcardn
	interruptcanceledcard = interruptcanceledcardn
	saveactionplayer =  saveactionplayern
	mainpass = mainpassn

def characterkilled(cardbekill,count):
	mute()
	global abilityattach
	c = 0
	list = []
	for card in table:
		if card.type == "Attachment":
			list.append(card)
	for card in cardbekill:
		for d in cardkill:
			if card.model == cardkill[d][1] and card.controller == me and cardkill[d][2] != "link":
				if cardkill[d][4] == "Attachment":
					if len(list) > 0:
						if not abilityattach.has_key(card._id):
							abilityattach[card._id] = 1
						else:abilityattach[card._id] += 1
				elif cardkill[d][4] != "Attachment":
					if not abilityattach.has_key(card._id):
						abilityattach[card._id] = 1
					else:abilityattach[card._id] += 1
	debug(abilityattach)
	for card in cardbekill:
		for d in cardkill:
			if card.model == cardkill[d][1] and cardkill[d][2] == "link" :
				for cards in table:
					if cards.controller == me and cards.name == cardkill[d][6]:
						if not abilityattach.has_key(cards._id):
							abilityattach[cards._id] = 1
						else:abilityattach[cards._id] += 1
	debug(abilityattach)
	if count == 1:remoteCall(otherplayer, "characterkilled", [cardbekill,2])
	else:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
				#if re.search('\d\spower', cardkill[d][3]):
					#powadd = re.search('\d\spower', cardkill[d][3]).group()
					#for c in table: 
						#if c.Type == "Faction" and c.controller == me:
							#c.markers[Power] += int(powadd[0])
def leaveforability(card):
	mute()
	debug(card)
	global abilityattach
	global sessionpass
	sessionpass = ""
	c = ""
	leavecardtype.append(card._id)
	for d in cardkill:
		if card.model == cardkill[d][1] and card.controller == me:
			if re.search('\d\spower', cardkill[d][3]):
				powadd = re.search('\d\spower', cardkill[d][3]).group()
				addhousepow(int(powadd[0]))
			if cardkill[d][2] == "other":
				if cardkill[d][4] == "card" and cardkill[d][3] == "discard":
					if len(players[1].hand) > 0:remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
				if cardkill[d][4] == "other" and cardkill[d][3] == "discard":
					if len(players[1].hand) > 0:remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
			if cardkill[d][2] == "all":
				if cardkill[d][4] == "Attachment" and cardkill[d][3] == "discard":
					c = "discattch"
					#discattch(table)
				if cardkill[d][4] == "Character" and cardkill[d][3] == "kneel":
					c = "kneelplayer"
					#kneelplayer(table)
	abilityattach[card._id] -= 1
	if abilityattach[card._id] == 0:del abilityattach[card._id]
	if c == "discattch":
		discattch(table)
		return
	if c == "kneelplayer":
		kneelplayer(table)
		return
	remoteCall(otherplayer,"interruptevent",["characterkill",1])

def discattch(group, x=0, y=0):
	mute()
	global sessionpass
	targetTuple = ([card._id for card in table if card.type == "Attachment"], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	sessionpass = "discattch"


def kneelplayer(group, x=0, y=0):
	mute()
	global sessionpass
	targetTuple = ([card._id for card in table if card.orientation == 0 and card.type == "Character"], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	sessionpass = "kneel"


def cardleavetable(count):
	mute()
	global leavecardtype
	global abilityattach
	global leavetablecard
	debug(leavecardtype)
	for card in table:
		if card.highlight == miljudgecolor and card.controller == me:
			leavetablecard.append(card)
			if card._id in leavecardtype:
				notify("{} killed {}.".format(me,card))
				for d in leavedeck:
					if card.model == leavedeck[d][1]:
						if leavedeck[d][2] == "deck":
							card.moveToBottom(me.deck)
							me.deck.shuffle()
					else:
						card.moveTo(me.piles['Dead pile'])
			else:
				if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":
					notify("{} killed {}.".format(otherplayer,card))
				else:
					notify("{} killed {}.".format(me,card))
				card.moveTo(me.piles['Dead pile'])
	leavecardtype = []
	abilityattach = []
	if count == 1:
		remoteCall(otherplayer, "getleavetablecard", [leavetablecard])
		remoteCall(otherplayer, "cardleavetable", [2])
	else:
		remoteCall(otherplayer, "getleavetablecard", [leavetablecard])
		f = (card for card in table  
				if card.name == "1st Player Token")
		for card1 in f:
			if card1.controller == me:
				checkreactioncard(1)
			else:
				remoteCall(otherplayer, "checkreaction", [1])

def getleavetablecard(leavetablecardn):
	global leavetablecard
	leavetablecard = leavetablecardn


def reaction(actioninsert,reactioncount):
	mute()
	global sessionpass
	global intertreaction
	if actioninsert == "leavetable":
		setGlobalVariable("mainstep", "77")
		if len(reactionattach) > 0:
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,"reaction")
					return
				if choice == 2:
					if reactioncount == 2:
						if getGlobalVariable("insertre") != "":
							restoreinterruptlib(1)
							return
						if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)
						else:remoteCall(winplayer, "keyword", [1])
					else:
						reactioncount += 1
						remoteCall(otherplayer, "reaction", ["leavetable",reactioncount])
					return
			if sessionpass == "reactionok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)
						else:remoteCall(winplayer, "keyword", [1])
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "reaction", ["leavetable",reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkreaction", [reactioncard,"leavetable"])
		else:
			if reactioncount == 2:
				if getGlobalVariable("insertre") != "":
					restoreinterruptlib(1)
					return
				if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)
				else:remoteCall(winplayer, "keyword", [1])
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["leavetable",reactioncount])
			return
	if actioninsert == "afterchallenge":
		if len(reactionattach) > 0:
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,"reactionaftc")
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						remoteCall(otherplayer, "reaction", ["afterchallenge",reactioncount])
					return
			if sessionpass == "reactionaftcok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "reaction", ["afterchallenge",reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkreaction", [reactioncard,"afterchallenge"])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["afterchallenge",reactioncount])
			return
	if actioninsert == "aftercalculate":
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,"reactionaftu")
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(5)
					else:
						reactioncount += 1
						remoteCall(otherplayer, "reaction", ["aftercalculate",reactioncount])
					return
			if sessionpass == "reactionaftuok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(5)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "reaction", ["aftercalculate",reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkreaction", [reactioncard,"aftercalculate"])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(5)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["aftercalculate",reactioncount])
			return
	if actioninsert == "aftercalculatef":
		if len(reactionattach) > 0:
			for card in table:
				for d in reactionattach:
					if card._id == d:
						reactionforability(card,"aftercalculate")
						return
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(3)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", ["aftercalculatef",reactioncount])
			return
	if actioninsert == "keywords":
		choiceList = ['reaction', 'cancel']
		colorList = ['#006b34' ,'#ae0603']
		choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
		if choice == 1:
			remoteCall(otherplayer, "checkreaction", [cardtoaction,"keywords"])
			return
		if choice == 2:
			keywordforability(1)

def checkreaction(reactioncard,repass):
	mute()
	global interruptcancelcard
	global interruptcancelplayer
	global inserttarget
	global interruptcancelok
	global interruptcanceledcard
	global mainpass
	global leavecardtype
	global sessionpass

	sessionpass = ""
	
	if checkcountercharater(reactioncard):
		if getGlobalVariable("insertre") == "1":
			interruptcanceledcard = []
		interruptcancelcard = reactioncard
		interruptcancelplayer = otherplayer
		inserttarget = interruptcancelcard
		mainpass = repass
		interruptcancelok = 1
		remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		remoteCall(me, "interruptevent", ["interruptcancel",2])
	else:
		remoteCall(otherplayer,"reactionforability",[reactioncard,repass])

def intoreaction(cards,count,sepass):
	mute()
	global sessionpass
	global recount
	sessionpass = ""
	targetTuple = ([d for d in reactionattach], me._id)
	#targetTuple = ([card._id for card in table if card.controller == me and cards.has_key(card._id)], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	sessionpass = sepass
	recount = count

def reactionforability(card,repass):
	mute()
	debug(card)
	global reactionattach
	global sessionpass
	global reactioncardlimit
	global intertreaction
	global cardtoaction
	global savetarget
	sessionpass = ""
	c = 0
	f = 0
	debug(mainpass)
	if repass == "leavetable":
		for d in leavereacion:
			if card.model == leavereacion[d][1] and card.controller == me:
				if re.search('\d\spower', leavereacion[d][4]):
					powadd = re.search('\d\spower', leavereacion[d][4]).group()
					card.markers[Power] += (int(powadd[0]))
					notify("{}'s {} reaction add 1 pow to him".format(me,card))
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == leavereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if leavereacion[d][2] == "Faction" and leavereacion[d][4] == "stand":
					for cards in table:
						if cards.type == "Character" and cards.controller == me:
							cards.orientation = 0
					notify("{}'s {} reaction stand each character".format(me,card))
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == leavereacion[d][5]:
						del reactionattach[card._id]
						c = 1
		if getGlobalVariable("insertre") != "":
			restoreinterruptlib(1)
			return
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(otherplayer, "reaction", ["leavetable",1])
	if repass == "afterchallenge":
		for d in afterchallengereacion:
			if card.model == afterchallengereacion[d][1] and card.controller == me:
				if re.search('\d\sgold', afterchallengereacion[d][4]):
					goldadd = re.search('\d\sgold', afterchallengereacion[d][4]).group()
					me.counters['Gold'].value += (int(goldadd[0]))
					notify("{}'s {} reaction get {} gold".format(me,card,int(goldadd[0])))#imp
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if afterchallengereacion[d][4] == "stand":
					card.orientation = 0
					notify("{}'s {} reaction stand himself".format(me,card))#ned
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if afterchallengereacion[d][4] == "stealth":
					for cardcant in table:
						if cardcant._id == int(getGlobalVariable("cantchallenge")):cardcant.highlight = cantchallengecolor
					notify("{}'s {} reaction its target cannot be declared as a defender for any challenges until the end of the phase.".format(me,card))#ghost
					setGlobalVariable("cantchallenge", "")
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
				if afterchallengereacion[d][4] == "makedefender":
					for cardbdf in table:
						if str(cardbdf._id) in getGlobalVariable("bedefend"):cardbdf.highlight = usedplotcolor
					notify("{}'s {} reaction its target must be declared as a defender for the challenge".format(me,card))#Dornish Paramour
					if not reactioncardlimit.has_key(card._id):
						reactioncardlimit[card._id] = 1
					else:reactioncardlimit[card._id] += 1
					if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
						del reactionattach[card._id]
						c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(otherplayer, "reaction", ["afterchallenge",1])
	if repass == "aftercalculate":
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me:
				if aftercalculate[d][4] == "disotherattachment":
					remoteCall(otherplayer,"disc",[cardtoaction])
					cardtoaction = []
					notify("{}'s {} reaction disc a attachment".format(me,card))#RattleshirtsRaiders					
				if aftercalculate[d][4] == "kill":
					card.highlight = sacrificecolor
					disc(card)
					f = 1
					notify("{}'s {} reaction kill {}".format(me,card,cardtoaction))#ThrowingAxe,Ice
					savetarget = cardtoaction
					cardtoaction = []
				if aftercalculate[d][4] == "attkilldef":
					f = 1
					disc(card)
					notify("{}'s {} reaction kill a character".format(me,card))#PuttotheSword
				if aftercalculate[d][4] == "disotherloaction":
					remoteCall(otherplayer,"disc",[cardtoaction])
					cardtoaction = []
					notify("{}'s {} reaction disc a loaction".format(me,card))#PuttotheTorch
				if re.search('\d\spow', aftercalculate[d][4]):
					powadd = re.search('\d\spower', aftercalculate[d][4]).group()
					addhousepow(int(powadd[0]))
					notify("{}'s {} reaction get {} pow".format(me,card,powadd))#SuperiorClaim
				if aftercalculate[d][4] == "stand":
					card.orientation = 0
					notify("{}'s {} reaction stand her".format(me,card))#AshaGreyjoy
				if aftercalculate[d][4] == "addpowself":
					card.markers[Power] += 1
					notify("{}'s {} reaction he gains 1 power".format(me,card))#TheonGreyjoy
				if aftercalculate[d][4] == "5pwinpow":
					ppoint = (attacker.counters['Str'].value - defender.counters['Str'].value)//5
					card.markers[Power] += ppoint
					notify("{}'s {} reaction he gains {} power".format(me,card,ppoint))#TheRedViper
				if aftercalculate[d][4] == "drawcardorpower":
					choiceList = ['draw 1 card', 'gain 1 power']
					colorList = ['#006b34' ,'#ae0603']
					choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
					if choice == 1:
						draw(me.deck)
						notify("{}'s {} reaction draw 1 card".format(me,card))#GreatKraken
					if choice == 2:
						addhousepow(1)
						notify("{}'s {} reaction gain 1 power".format(me,card))#GreatKraken
				if aftercalculate[d][4] == "drawcard":
					draw(me.deck)
					notify("{}'s {} reaction draw 1 card".format(me,card))#Lannisport
				if aftercalculate[d][4] == "losekill":
					f = 1
					notify("{}'s {} reaction kill a character".format(me,card))#LikeWarmRain
					cardtoaction = []
				if aftercalculate[d][4] == "returndefender":
					remoteCall(otherplayer,"returncard",[cardtoaction])
					notify("{}'s {} reaction return {} to its owner's hand".format(me,card,cardtoaction))#GhastonGrey
					cardtoaction = []
				if aftercalculate[d][4] == "addusedplotpow":
					powadd = 5#......
					addhousepow(int(powadd))
					notify("{}'s {} reaction get {} pow".format(me,card,powadd))#DoransGame
				if aftercalculate[d][4] == "draw2card":
					draw(me.deck)
					draw(me.deck)
					notify("{}'s {} reaction draw 2 card".format(me,card))#TheMander
				if aftercalculate[d][4] == "addmarker":
					cardtoaction.markers[TokenBlue] += 1		
					notify("{}'s {} reaction place a poison token on {}".format(me,card,cardtoaction))#TearsofLys
					cardtoaction = []
				if aftercalculate[d][4] == "subability2":
					cardtoaction.markers[TokenBlue] += 2
					notify("{}'s {} reaction {} gets -2 STR".format(me,card,cardtoaction))#PlazaofPunishment
					for cards in table:
						cards.target(False)
					if int(cardtoaction.strength) + cardtoaction.markers[STR_Up] - cardtoaction.markers[Burn] - 2 <= 0:
						f = 1
						savetarget = cardtoaction
					cardtoaction = []
				if aftercalculate[d][4] == "addclaim":
					kneel(card)
					debug(challengetype)
					notify("{}'s {} reaction raise the claim value by 1".format(me,card,cardtoaction))#Sunspear
				if aftercalculate[d][4] == "standstm":
					for cards in table:
						cards.target(False)
					kneel(cardtoaction)		
					notify("{}'s {} reaction stand {}".format(me,card,cardtoaction))#Rhaegal
					cardtoaction = []
				if aftercalculate[d][4] == "discard":
					remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])
					notify("{}'s {} reaction {} discard 1 card".format(me,card,otherplayer))#MaesterLomys
				if aftercalculate[d][4] == "addplayer":
					card.highlight = sacrificecolor
					disc(card)
					clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
					if len(clist) > 0:
						clist.reverse()
						for character in clist:
							x, y = character.position
							break
						clist.reverse()
						if me.isInverted:cardtoaction.moveToTable(x-80,y)
						else:cardtoaction.moveToTable(x+80,y)
					notify("{}'s {} reaction put {} into play".format(me,card,cardtoaction))#DothrakiSea
					cardtoaction = []
				if aftercalculate[d][4] == "cantchallenge":
					debug("cannot initiate challenges")
					notify("{}'s {} reaction {} cannot initiate challenges".format(me,card,otherplayer))#TheSwordintheDarkness
				if aftercalculate[d][4] == "cant1challenge":
					c1c = ''
					choiceList = ['Military', 'Intrigue', 'Power']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which challenge do you want to cannot initiate?", choiceList,colorList)
					if choice == 1:c1c = 'Military'
					if choice == 2:c1c = 'Intrigue'
					if choice == 3:c1c = 'Power'
					if choice != 0:notify("{}'s {} reaction cannot initiate {} challenges".format(me,card,c1c))#UnbowedUnbentUnbroken
				if aftercalculate[d][4] == "addplayer6":
					clist = [p for p in table
							if p.controller == me and p.type == "Character" and p.isFaceUp]
					if len(clist) > 0:
						clist.reverse()
						for character in clist:
							x, y = character.position
							break
						clist.reverse()
						if me.isInverted:cardtoaction.moveToTable(x-80,y)
						else:cardtoaction.moveToTable(x+80,y)
					notify("{}'s {} reaction put {} into play".format(me,card,cardtoaction))#TheQueenofThorns
					cardtoaction = []
				if aftercalculate[d][4] == "addhand":
					remoteCall(otherplayer, "choosetype", [card])#OlennasCunning
					return
				if aftercalculate[d][4] == "submarker":
					choiceList = []
					colorList = []
					if cardtoaction.Military == "Yes" or cardtoaction.markers[MilitaryIcon] > 0:
						choiceList.append("Military")
						colorList.append('#ae0603')
					if cardtoaction.Intrigue == "Yes" or cardtoaction.markers[IntrigueIcon] > 0:
						choiceList.append("Intrigue")
						colorList.append('#006b34')
					if cardtoaction.Power == "Yes" or cardtoaction.markers[PowerIcon] > 0:
						choiceList.append("Power")
						colorList.append('#1a4d8f')
					if choiceList != []:
						choice = askChoice("Which challenge icon do you want to loses?", choiceList,colorList)
					if choice != 0:
						c1c = choiceList[choice-1]
						notify("{}'s {} reaction {} loses {} challenge icon".format(me,card,cardtoaction,c1c))#MaesterCaleotte
					for cards in table:
						cards.target(False)
					cardtoaction = []
				if aftercalculate[d][4] == "movepow":
					remoteCall(otherplayer, "subhousepow", 1)
					addhousepow(1)
					notify("{}'s {} reaction move 1 power icon from {}".format(me,card,otherplayer))#AClashofKings
				if aftercalculate[d][4] == "addred":
					card.markers[TokenRed] += 1
					notify("{}'s {} forced reaction add 1 betrayal token".format(me,card))#SerJorahMormont
					if card.markers[TokenRed] == 3:
						card.highlight = sacrificecolor
						notify("{}'s {} reaction already have 3 betrayal token,sacrifice him".format(me,card))#SerJorahMormont
						disc(card)
				if aftercalculate[d][4] == "kneel":
					kneel(card)
					notify("{}'s {} forced reaction kneel it".format(me,card))#CastleBlack
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == aftercalculate[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		if f == 1:
			savetarget.highlight = miljudgecolor
			setGlobalVariable("aftcuevent", str(me._id))
			miljudgementfinish([savetarget],1)
			remoteCall(otherplayer, "miljudgementfinish", [[savetarget],1])
			remoteCall(otherplayer, "interruptevent", ["miljudgementfp",2])
		else:
			if "Forced Reaction" in card.Text:remoteCall(otherplayer, "reaction", ["aftercalculatef",1])
			else:remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if repass in "1234":
		if repass == "1":choosedtype = "Character"
		if repass == "2":choosedtype = "Location"
		if repass == "3":choosedtype = "Attachment"
		if repass == "4":choosedtype = "Event"
		listtype = []
		for cardt in me.deck:
			if cardt.type != choosedtype:
				listtype.append(cardt)
		if len(listtype) > 0:
			dlg = cardDlg(listtype)
			dlg.title = "These cards are in your deck:"
			dlg.text = "select 1 card add it to your hand."
			dlg.min = 1
			dlg.max = 1
			cards = dlg.show()
			c = 0
			if cards != None:
				cards[0].moveTo(me.hand)
				me.deck.shuffle()
				notify("{}'s {} reaction put {} into {}'s hand".format(me,card,cards[0],me))
		else:whisper("{} search failed".format(card))
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me:
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == aftercalculate[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if repass == "keywords":
		list = []
		for card in otherplayer.piles['Discard Pile']:
			if card.type == "Location":
				list.append(card)
				debug(card)
		dlg = cardDlg(list)
		dlg.title = "These cards are in your table:"
		dlg.text = "Declares at least 1 Location to move."
		dlg.min = 1
		dlg.max = 1
		cards = dlg.show()
		if cards != None:
			remoteCall(otherplayer, "movecard", [cards[0]])
			cards[0].controller = me
			notify("{}'s {} reaction put {} into play under {} control.".format(me,cardtoaction,cards[0],me))
		keywordattach.remove(cardtoaction)
		cardtoaction = []
		keywordforability(1)

def checkreactioncard(count):
	mute()
	global reactionattach
	for card in table:
		for d in leavereacion:
			if card.model == leavereacion[d][1] and card.controller == me:
				for cards in leavetablecard:
					if leavereacion[d][2] == "Traits":
					 	if leavereacion[d][3] == "Lord./Lady.":
					 		if cards.Traits.find("Lord.") !=-1 or cards.Traits.find("Lady.") !=-1:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					elif leavereacion[d][2] == "Faction":
						if cards.Faction.find(leavereacion[d][3]) != -1 and cards.controller == me and orientationintable(card):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	debug("reactionattach2")
	debug(reactionattach)
	if count == 1:remoteCall(otherplayer, "checkreactioncard", [2])
	else:remoteCall(otherplayer, "reaction", ["leavetable",1])

def checkafterchallengereacioncard(count):
	mute()
	global reactionattach
	for card in table:
		for d in afterchallengereacion:
			if card.model == afterchallengereacion[d][1] and card.controller == me:
				if afterchallengereacion[d][2] != "all":
				 	if afterchallengereacion[d][2] == str(challengetype):
				 		if afterchallengereacion[d][3] == "all":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
				elif afterchallengereacion[d][2] == "all":
					if afterchallengereacion[d][4] == "stand" and card.orientation == 1 and card.controller != attacker:
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1
					if afterchallengereacion[d][4] == "stealth" and int(getGlobalVariable("cantchallenge")) > 1 and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
						if checktablecount(0) > 0 and card.controller == attacker:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
					if afterchallengereacion[d][4] == "makedefender" and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
						if checktablecount(0) > 0 and card.controller == attacker:
							setGlobalVariable("bedefend","[]")
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	debug("reactionattach1")
	debug(reactionattach)
	if len(reactionattach) > 0:setGlobalVariable("aftcr", "1")
	if count == 1:remoteCall(otherplayer, "checkafterchallengereacioncard", [2])
	else:
		if getGlobalVariable("aftcr") == "1":
			setGlobalVariable("aftcr", "")
			if fplay(1) == me:reaction("afterchallenge",1)
			else: 
				remoteCall(otherplayer, "reaction", ["afterchallenge",1])
		else:
			challengeaction(1)

def selectstealth(group, x=0, y=0):
	mute()
	global sessionpass
	targetTuple = ([card._id for card in table if card.type == "Character" and card.controller != me and card.keywords.find("Stealth") == -1], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	sessionpass = "stealthselect"

def selectcard(group,dlgmax,dlgmin,dlgtitle,dlgtext):
	listname = []
	listsamename = []
	dictsame = {}
	disctlistcount = {}
	listcheckcard = []
	listunsamecard = []
	global selectplayer
	selectplayer = []
	for card in group:
		if card.name not in listname:
			listname.append(card.name) 
		else:
			listsamename.append(card.name)
	for cname in listsamename:
		dictsame[cname]= 0
	for cardname in group:
		if cardname.name in listsamename:dictsame[cardname.name] = dictsame[cardname.name]+1

	dlg = cardDlg(group)
	dlg.title = dlgtitle
	dlg.text = dlgtext
	dlg.max = dlgmax
	dlg.min = dlgmin
	select = dlg.show()
	if select == None:selectcard(group,dlgmax,dlgmin,dlgtitle,dlgtext)
	else:
		debug(listsamename)
		for countcard in select:
			if countcard.name in listsamename:
				disctlistcount[countcard.name] = 0
		for countcards in select:
			if countcards.name in listsamename:
				disctlistcount[countcards.name] = disctlistcount[countcards.name]+1
		debug(listsamename)
		debug(disctlistcount)
		debug(dictsame)
		for cardselect in select:
			if cardselect.name in listsamename:
				if disctlistcount[cardselect.name] != dictsame[cardselect.name]:
					listcheckcard.append(cardselect.name)
		for card in select:
			if card.name not in listcheckcard:
				selectplayer.append(card)
		debug(listcheckcard)
		if len(listcheckcard) > 0:
			samecardproscess(group,listcheckcard,disctlistcount)

def samecardproscess(group,listname,count):
	global selectplayer
	listcard = []
	listchoice = []
	listcolor = []
	#listname = [carda,cardb....]
	#count= {carda:1,cardb:2.....}
	processcardname = ""
	debug(listname)
	for c in listname:
		processcardname = c
		break
	debug(processcardname)
	for card in group:
		if card.name == processcardname and card not in selectplayer:
			listchoice.append(card.name+" ability: "+str(int(card.Strength)+card.markers[STR_Up]))
			listcolor.append('#8f8f8f')
			listcard.append(card)
	choice = askChoice("select one?", listchoice,listcolor)
	if choice == 0:samecardproscess(group,listname,count)
	else:choice -= 1

	selectplayer.append(listcard[choice])
	listcard[choice].highlight = leaveandabilitycolor

	count[processcardname] -= 1
	if count[processcardname] == 0:
		del count[processcardname]
		listname.remove(processcardname)
	debug(count)
	if len(count) > 0:
		samecardproscess(group,listname,count)
	else:
		notify("ok")
		debug(selectplayer)

def next(group, x=0, y=0):
	mute()
	global selectedcard
	global sessionpass
	global stealthcount
	global savetarget
	global abilityattach
	global nextcardtmp
	global cardtoaction
	global interruptcancelcard
	global interruptcancelplayer
	global saveactionplayer
	global inserttarget
	global savetarget
	global mainpass
	global dwtmpcard
	global listattach
	debug(sessionpass)
	selectedcard = []
	list = []
	listsave = []
	for card in table:
		if card.targetedBy == me:
			selectedcard.append(card)
	for card in me.hand:
		if card.targetedBy == me:
			selectedcard.append(card)
	if sessionpass == "stealthselect":
		if len(selectedcard) > stealthcount:
			whisper("You must select {} character.".format(stealthcount))
			return
		else:
			sessionpass = "stealthselectok"
			stealthcard(table)
	if sessionpass == "milkillplayerselect":
		claim = challengeclaim(table)
		for card in table:
			if card.type == "Character" and card.controller == me and card.filter != WaitColor:
				list.append(card)
		c = len(list)
		if c < claim:
			b = c
		else:
			b = claim
		if len(selectedcard) != b:
			whisper("You must select {} character.".format(b))
			return
	if sessionpass == "attatchcardselect":
		if len(selectedcard) > 1:
			whisper("You must select only one character to attach.")
			return
		if len(selectedcard) == 0:
			whisper("You must select only one character to attach.")
			return
	if sessionpass == "discattch":
		if len(selectedcard) > 1:
			whisper("You must select only one attachment to discard.")
			return
		elif len(selectedcard) == 1:
			for card in table:
				card.target(False)
			remoteCall(selectedcard[0].controller, "disc", [selectedcard[0]])
	if sessionpass == "kneel" or sessionpass == "initimidateselect" or sessionpass == "FilthyAccusationsselect":
		if len(selectedcard) > 1:
			whisper("You must select only one character to kneel.")
			return
		elif len(selectedcard) == 1:
			for card in table:
				card.target(False)
			remoteCall(selectedcard[0].controller, "kneel", [selectedcard[0]])
	if sessionpass == "miljudgementselect":
		if len(selectedcard) > 1:
			whisper("You must select only one character to save.")
			return
		if len(selectedcard) == 1:
			listsave = checksavecard(selectedcard)
			if listsave != []:
				debug(listsave)
				for card in table:
					card.target(False)
				savetarget = selectedcard[0]
				debug("savetarget")
				debug(savetarget)
				targetTuple = ([card._id for card in listsave], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				sessionpass = "savecardselect"
				notify("**{} into selectmode**".format(me))
				return
			else:
				whisper("You cannot save the character")
				return
	if sessionpass == "reactionaftc":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1 and selectedcard[0].model == afterchallengereacion['DornishParamour'][1] and getGlobalVariable("bedefend") != "":
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "bedefendselect"
			notify("**{} into selectmode**".format(me))
			return
	if sessionpass == "bedefendselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
	if sessionpass == "Direwolfselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1:
			dwtmpcard = selectedcard[0]
			#kneel(selectedcard[0])
			for card in me.hand:
				card.target(False)
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.highlight == IntrigueColor], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "killselect"
			notify("**{} into selectmode**".format(me))
			return			
	if sessionpass == "reactionaftu":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['RattleshirtsRaiders'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Attachment" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "discattchselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['ThrowingAxe'][1]:
			nextcardtmp = selectedcard[0]
			if challengetype == 1:color = MilitaryColor
			if challengetype == 2:color = IntrigueColor
			if challengetype == 3:color = PowerColor
			debug(color)
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.highlight == color], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "attkilldefselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['GhastonGrey'][1]:
			nextcardtmp = selectedcard[0]
			if challengetype == 1:color = MilitaryColor
			if challengetype == 2:color = IntrigueColor
			if challengetype == 3:color = PowerColor
			debug(color)
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.highlight == color], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "returndefenderselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['PuttotheSword'][1]:
			nextcardtmp = selectedcard[0]
			debug(nextcardtmp)
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "killselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['LikeWarmRain'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.controller == me and card.Traits == "Direwolf." and card.orientation == 0], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "Direwolfselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['PuttotheTorch'][1]:
			nextcardtmp = selectedcard[0]
			debug(nextcardtmp)
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Location" and card.controller != me], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "Locationselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['TearsofLys'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me and card.Intrigue != "Yes" and  card.markers[IntrigueIcon] == 0], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "lysselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['PlazaofPunishment'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			attach = eval(getGlobalVariable("attachmodify"))
			listpop = []
			for card in table:
				if card.controller != me:
					c = 0
					for d in attach:
						if card._id == d:
							c = 1
					if c == 0:
						listpop.append(card)
			targetTuple = ([card._id for card in table if card in listpop ], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "popselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['TheMander'][1]:
			kneel(selectedcard[0])
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['Rhaegal'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and "Stormborn." in card.Traits and card.orientation == 1], me._id) 
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "stmselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['DothrakiSea'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in me.hand if card.Type == "Character" and "Dothraki." in card.Traits], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "dothrakiselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['TheQueenofThorns'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in me.hand if "Tyrell." in card.Faction and int(card.cost) <= 6 and card.Type == "Character"], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "tyrellselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['MaesterCaleotte'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character"], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "submarkerselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == aftercalculate['Ice'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Type == "Character" and card.controller != me], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "iceselect"
			notify("**{} into selectmode**".format(me))
			return
	if sessionpass == "challenge":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			remoteCall(otherplayer, "action", ["challenge",1])
		if len(selectedcard) == 1 and "Ambush" in selectedcard[0].keywords:
			sessionpass = "ambush"
			
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['WildlingHorde'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if "Wildling" in card.Traits and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and card.controller == me], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "kneelhouseok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['SelyseBaratheon'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Faction == "Baratheon."], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "addintselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['OursistheFury'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Faction == "Baratheon." and card.type == "Character" and card.orientation == 1], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "adddefselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['SeenInFlames'][1]:
			nextcardtmp = selectedcard[0]
			sessionpass = "dischandselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['IronFleetScout'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.Faction == "Greyjoy." and card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor)], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "adddstrselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['TheKrakensGrasp'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.controller != me and card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and int(card.cost) <= 5], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "ignorestrselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['TheThingsIDoForLove'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			cost=askInteger("How much do you want to pay to play {} ? ".format(selectedcard[0].name),0)
			if cost > 0:
				targetTuple = ([card._id for card in table if card.controller != me and card.type == "Character" and int(card.cost) <= cost], me._id)
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				sessionpass = "addstrdrawselectok"
				notify("**{} into selectmode**".format(me))
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				remoteCall(otherplayer, "action", ["challenge",1])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['FortheNorth'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and card.faction == "Stark."], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "addclaimselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['WinterIsComing'][1]:
			nextcardtmp = selectedcard[0]
			sessionpass = "drawstarkselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['GatesofWinterfell'][1]:
			nextcardtmp = selectedcard[0]
			sessionpass = "drawstarkselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['Dracarys'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if "Dragon." in card.traits or card.model == "a2f21413-0272-47dc-a197-e364aa942d4c" and card.controller == me and card.orientation == 0], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "burnselect"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['FireandBlood'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			list2 = []
			for carddead in me.piles['Dead Pile']:
				if carddead.Faction == "Targaryen." and carddead.Unique =="Yes" and carddead.Type == "Character":
					list.append(carddead)
			dlg = cardDlg(list)
			dlg.title = "These cards are in your Dead Pile:"
			dlg.text = "Declares at least 1 card to action."
			dlg.min = 1
			dlg.max = 1
			cards = dlg.show()
			cardtoaction = cards[0]
			sessionpass = "returndeadselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['MargaeryTyrell'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character"], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "addstr3selectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['Heartsbane'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			attach = eval(getGlobalVariable("attachmodify"))
			for cardatt in table:
				if cardatt._id == attach[nextcardtmp._id]:
					cardtoaction = cardatt
			sessionpass = "attaddstr3selectok"
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['Highgarden'][1]:
			nextcardtmp = selectedcard[0]
			for card in table:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and card.controller == attacker], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "standremovechallengeselectok"
			notify("**{} into selectmode**".format(me))
			return
		if len(selectedcard) == 1 and selectedcard[0].model == actionchallenge['GrowingStrong'][1]:
			nextcardtmp = selectedcard[0]
			for card in me.hand:
				card.target(False)
			targetTuple = ([card._id for card in table if card.type == "Character" and card.Faction == "Tyrell."], me._id)
			setGlobalVariable("tableTargets", str(targetTuple))
			setGlobalVariable("selectmode", "1")
			sessionpass = "3playeraddstr2selectok"
			notify("**{} into selectmode**".format(me))
			return
	if sessionpass == "burnselect":
		dwtmpcard = selectedcard[0]
		for card in me.hand:
			card.target(False)
		for card in table:
			card.target(False)
		targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and int(card.cost)], me._id)
		setGlobalVariable("tableTargets", str(targetTuple))
		setGlobalVariable("selectmode", "1")
		sessionpass = "burnselectok"
		notify("**{} into selectmode**".format(me))
		return
	if sessionpass == "actionok":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
	if sessionpass == "marshalcardselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to marshal.")
			return
		if len(selectedcard) == 0:
			marshalphase(table)
			return
	if sessionpass == "Confiscationselect":
		if len(selectedcard) > 1:
			whisper("You must select only one attachment.")
			return
	if sessionpass == "savecardselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to save.")
			return
	if sessionpass == "killability" or sessionpass == "attkilldefselect":
		if len(selectedcard) > 1:
			whisper("You must select only one Character.")
			return
	if sessionpass == "killabilitychooseone":
		if len(selectedcard) > 1:
			whisper("You must select only one Character.")
			return
	if sessionpass == "reaction" or sessionpass == "reactionaftc":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
	for cardn in table:
		if cardn.name == "nextbutton" and cardn.controller == me:
			cardn.delete()
			stealthcount = 0
	setGlobalVariable("selectmode", "0")
	if intertreaction == 0 and sessionpass != "attatchcardselect":
		for card in table:
			card.target(False)
	if sessionpass == "milselect":
		sessionpass = "milselectok"
		announceMil(table)
		return
	if sessionpass == "intselect":
		sessionpass = "intselectok"
		announceInt(table)
		return
	if sessionpass == "powselect":
		sessionpass = "powselectok"
		announcePow(table)
		return
	if sessionpass == "mildefselect":
		sessionpass = "mildefselectok"
		defMil(table)
		return
	if sessionpass == "intdefselect":
		sessionpass = "intdefselectok"
		defInt(table)
		return
	if sessionpass == "powdefselect":
		sessionpass = "powdefselectok"
		defPow(table)
		return
	if sessionpass == "miljudgementselect":
		sessionpass = "miljudgementselectok"
		interruptevent("miljudgementfp",smcount)
	if sessionpass == "milkillplayerselect":
		sessionpass = "milkillplayerselectok"
		Militarychallenge(b)
	if sessionpass == "savecardselect":
		sessionpass = "savecardselectok"
		interruptevent("miljudgementfp",smcount)
	if sessionpass == "killability":
		sessionpass = "killabilityok"
		interruptevent("characterkill",1)
	if sessionpass == "discattch" or sessionpass == "kneel":
		remoteCall(otherplayer,"interruptevent",["characterkill",1])
	if sessionpass == "reaction":
		sessionpass = "reactionok"
		reaction("leavetable",1)
	if sessionpass == "reactionaftc":
		sessionpass = "reactionaftcok"
		reaction("afterchallenge",1)
	if sessionpass == "bedefendselect":
		tmp = eval(getGlobalVariable("bedefend"))
		tmp.append(selectedcard[0]._id)
		setGlobalVariable("bedefend",str(tmp))
		selectedcard[0] = nextcardtmp
		nextcardtmp = []
		sessionpass = "reactionaftcok"
		debug(getGlobalVariable("bedefend"))
		reaction("afterchallenge",1)
	if sessionpass == "attkilldefselect" or sessionpass == "iceselect":
		if len(selectedcard) == 1:
			savetarget = selectedcard[0]
			debug(savetarget)
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		else:
			delreactioncard(nextcardtmp)
			#remoteCall(otherplayer,"disc",[selectedcard[0]])
		nextcardtmp = []
		sessionpass = "reactionaftuok"
		if cardtoaction != []:setTimer(me,"reactionaftuok",table)
		else:reaction("aftercalculate",1)
	if sessionpass == "discattchselect" or sessionpass == "popselect" or sessionpass == "stmselect" or sessionpass == "dothrakiselect" or sessionpass == "tyrellselect" or sessionpass == "submarkerselect":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			if sessionpass == "popselect":kneel(selectedcard[0])
			if sessionpass != "dothrakiselect" and sessionpass != "tyrellselect":
				selectedcard[0].arrow(cardtoaction)
		elif len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
			return
		nextcardtmp = []
		sessionpass = "reactionaftuok"
		reaction("aftercalculate",1)
	if sessionpass == "returndefenderselect":
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
		elif len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
			return
		elif len(selectedcard) > 1:
			whisper("You must select only one card.")
			return
		nextcardtmp = []
		sessionpass = "reactionaftuok"
		reaction("aftercalculate",1)
	if sessionpass in  ("killselect","Locationselect","lysselect") and nextcardtmp.type == "Event":
		if play(nextcardtmp):
			if dwtmpcard != []:
				kneel(dwtmpcard)
				dwtmpcard = []
			cardtoaction = selectedcard[0]
			savetarget = selectedcard[0]
			interruptcancelcard = nextcardtmp
			interruptcancelplayer = me
			saveactionplayer = me
			inserttarget = interruptcancelcard
			mainpass = "aftercalculate"
			remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
			remoteCall(me, "setTimer", [me,"interruptcancel",table])
		else:
			delreactioncard(nextcardtmp)
			selectedcard = []
			reaction("aftercalculate",1)
	if selectedcard != []:
		if sessionpass == "reactionaftu" and selectedcard[0].type == "Event":
			if play(selectedcard[0]):
				interruptcancelcard = selectedcard[0]
				interruptcancelplayer = me
				inserttarget = interruptcancelcard
				mainpass = "aftercalculate"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])
			else:
				delreactioncard(nextcardtmp)
				selectedcard = []
				reaction("aftercalculate",1)
		elif sessionpass == "reactionaftu" and selectedcard[0].type in ("Character","Location"):
			sessionpass = "reactionaftuok"
			reaction("aftercalculate",1)
		elif sessionpass == "reactionaftu" and selectedcard[0].type == "Plot":
			reactionforability(selectedcard[0],"aftercalculate")
	elif sessionpass == "reactionaftu":
		sessionpass = "reactionaftuok"
		remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if sessionpass == "Direwolfselect":
		if len(selectedcard) == 0:
			delreactioncard(nextcardtmp)
			selectedcard = []
			remoteCall(otherplayer, "reaction", ["aftercalculate",1])
	if sessionpass == "initimidateselect":
		if len(selectedcard) != 0:
			selectedcard[0].orientation = 1
			notify("{}'s {} kneel {} by Initimidate".format(me,cardtoaction,selectedcard[0]))
			cardtoaction = []
		keywordforability(1)
	if sessionpass in("kneelhouseok","addintselectok","adddefselectok","dischandselectok","adddstrselectok","ignorestrselectok","returnhandselectok","drawstarkselectok","burnselectok","returndeadselectok","addstrdrawselectok","addclaimselectok","addstr3selectok","attaddstr3selectok","standremovechallengeselectok","3playeraddstr2selectok","removechallengeok"):
		if len(selectedcard) > 1 and sessionpass != "3playeraddstr2selectok":
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) > 3 and sessionpass == "3playeraddstr2selectok":
			whisper("You must select at most 3 character to action.")
			return
		if len(selectedcard) == 1 and sessionpass != "3playeraddstr2selectok":
			if sessionpass != "returndeadselectok" and sessionpass != "attaddstr3selectok":cardtoaction = selectedcard[0]
			if sessionpass == "kneelhouseok" or sessionpass == "returnhandselectok":
				if sessionpass == "kneelhouseok":selectedcard[0] = nextcardtmp
				for cardhouse in table:
					if cardhouse.type == "Faction" and cardhouse.controller == me:
						kneel(cardhouse)
			if sessionpass == "addintselectok" or sessionpass == "standremovechallengeselectok":
				selectedcard[0] = nextcardtmp
				me.counters['Gold'].value -= 1
				for incomecard in table:
					if incomecard.controller == me and incomecard.markers[Gold] > 0:
						incomecard.markers[Gold] -= 1
			if sessionpass in ("adddefselectok","dischandselectok","ignorestrselectok","returnhandselectok","burnselectok","returndeadselectok","addstrdrawselectok","addclaimselectok","removechallengeok"):
				if sessionpass == "returndeadselectok":
					debug(cardtoaction)
					if cardtoaction == None:
						delactioncard(nextcardtmp)
						nextcardtmp = []
						sessionpass = ""
						remoteCall(otherplayer, "action", ["challenge",1])
						return
				if sessionpass == "removechallengeok":
					savetarget = selectedcard[0]
					debug(savetarget)
					interruptcancelcard = nextcardtmp
					interruptcancelplayer = me
					saveactionplayer = me
					inserttarget = interruptcancelcard
					mainpass = "challengeaction"
					remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
					remoteCall(me, "setTimer", [me,"interruptcancel",table])
					nextcardtmp = []
					return
				if play(nextcardtmp):
					if dwtmpcard != []:
						kneel(dwtmpcard)
						dwtmpcard = []
					if sessionpass != "returndeadselectok":cardtoaction = selectedcard[0]
					savetarget = selectedcard[0]
					debug(savetarget)
					interruptcancelcard = nextcardtmp
					interruptcancelplayer = me
					saveactionplayer = me
					inserttarget = interruptcancelcard
					mainpass = "challengeaction"
					remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
					remoteCall(me, "setTimer", [me,"interruptcancel",table])
					nextcardtmp = []
					return
				else:
					delactioncard(nextcardtmp)
					nextcardtmp = []
					sessionpass = ""
					remoteCall(otherplayer, "action", ["challenge",1])
					return
			if sessionpass == "adddstrselectok" or sessionpass == "addstr3selectok" or sessionpass == "attaddstr3selectok" or sessionpass == "standremovechallengeselectok":
				selectedcard[0] = nextcardtmp
				kneel(nextcardtmp)
			if sessionpass == "drawstarkselectok":
				cardtoaction = me.deck.top()
				kneel(nextcardtmp)
		elif sessionpass != "3playeraddstr2selectok":
			delactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "action", ["challenge",1])
			return
		if sessionpass == "3playeraddstr2selectok":
			if play(nextcardtmp):
				cardtoaction = selectedcard
				savetarget = selectedcard[0]
				debug(savetarget)
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "challengeaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				remoteCall(otherplayer, "action", ["challenge",1])
				return
		nextcardtmp = []
		sessionpass = "actionok"
		action("challenge",1)
	if sessionpass == "ambush":
		if play(selectedcard[0]):
			if selectedcard[0].model == actionchallenge['OlennasInformant'][1]:
				cardtoaction = selectedcard
				savetarget = selectedcard[0]
				debug(savetarget)
				interruptcancelcard = selectedcard[0]
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "challengeaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(otherplayer, "interruptevent", ["interruptcancel",2])			
			if selectedcard[0].model == actionchallenge['AreoHotah'][1]:
				if checkinchallengeplay("all",0):
					nextcardtmp = selectedcard[0]
					for card in me.hand:
						card.target(False)
					targetTuple = ([card._id for card in table if card.type == "Character" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor)], me._id)
					setGlobalVariable("tableTargets", str(targetTuple))
					setGlobalVariable("selectmode", "1")
					if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
					else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
					sessionpass = "removechallengeok"
					notify("**{} into selectmode**".format(me))
					return
				else:
					for card in me.hand:
						card.target(False)
					delactioncard(selectedcard[0])
					nextcardtmp = []
					sessionpass = ""
					remoteCall(otherplayer, "action", ["challenge",1])
					return

		else:
			for card in me.hand:
				card.target(False)
			delactioncard(selectedcard[0])
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "action", ["challenge",1])
			return
	if sessionpass == "attatchcardselect":
		if play(listattach[0]):
			del listattach[0]
			if len(listattach) > 0:attatchcard(listattach)
			else:
				reordertable(table)
	if sessionpass == "marshalcardselect":
		if play(selectedcard[0]):marshalphase(table)
		else:marshalphase(table)
	if sessionpass in ("Confiscationselect","FilthyAccusationsselect"):
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			selectedcard[0].arrow(cardtoaction)
			remoteCall(me, "setTimer", [me,sessionpass,table])
		elif len(selectedcard) == 0:
			nextcardtmp = []
			sessionpass = ""
			return


def stealthcard(group, x=0, y=0):
	mute()
	global sessionpass
	global selectedcard
	if sessionpass == "stealthselectok" and selectedcard != []:
		for card in selectedcard:
			card.highlight = Stealthcolor
			if getGlobalVariable("cantchallenge") == "1":setGlobalVariable("cantchallenge", card._id)
			debug(getGlobalVariable("cantchallenge"))
		sessionpass = ""
		selectedcard = []
	setGlobalVariable("selectmode", "0")
	checkafterchallengereacioncard(1)

def ondbclick(args):
	mute()
	if getGlobalVariable("selectmode") == "1" or me.getGlobalVariable("setupOk") == "4":
		list2 = []
		if me.getGlobalVariable("setupOk") == "4":tuplecard = eval(me.getGlobalVariable("tableTargets"))
		else:tuplecard = eval(getGlobalVariable("tableTargets"))
		debug(tuplecard)
		if me._id == tuplecard[1]:
			if args.card.name == "nextbutton":next(table)
			else:
				if args.card._id in tuplecard[0]:
					if args.card.targetedBy == me:
						args.card.target(False)
					else:
						args.card.target(True)
				else:
					whisper("card cant be selected")
		else:
			whisper("is not your turn")

def test(group, x=0, y=0):
	mute()
	reavelplot(table)

def checksavecard(savecard):
	list = []
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		for cards in savecard:
			Faction = cards.Faction
			savetarget = cards
			if card.controller == me and cards.controller == me and card.name == cards.name and card.filter == WaitColor:
				list.append(card)
	for c in me.hand:
		for d in saveaction:
			if saveaction[d][3] == "Hand" and c.model == saveaction[d][1]:
				if saveaction[d][4] == "all":list.append(c)
				elif saveaction[d][4] == Faction:list.append(c)
	for c in table:
		for d in saveaction:
			if saveaction[d][3] == "table" and c.model == saveaction[d][1] and c.controller == me:
				if saveaction[d][5] == "Attachment":
					if attach.has_key(c._id):
						if attach[c._id] == savetarget._id:list.append(c)
				else:
					if saveaction[d][2] != "kneel":
						if saveaction[d][4] == "all":list.append(c)
						elif saveaction[d][4] == Faction:list.append(c)
					elif saveaction[d][2] == "kneel" and c.orientation == 0:
						if saveaction[d][4] == "all":list.append(c)
						elif saveaction[d][4] == Faction:list.append(c)
	return list

def reactionattachsub(card):
	mute()
	global reactionattach
	reactionattach[card._id] -= 1
	if reactionattach[card._id] == 0:del reactionattach[card._id]

def actionattachsub(card):
	mute()
	global actionattach
	actionattach[card._id] -= 1
	if actionattach[card._id] == 0:del actionattach[card._id]

def abilityattachsub(card):
	mute()
	global abilityattach
	abilityattach[card._id] -= 1
	if abilityattach[card._id] == 0:del abilityattach[card._id]

def interruptreaction(card,count):
	mute()
	global intertreaction
	intertreaction = count
	reactionattach[card._id] = 1
	reaction("leavetable",1)

def backupinterruptlib(count):
	mute()
	global interruptlibtmp
	global interruptlib
	global interruptpass
	global interruptpasstmp
	interruptlibtmp = interruptlib
	interruptlib = {}
	interruptpasstmp = interruptpass
	interruptpass = 0
	savetargetinserttargettmp(savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass)


def restoreinterruptlib(count):
	mute()
	global interruptlibtmp
	global interruptlib
	global interruptpass
	global interruptpasstmp
	global interruptcancellastcard
	global interruptcanceledcard
	global interruptcancelcard
	global isinsertreaction
	interruptlib = interruptlibtmp
	interruptlibtmp = {}
	interruptpass = interruptpasstmp
	interruptpasstmp = 0
	isinsertreaction = 0
	if count == 1:
		remoteCall(otherplayer,"restoreinterruptlib",[2])
	else:
		savetargetinserttarget(savetargettmp,inserttargettmp,interruptcancelcardtmp,interruptcancelplayertmp,interruptcancellastcardtmp,interruptcanceledcardtmp,interruptcanceloktmp,saveactionplayertmp,mainpasstmp)
		remoteCall(otherplayer,"savetargetinserttarget",[savetargettmp,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		debug("interruptlib")
		debug(interruptlib)
		debug(getGlobalVariable("insertre"))
		debug(interruptpass)
		if getGlobalVariable("insertre") == "1":
			if interruptlib["pass"+str(interruptpass)][0].controller == me:disc(interruptlib["pass"+str(interruptpass)][0])
			else:remoteCall(otherplayer, "disc", [interruptlib["pass"+str(interruptpass)][0]])
			del interruptlib["pass"+str(interruptpass)]
			remoteCall(otherplayer,"interruptlibdel",[interruptpass])
			interruptpass -= 1
		if getGlobalVariable("insertre") == "1" or getGlobalVariable("insertre") == "2":
			setGlobalVariable("insertre", "")
			if interruptpass == 0:
				notify("over,disc card")
				debug(inserttarget)
				debug(interruptcancelok)
				if mainpass == "leave":
					if interruptcancelok == 1:
						leavecardtype.append(inserttarget._id)
						remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
					else:
						remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
						if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
						else:interruptevent("characterkill",1)
				elif mainpass == "leavereaction":
					if interruptcancelok == 1:
						remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
					else:
						remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
						if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
						else:reaction("leavetable",1)
				elif mainpass == "afterchallenge":
					if interruptcancelok == 1:
						remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
					else:
						remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
						if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
						else:reaction("afterchallenge",1)
				else:
					if interruptcancelok == 1:
						savetarget.highlight = milsavecolor
						savepassfinish(1)
					else:
						if inserttarget.controller == me:disc(inserttarget)
						else:remoteCall(otherplayer, "disc", [inserttarget])
					notify("ballanceover")
					if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
					else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
			else:
				interruptcancellastcard = interruptlib["pass"+str(interruptpass)][1]
				interruptcanceledcard = interruptlib["pass"+str(interruptpass)][0]
				interruptcancelcard = interruptcanceledcard
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				if interruptlib["pass"+str(interruptpass)][2] == me:remoteCall(otherplayer, "interruptevent", ["interruptcancel",1])
				else:
					debug(interruptlib)
					debug(interruptcancelcard)
					remoteCall(me, "interruptevent", ["interruptcancel",1])
					return
		if getGlobalVariable("insertre") == "3":
			setGlobalVariable("insertre", "")
			notify("over,disc card")
			debug(interruptcancelok)
			debug(inserttarget)
			if mainpass == "leave":
				if interruptcancelok == 1:
					leavecardtype.append(inserttarget._id)
					remoteCall(inserttarget.controller,"leaveforability",[inserttarget])
				else:
					remoteCall(inserttarget.controller,"abilityattachsub",[inserttarget])
					if inserttarget.controller == me:remoteCall(otherplayer, "interruptevent", ["characterkill",1])
					else:interruptevent("characterkill",1)
			elif mainpass == "leavereaction":
				if interruptcancelok == 1:
					remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
				else:
					remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
					if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["leavetable",1])
					else:reaction("leavetable",1)
			elif mainpass == "afterchallenge":
				if interruptcancelok == 1:
					remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
				else:
					remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
					if inserttarget.controller == me:remoteCall(otherplayer, "reaction", ["afterchallenge",1])
					else:reaction("afterchallenge",1)
			else:		
				if interruptcancelok == 1:
					savetarget.highlight = milsavecolor
					savepassfinish(1)
				else:
					if inserttarget.type != "Character":
						if inserttarget.controller == me:disc(inserttarget)
						else:remoteCall(otherplayer, "disc", [inserttarget])
				notify("ballanceover")
				if saveactionplayer == me:remoteCall(otherplayer, "interruptevent", ["miljudgementfp",1])
				else :remoteCall(me, "interruptevent", ["miljudgementfp",1])
				
def savetargetinserttargettmp(savetargetn,inserttargetn,interruptcancelcardn,interruptcancelplayern,interruptcancellastcardn,interruptcanceledcardn,interruptcancelokn,saveactionplayern,mainpassn):
	mute()
	global savetargettmp
	global inserttargettmp
	global interruptcancelcardtmp
	global interruptcancelplayertmp
	global interruptcanceledcardtmp
	global interruptcancellastcardtmp
	global interruptlibtmp
	global interruptcanceloktmp
	global saveactionplayertmp
	global mainpasstmp

	interruptcanceloktmp = interruptcancelokn
	savetargettmp = savetargetn
	inserttargettmp = inserttargetn
	interruptcancelcardtmp = interruptcancelcardn
	interruptcancelplayertmp = interruptcancelplayern
	interruptcancellastcardtmp = interruptcancellastcardn
	interruptcanceledcardtmp = interruptcanceledcardn
	saveactionplayertmp =  saveactionplayern
	mainpasstmp = mainpassn

def orientationintable(cards):
	mute()
	c = 0
	for card in table:
		if card.Type == "Character" and card.controller == cards.controller and card.orientation == 0:
			c = 1
	if c == 1:return True

def checkinsertreaction(cards):
	mute()
	global insertreactioncard
	c = 0
	for card in table:
		for d in leavereacion:
			if card.model == leavereacion[d][1] and card.controller == cards.controller:
				if leavereacion[d][2] == "Faction":
					if cards.Faction.find(leavereacion[d][3]) != -1:
						c = 1
						insertreactioncard = card
	if c == 1:return True


def checktablecount(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me:
			list.append(card)

	if len(list) > count:
		return len(list)
	else:return 0

def checktablestealthcount(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me and card.keywords.find("Stealth") == -1:
			list.append(card)
	if len(list) > count:
		return len(list)
	else:return 0

def fplay(n):
	for card in table:
		if card.name == "1st Player Token":return card.controller

def checkotherattachment(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Attachment" and card.controller != me:
			list.append(card)
	return len(list)

def checkotherloaction(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Location" and card.controller != me:
			list.append(card)
	return len(list)

def checkothercharacter(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me:
			list.append(card)
	return len(list)

def checktearsofLys(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Character" and card.controller != me and card.Intrigue != "Yes" and  card.markers[IntrigueIcon] == 0:
			list.append(card)
	return len(list)


def checkaftercalculatereacioncard(count):
	mute()
	global reactionattach
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me and aftercalculate[d][6] == "table":
				if aftercalculate[d][2] == "all":
					if winplayer != me:
						if aftercalculate[d][4] == "returndefender" and card.orientation == 0 and aftercalculate[d][3] == "defender" and defender == me:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "addclaim" and card.orientation == 0 and aftercalculate[d][3] == "defender" and defender == me:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "submarker" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer == me:
						if aftercalculate[d][4] == "draw2card" and card.orientation == 0 and aftercalculate[d][3] == "all":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "standstm" and aftercalculate[d][3] == "all" and checkstm(1):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
				if aftercalculate[d][2] == "all" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
				 	if aftercalculate[d][3] == "attacker" and attacker == me and winplayer == me:
				 		if aftercalculate[d][4] == "disotherattachment" and checkotherattachment(1) > 0:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "5pwinpow" and attacker.counters['Str'].value - defender.counters['Str'].value >= aftercalculate[d][7]:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][7] == "uo" and unopposed == 1:
							if aftercalculate[d][4] == "stand" and card.orientation == 1:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
							if aftercalculate[d][4] == "addpowself":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if aftercalculate[d][3] == "attacker" and attacker == me and winplayer == me:
						if aftercalculate[d][7] == "uo" and unopposed == 1:
							if aftercalculate[d][4] == "drawcardorpower":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "attkilldef":
							if attach.has_key(card._id):
								c = 0
								for attachcard in table:
									if attach[card._id] == attachcard._id and checkinchallengeplay(otherplayer,0) and attachcard.controller == me and attachcard.highlight in(MilitaryColor,IntrigueColor,PowerColor):
										c = 1
								if  c == 1:
									if not reactionattach.has_key(card._id):
										reactionattach[card._id] = 1
									else:reactionattach[card._id] += 1
				if aftercalculate[d][2] != "all":
					if aftercalculate[d][2] == str(challengetype) and winplayer == me:
						if aftercalculate[d][4] == "drawcard":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "subability2" and card.orientation == 0 and checkattachcard(1):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "discard" and aftercalculate[d][3] == "defender" and defender == me:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "addplayer" and checkdothrakhand(1):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if card.highlight == IntrigueColor and aftercalculate[d][4] == "addplayer6" and checktyrellcharacter(6):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						if aftercalculate[d][4] == "kill" and checkice(card._id):
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
						debug(checkhousepow(otherplayer))
						if card.type == "Plot" and card.highlight == None and aftercalculate[d][4] == "movepow" and checkhousepow(otherplayer) > 0:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	for card in me.hand:
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and aftercalculate[d][6] == "Hand":
				if aftercalculate[d][2] != "all":
					if str(challengetype) in aftercalculate[d][2] and winplayer == me:
						if aftercalculate[d][4] == "addhand":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
				 	if aftercalculate[d][2] == str(challengetype) and attacker == me and winplayer == me:
				 		if aftercalculate[d][7] != "" and attacker.counters['Str'].value - defender.counters['Str'].value >= aftercalculate[d][7]:
					 		if aftercalculate[d][4] == "disotherloaction" and checkotherloaction(1) > 0:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
							if aftercalculate[d][4] == "kill" and checkothercharacter(1) > 0:
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
						if checktearsofLys(1) > 0 and aftercalculate[d][4] == "addmarker":
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
					if aftercalculate[d][2] == str(challengetype) and winplayer == me:
				 		if aftercalculate[d][7] != "" and attacker.counters['Str'].value - defender.counters['Str'].value >= aftercalculate[d][7]:
							if re.search('\d\spow', aftercalculate[d][4]):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
							if aftercalculate[d][4] == "addusedplotpow":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer != me:
						if aftercalculate[d][2] == str(challengetype):
							if aftercalculate[d][4] == "losekill" and checkinchallengeplay(otherplayer,0) and checkmytableTraits("Direwolf."):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1

				if aftercalculate[d][2] == "all":
					if winplayer == me:
						if aftercalculate[d][7] != "" and me.counters['Str'].value - otherplayer.counters['Str'].value >= aftercalculate[d][7]:
							if aftercalculate[d][4] == "cantchallenge" and aftercalculate[d][3] == "defender" and defender == me and checknwattacker(1):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer != me:
						if aftercalculate[d][3] == "defender" and defender == me:
							if aftercalculate[d][4] == "cant1challenge":
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
				
	debug("reactionattach4")
	debug(reactionattach)
	if len(reactionattach) > 0:setGlobalVariable("aftcu", "1")
	if count == 1:remoteCall(otherplayer, "checkaftercalculatereacioncard", [2])
	else:
		if getGlobalVariable("aftcu") == "1":
			setGlobalVariable("aftcu", "")
			if fplay(1) == me:reaction("aftercalculate",1)
			else: 
				remoteCall(otherplayer, "reaction", ["aftercalculate",1])
		else:
			if fplay(1) == me:balancechallengefinish(challengetype,winplayer)
			else:remoteCall(otherplayer, "balancechallengefinish", [challengetype,winplayer])
			return

def checkaftercalculatereacioncardforce(count):
	mute()
	global reactionattach
	for card in table:
		for d in aftercalculate:
			if card.model == aftercalculate[d][1] and card.controller == me and aftercalculate[d][6] == "table" and "Forced Reaction" in card.Text:
				if aftercalculate[d][2] == "all":
					if winplayer == me:
						if aftercalculate[d][4] == "addred" and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
								if not reactionattach.has_key(card._id):
									reactionattach[card._id] = 1
								else:reactionattach[card._id] += 1
					if winplayer != me:
						if aftercalculate[d][4] == "kneel" and aftercalculate[d][7] == "uo" and unopposed == 1 and card.orientation == 0:
							if not reactionattach.has_key(card._id):
								reactionattach[card._id] = 1
							else:reactionattach[card._id] += 1
	debug("reactionattach3")
	debug(reactionattach)
	if len(reactionattach) > 0:setGlobalVariable("aftcu", "1")
	if count == 1:remoteCall(otherplayer, "checkaftercalculatereacioncardforce", [2])
	else:
		if getGlobalVariable("aftcu") == "1":
			setGlobalVariable("aftcu", "")
			if fplay(1) == me:reaction("aftercalculatef",1)
			else: 
				remoteCall(otherplayer, "reaction", ["aftercalculatef",1])
		else:
			if fplay(1) == me:checkaftercalculatereacioncard(1)
			else:remoteCall(otherplayer, "checkaftercalculatereacioncard", [1])
			return

def delreactioncard(card):
	mute()
	global reactioncardlimit
	global reactionattach
	c = 0
	if not reactioncardlimit.has_key(card._id):
		reactioncardlimit[card._id] = 1
	else:reactioncardlimit[card._id] += 1
	for d in afterchallengereacion:
		if card.model == aftercalculate[d][1]:
			if reactioncardlimit[card._id] == afterchallengereacion[d][5]:
				del reactionattach[card._id]
				c = 1
	for d in aftercalculate:
		if card.model == aftercalculate[d][1]:
			if reactioncardlimit[card._id] == aftercalculate[d][5]:
				del reactionattach[card._id]
				c = 1
	for d in leavereacion:
		if card.model == leavereacion[d][1]:
			if reactioncardlimit[card._id] == leavereacion[d][5]:
				del reactionattach[card._id]
				c = 1
	if c == 0:
		reactionattach[card._id] -= 1
		if reactionattach[card._id] == 0:del reactionattach[card._id]
	notify("reaction cancel.")

def checkinchallengeplay(person,cost):
	mute()
	c = 0
	for card in table:
		if person != "all":
			if card.controller == person:
				if challengetype == 1 and card.highlight == MilitaryColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
				if challengetype == 2 and card.highlight == IntrigueColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
				if challengetype == 2 and card.highlight == PowerColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
		else:
			if challengetype == 1 and card.highlight == MilitaryColor:
					if cost != 0:
						if int(card.cost) <= cost:
							c = 1
					else:c = 1
			if challengetype == 2 and card.highlight == IntrigueColor:
				if cost != 0:
					if int(card.cost) <= cost:
						c = 1
				else:c = 1
			if challengetype == 2 and card.highlight == PowerColor:
				if cost != 0:
					if int(card.cost) <= cost:
						c = 1
				else:c = 1
	if c == 1:return True

def checkmytableTraits(cardTraits):
	mute()
	for card in table:
		if card.controller == me and card.Traits == cardTraits and card.orientation == 0:
			return True
			break
def returncard(card):
	mute()
	card.moveTo(me.hand)

def checkattachcard(card):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if card.controller != me:
			c = 0
			for d in attach:
				if card._id == d:
					c = 1
			if c == 0:
				return True
				break

def checkattachment(count):
	mute()
	list = []
	for card in table:
		if card.Type == "Attachment":
			list.append(card)
	return len(list)

def checkstm(card):
	mute()
	for card in table:
		if card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and "Stormborn." in card.Traits and card.orientation == 1 and card.Type == "Character":
			return True
			break

def checkdothrakhand(card):
	mute()
	for card in me.hand:
		if "Dothraki." in card.Traits:
			return True
			break

def checknwattacker(card):
	mute()
	for card in table:
		if card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor) and "Night's Watch." in card.Faction and card.Type == "Character":
			return True
			break
def checktyrellcharacter(cardcost):
	mute()
	for card in me.hand:
		if "Tyrell." in card.Faction and int(card.cost) <= cardcost and card.Type == "Character":
			return True
			break

def clearreaction(count):
	mute()
	global reactionattach
	global sessionpass
	reactionattach = {}
	sessionpass = ""
	if count == 1:remoteCall(otherplayer, "clearreaction", [2])
	if count == 2:
		challengeaction(1)
	if count == 3:remoteCall(otherplayer, "clearreaction", [4])
	if count == 4:
		if fplay(1) == me:checkaftercalculatereacioncard(1)
		else:remoteCall(otherplayer, "checkaftercalculatereacioncard", [1])
	if count == 5:remoteCall(otherplayer, "clearreaction", [6])
	if count == 6:
		if fplay(1) == me:balancechallengefinish(challengetype,winplayer)
		else:remoteCall(otherplayer, "balancechallengefinish", [challengetype,winplayer])

def clearaction(count):
	mute()
	global actionattach
	global sessionpass
	actionattach = {}
	sessionpass = ""
	if count == 1:remoteCall(otherplayer, "clearaction", [2])
	if count == 2:
		if attacker == []:
			if getGlobalVariable("activeplayer") == str(me._id):challengeAnnounce(table)
			else:remoteCall(players[1], "challengeAnnounce", table)
		else:
			if defender == []:
				if attacker == me:remoteCall(otherplayer, "announceOpp", [table])
				else:announceOpp(table)
			else:
				challenge(table)

def choosetype(card):
	mute()
	choiceList = ['Character', 'Location', 'Attachment', 'Event']
	colorList = ['#ae0603' ,'#006b34','#1a4d8f','#a0522d']
	choice = askChoice("Which type do you want to select?", choiceList,colorList)
	if choice == 0:
		choosetype(card)
		return
	else:remoteCall(otherplayer, "reactionforability", [card,str(choice)])

def checkice(cardid):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if attach[cardid] == card._id and card.controller == me and card.highlight == MilitaryColor:
			return True
			break

def checkheartsbane(cardid):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if attach[cardid] == card._id and card.controller == me and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
			return True
			break

def checkstandplayer(group, x = 0, y = 0):
	mute()
	for card in table:
		if card.type == "Character" and card.orientation == 0:
			return True

def checkhousepow(player):
	mute()
	for card in table:
		if card.type == "Faction" and card.controller == player:
			return card.markers[Power]


def keyword(count):
	mute()
	global keywordattach
	for card in table:
		for d in keywordslib:
			if card.model == keywordslib[d][1] and card.controller == me and card.highlight in(MilitaryColor,IntrigueColor,PowerColor):
				if winplayer == me:
					keywordattach.append(card)
	debug(keywordattach)
	keywordforability(1)


def keywordforability(count):
	mute()
	global keywordattach
	global sessionpass
	global cardtoaction
	c = 0
	
	if len(keywordattach) > 0:
		for card in keywordattach:
			for d in keywordslib:
				if card.model == keywordslib[d][1] and card.controller == me:
					if count == 1:
						if "Renown" in keywordslib[d][2]:
							card.markers[Power] += 1
							notify("{}'s {} add 1 pow by Renown".format(me,card))
						if "Insight" in keywordslib[d][2] and len(me.deck) > 0:
							draw(me.deck)
							notify("{}'s {} draw 1 card by Insight".format(me,card))
						if "Pillage" in keywordslib[d][2] and len(otherplayer.deck) > 0:
							remoteCall(otherplayer, "disctop", [1])
							notify("{}'s {} discards 1 cards from the top of {} Deck by Pillage".format(me,card,otherplayer))
							setTimer(me,"keywords",table)
							return
					for f in keywordsreaction:
						if card.model == keywordsreaction[f][1] and len(otherplayer.piles['Discard Pile']) > 0:
							for cards in otherplayer.piles['Discard Pile']:
								if cards.type == "Location":
									cardtoaction = card
									reaction("keywords",1)
									return
					count = 1
					debug(card)
					debug(keywordslib[d][2])
					if "Initimidate" in keywordslib[d][2] and checkothercharacter(1) > 0:

						cardtoaction = card
						keywordattach.remove(card)
						sessionpass = ""
						targetTuple = ([cards._id for cards in table if cards.controller != me and cards.type == "Character" and int(cards.Cost) <= me.counters['Str'].value - otherplayer.counters['Str'].value and cards.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "1")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
						notify("**{} into selectmode**".format(me))
						sessionpass = "initimidateselect"				
						return
					keywordattach.remove(card)
		keywordforability(1)
	else:
		setGlobalVariable("mainstep", "78")
		notify("kw over")
		challengebalanceover(1)

def movecard(card):
	card.moveToTable(-200,200)

def disctop(player):
	mute()
	card = me.deck.top()
	card.moveTo(me.piles['Discard pile'])

def checktraits(traits,condition,player):
	mute()
	for card in table:
		if card.controller == player and traits in card.Traits:
			if condition == "challenge":
				if card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
					return True
			else:return True

def checkfaction(faction):
	mute()
	for card in table:
		if card.Faction == faction:
			return True

def checkchallengefaction(faction):
	mute()
	for card in table:
		if card.Faction == faction and card.highlight in (MilitaryColor,IntrigueColor,PowerColor):
			return True

def checkkneelfaction(faction):
	mute()
	for card in table:
		if card.Faction == faction and card.orientation == 1 and card.controller == me:
			return True

def checkmefaction(faction):
	mute()
	for card in table:
		if card.Faction == faction and card.controller == me and card.type == "Character":
			return True

def checkburn(player):
	mute()
	for card in table:
		if "Dragon." in card.traits or card.model == "a2f21413-0272-47dc-a197-e364aa942d4c":
			if card.controller == player and card.orientation == 0:
				return True

def checkdeadtargaryen(ok):
	mute()
	for card in me.piles['Dead Pile']:
		if card.Faction == "Targaryen." and card.Unique =="Yes" and card.Type == "Character":
			return True

def checkpr(player):
	mute()
	for card in table:
		if card.model == "12bc6cd7-39f0-44b7-9492-101d8083c468" and card.controller == player:
			return True

def challengeaction(count):
	mute()
	global actionattach
	for card in table:
		for d in actionchallenge:
			if card.model == actionchallenge[d][1] and card.controller == me and actionchallenge[d][3] == "table":
				if actionchallenge[d][2] == "kneelhouse+2str" and checktraits("Wildling","challenge",me):
					for housecard in table:
						if housecard.type == "Faction" and housecard.controller == me and housecard.orientation == 0:
							if not actionattach.has_key(card._id):
								actionattach[card._id] = 1
							else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "addinticon" and checkfaction("Baratheon."):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "addstr" and checkchallengefaction("Greyjoy.") and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "drawstark" and card.orientation == 0 and len(me.hand) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "addstr3" and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "attaddstr3" and checkheartsbane(card._id) and card.orientation == 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if actionchallenge[d][2] == "standremovechallenge" and checkinchallengeplay(attacker,0) and card.orientation == 0 and me.counters['Gold'].value > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
	for card in me.hand:
		for d in actionchallenge:
			if card.model == actionchallenge[d][1] and actionchallenge[d][3] == "Hand":
				if actionchallenge[d][5] == "":
					if actionchallenge[d][2] == "dischand" and checktraits("R'hllor.","",me) and len(otherplayer.hand) > 0:
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "addstrdraw" and checkchallengefaction("Stark."):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "addclaim":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "burn" and checkburn(me) and checkinchallengeplay("all",0) :
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "returndead" and checkdeadtargaryen(1):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "3playeraddstr2" and checkfaction("Tyrell."):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "fplay" and fplay(1) == me:
					if actionchallenge[d][2] == "ignorestr":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "defender" and defender == me:
					if actionchallenge[d][2] == "adddef" and  checkkneelfaction("Baratheon."):
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "Lord./Lady." and checktraits("Lord.","",me) or checktraits("Lady.","",me):
					if actionchallenge[d][2] == "kneelhousereturnhand" and checkothercharacter(1) > 0:
						for housecard in table:
							if housecard.type == "Faction" and housecard.controller == me and housecard.orientation == 0:
								if not actionattach.has_key(card._id):
									actionattach[card._id] = 1
								else:actionattach[card._id] += 1
				if actionchallenge[d][5] == "ambush":
					if actionchallenge[d][2] == "choosechallenge":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1
					if actionchallenge[d][2] == "removechallenge":
						if not actionattach.has_key(card._id):
							actionattach[card._id] = 1
						else:actionattach[card._id] += 1


	debug(actionattach)
	if len(actionattach) > 0:setGlobalVariable("action", "1")
	if count == 1:remoteCall(otherplayer, "challengeaction", [2])
	if count == 2:
		if getGlobalVariable("action") == "1":
			setGlobalVariable("action", "0")
			if fplay(1) == me:action("challenge",1)
			else:remoteCall(otherplayer, "action", ["challenge",1])
		else:
			if attacker == []:
				if getGlobalVariable("activeplayer") == str(me._id):challengeAnnounce(table)
				else:remoteCall(players[1], "challengeAnnounce", table)
			else:
				if defender == []:
					if attacker == me:remoteCall(otherplayer, "announceOpp", [table])
					else:announceOpp(table)
				else:
					challenge(table)

def action(actioninsert,actioncount):
	mute()
	global sessionpass
	global intertreaction
	if actioninsert == "challenge":
		#if getGlobalVariable("mainstep") == "7":setGlobalVariable("mainstep", "77")
		if len(actionattach) > 0:
			if sessionpass == "":
				choiceList = ['action', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoaction(actionattach,actioncount,"challenge")
					return
				if choice == 2:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						remoteCall(otherplayer, "action", ["challenge",actioncount])
					return
			if sessionpass == "actionok":
				actioncards = selectedcard
				if actioncards == []:
					if actioncount == 2:
						notify("action over")
						clearaction(1)
					else:
						actioncount += 1
						sessionpass = ""
						remoteCall(otherplayer, "action", ["challenge",actioncount])
					return
				else:
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkaction", [actioncard,"challengeaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(otherplayer, "action", ["challenge",actioncount])
			return

def checkaction(actioncard,repass):
	mute()
	global interruptcancelcard
	global interruptcancelplayer
	global inserttarget
	global interruptcancelok
	global interruptcanceledcard
	global mainpass
	global leavecardtype
	global sessionpass

	sessionpass = ""
	
	if checkcountercharater(actioncard):
		interruptcancelcard = reactioncard
		interruptcancelplayer = otherplayer
		inserttarget = interruptcancelcard
		mainpass = repass
		interruptcancelok = 1
		remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		remoteCall(me, "interruptevent", ["interruptcancel",2])
	else:
		remoteCall(otherplayer,"actionforability",[actioncard,repass])

def intoaction(cards,count,sepass):
	mute()
	global sessionpass
	global recount
	sessionpass = ""
	targetTuple = ([d for d in actionattach], me._id)
	#targetTuple = ([card._id for card in table if card.controller == me and cards.has_key(card._id)], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",130,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-300,200)
	notify("**{} into selectmode**".format(me))
	sessionpass = sepass
	recount = count

def delactioncard(card):
	mute()
	global actioncardlimit
	global actionattach
	c = 0
	if not actioncardlimit.has_key(card._id):
		actioncardlimit[card._id] = 1
	else:actioncardlimit[card._id] += 1
	
	for d in actionchallenge:
		if card.model == actionchallenge[d][1]:
			if actioncardlimit[card._id] == actionchallenge[d][5]:
				del actionattach[card._id]
				c = 1
	if c == 0:
		actionattach[card._id] -= 1
		if actionattach[card._id] == 0:del actionattach[card._id]
	notify("action cancel.")



def actionforability(card,repass):
	mute()
	debug(card)
	global actionattach
	global actioncardlimit
	global sessionpass
	global intertreaction
	global cardtoaction
	global savetarget
	sessionpass = ""
	c = 0
	f = 0
	debug(mainpass)
	if repass == "challengeaction":
		for d in actionchallenge:
			if card.model == actionchallenge[d][1] and card.controller == me:
				if actionchallenge[d][2] == "kneelhouse+2str":
					cardtoaction.markers[STR_Up] += 2
					notify("{}'s {} action {} gets +2 STR".format(me,card,cardtoaction))#WildlingHorde
				if actionchallenge[d][2] == "addinticon":
					cardtoaction.markers[IntrigueIcon] += 1
					notify("{}'s {} action {} gets Intrigue Icon".format(me,card,cardtoaction))#SelyseBaratheon
				if actionchallenge[d][2] == "adddef":
					if challengetype == 1:cardtoaction.highlight = MilitaryColor
					if challengetype == 2:cardtoaction.highlight = IntrigueColor
					if challengetype == 3:cardtoaction.highlight = PowerColor
					aftercalculatestand = eval(getGlobalVariable("aftercalculatestand"))
					aftercalculatestand.append(cardtoaction._id)
					setGlobalVariable("aftercalculatestand", str(aftercalculatestand))
					notify("{}'s {} action {} participating as a defender".format(me,card,cardtoaction))#OursistheFury
				if actionchallenge[d][2] == "dischand":
					remoteCall(otherplayer, "handview", ['all'])
					list = []
					for cardhand in otherplayer.hand:
						list.append(cardhand)
					dlg = cardDlg(list)
					dlg.title = "These cards are in your table:"
					dlg.text = "Declares at least 1 card to disc."
					dlg.min = 1
					dlg.max = 1
					cards = dlg.show()
					if cards != None:
						remoteCall(otherplayer, "disc", [cards[0]])
						notify("{}'s {} action discard {} from {} hand".format(me,card,cards[0],otherplayer))#SeenInFlames
					remoteCall(otherplayer, "handview", ['me'])
				if actionchallenge[d][2] == "addstr":
					strup = 1
					if fplay(1) == me:strup = 2
					cardtoaction.markers[STR_Up] += strup
					notify("{}'s {} action {} gets +{} STR".format(me,card,cardtoaction,strup))#IronFleetScout
				if actionchallenge[d][2] == "ignorestr":
					ignorestr = eval(getGlobalVariable("ignorestr"))
					ignorestr.append(cardtoaction._id)
					setGlobalVariable("ignorestr", str(ignorestr))
					notify("{}'s {} action {} does not contribute its STR to the challenge".format(me,card,cardtoaction))#TheKrakensGrasp
				if actionchallenge[d][2] == "kneelhousereturnhand":
					remoteCall(otherplayer,"returncard",[cardtoaction])
					notify("{}'s {} action return {} into {}'s hand.".format(me,card,cardtoaction,otherplayer))#TheThingsIDoForLove
				if actionchallenge[d][2] == "drawstark":
					if me.isInverted: cardtoaction.moveToTable(150,-230)
					else: cardtoaction.moveToTable(-130,130)
					notify("{} reveal {}.".format(me,cardtoaction))
					if cardtoaction.Faction == "Stark.":
						cardtoaction.moveTo(me.hand)
						notify("{}'s {} action put {} into {}'s hand.".format(me,card,cardtoaction,me))#GatesofWinterfell
					else:
						cardtoaction.moveTo(me.deck)
						cardtoaction.index = 0
				if actionchallenge[d][2] == "addstrdraw":
					cardtoaction.markers[STR_Up] += 2
					aftercalculatedraw = eval(getGlobalVariable("aftercalculatedraw"))
					aftercalculatedraw.append(cardtoaction._id)
					setGlobalVariable("aftercalculatedraw", str(aftercalculatedraw))
					debug(getGlobalVariable("aftercalculatedraw"))
					notify("{}'s {} action {} gets +2 STR.".format(me,card,cardtoaction))#FortheNorth
				if actionchallenge[d][2] == "addclaim":
					notify("{}'s {} action raise the claim value by 1.".format(me,card))#WinterIsComing
				if actionchallenge[d][2] == "burn":
					cardtoaction.markers[Burn] += 1
					notify("{}'s {} action {} gets -4 STR".format(me,card,cardtoaction))#Dracarys
					for cards in table:
						cards.target(False)
					if int(cardtoaction.strength) + cardtoaction.markers[STR_Up] - cardtoaction.markers[Burn]*4 <= 0:
						f = 1
						savetarget = cardtoaction
				if actionchallenge[d][2] == "returndead":
					if "Hatchling." in cardtoaction.Traits:
						if me.isInverted: cardtoaction.moveToTable(150,-230)
						else: cardtoaction.moveToTable(-130,130)
						notify("{}'s {} action put {} into play".format(me,card,cardtoaction))#FireandBlood
					else:
						cardtoaction.moveTo(me.deck)
						me.deck.shuffle()
						notify("{}'s {} action shuffle {} back into {}'s' deck".format(me,card,cardtoaction,me))#FireandBlood
				if actionchallenge[d][2] == "addstr3":
					cardtoaction.markers[STR_Up] += 3
					notify("{}'s {} action {} gets +3 STR.".format(me,card,cardtoaction))#MargaeryTyrell
				if actionchallenge[d][2] == "attaddstr3":
					cardtoaction.markers[STR_Up] += 3
					notify("{}'s {} action {} gets +3 STR.".format(me,card,cardtoaction))#Heartsbane
				if actionchallenge[d][2] == "standremovechallenge":
					cardtoaction.orientation = 0
					cardtoaction.highlight = None
					notify("{}'s {} action Stand {} and remove it from the challenge.".format(me,card,cardtoaction))#Highgarden
				if actionchallenge[d][2] == "3playeraddstr2":
					for addcard in cardtoaction:
						addcard.markers[STR_Up] += 2
						notify("{}'s {} action {} gets +2 STR.".format(me,card,addcard))#GrowingStrong
				if actionchallenge[d][2] == "choosechallenge":
					choiceList = ['Military', 'Intrigue', 'Power']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which challenge do you want to cannot initiate?", choiceList,colorList)
					if choice == 0:
						actionforability(card,repass)
						return
					if choice == 1:notify("{}'s {} action name a Military challenge.".format(me,card))#OlennasInformant
					if choice == 2:notify("{}'s {} action name a Intrigue challenge.".format(me,card))#OlennasInformant
					if choice == 3:notify("{}'s {} action name a Power challenge.".format(me,card))#OlennasInformant
				if actionchallenge[d][2] == "removechallenge":
					card.target(False)
					cardtoaction.highlight = None
					notify("{}'s {} action remove {} from the challenge.".format(me,card,cardtoaction))#AreoHotah

				cardtoaction == []
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == actionchallenge[d][4]:
					del actionattach[card._id]
					c = 1
		if c == 0:
			actionattach[card._id] -= 1
			if actionattach[card._id] == 0:del actionattach[card._id]
		if f == 1:
			savetarget.highlight = miljudgecolor
			setGlobalVariable("chaevent", str(me._id))
			miljudgementfinish([savetarget],1)
			remoteCall(otherplayer, "miljudgementfinish", [[savetarget],1])
			remoteCall(otherplayer, "interruptevent", ["miljudgementfp",2])
		else:
			remoteCall(otherplayer, "action", ["challenge",1])

def handview(vs):
	mute()
	me.hand.visibility = vs