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
targetcardcolor = "#e69138"
cantselectcardclor = "#000000"
targetcardfilter = "#55e69138"
cantselectcardfilter = "#88000000"
sourcecardcolor = "#3d85c6"
sourcecardcfilter = "#773d85c6"
showtablecolor = "#000002"
showtablefilter = "#00000002"
standcolor = "#000003"
standfilter = "#00000003"
discfilter = "#00000004"

GameURL = "http://octgn.gamersjudgement.com/wordpress/agot2/"
FAQ_URL = "https://images-cdn.fantasyflightgames.com/filer_public/03/43/034309e6-c3a2-4575-8062-32ede5798ef8/gt01_rules-reference-web.pdf"
#add
MilitaryIcon = ("MilitaryIcon", "7e9610d4-c06d-437d-a5e6-100000000001")
IntrigueIcon = ("IntrigueIcon", "0cabfb36-01b4-46c4-bb2a-42889fb63e8b")
PowerIcon = ("PowerIcon", "a6b9db40-b0ad-4b22-b049-5837c4ece904")
subMilitaryIcon = ("subMilitaryIcon", "786f6eb1-22bf-4623-9423-7854f5f078d6")
subIntrigueIcon = ("subIntrigueIcon", "7dadfabe-8024-4d93-91a7-81c11a51ff24")
subPowerIcon = ("subPowerIcon", "d042dab3-176a-471e-a917-1041c64c6579")
poisonIcon = ("poisonIcon", "aba7e269-4096-4b60-b1c5-0ab97dd9caa0")
standIcon = ("standIcon", "353db31d-b5d7-4f17-9683-08b03151ff83")
betrayalIcon = ("betrayalIcon", "d042dab3-176a-471e-a917-1041c64c6579")
cardtmp = []

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
liststeal = []
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
top5card = []
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
manualcard = []

listattach = []

#turnreset

addiconmil_turn = []
addiconint_turn = []
addiconpow_turn = []
subiconmil_turn = []
subiconint_turn = []
subiconpow_turn = []
returntohand_turn = []
disc_turn = []

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
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0:
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
		if stealth == "0" and not check511():
			if checktablestealthcount(0):
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					stealthdict()
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						selectstealth(table)
						return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":remoteCall(otherplayer, "challengedeficon", ["mil"])
			# if getGlobalVariable("mainstep") == "0":setGlobalVariable("mainstep", "1")
			# #checkafterchallengereacioncard(1)
			# b = str(int(me.getGlobalVariable("milcount"))+1)
			# me.setGlobalVariable("milcount",b)
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
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0:
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
		if stealth == "0" and not check511():
			if checktablestealthcount(0):
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					stealthdict()
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						selectstealth(table)
						return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":remoteCall(otherplayer, "challengedeficon", ["int"])
			# setGlobalVariable("mainstep", "1")
			# #checkafterchallengereacioncard(1)
			# b = str(int(me.getGlobalVariable("intcount"))+1)
			# me.setGlobalVariable("intcount",b)
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
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0:
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
		if stealth == "0" and not check511():
			if checktablestealthcount(0):
				choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
				if choice == True:
					stealthdict()
					notify("{} is ready to use the stealth keyword.".format(me))
					if getGlobalVariable("automode") == "1":
						selectstealth(table)
						return
				else:
					notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
		if getGlobalVariable("automode") == "1":remoteCall(otherplayer, "challengedeficon", ["pow"])
			# setGlobalVariable("mainstep", "1")
			# #checkafterchallengereacioncard(1)
			# b = str(int(me.getGlobalVariable("powcount"))+1)
			# me.setGlobalVariable("powcount",b)
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
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"milicon") and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "2")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"inticon") and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "2")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
						sessionpass = "intdefselect"
						notify("**{} into selectmode**".format(me))
				elif choice == 2:
					if getGlobalVariable("automode") == "1":
						c = 0
						for card in table:
							if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0 and card.highlight != IntrigueColor:
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
						targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"powicon") and card.orientation == 0], me._id) 
						setGlobalVariable("tableTargets", str(targetTuple))
						setGlobalVariable("selectmode", "2")
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0:
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
		# defender = me
		# remoteCall(otherplayer, "getdefender", [defender])
		sessionpass = ""
		selectedcard = []
		#challengeaction(1)

def defInt(group, x = 0, y = 0):
	mute()
	global defender
	global selectedcard
	global sessionpass
	if sessionpass != "intdefselectok":
		list = []
		for card in table:
			card.target(False)
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0:
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
				if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0 and card.highlight != IntrigueColor:
					card.highlight = IntrigueColor
					card.orientation = 1
			setGlobalVariable("bedefend","")
		notify("**{} declares INT defenders.**".format(me))
	else:
		if getGlobalVariable("automode") == "1":
			c = 0
			for card in table:
				if str(card._id) in getGlobalVariable("bedefend") and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0 and card.highlight != IntrigueColor:
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
		#challengeaction(1)

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
			if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0:
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
		#challengeaction(1)
		
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
		notify('{} kneels {}.'.format(me, card))
	else:
		notify('{} stands {}.'.format(me, card))

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
	if getGlobalVariable("automode") != "1":
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
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,-175)
	else:
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-320,85)

	notify("**{} is ready to setup**".format(me))
	if me._id == int(getGlobalVariable("aside")):
		if me.isInverted: 
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",380,-100)
		else:
			table.create("73a6655b-60b6-4080-b428-f4e0099e0f77",-160,8)
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
	countcards = -60
	countcardss = -60
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
				if not checksetupattch(cards):
					confirm("Attachment card's target error.")
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
			if getGlobalVariable("automode") == "1":
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

def checksetupattch(cards):
	c = 0
	f = 1
	listat = []
	listc = []
	for card in cards:
		if card.type == "Character":
			if 'No attachments.' not in card.Keywords:
				c = 1
				listc.append(card)
		if card.type == "Attachment":
			listat.append(card)
			if card.Keywords == "Opponent’s character only.":
				c = 0
				break
	if len(listat) > 0:
		for atcard in listat:
			if re.search(r'(.*) or (.*) character only.', atcard.Text,re.I):
				f = 0
				for targetcard in listc:
					if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
						debug(targetcard)
						f = 1
			elif re.search(r'\[(.*)] character only.', atcard.Text,re.I):
				chaonly = re.search(r'\[(.*)] character only.', atcard.Text,re.I).group(1)
				f = 0
				for targetcard in listc:
					if chaonly in targetcard.Faction or targetcard.Traits.find(chaonly) != -1:
						f = 1
	debug(f)
	debug(c)
	if f == 1 and c == 1:return True

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
	global cardtmp
	attachid = []
	if re.search(r'(.*) or (.*) character only.', listattach[0].Text,re.I):
		for targetcard in table:
			if targetcard.type == "Character" and targetcard.controller == me:
				if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
					attachid.append(targetcard._id)
	elif re.search(r'\[(.*)] character only.', listattach[0].Text,re.I):
		chaonly = re.search(r'\[(.*)] character only.', listattach[0].Text,re.I).group(1)
		for targetcard in table:
			if targetcard.type == "Character" and targetcard.controller == me:
				if chaonly in targetcard.Faction or targetcard.Traits.find(chaonly) != -1:
					attachid.append(targetcard._id)
	if attachid != []:selectlist = attachid
	else:selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
	selectcardnext(selectlist,"attatchcardselect",table,listattach[0],me,1)
	#selectcardnext(selectlist,spass,deck = table,actioncard = [],)
	# targetTuple = ([card._id for card in table if card.Type in "Character" and card.controller == me], me._id)
	# me.setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	# sessionpass = "attatchcardselect"
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	# for card in table:
	# 	if card.type not in ("Internal","Agenda","Faction"):
	# 		if card._id not in targetTuple[0] and card._id != listattach[0]._id:
	# 			card.filter="#88000000"
	# notify("**{} into selectmode**".format(me))
	whisper("Please select a target for {}".format(listattach[0]))

def reordertable(group, x = 0, y = 0):
	mute()
	countcards = -60
	countcard = -60
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
					if carda._id == cardindex and carda.controller == me:
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

	# targetTuple = (["setupOk"], me._id)
	# me.setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,-250)
	else:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,200)
	# notify("**{} into selectmode**".format(me))

def setupnext(group, x = 0, y = 0):
	mute()
	for cardn in table:
		if cardn.name == "setupnextbutton" and cardn.controller == me:
			cardn.delete()#delete setupnextbutton
	me.setGlobalVariable("setupOk","6")
	if me.getGlobalVariable("setupOk") == players[1].getGlobalVariable("setupOk") == "6":
		setGlobalVariable("selectmode", "0")
		notify("Plot phase start")
		remoteCall(me, "revealplot", [table])
		remoteCall(players[1], "revealplot", [table])

def plotnext(group, x = 0, y = 0):
	mute()
	for cardn in table:
		if cardn.name == "plotnextbutton" and cardn.controller == me:
			cardn.delete()#delete plotnextbutton
	me.setGlobalVariable("plotOk","finished")
	if me.getGlobalVariable("plotOk") == players[1].getGlobalVariable("plotOk") == "finished":
		notify("plot phase over")
		setGlobalVariable("selectmode", "0")
		setGlobalVariable("reavelplot","0")
		setGlobalVariable("generalaction","0")
		setGlobalVariable("drawphase","1")
		notify("draw phase start")
		drawphase(table)
		return

def drawnext(group, x = 0, y = 0):
	mute()
	for cardn in table:
		if cardn.name == "drawnextbutton" and cardn.controller == me:
			cardn.delete()#delete drawnextbutton
	me.setGlobalVariable("drawOk","finished")
	if me.getGlobalVariable("drawOk") == players[1].getGlobalVariable("drawOk") == "finished":
		setGlobalVariable("selectmode", "0")
		notify("draw phase over")
		setGlobalVariable("drawphase","0")
		notify("marshal phase start")
		marshalcountincome()
		return

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
	debug(getGlobalVariable("Kingdomgold0"))
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
			if getGlobalVariable("Kingdomgold0") == "1" and "Kingdom" in plotcard.Traits:me.counters['Gold'].value += 0
			elif getGlobalVariable("Edictgold0") == "1" and "Edict" in plotcard.Traits:me.counters['Gold'].value += 0
			else:
				me.counters['Gold'].value += int(plotcard.plotgoldincome)
			plotcard.markers[Gold] = me.counters['Gold'].value
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
		#notify("{} has a total of {} power.".format(person.name,person.counters['Power'].value))


def checkcardmodel(model,controller = me):
	mute()
	for card in table:
		if controller == "" and card.model == model:return True
		if controller != "" and card.controller == controller and card.model == model:return True


def endphase(group, x=0, y=0):
	mute()
	for cardn in table:
		if cardn.name == "endbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("dominancephase") == "1":
		setGlobalVariable("dominancephase","2")
		return
	if getGlobalVariable("dominancephase") == "2":
		resetperturn()
		setGlobalVariable("dominancephase","0")
		notify("dominanceend")
		standingphasestart(1)
		return
	if getGlobalVariable("standingphase") == "1":
		setGlobalVariable("standingphase","2")
		return
	if getGlobalVariable("standingphase") == "2":
		resetperturn()
		setGlobalVariable("standingphase","0")
		notify("standingend")
		taxationphasestart(1)
		return
	if getGlobalVariable("marshalphase") == "1":
		setGlobalVariable("marshalphase","2")
		return
	if getGlobalVariable("marshalphase") == "2":
		resetperturn()
		setGlobalVariable("marshalphase","0")
		notify("marshalend")
		challengephasestart(1)
		return
	if getGlobalVariable("taxationphase") == "1":
		setGlobalVariable("taxationphase","2")
		return
	if getGlobalVariable("taxationphase") == "2":
		resetperturn()
		setGlobalVariable("taxationphase","0")
		notify("taxationend")
		startnextphase(1)
		return
	if getGlobalVariable("challengephase") == "2":
		setGlobalVariable("challengephase","3")
		return
	if getGlobalVariable("challengephase") == "3":
		resetperturn()
		setGlobalVariable("challengephase","0")
		setGlobalVariable("activeplayer","")
		notify("challengephaseend")
		dominancephasestart(1)
		return


def taxationphasetmp(group, x = 0, y = 0): 
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
	me.setGlobalVariable("milcount","0")
	me.setGlobalVariable("milcountmax","1")	
	me.setGlobalVariable("intcount","0")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","0")
	me.setGlobalVariable("powcountmax","1")
	me.setGlobalVariable("active","0")
	me.setGlobalVariable("reduceloyal_turn", "0")

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
		setGlobalVariable("generalaction", "0")
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
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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

def challengephasestart(count):
	mute()
	if me.isInverted:table.create("2d4834e4-bd76-4e8d-9e5a-638cd25e6107",-375,-250)
	else:table.create("2d4834e4-bd76-4e8d-9e5a-638cd25e6107",-375,200)
	if count == 1:remoteCall(players[1], "challengephasestart", [2])

def challengenext():
	mute()
	for cardn in table:
		if cardn.name == "challengenextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("challengephase") == "0":
		setGlobalVariable("challengephase", "1")
		return
	if getGlobalVariable("challengephase") == "1":
		setGlobalVariable("activeplayer",str(fplay(1)._id))
		fplay(1).setGlobalVariable("active","1")
		if fplay(1) == me:challengeAnnounce(table)
		else: remoteCall(players[1], "challengeAnnounce", [table])

def challengeAnnounce(group, x=0, y=0):
	mute()
	me.setGlobalVariable("active","1")
	if me.isInverted:table.create("bb79eb8b-2593-4b1f-a62d-c0e86b6aaf14",-240,-175)
	else:table.create("bb79eb8b-2593-4b1f-a62d-c0e86b6aaf14",-240,125)
	if me.isInverted:table.create("ce281a89-276d-4a1c-b542-91680776b1d4",-240,-215)
	else:table.create("ce281a89-276d-4a1c-b542-91680776b1d4",-240,85)
	if me.isInverted:table.create("db7fc2af-6201-4112-9512-e78f10f5cd14",-280,-195)
	else:table.create("db7fc2af-6201-4112-9512-e78f10f5cd14",-280,105)
	if me.isInverted:table.create("6d6562bf-3f80-4964-b342-9c3f48e3be06",-320,-215)
	else:table.create("6d6562bf-3f80-4964-b342-9c3f48e3be06",-320,125)

def challengedeficon(ctype):
	mute()
	if ctype == "mil":
		if me.isInverted:table.create("a576df8f-7ff2-4b79-bb7d-8fa54d47ccf8",-375,-250)
		else:table.create("a576df8f-7ff2-4b79-bb7d-8fa54d47ccf8",-240,150)
	if ctype == "int":
		if me.isInverted:table.create("6ebd872e-b372-4973-b793-cd4d84d31476",-375,-250)
		else:table.create("6ebd872e-b372-4973-b793-cd4d84d31476",-240,150)
	if ctype == "int":
		if me.isInverted:table.create("9944aa40-0680-4f77-a668-80b5585af2df",-375,-250)
		else:table.create("9944aa40-0680-4f77-a668-80b5585af2df",-240,150)
	if me.isInverted:table.create("0952de65-f260-49d1-a8aa-184a6ff7251b",150,-250)
	else:table.create("0952de65-f260-49d1-a8aa-184a6ff7251b",-300,150)


def challengeAnnounceold(group, x=0, y=0):
	mute()
	cc = 0
	ccc = 1
	cccc = 0
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
			if me.getGlobalVariable("limitchallenge") != "0":
				if int(me.getGlobalVariable("milcount")) == int(me.getGlobalVariable("limitchallenge")) or int(me.getGlobalVariable("intcount")) == int(me.getGlobalVariable("limitchallenge")) or int(me.getGlobalVariable("powcount")) == int(me.getGlobalVariable("limitchallenge")):
					ccc = 0
					whisper("you cannot challenge this phase.")#SneakAttack
			for card in table:
				if card.model == "09903f79-6155-4a63-9b52-e10fb2e69898" and card.controller == me:
					cccc = 1
					break
			if int(me.getGlobalVariable("milcount")) < (int(me.getGlobalVariable("milcountmax")) + cccc) and ccc == 1:
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0:
						choiceList.append('Military')
						colorList.append('#ae0603')
						cc = 1
						break
			if int(me.getGlobalVariable("intcount")) < int(me.getGlobalVariable("intcountmax")):
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0:
						choiceList.append('Intrigue')
						colorList.append('#006b34')
						cc = 1
						break
			if int(me.getGlobalVariable("powcount")) < int(me.getGlobalVariable("powcountmax")) and ccc == 1:
				for card in table: 
					if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0:
						choiceList.append('Power')
						colorList.append('#1a4d8f')
						cc = 1
						break
			if cc == 1:
				choiceList.append('No challenge and Pass')
				colorList.append('#D8D8D8')
				choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
			else:
				return
				# if getGlobalVariable("challengephase") == "1":
				# 	setGlobalVariable("challengephase","2")
				# 	notify("{} has been active player".format(players[1]))
				# 	remoteCall(players[1], "challengeAnnounce", table)
				# 	return
				# if getGlobalVariable("challengephase") == "2":
				# 	setGlobalVariable("challengephase","0")
				# 	remoteCall(players[1], "dominance", table)
				# 	return
		if getGlobalVariable("automode") != "1":
			if choice == 1:announceMil(table)
			if choice == 2:announceInt(table)
			if choice == 3:announcePow(table)
			if choice == 4:notify("{} has no challenge to initiate.".format(me))
			if choice == 0:return
		else:
			if choiceList[choice-1] == 'Military':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "2")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
				sessionpass = "milselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'Intrigue':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
				sessionpass = "intselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'Power':
				targetTuple = ([card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0], me._id) 
				setGlobalVariable("tableTargets", str(targetTuple))
				setGlobalVariable("selectmode", "1")
				if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
				else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
				sessionpass = "powselect"
				notify("**{} into selectmode**".format(me))
			elif choiceList[choice-1] == 'No challenge and Pass':
				notify("{} has no challenge to initiate.".format(me))
				# if getGlobalVariable("challengephase") == "1":
				# 	setGlobalVariable("challengephase","2")
				# 	setGlobalVariable("activeplayer",str(players[1]._id))
				# 	players[1].setGlobalVariable("active","1")
				# 	notify("{} has been active player".format(players[1]))
				# 	remoteCall(players[1], "challengeAnnounce", table)
				# 	return
				# if getGlobalVariable("challengephase") == "2":
				# 	setGlobalVariable("challengephase","0")
				# 	remoteCall(players[1], "dominance", table)
				# 	return
			else:
				notify("{} has no challenge to initiate.".format(me))
				# if getGlobalVariable("challengephase") == "1":
				# 	setGlobalVariable("challengephase","2")
				# 	setGlobalVariable("activeplayer",str(players[1]._id))
				# 	players[1].setGlobalVariable("active","1")
				# 	notify("{} has been active player".format(players[1]))
				# 	remoteCall(players[1], "challengeAnnounce", table)
				# 	return
				# if me.getGlobalVariable("active") == players[1].getGlobalVariable("active") == "1":
				# 	setGlobalVariable("challengephase","0")
				# 	remoteCall(players[1], "dominance", table)
				# 	return
	else:
		notify("challenge already happened.")

def selectchallenge(ctype):
	mute()
	if ctype in("mil","int","pow"):
		for card in table:
			if card.highlight != Stealthcolor:card.highlight = None
			card.target(False)
	if ctype == "mil":
		for cardn in table:
			if cardn.name in ("DefendMil","DefendInt","DefendPow","DefendNon"):
				cardn.delete()
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"milicon") and card.orientation == 0]
		selectcardnext(targetTuple,"milselect",table,[],me,1,99)
	if ctype == "int":
		for cardn in table:
			if cardn.name in ("DefendMil","DefendInt","DefendPow","DefendNon"):
				cardn.delete()
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"inticon") and card.orientation == 0]
		selectcardnext(targetTuple,"intselect",table,[],me,1,99)
	if ctype == "pow":
		for cardn in table:
			if cardn.name in ("DefendMil","DefendInt","DefendPow","DefendNon"):
				cardn.delete()
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and checkchallengeicon(card,"powicon") and card.orientation == 0]
		selectcardnext(targetTuple,"powselect",table,[],me,1,99)
	if ctype == "defmil":
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"milicon") and card.orientation == 0]
		selectcardnext(targetTuple,"mildefselect",table,[],me,1,99)
	if ctype == "defint":
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"inticon") and card.orientation == 0]
		selectcardnext(targetTuple,"intdefselect",table,[],me,1,99)
	if ctype == "defpow":
		targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.isFaceUp and card.highlight != Stealthcolor and checkchallengeicon(card,"powicon") and card.orientation == 0]
		selectcardnext(targetTuple,"powdefselect",table,[],me,1,99)
	if ctype == "end":
		for cardn in table:
			if cardn.name in ("AttackMil","AttackInt","AttackPow","AttackNon") and cardn.controller == me:
				cardn.delete()
		remoteCall(players[1], "deletecicon", [])
		if getGlobalVariable("challengephase") == "1":
			setGlobalVariable("challengephase","2")
			setGlobalVariable("activeplayer",str(players[1]._id))
			notify("{} has been active player".format(players[1]))
			remoteCall(players[1], "challengeAnnounce", [table])
			return
		if me.getGlobalVariable("active") == players[1].getGlobalVariable("active") == "1":
			for card in table:
				card.highlight = None
				card.target(False)
			challengephaseend(table)
			remoteCall(players[1], "challengephaseend", [table])
			return
	if ctype == "nodef":
		notify("{} declares no defenders.".format(me))

def deletecicon():
	mute()
	for cardn in table:
		if cardn.name in ("DefendInt","DefendPow","DefendNon"):
			cardn.delete()


def challengephaseend(group, x=0, y=0):
	mute()
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,-250)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,200)

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
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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
	if len(me.piles['Plot Deck']) == 0:return
	dlg=cardDlg([c for c in me.piles['Plot Deck']])
	dlg.title = "These cards are in your unused-plot pile:"
	dlg.text = "Select a plot card to reveal."
	cards = dlg.show()
	if cards != None:
		#reset
		setGlobalVariable("challengeplayer","0")
		me.setGlobalVariable("cantuseevent", "0")
		me.setGlobalVariable("cantuselocation", "0")
		me.setGlobalVariable("cantuseattach", "0")
		setGlobalVariable("Kingdomgold0","0")
		setGlobalVariable("Edictgold0","0")
		setGlobalVariable("winint","0")
		me.setGlobalVariable("intwin", "0")
		me.setGlobalVariable("submilclaim", "0")
		me.setGlobalVariable("subintclaim", "0")
		me.setGlobalVariable("subpowclaim", "0")
		me.setGlobalVariable("limitchallenge", "0")
		setGlobalVariable("plotdisc","0")
		setGlobalVariable("plotkill","0")
		setGlobalVariable("firstreveal", "")
		
		countxy = 5
		for c in table: 
			if c.Type == "Plot" and c.controller == me:
				c.markers[standIcon] = 0
				c.filter = "#0099ffff"
				x, y = c.position
				plot = 1
				#if me.isInverted:c.moveToTable(x, y-30)
				#else:c.moveToTable(x, y+30)
		for card in cards:
			if plot == 0:
				if me.isInverted:card.moveToTable(-430,-75,True)
				else:card.moveToTable(-430,10,True)
			else:
				if me.isInverted:card.moveToTable(x-5, y-20,True)
				else:card.moveToTable(x-5, y+20,True)
			me.setGlobalVariable("turn","1")
			if getGlobalVariable("automode") == "0":
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
		askfirstplayer(table)
		return
	if getGlobalVariable("automode") == "1":askfirstreveal(table)

def askfirstreveal(group, x = 0, y = 0):
	mute()
	meplotcard = []
	otherplotcard = []
	colorList = []
	if fplay(1) == me:
		for card in table:
			if card.type == "Plot" and card.controller == me and card.filter == None and "When Revealed" in card.text:
				colorList.append("#1a4d8f")
				meplotcard = card
			if card.type == "Plot" and card.controller == players[1] and card.filter == None and "When Revealed" in card.text:
				colorList.append('#ae0603')
				otherplotcard = card
		if len(colorList) > 1:
			choiceList = ["{}'s {}".format(me,meplotcard.name),"{}'s {}".format(players[1],otherplotcard.name)]
			choice = askChoice("Decide who will First reveal.", choiceList,colorList)
			if choice == 1:
				notify("{} First reveal.".format(me))
				setGlobalVariable("reavelplot","1")
				setGlobalVariable("firstreveal", str(me._id))
				reavelplot(table)
			if choice == 2:
				notify("{} First reveal.".format(players[1]))
				setGlobalVariable("reavelplot","1")
				setGlobalVariable("firstreveal", str(players[1]._id))
				remoteCall(players[1], "reavelplot", table)
			if choice == 0:askfirstreveal(table)
		else:
			setGlobalVariable("reavelplot","1")
			if meplotcard != []:
				setGlobalVariable("firstreveal", str(me._id))
				remoteCall(me, "reavelplot", table)
			elif otherplotcard != []:
				setGlobalVariable("firstreveal", str(players[1]._id))
				remoteCall(players[1], "reavelplot", table)
			else:
				setGlobalVariable("firstreveal", str(me._id))
				setGlobalVariable("reavelplot","1")
				remoteCall(me, "reavelplot", table)
	else:remoteCall(players[1], "askfirstreveal", table)

def reavelplot(group, x = 0, y = 0):
	mute()
	for card in table:
		if card.type == "Plot" and card.controller == me and card.filter == None:
			notify("use {}'s ability".format(card))
			plotability(card)
			return
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		remoteCall(players[1], "reavelplot", table)
		return
	if getGlobalVariable("reavelplot") == "2":
		notify("plot phase over")
		setGlobalVariable("reavelplot","0")
		setGlobalVariable("drawphase","1")
		notify("draw phase start")
		drawphase(table)

def plotability(card):
	mute()
	global sessionpass
	global nextcardtmp
	global plotcard
	list10 = []
	listcount = 0
	searchok = 0
	drawcount = 0
	cards = None
	for d in plotdict:
		if card.model == plotdict[d][1] and card.controller == me:
			if plotdict[d][2] == "manual":
				manualprocess(card,"plotability")
				return
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
				if len(me.deck) < 10:listcount = len(me.deck)
				else:listcount = 10
				for c in me.deck.top(listcount):
					if c.Type in ("Attachment","Location"):
						searchok = 1
				dlg = cardDlg(me.deck.top(listcount))
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Location or Attachment card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if cards[0].Type in ("Attachment","Location"):
						cards[0].moveTo(me.hand)
						me.deck.shuffle()
						notify("{} reaveled {}, add {} to {} hand.".format(me,card,cards[0],me))#BuildingOrders
					else:
						if searchok == 1:
							if confirm("There is a Attachment or Location in these cards, select again？"):
								plotability(card)
								return
						else:notify("search failed")
				else:
					if searchok == 1:
						if confirm("There is a Attachment or Location in these cards, select again？"):
							plotability(card)
							return
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
					cardmarkers(card,"milicon",1)
					players[1].setGlobalVariable("submilclaim", str(int(players[1].getGlobalVariable("submilclaim"))+1))
				if choice == 2:
					cardmarkers(card,"inticon",1)
					players[1].setGlobalVariable("subintclaim", str(int(players[1].getGlobalVariable("subintclaim"))+1))
				if choice == 3:
					addPower(card)
					players[1].setGlobalVariable("subpowclaim", str(int(players[1].getGlobalVariable("subpowclaim"))+1))
				if choice == 0:
					plotability(card)
					return
				notify("{} reaveled {}, reduce the claim value on the attacker's revealed plot card by 1 during {} challenges.".format(me,card,choiceList[choice-1]))#CalmOverWesteros
			if plotdict[d][2] == "discattachment":
				if checkattachment(1) > 0:
					plotcard = card
					nextcardtmp = card
					selectlist = checkcardid(deck = table,cardtype = "Attachment")
					selectcardnext(selectlist,"Confiscationselect",table,card,"",1)
					return
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
					selectlist = checkcardid(deck = table,cardtype = "Character",stand = 0)
					selectcardnext(selectlist,"FilthyAccusationsselect",table,card,"",1)
					return
			if plotdict[d][2] == "discplayer":
				cards = players[1].hand.random()
				remoteCall(players[1], "HeadsonSpikes", [card,cards])
				return
			if plotdict[d][2] == "challenge1player":
				setGlobalVariable("challengeplayer","1")
				notify("{} reaveled {}, Each player cannot declare more than 1 character as an attacker or a defender in each challenge.".format(me,card))#JoustingContest
			if plotdict[d][2] == "challenge1player":
				me.setGlobalVariable("cantuseevent", "1")
				me.setGlobalVariable("cantuselocation", "1")
				me.setGlobalVariable("cantuseattach", "1")
				notify("{} reaveled {}, {} cannot marshal locations or attachments, or play events.".format(me,card,me))#MarchingOrders
			if plotdict[d][2] == "gold0":
				setGlobalVariable("Kingdomgold0","1")
				setGlobalVariable("Edictgold0","1")
				notify("{} reaveled {}, Treat the base gold value on each revealed Kingdom and each revealed Edict plot card as if it were 0.".format(me,card))#NavalSuperiority
			if plotdict[d][2] == "adddisc3":
				if len(me.piles['Discard pile']) > 0:
					for c in me.piles['Discard pile']:
						list10.append(c)
					dlg = cardDlg(list10)
					dlg.title = "These cards are in your deck:"
					dlg.text = "select Choose up to 3 cards shuffle them into your deck."
					dlg.min = 0
					dlg.max = 3
					cards = dlg.show()
					if cards != None:
						for dc in cards:
							dc.moveTo(me.deck)
						me.deck.shuffle()
						drawcount = len(cards)
				else:drawcount = 0
				notify("{} reaveled {}, choose {} cards shuffle them into {} deck..".format(me,card,drawcount,me))#Rebuilding
			if plotdict[d][2] == "1challenge":
				me.setGlobalVariable("limitchallenge", "1")
				notify("{} reaveled {}, {} cannot initiate more than 1 challenge in the challenges phase.".format(me,card,me))#SneakAttack
			if plotdict[d][2] == "10searchcha":
				if len(me.deck) < 10:listcount = len(me.deck)
				else:listcount = 10
				for c in me.deck.top(listcount):
					if c.Type in ("Character"):
						searchok = 1
				dlg = cardDlg(me.deck.top(listcount))
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Character card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if cards[0].Type in ("Character"):
						cards[0].moveTo(me.hand)
						me.deck.shuffle()
						notify("{} reaveled {}, add {} to {} hand.".format(me,card,cards[0],me))#Summons
					else:
						debug("1111")
						if searchok == 1:
							if confirm("There is a Character in these cards, select again？"):
								debug("3333")
								plotability(card)
								return
						else:notify("search failed")
				else:
					debug("222")
					if searchok == 1:
						if confirm("There is a Character in these cards, select again？"):
							plotability(card)
							return
					else:notify("search failed")
			if plotdict[d][2] == "search5c":
				choiceList = ['Hand','Discard pile']
				colorList = ['#ae0603' ,'#1a4d8f']
				choice = askChoice("Which deck do you want to select?", choiceList,colorList)
				if choice == 0:
					plotability(card)
					return
				if choice == 1:
					for c in me.hand:
						if c.type == "Character" and int(c.cost) <= 5:
							list10.append(c)
				if choice == 2:
					for c in me.piles['Discard pile']:
						if c.type == "Character" and int(c.cost) <= 5:
							list10.append(c)
				dlg = cardDlg(list10)
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Character card put it into play.do not select card to reselect."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if me.isInverted:cards[0].moveToTable(20,-100)			
					else:cards[0].moveToTable(-20,0)
					notify("{} reaveled {}, put {} to into play.".format(me,card,cards[0]))#Reinforcements
				elif cards == []:plotability(card)
			if plotdict[d][2] == "disc1player":
				notify("{} reaveled {}, Each player chooses a character he or she controls (if able), and discards it from play (cannot be saved).".format(me,card))#MarchedtotheWall
				if fplay(1) == me:plotdisccharacter("disc1",card)
				else:remoteCall(players[1], "plotdisccharacter", ["disc1",card])
				return
			if plotdict[d][2] == "kill3player":
				if fplay(1) == me:plotdisccharacter("kill1",card)
				else:remoteCall(players[1], "plotdisccharacter", ["kill1",card])
				return
			if plotdict[d][2] == "addstandicon":
				card.markers[standIcon] = 1
				notify("{} reaveled {}, Place a stand token on {}.".format(me,card,card))#PowerBehindtheThrone
			if plotdict[d][2] == "gain3gold":
				remoteCall(players[1], "addplotgold", table)
				remoteCall(players[1], "addplotgold", table)
				remoteCall(players[1], "addplotgold", table)
				notify("{} reaveled {}, {} gains 3 gold.".format(me,card,players[1]))#TradingwiththePentoshi
			if plotdict[d][2] == "search3maester":
				for c in me.deck:
					if "Maester" in c.traits:
						searchok = 1
				dlg = cardDlg(me.deck)
				dlg.title = "These cards are in your deck:"
				dlg.text = "select 1 Maester Character card add it to your hand."
				dlg.min = 0
				dlg.max = 1
				cards = dlg.show()
				if cards != [] and cards != None:
					if "Maester" in cards[0].traits:
						cardintable(cards[0],"Character")
						#cards[0].moveTo(me.hand)
						me.deck.shuffle()
						notify("{} reaveled {}, add {} to {} hand.".format(me,card,cards[0],me))#HeretoServe
					else:
						debug("1111")
						if searchok == 1:
							if confirm("There is a Maester Character in these cards, select again？"):
								debug("3333")
								plotability(card)
								return
						else:notify("search failed")
				else:
					debug("222")
					if searchok == 1:
						if confirm("There is a Character in these cards, select again？"):
							plotability(card)
							return
					else:notify("search failed")
			if plotdict[d][2] == "select2location":
				if fplay(1) == me:plotdisccharacter("disclocation1",card)
				else:remoteCall(players[1], "plotdisccharacter", ["disclocation1",card])
				return
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
		else:reavelplot(table)
		return
	if getGlobalVariable("reavelplot") == "2":
		resetplot()
		remoteCall(players[1], "resetplot", [])
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)
		return

def resetplot():
	if len(me.piles['Plot Deck']) == 0:
		for card in table:
				if card.Type == "Plot" and card.controller == me and card.filter == usedplotcolor:
					card.moveTo(me.piles['Plot Deck'])
	for card in table:
		if card.Type == "Plot" and card.controller == me:
			if me.isInverted:card.moveToTable(-430,-75,True)
			else:card.moveToTable(-430,10,True)

def addplotgold(group, x = 0, y = 0):
	mute()
	for card in table:
		if card.type == "Plot" and card.controller == me and card.filter == None:addGold(card)


def plotdisccharacter(typep,card):
	mute()
	global sessionpass
	global plotcard
	if typep == "disc1":
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotdisccharacter1",table,card,"",1)
			setGlobalVariable("plotdisc","1")
		else:remoteCall(players[1], "plotdisccharacter", ["disc2",card])
	if typep == "disc2":
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotdisccharacter2",table,card,"",1)
			setGlobalVariable("plotdisc","1")
		else:remoteCall(fplay(1), "callplotleave", [1])
	if typep == "kill1":
		setGlobalVariable("plotkill","1")
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotkillcharacter1",table,card,"",1,mode = 3)
		else:remoteCall(players[1], "plotdisccharacter", ["kill2",card])
	if typep == "kill2":
		setGlobalVariable("plotkill","1")
		plotcard = card
		if checkcharacter(me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me)
			selectcardnext(selectlist,"plotkillcharacter2",table,card,"",1,mode = 3)
		else:
			cardbekill = []
			for card in table:
				if card.highlight == miljudgecolor:cardbekill.append(card)
			remoteCall(fplay(1), "characterkilled", [cardbekill,1])
	if typep == "disclocation1":
		plotcard = card
		if checkcardstatus(cardtype = "Location",player = me):
			selectlist = checkcardid(deck = table,cardtype = "Location",player = me)
			selectcardnext(selectlist,"plotdisclocation1",table,[],"",1,2)
		else:remoteCall(players[1], "plotdisccharacter", ["disc2",card])
	if typep == "disclocation2":
		plotcard = card
		if checkcardstatus(cardtype = "Location",player = me):
			selectlist = checkcardid(deck = table,cardtype = "Location",player = me)
			selectcardnext(selectlist,"plotdisclocation2",table,[],"",1,2)
			
def disclocation(count):#PoliticalDisaster
	mute()
	for card in table:
		if card.filter == discfilter and card.type == "Location" and card.controller == me:
			disc(card)
	if count == 1:
		remoteCall(players[1], "disclocation", [2])
		return
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
		else:reavelplot(table)
		return
	if getGlobalVariable("reavelplot") == "2":
		resetplot()
		remoteCall(players[1], "resetplot", [])
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)
		return

def plotleave(cardbekill,count):
	mute()
	global abilityattach
	debug(cardbekill)
	c = 0
	list = []
	for cardt in table:
		if cardt.type == "Attachment":
			list.append(cardt)
	debug(list)
	for card in cardbekill:
		whisper("{}".format(card))
		for d in cardkill:
			if card.model == cardkill[d][1] and card.controller == me and cardkill[d][2] != "link":
				if cardkill[d][4] == "Attachment":
					if len(list) > 0:
						if not abilityattach.has_key(card._id):
							abilityattach[card._id] = 1
						else:abilityattach[card._id] += 1
	debug(abilityattach)
	if count == 1:remoteCall(players[1], "callplotleave", [2])
	if count == 2:remoteCall(fplay(1), "interruptevent", ["characterkill",1])


def plotdisccard(count):
	mute()
	global selectedcard
	global sessionpass
	global nextcardtmp
	global plotcard
	if nextcardtmp != []:disc(nextcardtmp)
	notify("{} disc {} for {}.".format(me,nextcardtmp,plotcard))#MarchedtotheWall
	nextcardtmp = []
	selectedcard = []
	plotcard = []
	if count == 1:
		remoteCall(otherplayer, "plotdisccard", [2])
	else:
		setGlobalVariable("plotdisc","0")
		if getGlobalVariable("reavelplot") == "1":
			setGlobalVariable("reavelplot","2")
			if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
			else:reavelplot(table)
			return
		if getGlobalVariable("reavelplot") == "2":
			if fplay(1) == me:actiongeneral(1)
			else:remoteCall(players[1], "actiongeneral", 1)


def HeadsonSpikes(card,cards):
	mute()
	if cards.type == "Character":
		cards.moveTo(me.piles['Dead pile'])
		remoteCall(players[1], "addhousepow", [2])
		notify("{} reaveled {}, {} disc {} and gain 2 power for {} faction.".format(players[1],card,me,cards,players[1]))#HeadsonSpikes
	else:
		cards.moveTo(me.piles['Discard pile'])
		notify("{} reaveled {}, {} disc {}.".format(players[1],card,me,cards))#HeadsonSpikes
	if getGlobalVariable("reavelplot") == "1":
		setGlobalVariable("reavelplot","2")
		if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
		else:reavelplot(table)
		return
	if getGlobalVariable("reavelplot") == "2":
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)

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
		if fplay(1) == me:actiongeneral(1)
		else:remoteCall(players[1], "actiongeneral", 1)
		# notify("draw phase over")
		# setGlobalVariable("drawphase","0")
		# notify("marshal phase start")
		# setGlobalVariable("marshalphase","1")
		# me.setGlobalVariable("inmarshal","1")
		# if fplay(1) == me:marshalphase(table)
		# else:remoteCall(players[1], "marshalphase", table)

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

def marshalcountincome():
	mute()
	setGlobalVariable("marshalphase","1")
	if fplay(1) == me:
		setGlobalVariable("activeplayer",str(me._id))
		me.setGlobalVariable("active","1")
		marshalaction()
	else:
		setGlobalVariable("activeplayer",str(players[1]._id))
		players[1].setGlobalVariable("active","1")
		remoteCall(players[1], "marshalaction", [])

def marshalend():
	mute()
	for cardn in table:
		if cardn.name == "marshalendbutton" and cardn.controller == me:
			cardn.delete()
	if fplay(1) == me:remoteCall(players[1], "marshalaction", [])
	else:
		marshalphaseend()
		remoteCall(players[1], "marshalphaseend", [])

	
def marshalaction():
	mute()
	countincome(table)
	if me.isInverted:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-375,-250)
	else:table.create("f5fb1824-1d0e-4a4a-a431-46e0a06f1a42",-375,200)

def marshalphaseend():
	mute()
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,-250)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,200)

def marshalcard(group, x = 0, y = 0):
	mute()
	global sessionpass
	targetTuple = ([card._id for card in me.hand if card.type in ("Character","Location","Attachment")], me._id) 
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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
					if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and cardc.model == "df79718d-b01d-4338-8907-7b6abff58303":cardmarkers(cardc,"milicon",-1)#096
					if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
						stradd = re.search('\+\d\sSTR', card.Text).group()
						cardc.markers[STR_Up] -= int(stradd[1])
					if re.search('\[INT]\sicon', card.Text):cardc.cardmarkers(card,"inticon",-1)
					if re.search('\[POW]\sicon', card.Text):cardc.markers[PowerIcon] -= 1
					if re.search('\[MIL]\sicon', card.Text) and cardc.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(cardc,"milicon",-1)
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
	elif card.type == "Location":
		for dcard in table:
			if dcard.name == card.name and dcard.filter == DuplicateColor and dcard.controller == me:
				list.append(dcard)
		if len(list) > 0:
			choiceList = ['Disc Location', 'Disc Duplicate']
			colorList = ['#ae0603' ,'#D8D8D8']
			choice = askChoice("Which pass do you want to action?", choiceList,colorList)
			if choice == 2:
				list[0].moveTo(me.piles['Discard pile'])
				notify("{} discard {}'s duplicate.".format(me,card))
				return
			elif choice == 1:
				for disccard in list:
					disccard.moveTo(me.piles['Discard pile'])
					notify("{} discard {}'s duplicate.".format(me,card))
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
	#if getGlobalVariable("selectmode") == "0" and me.getGlobalVariable("setupOk") != "4":
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
	if getGlobalVariable("firstplay") == str(me._id):
		if me.isInverted: 
			card.moveToTable(-160,-100)
			card.controller = me
		else:
			card.moveToTable(-160,8)
			card.controller = me
	elif getGlobalVariable("firstplay") == str(players[1]._id):
		if me.isInverted: 
			card.moveToTable(-160,8)
			card.controller = players[1]
		else:
			card.moveToTable(-160,-100)
			card.controller = players[1]
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

def cardintable(card,cardtype):
	mute()
	clist = [p for p in table
				if p.controller == me and p.type == cardtype and p.isFaceUp]
	if len(clist) > 0:
		clist.reverse()
		for character in clist:
			x, y = character.position
			break
		clist.reverse()
		if me.isInverted: card.moveToTable(x-80,y)
		else:card.moveToTable(x+80,y)
	else:
		if me.isInverted:card.moveToTable(-60,-100)			
		else:card.moveToTable(-60,10)

def play(card):
	mute()
	ambush = 0
	fll = 0
	if getGlobalVariable("selectmode") == "1":return#and sessionpass == "savecardselect":return
	if card.type == "Event" and me.getGlobalVariable("cantuseevent") == "1":
		whisper("You cannot play events.")
		return
	if card.type == "Location" and me.getGlobalVariable("cantuselocation") == "1":
		whisper("You cannot marshal locations .")
		return
	if card.type == "Attachment" and me.getGlobalVariable("cantuseattach") == "1":
		whisper("You cannot marshal attachments ")
		return
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
		if card.loyal == "Yes":
			cost -= int(me.getGlobalVariable("reduceloyal_turn"))
			if me.getGlobalVariable("reduceloyal_turn") != "0":notify("Reduce the cost of the next loyal card you marshal or play this phase by 1 from Fealty")
			me.setGlobalVariable("reduceloyal_turn", "0")


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
				if targetcard.filter == targetcardcolor or targetcard.targetedBy == me:
					if targetcard.Keywords == 'No attachments.':
						whisper("{} cannot be attached.".format(targetcard))
						targetcard.filter = None
						if cardtmp != []:cardtmp.arrow(cardtmp,False)
					elif re.search(r'(.*) or (.*) character only.', card.Text,re.I):
						if targetcard.Traits.find('Lord') != -1 or targetcard.Traits.find('Lady') != -1:
							list.append(targetcard)
							targetcard.filter = None
							if cardtmp != []:cardtmp.arrow(cardtmp,False)
						else:
							whisper("{} can only be attached to [Lord or Lady] characters.".format(card))
							targetcard.filter = None
							if cardtmp != []:cardtmp.arrow(cardtmp,False)
					elif re.search(r'\[(.*)] character only.', card.Text,re.I):
						chaonly = re.search(r'\[(.*)] character only.', card.Text,re.I).group(1)
						if targetcard.Faction.find(chaonly) != -1 or targetcard.Traits.find(chaonly) != -1:
							list.append(targetcard)
							targetcard.filter = None
							if cardtmp != []:cardtmp.arrow(cardtmp,False)
						else:
							whisper("{} can only be attached to [{}] characters.".format(card,chaonly))
							targetcard.filter = None
							if cardtmp != []:cardtmp.arrow(cardtmp,False)
					else:
						if me.getGlobalVariable("setupOk") in ("4","5"):
							if targetcard.controller == me:list.append(targetcard)
						else:list.append(targetcard)
						targetcard.filter = None
						if cardtmp != []:cardtmp.arrow(cardtmp,False)
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
						if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and choose.model == "df79718d-b01d-4338-8907-7b6abff58303":cardmarkers(choose,"milicon",1)#096
						if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":choose.markers[STR_Up] += countusedplot
						if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', card.Text).group()
							choose.markers[STR_Up] += int(stradd[1])
						if re.search('\[INT]\sicon', card.Text):cardmarkers(choose,"inticon",1)
						if re.search('\[POW]\sicon', card.Text):cardmarkers(choose,"powicon",1)
						if re.search('\[MIL]\sicon', card.Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(choose,"milicon",1)
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
					if me.isInverted: card.moveToTable(x+80,y)
					else:card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(-60,-100)			
					else:card.moveToTable(-60,10)
			elif card.Type == "Location":
				clist = [p for p in table
							if p.controller == me and p.type == "Location" and p.isFaceUp]
				if len(clist) > 0:
					clist.reverse()
					for location in clist:
						x, y = location.position
						break
					clist.reverse()
					if me.isInverted: card.moveToTable(x+80,y)
					else:card.moveToTable(x+80,y)
				else:
					if me.isInverted:card.moveToTable(-60,-220)			
					else:card.moveToTable(-60,120)
			elif card.type == "Event":
				if me.isInverted: card.moveToTable(-130,-230)
				else: card.moveToTable(-130,130)
				if me.getGlobalVariable("firstevent") == "0":me.setGlobalVariable("firstevent", "1")
				#whisper("Select a target.")
				#checksaveevent(card)
			else:
				if me.isInverted: card.moveToTable(-130,-230)
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
	setGlobalVariable("Invertedloaddeck","0")
	setGlobalVariable("selectgamemode","0")
	# ver = "1.4.2.0"
	# log = changelogcn["1.4.2.0"]
	# log = '\n\n>>> '.join(log)
	# choice = confirm("Changes in {}:\n>>> {}\n\nSee more info?".format(ver, log))
	# if choice == True:openUrl('https://github.com/TassLehoff/AGoTv2-OCTGN')
	
	if not me.isInverted:
		notify("waiting for HOST select game mode.")
		selectgamemode()



def selectgamemode():
	mute()
	choiceList = ['Automation', 'Manually']
	colorList = ['#ae0603' ,'#006b34']
	choice = askChoice("select game mode", choiceList,colorList)
	if choice == 1:setGlobalVariable("automode","1")
	elif choice == 2:setGlobalVariable("automode","0")
	else:
		selectgamemode()
		return
	setGlobalVariable("selectgamemode","1")
	if getGlobalVariable("Invertedloaddeck") =="1":remoteCall(players[1], "afterload", [players[1]])


def onloaddeck(args):
	mute()
	if args.player == me:
		if getGlobalVariable("selectgamemode") =="1":afterload(me)
		else:
			setGlobalVariable("Invertedloaddeck","1")
			notify("waiting for host select game mode")

def afterload(player):
	mute()
	c = len(players)
	setGlobalVariable("numplayer","{}".format(c))
	if not me.isInverted:
		setGlobalVariable("AID","{}".format(me))
		setGlobalVariable("aside","{}".format(me._id))
	else:
		setGlobalVariable("BID","{}".format(me))
		setGlobalVariable("bside","{}".format(me._id))

	setGlobalVariable("actioncancel", "0")
	setGlobalVariable("tableTargets", "")
	setGlobalVariable("selectmode", "0")
	setGlobalVariable("insertre", "")
	setGlobalVariable("cantchallenge", "0")
	setGlobalVariable("bedefend", "")
	setGlobalVariable("aftcr", "")
	setGlobalVariable("aftcu", "")
	setGlobalVariable("dominancestart", "")
	setGlobalVariable("dominancewin", "")
	setGlobalVariable("dominancewinplayer","")
	setGlobalVariable("dominanceend", "")
	setGlobalVariable("standingstart", "")
	setGlobalVariable("standingover", "")
	setGlobalVariable("standingend", "")
	setGlobalVariable("taxationstart", "")
	setGlobalVariable("taxationreturn", "")
	setGlobalVariable("taxationrcheckhand", "")
	setGlobalVariable("taxationend", "")
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
	setGlobalVariable("reavelplot","1")
	setGlobalVariable("drawphase","0")
	setGlobalVariable("marshalphase","0")
	me.setGlobalVariable("inmarshal","1")
	me.setGlobalVariable("firstevent", "0")
	me.setGlobalVariable("firstcharacter", "0")
	me.setGlobalVariable("firstll", "0")#A Noble Cause
	setGlobalVariable("firstreveal", "")
	setGlobalVariable("challengephase","0")
	setGlobalVariable("dominancephase","0")
	setGlobalVariable("standingphase","0")
	setGlobalVariable("taxationphase","0")
	me.setGlobalVariable("milcount","0")
	me.setGlobalVariable("milcountmax","1")
	me.setGlobalVariable("intcount","0")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","0")
	me.setGlobalVariable("powcountmax","1")
	setGlobalVariable("action","0")
	setGlobalVariable("activeplayer","")
	me.setGlobalVariable("active","0")
	setGlobalVariable("winint","0")
	me.setGlobalVariable("intwin", "0")
	me.setGlobalVariable("submilclaim", "0")
	me.setGlobalVariable("subintclaim", "0")
	me.setGlobalVariable("subpowclaim", "0")
	setGlobalVariable("challengeplayer","0")

	me.setGlobalVariable("cantuseevent", "0")
	me.setGlobalVariable("cantuselocation", "0")
	me.setGlobalVariable("cantuseattach", "0")

	setGlobalVariable("Kingdomgold0","0")
	setGlobalVariable("Edictgold0","0")

	me.setGlobalVariable("limitchallenge", "0")

	setGlobalVariable("plotdisc","0")
	setGlobalVariable("plotkill","0")
	me.setGlobalVariable("plotOk","")
	me.setGlobalVariable("drawOk","")

	setGlobalVariable("generalaction", "0")
	setGlobalVariable("dominanceaction", "0")
	setGlobalVariable("standingaction", "0")
	setGlobalVariable("actiontaxation", "0")
	

	me.setGlobalVariable("reduceloyal_turn", "0")
	if player == me:
		checkdeck()
		setup(table)
		
def onmoved(args):
	mute()
	index = 0
	for card in args.cards:
		attach = eval(getGlobalVariable("attachmodify"))
		if args.cards[index].type == "Character" and args.toGroups[index].name == "Table" and args.fromGroups[index].name == "Table" and card.controller == me and card.filter != WaitColor:
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
		if card.type == "Attachment" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.controller == me:
			for card in table:
				if attach.has_key(args.cards[index]._id):
					if attach[args.cards[index]._id] == card._id:
						del attach[args.cards[index]._id]
						setGlobalVariable("attachmodify",str(attach))
						debug(getGlobalVariable("attachmodify"))
					#rollback
						if args.cards[index].model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
							card.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
						if args.cards[index].model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and card.model == "df79718d-b01d-4338-8907-7b6abff58303":cardmarkers(card,"milicon",-1)#096
						if re.search('\+\d\sSTR', args.cards[index].Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', args.cards[index].Text).group()
							card.markers[STR_Up] -= int(stradd[1])
						if re.search('\[INT]\sicon', args.cards[index].Text):cardmarkers(card,"inticon",-1)
						if re.search('\[POW]\sicon', args.cards[index].Text):subPower(card)
						if re.search('\[MIL]\sicon', args.cards[index].Text) and args.cards[index].model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":cardmarkers(card,"milicon",-1)
			args.cards[index].resetProperties()
		if args.cards[index].type == "Character" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.controller == me:
			for d in attach:
				if attach[d] == args.cards[index]._id:
					for cardd in table:
						if cardd._id == d:
							remoteCall(cardd.owner, "disc", [cardd])
							del attach[d]
							setGlobalVariable("attachmodify",str(attach))
							debug(getGlobalVariable("attachmodify"))
		#Warship and Drowned Men
		if args.cards[index].model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and "Warship" in cardadd.traits:args.cards[index].markers[STR_Up] += 1
		if args.cards[index].model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and "The Reach" in cardadd.traits:args.cards[index].markers[STR_Up] += 1
		if args.cards[index].Faction == "Night's Watch." and args.cards[index].type == "Character" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and cardadd.model == "5d20e021-5d12-4338-8bdd-42d008bff919" and cardadd.filter != WaitColor:args.cards[index].markers[STR_Up] += 1
		if args.cards[index].model == "390a8cf7-8bc4-45c1-bea5-e6a694e9f2d5" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:args.cards[index].markers[STR_Up] += me.counters['Gold'].value
		if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and cardadd.model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and "Direwolf" in cardadd.traits:args.cards[index].markers[STR_Up] += 1
				if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.cards[index]._id != cardadd._id:
					for cardadd2 in table:
						if cardadd2.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd2._id != cardadd._id and cardadd2._id != args.cards[index]._id:cardadd2.markers[STR_Up] -= 1
				if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":
					for cardadd2 in table:
						if cardadd2.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and cardadd2._id != cardadd._id:cardadd2.markers[STR_Up] += 1
		if args.cards[index].model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			for cardadd in table:
				if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.cards[index]._id != cardadd._id:cardadd.markers[STR_Up] -= 1
		if args.cards[index].model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Direwolf" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":cardadd.markers[STR_Up] += 1
		if args.cards[index].model != "c41d4a72-6919-4e32-97ef-a4b0f1acb281" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Direwolf" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "c41d4a72-6919-4e32-97ef-a4b0f1acb281":cardadd.markers[STR_Up] -= 1
		if args.cards[index].type == "Location" and args.toGroups[index].name == "Table" and args.fromGroups[index].name != "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Warship" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002":cardadd.markers[STR_Up] += 1
			if "The Reach" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54":cardadd.markers[STR_Up] += 1
			if args.cards[index].model == "5d20e021-5d12-4338-8bdd-42d008bff919":
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch." and cardadd.type == "Character" and cardadd.filter != WaitColor:cardadd.markers[STR_Up] += 1
		if args.cards[index].type == "Location" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and args.cards[index].controller == me and args.cards[index].filter != WaitColor:
			if "Warship" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "cbeb3a37-d4c1-4697-b8d2-e366b4569002":cardadd.markers[STR_Up] -= 1
			if "The Reach" in args.cards[index].traits:
				for cardadd in table:
					if cardadd.controller == me and cardadd.model == "3e1a5952-f5d1-4bca-9226-2b94531cfa54":cardadd.markers[STR_Up] -= 1
			if args.cards[index].model == "5d20e021-5d12-4338-8bdd-42d008bff919":
				for cardadd in table:
					if cardadd.controller == me and cardadd.Faction == "Night's Watch."and cardadd.type == "Character" and cardadd.filter != WaitColor:cardadd.markers[STR_Up] -= 1

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
    global sessionpass
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
		if actioninsert == "Confiscationselect":
			remoteCall(cardtoaction.controller,"disc",[cardtoaction])
			notify("{} reaveled {}, discard {} from play.".format(me,plotcard,cardtoaction))#Confiscation
			plotcard.target(False)
			cardtoaction = []
			plotcard = []
		if actioninsert == "FilthyAccusationsselect":
			remoteCall(cardtoaction.controller, "kneel", [cardtoaction])
			notify("{} reaveled {}, kneel {}.".format(me,plotcard,cardtoaction))#FilthyAccusations
			plotcard.target(False)
			cardtoaction = []
			plotcard = []

		if actioninsert in ("FilthyAccusationsselect","Confiscationselect"):
			sessionpass = ""
			if getGlobalVariable("reavelplot") == "1":
				setGlobalVariable("reavelplot","2")
				if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
				else:reavelplot(table)
				return
			if getGlobalVariable("reavelplot") == "2":
				if fplay(1) == me:actiongeneral(1)
				else:remoteCall(players[1], "actiongeneral", 1)


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
		if checkcountercharater(interruptcancelcard):
			if interruptpasscount < 2:
				choiceList = ['interrupt', 'cancel']
				colorList = ['#ae0603' ,'#006b34']
				choice = askChoice("Do you want to interrupt {}'s {} ?".format(interruptcancelplayer,interruptcancelcard.name), choiceList,colorList)
			if interruptpasscount == 2:
				choiceList = ['interrupt', 'cancel']
				colorList = ['#ae0603' ,'#006b34']
				choice = askChoice("Do you want to interrupt {}'s {} ?".format(interruptcancelplayer,interruptcancelcard.name), choiceList,colorList)
		else:choice = 2
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
							elif mainpass in("dominancestart","dominancewin","dominanceend"):
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
									remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
									else:reaction(mainpass,1)
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
							elif mainpass == "generalaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
									else:action("general",1)
							elif mainpass == "dominanceaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
									else:action("dominance",1)
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
						elif mainpass in("dominancestart","dominancewin","dominanceend"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
								else:reaction(mainpass,1)
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
						elif mainpass == "generalaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
								else:action("general",1)
						elif mainpass == "dominanceaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
									else:action("dominance",1)
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
						elif mainpass in("dominancestart","dominancewin","dominanceend"):
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
								remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
								else:reaction(mainpass,1)
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
						elif mainpass == "generalaction":
							if inserttarget.type == "Event":
								if inserttarget.controller == me:disc(inserttarget)
								else:remoteCall(otherplayer, "disc", [inserttarget])
							if interruptcancelok == 1:
								remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
							else:
								for card in table:
									card.target(False)
									if card.filter == showtablecolor:
										remoteCall(card.controller,"returncard",[card])
								remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
								if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
								else:action("general",1)
						elif mainpass == "dominanceaction":
								if inserttarget.type == "Event":
									if inserttarget.controller == me:disc(inserttarget)
									else:remoteCall(otherplayer, "disc", [inserttarget])
								if interruptcancelok == 1:
									remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
								else:
									for card in table:
										card.target(False)
										if card.filter == showtablecolor:
											remoteCall(card.controller,"returncard",[card])
									remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
									if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
									else:action("dominance",1)
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
					elif mainpass in("dominancestart","dominancewin","dominanceend"):
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"reactionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
							remoteCall(inserttarget.controller,"reactionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "reaction", [mainpass,1])
							else:reaction(mainpass,1)
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
					elif mainpass == "generalaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
								if card.filter == showtablecolor:
									remoteCall(card.controller,"returncard",[card])
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["general",1])
							else:action("general",1)
					elif mainpass == "dominanceaction":
						if inserttarget.type == "Event":
							if inserttarget.controller == me:disc(inserttarget)
							else:remoteCall(otherplayer, "disc", [inserttarget])
						if interruptcancelok == 1:
							remoteCall(inserttarget.controller,"actionforability",[inserttarget,mainpass])
						else:
							for card in table:
								card.target(False)
								if card.filter == showtablecolor:
									remoteCall(card.controller,"returncard",[card])
							remoteCall(inserttarget.controller,"actionattachsub",[inserttarget])
							if inserttarget.controller == me:remoteCall(otherplayer, "action", ["dominance",1])
							else:action("dominance",1)
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
				intocharacterkill(abilityattach,interruptpasscount)
				return
			if sessionpass == "killabilityok":
				killcards = selectedcard
				if killcards == []:
					if interruptpasscount == 2:
						if getGlobalVariable("plotdisc") == "1":plotdisccard(1)
						else:cardleavetable(1)
					else:
						interruptpasscount += 1
						sessionpass = ""
						remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					debug(killcards[0])
					killcard = killcards[0]
					sessionpass = ""
					remoteCall(otherplayer, "checkinterruptkill", [killcard])
		else:
			if interruptpasscount == 2:
				if getGlobalVariable("plotdisc") == "1":plotdisccard(1)
				else:cardleavetable(1)
			else:
				interruptpasscount += 1
				remoteCall(otherplayer, "interruptevent", ["characterkill",interruptpasscount])
			return

def intocharacterkill(cards,count):
	mute()
	global sessionpass
	global kbcount
	sessionpass = ""
	targetTuple = [card._id for card in table if card.controller == me and cards.has_key(card._id)]
	selectcardnext(targetTuple,"killability",table,[],"",1)
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
	subcost = 0
	# for cardhand in me.hand:
	# 	for d in counterevent:
	# 		if cardhand.model == counterevent[d][1] and counterevent[d][4].find(charatercard.Type) != -1:
	# 			if counterevent[d][5] == "all":
	# 				if counterevent[d][7] == "opponent" and charatercard.controller != me:ee = 1
	# 				elif counterevent[d][7] == "all":ee = 1
	# 			elif counterevent[d][5] != "all":
	# 				for cardunique in table:
	# 					if cardunique.Faction == counterevent[d][5] and cardunique.Unique == counterevent[d][6]:
	# 						if counterevent[d][7] == "opponent" and charatercard.controller != me:ee = 1
	# 						elif counterevent[d][7] == "all":ee = 1
	# if ee == 1:return True
	if charatercard.type in("Location","Character","Attachment"):
		if checkcardstatus(deck = table,player = me,cardtype = "Faction",faction = "Lannister."):
			if checkcardstatus(deck = table,player = me,cardtype = "Character",faction = "Lannister.",unique = "Yes"):
				if me.counters['Gold'].value >= 1:
					ee = 1
	elif charatercard.type == "Event":
		if charatercard.cost == "X":ee = 1
		else:
			if me.getGlobalVariable("firstevent") == "0" and checkpr(me):subcost = 1
			if me.counters['Gold'].value >= int(charatercard.cost)-subcost:ee = 1
			if checkcardstatus(deck = table,player = me,model = "9e56783a-c133-4f81-9914-4e81b92ba5d1"):ee = 1

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
	global cardtmp
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
		cardtmp = card
		discattch(table)
		return
	if c == "kneelplayer":
		cardtmp = card
		kneelplayer(table)
		return
	remoteCall(otherplayer,"interruptevent",["characterkill",1])

def discattch(group, x=0, y=0):
	mute()
	selectlist = checkcardid(deck = table,cardtype = "Attachment")
	selectcardnext(selectlist,"discattch",table,cardtmp,"",1)


def kneelplayer(group, x=0, y=0):
	mute()
	global sessionpass
	selectlist = checkcardid(deck = table,cardtype = "Character",stand = 0)
	selectcardnext(selectlist,"kneel",table,cardtmp,"",1)


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
	abilityattach = {}
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
				remoteCall(otherplayer, "checkreactioncard", [1])

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
				intoreaction(reactionattach,reactioncount,"reaction")
				return
			if sessionpass == "reactionok":
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						if getGlobalVariable("plotkill") == "1":
							if getGlobalVariable("reavelplot") == "1":
								setGlobalVariable("reavelplot","2")
								if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
								else:reavelplot(table)
								return
							if getGlobalVariable("reavelplot") == "2":
								setGlobalVariable("plotkill","0")
								if fplay(1) == me:actiongeneral(1)
								else:remoteCall(players[1], "actiongeneral", 1)
								return
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
				if getGlobalVariable("plotkill") == "1":
					if getGlobalVariable("reavelplot") == "1":
						setGlobalVariable("reavelplot","2")
						if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
						else:reavelplot(table)
						return
					if getGlobalVariable("reavelplot") == "2":
						setGlobalVariable("plotkill","0")
						if fplay(1) == me:actiongeneral(1)
						else:remoteCall(players[1], "actiongeneral", 1)
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
	if actioninsert in ("dominancestart","dominancewin","dominanceend"):
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,actioninsert)
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
			if sessionpass in ("reactiondsuok","reactiondswinok"):
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", [actioninsert,reactioncount])
			return
	if actioninsert in ("standingstart","standingover","standingend"):
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,actioninsert)
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
			if sessionpass in ("reactionstandingok"):
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", [actioninsert,reactioncount])
			return
	if actioninsert in ("taxationstart","taxationreturnover","taxationcheckhandover","taxationend"):
		if len(reactionattach) > 0:
			debug(sessionpass)
			if sessionpass == "":
				choiceList = ['reaction', 'cancel']
				colorList = ['#006b34' ,'#ae0603']
				choice = askChoice("Which Pass do you want to action?", choiceList,colorList)
				if choice == 1:
					intoreaction(reactionattach,reactioncount,actioninsert)
					return
				if choice == 2:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
			if sessionpass in ("reactiontaxationok"):
				reactioncards = selectedcard
				if reactioncards == []:
					if reactioncount == 2:
						notify("reaction over")
						clearreaction(1)
					else:
						reactioncount += 1
						sessionpass = ""
						remoteCall(players[1], "reaction", [actioninsert,reactioncount])
					return
				else:
					debug(reactioncards[0])
					reactioncard = reactioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkreaction", [reactioncard,actioninsert])
		else:
			if reactioncount == 2:
				notify("reaction over")
				clearreaction(1)
			else:
				reactioncount += 1
				remoteCall(otherplayer, "reaction", [actioninsert,reactioncount])
			return

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
		remoteCall(players[1],"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
		remoteCall(me, "interruptevent", ["interruptcancel",2])
	else:
		remoteCall(players[1],"reactionforability",[reactioncard,repass])

def intoreaction(cards,count,sepass):
	mute()
	global sessionpass
	global recount
	sessionpass = ""
	targetTuple = [d for d in reactionattach]
	selectcardnext(targetTuple,sepass,table,[],me,1)
	#targetTuple = ([card._id for card in table if card.controller == me and cards.has_key(card._id)], me._id) 
	# setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	# if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	# else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	# notify("**{} into selectmode**".format(me))
	# sessionpass = sepass
	recount = count

def reactionforability(card,repass):
	mute()
	debug(card)
	debug(repass)
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
					if checkchallengeicon(cardtoaction,"milicon") > 0:
						choiceList.append("Military")
						colorList.append('#ae0603')
					if checkchallengeicon(cardtoaction,"inticon") > 0:
						choiceList.append("Intrigue")
						colorList.append('#006b34')
					if checkchallengeicon(cardtoaction,"powicon") > 0:
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
					card.markers[betrayalIcon] += 1
					notify("{}'s {} forced reaction add 1 betrayal token".format(me,card))#SerJorahMormont
					if card.markers[betrayalIcon] == 3:
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
	if repass == "dominancestart":
		for d in dominancestart:
			if card.model == dominancestart[d][1] and card.controller == me:
				if dominancestart[d][2] == "stand":
					card.orientation = 0
					notify("{}'s {} reaction stand himself".format(me,card))#FieryFollowers
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == dominancestart[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(players[1], "reaction", ["dominancestart",1])
	if repass == "dominancewin":
		for d in dominancewin:
			if card.model == dominancewin[d][1] and card.controller == me:
				if dominancewin[d][2] == "2power":
					addhousepow(2)
					notify("{}'s {} reaction add 2 power".format(me,card))#AFeastforCrows
				if dominancewin[d][2] == "move1pow":
					remoteCall(otherplayer, "subhousepow", 1)
					addhousepow(1)
					notify("{}'s {} reaction move 1 power icon from {}".format(me,card,players[1]))#ChamberofthePaintedTable
				if dominancewin[d][2] == "returniron":
					for cardhand in me.piles['Discard Pile']:
						if "Ironborn" in cardhand.traits and cardhand.type == "Character":
							list.append(cardhand)
					dlg = cardDlg(list)
					dlg.title = "These cards are in your Discard Pile:"
					dlg.text = "Declares at least 1 Ironborn Character put it into play."
					dlg.min = 1
					dlg.max = 1
					cards = dlg.show()
					if cards != None:
						cardintable(cards[0],"Character")
						notify("{}'s {} action put {} into play".format(me,card,cards[0]))#AeronDamphair
				if not reactioncardlimit.has_key(card._id):
					reactioncardlimit[card._id] = 1
				else:reactioncardlimit[card._id] += 1
				if reactioncardlimit[card._id] == dominancewin[d][5]:
					del reactionattach[card._id]
					c = 1
		if c == 0:
			reactionattach[card._id] -= 1
			if reactionattach[card._id] == 0:del reactionattach[card._id]
		remoteCall(players[1], "reaction", ["dominancewin",1])

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
	targetTuple = [card._id for card in table if card.type == "Character" and card.controller == me and card.keywords.find("Stealth") != -1 and card.highlight in(MilitaryColor,IntrigueColor,PowerColor)]
	selectcardnext(targetTuple,"stealthselect",table,[],me,1)
	# setGlobalVariable("tableTargets", str(targetTuple))
	# setGlobalVariable("selectmode", "1")
	# if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
	# else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	# notify("**{} into selectmode**".format(me))
	# sessionpass = "stealthselect"

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
	global cardtmp
	global liststeal
	debug(sessionpass)
	selectedcard = []
	list = []
	listsave = []

	for card in table:
		if card.filter == targetcardcolor:
			if me.getGlobalVariable("setupOk") in ("4","5"):
				if card.controller == me:selectedcard.append(card)
			else:selectedcard.append(card)
	for card in me.hand:
		if card.filter == targetcardcolor:
			selectedcard.append(card)
	if sessionpass == "stealthselect":
		if len(selectedcard) > 1:
			whisper("You must select {} character.".format(stealthcount))
			return
		if len(selectedcard) == 0:
			liststeal = []
		else:
			nextcardtmp = selectedcard[0]
			selectlist = [card._id for card in table if card.Type == "Character" and card.controller != me and card.keywords.find("Stealth") == -1 and card.highlight == None]
			selectcardnext(selectlist,"stealthselectok",table,nextcardtmp,me)
			return
			# sessionpass = "stealthselectok"
			# stealthcard(table)
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
			disc(listattach[0])
			del listattach[0]
			selectedcard = []
			if len(listattach) > 0:attatchcard(listattach)
			else:
				reordertable(table)
			return
	if sessionpass == "discattch":
		if len(selectedcard) > 1:
			whisper("You must select only one attachment to discard.")
			return
		elif len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			remoteCall(otherplayer,"interruptevent",["characterkill",1])
			return
		elif len(selectedcard) == 1:
			for card in table:
				card.target(False)
			remoteCall(selectedcard[0].controller, "disc", [selectedcard[0]])
	if sessionpass == "kneel" or sessionpass == "initimidateselect" or sessionpass == "FilthyAccusationsselect":
		if len(selectedcard) > 1:
			whisper("You must select only one character to kneel.")
			return
		elif len(selectedcard) == 0 and sessionpass != "FilthyAccusationsselect":
			sessionpass = ""
			clearfilter("")
			remoteCall(otherplayer,"interruptevent",["characterkill",1])
		elif len(selectedcard) == 1 and sessionpass != "FilthyAccusationsselect":
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
			return
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
	if sessionpass in ("general","dominance","standing","taxation"):
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("action over")
				clearaction(1)
			else:remoteCall(otherplayer, "action", [sessionpass,2])
			sessionpass = ""
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['HearMeRoar'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = me.hand,cardtype = "Character",faction = "Lannister.")
			selectcardnext(selectlist,"addlanselectok",me.hand,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['ArianneMartell'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = me.hand,cardtype = "Character",cost = 5)
			debug(selectlist)
			selectcardnext(selectlist,"add5returnmeselectok",me.hand,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['EdricDayne'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "1goldiconselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Confinement'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",cost = 4)
			selectcardnext(selectlist,"loseiconselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['OldForestHunter'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = me.hand)
			selectcardnext(selectlist,"d1cg1gselectok",me.hand,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['VeteranBuilder'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Location",stand = 1)
			selectcardnext(selectlist,"standlocationselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['MagisterIllyrio'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",stand = 1)
			selectcardnext(selectlist,"2gstandcselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Handmaiden'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",traits = "Lady.",stand = 1)
			selectcardnext(selectlist,"standladyselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['WakingtheDragon'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",faction = "Targaryen.",unique = "Yes")
			selectcardnext(selectlist,"standtcselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['TheBearandtheMaidenFair'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "5t3bselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Fealty'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "kneelfactionselectok"
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['PowerBehindtheThrone'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			selectlist = checkcardid(deck = table,cardtype = "Character",stand = 1)
			selectcardnext(selectlist,"standiconselectok",table,nextcardtmp,me)
			return
		if len(selectedcard) == 1 and selectedcard[0].model == generalaction['Halder'][1] and generalaction['Halder'][2] == "manual":
			manualprocess(selectedcard[0],"generalaction")
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceaction['TaketheBlack'][1]:
			setGlobalVariable("selectmode", "0")
			play(selectedcard[0])
			manualprocess(selectedcard[0],"dominance")
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceaction['MessengerRaven'][1]:
			for card in me.hand:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "returndraw1selectok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceaction['TheTickler'][1]:
			setGlobalVariable("selectmode", "0")
			manualprocess(selectedcard[0],"dominance")

	if sessionpass == "dominancestart":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("reaction over")
				clearaction(1)
			else:
				remoteCall(players[1], "reaction", ["dominancestart",2])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == dominancestart['FieryFollowers'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominancestandok"
	if sessionpass == "dominancewin":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
			return
		if len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("reaction over")
				clearaction(1)
			else:
				remoteCall(players[1], "reaction", ["dominancewin",2])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == dominancewin['AFeastforCrows'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominance2powerok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominancewin['ChamberofthePaintedTable'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominancemove1powok"
		if len(selectedcard) == 1 and selectedcard[0].model == dominancewin['AeronDamphair'][1]:
			for card in table:card.target(False)
			nextcardtmp = selectedcard[0]
			sessionpass = "dominancereturnironok"
	if sessionpass == "dominanceend":
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
		if len(selectedcard) == 0:
			sessionpass = ""
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("reaction over")
				clearaction(1)
			else:
				remoteCall(players[1], "reaction", ["dominanceend",2])
				return
		if len(selectedcard) == 1 and selectedcard[0].model == dominanceend['Varys'][1]:
			manualprocess(selectedcard[0],"dominanceend")

	if sessionpass in("addlanselectok","add5returnmeselectok","loseiconselectok","standlocationselectok","2gstandcselectok","standladyselectok","standtcselectok","5t3bselectok","standiconselectok","d1cg1gselectok"):
		if len(selectedcard) > 1:
			whisper("You must select only one card to action.")
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
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				setGlobalVariable("actioncancel", "0")
				notify("action over")
				if getGlobalVariable("plotdisc") == "1":plotdisccard(1)
				else:cardleavetable(1)
			else:remoteCall(otherplayer, "action", [sessionpass,2])
			sessionpass = ""
			return
	if sessionpass == "plotdisccharacter1" or sessionpass == "plotdisccharacter2":
		if len(selectedcard) > 1 or len(selectedcard) == 0:
			whisper("You must select only one Character.")
			return
	if sessionpass == "plotkillcharacter1" or sessionpass == "plotkillcharacter2":
		if len(selectedcard) > 3:
			whisper("You must select up to 3 characters.")
			return
		if len(selectedcard) == 0:
			if not confirm ("This will kill all of your characters,continue?"):return
	if sessionpass == "killabilitychooseone":
		if len(selectedcard) > 1:
			whisper("You must select only one Character.")
			return
	if sessionpass == "reaction" or sessionpass == "reactionaftc":
		if len(selectedcard) > 1:
			whisper("You must select only one card to reaction.")
			return
		if len(selectedcard) == 0:
			clearfilter("")
			for cardn in table:
				if cardn.name == "nextbutton" and cardn.controller == me:
					cardn.delete()#delete nextbutton
					stealthcount = 0
			setGlobalVariable("selectmode", "0")
			actioncancelcount = int(getGlobalVariable("actioncancel"))+1
			setGlobalVariable("actioncancel", str(actioncancelcount))
			if actioncancelcount == 2:
				if sessionpass == "reactionaftc":
					setGlobalVariable("actioncancel", "0")
					notify("reaction over")
					clearaction(1)
					return
				if sessionpass == "reaction":
					if getGlobalVariable("insertre") != "":
						restoreinterruptlib(1)
						return
					if getGlobalVariable("plotkill") == "1":
						if getGlobalVariable("reavelplot") == "1":
							setGlobalVariable("reavelplot","2")
							if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
							else:reavelplot(table)
							return
						if getGlobalVariable("reavelplot") == "2":
							setGlobalVariable("plotkill","0")
							if fplay(1) == me:actiongeneral(1)
							else:remoteCall(players[1], "actiongeneral", 1)
							return
					if getGlobalVariable("aftcuevent") != "-1" or getGlobalVariable("chaevent") != "-1":challengebalanceover(1)			
					else:remoteCall(winplayer, "keyword", [1])
			else:remoteCall(otherplayer, "reaction", [sessionpass,2])
			sessionpass = ""
			return
	if sessionpass  in ("milselect","intselect","powselect","mildefselect","intdefselect","powdefselect"):
		if getGlobalVariable("challengeplayer") != "0":
			cpc = int(getGlobalVariable("challengeplayer"))
			if len(selectedcard) > cpc:
				whisper("You must select only {} Character.".format(cpc))
				for card in table:
					card.target(False)
				return
	for cardn in table:
		if cardn.name == "nextbutton" and cardn.controller == me:
			cardn.delete()#delete nextbutton
			stealthcount = 0
	setGlobalVariable("selectmode", "0")
	if intertreaction == 0 and sessionpass != "attatchcardselect":
		cardtmp = []
		clearfilter("")
		for card in table:
			card.target(False)
		for card in me.hand:
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
					if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
					else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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
			clearfilter(me)
			del listattach[0]
			selectedcard = []
			if len(listattach) > 0:attatchcard(listattach)
			else:
				reordertable(table)
		else:
			clearfilter(me)
			del listattach[0]
			selectedcard = []
			if len(listattach) > 0:attatchcard(listattach)
			else:
				reordertable(table)

	if sessionpass == "stealthselectok":
		sessionpass = ""
		if len(selectedcard) == 1:
			cardtoaction = selectedcard[0]
			selectedcard[0] = nextcardtmp
			cardtoaction.highlight = Stealthcolor
			if getGlobalVariable("cantchallenge") == "1":setGlobalVariable("cantchallenge", card._id)
			liststeal.remove(selectedcard[0])
			cardtoaction = []
			if len(liststeal) > 0:
				if checktablestealthcount(0):
					selectstealth(table)
		elif len(selectedcard) == 0:
			liststeal = []
			return
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
			if getGlobalVariable("reavelplot") == "1":
				setGlobalVariable("reavelplot","2")
				if str(me._id) == getGlobalVariable("firstreveal"):remoteCall(players[1], "reavelplot", table)
				else:reavelplot(table)
				return
			if getGlobalVariable("reavelplot") == "2":
				if fplay(1) == me:actiongeneral(1)
				else:remoteCall(players[1], "actiongeneral", 1)
			return
	if sessionpass == "plotdisccharacter1":
		sessionpass = ""
		nextcardtmp = selectedcard[0]
		remoteCall(players[1], "plotdisccharacter", ["disc2",plotcard])
	if sessionpass == "plotdisccharacter2":
		sessionpass = ""
		nextcardtmp = selectedcard[0]
		remoteCall(fplay(1), "callplotleave", [1])
	if sessionpass == "standcharacter1":
		sessionpass = ""
		if len(selectedcard) != 0:
			for standcard in selectedcard:
				standcard.filter = standfilter
		remoteCall(players[1], "standcharacter", ["stand2"])
	if sessionpass == "standcharacter2":
		sessionpass = ""
		if len(selectedcard) != 0:
			for standcard in selectedcard:
				standcard.filter = standfilter
		remoteCall(fplay(1), "standcharacterend", [1])
	if sessionpass == "plotdisclocation1":
		sessionpass = ""
		for disccard in table:
			if disccard.controller == me and disccard.type == "Location" and disccard.filter != WaitColor and disccard not in selectedcard:
				disccard.filter = discfilter
		remoteCall(players[1], "plotdisccharacter", ["plotdisclocation2"])
	if sessionpass == "plotdisclocation2":
		sessionpass = ""
		for disccard in table:
			if disccard.controller == me and disccard.type == "Location" and disccard.filter != WaitColor and disccard not in selectedcard:
				disccard.filter = discfilter
		
	if sessionpass == "plotkillcharacter1":
		sessionpass = ""
		for cards in table:
			if cards.Type == "Character" and cards.filter == None and cards.controller == me and cards not in selectedcard:cards.highlight = miljudgecolor
		remoteCall(players[1], "plotdisccharacter", ["kill2",plotcard])
	if sessionpass == "plotkillcharacter2":
		sessionpass = ""
		for cards in table:
			if cards.Type == "Character" and cards.filter == None and cards.controller == me and cards not in selectedcard:cards.highlight = miljudgecolor
		cardbekill = []
		for card in table:
			if card.highlight == miljudgecolor:cardbekill.append(card)
		remoteCall(fplay(1), "characterkilled", [cardbekill,1])
	if sessionpass in ("1goldiconselectok","kneelfactionselectok","d1cg1gselectok"):
		if sessionpass == "1goldiconselectok":
			me.counters['Gold'].value -= 1
			for incomecard in table:
				if incomecard.controller == me and incomecard.markers[Gold] > 0:
					incomecard.markers[Gold] -= 1
		if sessionpass == "d1cg1gselectok":
			disc(selectedcard[0])
			selectedcard[0] = nextcardtmp
		
		if sessionpass == "kneelfactionselectok":
			for cardf in table:
				if cardf.Type == "Faction" and cardf.orientation == 1 and cardf.controller == me:
					cardf.orientation = 1
		nextcardtmp = []
		sessionpass = "actionok"
		if getGlobalVariable("dominanceaction") != "0":action("dominance",1)
		else:action("general",1)
		return
	if sessionpass in("addlanselectok","add5returnmeselectok","loseiconselectok","standlocationselectok","2gstandcselectok","standladyselectok","standtcselectok","5t3bselectok","standiconselectok","d1cg1gselectok"):
		if len(selectedcard) == 0:
			delactioncard(nextcardtmp)
			nextcardtmp = []
			sessionpass = ""
			remoteCall(otherplayer, "action", ["general",1])
			return
		if sessionpass == "2gstandcselectok":
			me.counters['Gold'].value -= 2
			for incomecard in table:
				if incomecard.controller == me and incomecard.markers[Gold] > 0:
					incomecard.markers[Gold] -= 2
		if sessionpass in("add5returnmeselectok","standlocationselectok","2gstandcselectok","standladyselectok","standiconselectok"):
			cardtoaction = selectedcard[0]
			if sessionpass in ("add5returnmeselectok"):
				savetarget = selectedcard[0]
				cardtoaction.moveToTable(100,200)
				cardtoaction.filter = showtablefilter
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "generalaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				selectedcard[0] = nextcardtmp
				selectedcard[0].arrow(cardtoaction)
		if sessionpass in("addlanselectok","loseiconselectok","5t3bselectok","standtcselectok"):
			if play(nextcardtmp):
				cardtoaction = selectedcard[0]
				savetarget = selectedcard[0]
				debug(savetarget)
				if sessionpass in ("addlanselectok"):
					cardtoaction.moveToTable(100,200)
					cardtoaction.filter = showtablefilter
				interruptcancelcard = nextcardtmp
				interruptcancelplayer = me
				saveactionplayer = me
				inserttarget = interruptcancelcard
				mainpass = "generalaction"
				remoteCall(otherplayer,"savetargetinserttarget",[savetarget,inserttarget,interruptcancelcard,interruptcancelplayer,interruptcancellastcard,interruptcanceledcard,interruptcancelok,saveactionplayer,mainpass])
				remoteCall(me, "setTimer", [me,"interruptcancel",table])
				nextcardtmp = []
				return
			else:
				delactioncard(nextcardtmp)
				nextcardtmp = []
				sessionpass = ""
				remoteCall(otherplayer, "action", ["general",1])
				return
		nextcardtmp = []
		sessionpass = "actionok"
		action("general",1)
		return
	if sessionpass == "dominancestandok":
		nextcardtmp = []
		sessionpass = "reactiondsuok"
		reaction("dominancestart",1)
		return
	if sessionpass in ("dominance2powerok","dominancemove1powok","dominancereturnironok"):
		nextcardtmp = []
		sessionpass = "reactiondswinok"
		reaction("dominancewin",1)
		return
	if sessionpass in ("returndraw1selectok","12131313"):
		nextcardtmp = []
		sessionpass = "actionok"
		action("dominance",1)
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
	#checkafterchallengereacioncard(1)

def onclick(args):
	mute()
	if getGlobalVariable("selectmode") != "0" and args.card.type not in ("Internal"):
		list2 = []
		if me.getGlobalVariable("setupOk") in ("4","5") or me.getGlobalVariable("plotOk") == "ok" or me.getGlobalVariable("drawOk") == "ok":tuplecard = eval(me.getGlobalVariable("tableTargets"))
		else:tuplecard = eval(getGlobalVariable("tableTargets"))
		debug(tuplecard)
		if me._id == tuplecard[1]:
			if args.card.type not in ("Internal"):
				if tuplecard[0] == ["setupOk"]:
					whisper("card cant be selected")
					return
				if cardtmp != []:
					if args.card._id in tuplecard[0]:
						if args.card.filter == targetcardcolor:
							if getGlobalVariable("selectmode") == "1":
								cardtmp.arrow(cardtmp,False)
								args.card.filter = None
							else:
								args.card.filter = None
								cardtmp.arrow(cardtmp,False)
								for card in table:
									if card.filter == targetcardcolor:cardtmp.arrow(card)
													
						else:
							if getGlobalVariable("selectmode") == "1":
								cardtmp.arrow(cardtmp,False)
								for card in table:
									if card.filter == targetcardcolor:card.filter = None
								cardtmp.arrow(args.card)
								args.card.filter = targetcardfilter
							else:
								debug(targetlen())
								if targetlen() == int(getGlobalVariable("selectmode")):return
								cardtmp.arrow(args.card)
								args.card.filter = targetcardfilter
					else:
						whisper("card cant be selected")
				else:
					if args.card._id in tuplecard[0]:
						if getGlobalVariable("selectmode") == "1":
							if args.card.filter == targetcardcolor:
								args.card.filter = None
							else:
								for card in table:
									if card.filter == targetcardcolor:card.filter = None
								args.card.filter = targetcardfilter
						else:
							if args.card.filter == targetcardcolor:
								args.card.filter = None
							else:
								debug(targetlen())
								if targetlen() == int(getGlobalVariable("selectmode")):return
								args.card.filter = targetcardfilter
					else:
						whisper("card cant be selected")
		else:
			whisper("is not your turn")

def targetlen():
	mute()
	list = []
	for card in table:
		if card.filter == targetcardcolor:
			list.append(card)
	return len(list)


def ondbclick(args):
	mute()

	if args.card.name == "nextbutton" and args.card.controller == me:next(table)
	elif args.card.name == "setupnextbutton" and args.card.controller == me:setupnext(table)
	elif args.card.name == "plotnextbutton" and args.card.controller == me:plotnext(table)
	elif args.card.name == "drawnextbutton" and args.card.controller == me:drawnext(table)
	elif args.card.name == "manualbutton" and args.card.controller == me:resumeprocess()
	elif args.card.name == "endbutton" and args.card.controller == me:endphase(table)
	elif args.card.name == "marshalendbutton" and args.card.controller == me:marshalend()
	elif args.card.name == "challengenextbutton" and args.card.controller == me:challengenext()
	elif args.card.name == "dominancenextbutton" and args.card.controller == me:dominancenext()
	elif args.card.name == "standingnextbutton" and args.card.controller == me:standingnext()
	elif args.card.name == "taxationnextbutton" and args.card.controller == me:taxationnext()
	elif args.card.name == "AttackMil" and args.card.controller == me:selectchallenge("mil")
	elif args.card.name == "AttackInt" and args.card.controller == me:selectchallenge("int")
	elif args.card.name == "AttackPow" and args.card.controller == me:selectchallenge("pow")
	elif args.card.name == "AttackNon" and args.card.controller == me:selectchallenge("end")
	elif args.card.name == "DefendMil" and args.card.controller == me:selectchallenge("defmil")
	elif args.card.name == "DefendInt" and args.card.controller == me:selectchallenge("defint")
	elif args.card.name == "DefendPow" and args.card.controller == me:selectchallenge("defpow")
	elif args.card.name == "DefendNon" and args.card.controller == me:selectchallenge("nodef")

		

def test(group, x=0, y=0):
	mute()
	actiongeneral(2)
	resetperturn()
	#resetplot()
	#challengeAnnounce(table)
	#taxationphasestart(1)
	#setGlobalVariable("standingphase","1")
	#dominancewinplayer = me
	#setGlobalVariable("drawphase","2")
	#standcharacter("stand1")
	#actiongeneral(1)
	#reavelplot(table)
	#dominancewinreaction(1)
	#dominancestartreaction(1)
	#debug(checkstannis())
	#marshalcountincome()
	
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
	for card in table:
		if card.Type == "Character" and card.controller != me and card.keywords.find("Stealth") == -1 and card.highlight == None:
			return True

def stealthdict():
	mute()
	global liststeal
	for card in table:
		if card.Type == "Character" and card.controller == me and card.keywords.find("Stealth") != -1:
			liststeal.append(card)
	return liststeal

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

def checkcharacter(player):
	mute()
	for card in table:
		if card.Type == "Character" and card.controller == player:
			return True

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
	if count == 1:remoteCall(players[1], "clearreaction", [2])
	if count == 2:
		if getGlobalVariable("dominancestart") == "2":
			setGlobalVariable("dominancestart", "0")
			if fplay(1) == me:dominance(table)
			else: remoteCall(players[1], "dominance", [table])
			return
		if getGlobalVariable("dominancewin") == "2":
			setGlobalVariable("dominancewin", "0")
			if fplay(1) == me:actiondominance(1)
			else: remoteCall(players[1], "actiondominance", [1])
			return
		if getGlobalVariable("dominanceend") == "2":
			setGlobalVariable("dominanceend", "0")
			dominancephaseend(table)
			remoteCall(players[1], "dominancephaseend", [table])
			return
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
	debug(getGlobalVariable("drawphase"))
	if getGlobalVariable("reavelplot") == "2":
		if me.isInverted:table.create("634c8980-9e07-40ba-a259-df1fe8fd184a",-375,-250)
		else:table.create("634c8980-9e07-40ba-a259-df1fe8fd184a",-375,200)
	if getGlobalVariable("drawphase") == "2":
		if me.isInverted:table.create("76d32ba3-bb1b-4c88-8e99-4381e45595e9",-375,-250)
		else:table.create("76d32ba3-bb1b-4c88-8e99-4381e45595e9",-375,200)
	if count == 1:

		remoteCall(players[1], "clearaction", [2])
	if count == 2:
		if getGlobalVariable("reavelplot") == "2":

			return
		if getGlobalVariable("drawphase") == "2":

			return
		if getGlobalVariable("dominanceaction") == "2":
			setGlobalVariable("dominanceaction","0")
			if fplay(1) == me:dominanceendreaction(1)
			else: remoteCall(players[1], "dominanceendreaction", [1])
			return
		if getGlobalVariable("standingaction") == "2":
			setGlobalVariable("standingaction","0")
			if fplay(1) == me:standingendreaction(1)
			else: remoteCall(players[1], "standingendreaction", [1])
			return
		if getGlobalVariable("actiontaxation") == "2":
			setGlobalVariable("actiontaxation","0")
			if fplay(1) == me:taxationendreaction(1)
			else: remoteCall(players[1], "taxationendreaction", [1])
			return
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
						if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
						else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
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

def checkhandfaction(faction,deck,player):
	mute()
	for card in deck:
		if card.controller == player and card.Faction == faction:
			return True

def checkcost(cost):
	mute()
	for card in table:
		if int(card.cost) <= cost:
			return True

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

def checkcardstatus(deck = table,faction = "",cardtype = "",cardstr = -1,stand = -1,unique = "",cost = -1,player = "",traits = "",mil = "",intcard = "",powcard = "",highlight = "",model = ""):
	mute()
	for card in deck:
		if card.type not in ("Internal"):
			if checkcardunique(card,unique) and checkcardstand(card,stand) and checkcardstr(card,cardstr) and checkcardcost(card,cost) and checkcardtype(card,cardtype) and checkcardfaction(card,faction) and checkcardplayer(card,player) and checkcardtraits(card,traits) and checkcardmil(card,mil) and checkcardint(card,intcard) and checkcardpow(card,powcard) and checkcardhl(card,highlight):
				return True

def checkcardid(deck = table,faction = "",cardtype = "",cardstr = -1,stand = -1,unique = "",cost = -1,player = "",traits = "",mil = "",intcard = "",powcard = "",highlight = ""):
	mute()
	listid = []
	for card in deck:
		if card.type not in ("Internal"):
			if checkcardunique(card,unique) and checkcardstand(card,stand) and checkcardstr(card,cardstr) and checkcardcost(card,cost) and checkcardtype(card,cardtype) and checkcardfaction(card,faction) and checkcardplayer(card,player) and checkcardtraits(card,traits) and checkcardmil(card,mil) and checkcardint(card,intcard) and checkcardpow(card,powcard) and checkcardhl(card,highlight) and card.filter != WaitColor:
				listid.append(card._id)
	return listid

def checkcardunique(card,unique):
	mute()
	if unique != "" and card.unique == unique:return True
	if unique == "":return True

def checkcardstand(card,stand):
	mute()
	if stand != -1 and card.orientation == stand:return True
	if stand == -1:return True

def checkcardstr(card,cardstr):
	mute()
	if cardstr != -1 and card.type == "Character":
		if int(card.strength) <= cardstr:return True
	if cardstr == -1:return True

def checkcardcost(card,cost):
	mute()
	if cost != -1 and card.type not in ("Internal","Faction","Agenda"):
		if int(card.cost) <= cost:return True
	if cost == -1:return True

def checkcardtype(card,cardtype):
	mute()
	if cardtype != "" and card.type in cardtype:return True
	if cardtype == "":return True

def checkcardfaction(card,faction):
	mute()
	if faction != "" and faction == card.faction:return True
	if faction == "":return True

def checkcardplayer(card,player):
	mute()
	if player != "" and card.controller == player:return True
	if player == "":return True

def checkcardtraits(card,traits):
	mute()
	if traits != "" and traits in card.traits:return True
	if traits == "":return True

def checkcardmil(card,mil):
	mute()
	if mil != "" and card.Military == mil:return True
	if mil == "":return True

def checkcardint(card,intcard):
	mute()
	if intcard != "" and card.Intrigue == intcard:return True
	if intcard == "":return True

def checkcardpow(card,powcard):
	mute()
	if powcard != "" and card.Power == powcard:return True
	if powcard == "":return True

def checkcardhl(card,highlight):
	mute()
	if highlight != "" and card.highlight in highlight:return True
	if highlight == "":return True


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

def actiongeneral(count):
	mute()
	global actionattach
	for card in me.hand:
		for d in generalaction:
			if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "Hand":
				if generalaction[d][2] == "addlan" and checkcardstatus(deck = me.hand,player = me,cardtype = "Character"):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "loseicon" and checkcardstatus(cardtype = "Character",cardstr = 4):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standtc" and checkcardstatus(unique = "Yes",faction = "Targaryen.",player = me,stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "5t3b" and len(me.deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1

	for card in table:
		for d in generalaction:
			if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "table":
				if card.type == "Character" and check511():continue
				if generalaction[d][2] == "add5returnme" and checkcardstatus(deck = me.hand,cost = 5):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "1goldicon":
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "d1cg1g" and len(me.hand) > 1:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standlocation" and checkcardstatus(cardtype = "Location",stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "2gstandc" and checkcardstatus(cardtype = "Character",stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standlady" and checkcardstatus(traits = "Lady.",stand = 1):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "kneelfaction" and checkcardstatus(cardtype = "Faction",stand = 0):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "standicon" and card.markers[standIcon] == 1:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if generalaction[d][2] == "manual":
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1


	debug(actionattach)
	if len(actionattach) > 0:setGlobalVariable("generalaction", "1")
	if count == 1:remoteCall(players[1], "actiongeneral", [2])
	if count == 2:
		debug(getGlobalVariable("generalaction"))
		if getGlobalVariable("generalaction") == "1":
			setGlobalVariable("generalaction", "2")
			if fplay(1) == me:action("general",1)
			else:remoteCall(otherplayer, "action", ["general",1])
		else:
			clearaction(1)


def action(actioninsert,actioncount):
	mute()
	debug(actioninsert)
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
				if choice in (2,0):
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
	if actioninsert == "general":
		debug(sessionpass)
		debug(checkactionattach("generalaction"))
		if len(checkactionattach("generalaction")) > 0 or sessionpass == "actionok":
			if sessionpass == "":
				intoaction(actionattach,actioncount,"general")
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
						remoteCall(players[1], "action", ["general",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"generalaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["general",actioncount])
			return
	if actioninsert == "dominance":
		debug(sessionpass)
		debug(checkactionattach("dominance"))
		if len(checkactionattach("dominance")) > 0 or sessionpass == "actionok":
			if sessionpass == "":
				intoaction(actionattach,actioncount,"dominance")
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
						remoteCall(players[1], "action", ["dominance",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"dominanceaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["dominance",actioncount])
			return
	if actioninsert == "standing":
		debug(sessionpass)
		debug(checkactionattach("standing"))
		if len(checkactionattach("standing")) > 0 or sessionpass == "actionok":
			if sessionpass == "":
				intoaction(actionattach,actioncount,"standing")
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
						remoteCall(players[1], "action", ["standing",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"standingaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["standing",actioncount])
			return
	if actioninsert == "taxation":
		debug(sessionpass)
		debug(checkactionattach("taxation"))
		if len(checkactionattach("taxation")) > 0 or sessionpass == "actionok":
			if sessionpass == "":
				intoaction(actionattach,actioncount,"taxation")
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
						remoteCall(players[1], "action", ["taxation",actioncount])
					return
				else:
					setGlobalVariable("actioncancel", "0")
					actioncard = actioncards[0]
					sessionpass = ""
					remoteCall(players[1], "checkaction", [actioncard,"taxationaction"])
		else:
			if actioncount == 2:
				notify("action over")
				clearaction(1)
			else:
				actioncount += 1
				remoteCall(players[1], "action", ["taxation",actioncount])
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
	global recount
	sessionpass = ""
	targetTuple = [d for d in checkactionattach(sepass)]
	selectcardnext(targetTuple,sepass,table,[],me,1)
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
	global addiconmil_turn
	global addiconint_turn
	global addiconpow_turn
	global subiconmil_turn
	global subiconint_turn
	global subiconpow_turn
	global returntohand_turn
	global disc_turn
	sessionpass = ""
	c = 0
	f = 0
	debug(actionattach)
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
	if repass in ("generalaction","dominanceaction"):
		for d in generalaction:
			if card.model == generalaction[d][1] and card.controller == me:
				if generalaction[d][2] == "addlan":
					cardintable(cardtoaction,"Character")
					notify("{}'s {} action put {} into play".format(me,card,cardtoaction))#HearMeRoar
					disc_turn.append(cardtoaction)
				if generalaction[d][2] == "add5returnme":
					uniquecards = []
					dc = 0
					for u in table:
						if u.controller == me and u.unique == "Yes" and u.filter != WaitColor and u._id != cardtoaction._id:
							uniquecards.append(u.name)
							if cardtoaction.name in uniquecards: 
								cost=0
								dc = 1   #Duplicates
								x,y = u.position
								break
					if dc == 1:
						if me.isInverted: 
							cardtoaction.moveToTable(x-8,y-8)
						else:
							cardtoaction.moveToTable(x+8,y+8)
						cardtoaction.filter = "#005c3521"
						cardtoaction.sendToBack()
						notify("{}'s {} action put {}'s duplicate into play".format(me,card,cardtoaction))#ArianneMartell
					else:
						cardintable(cardtoaction,"Character")
						card.moveTo(me.hand)
						notify("{}'s {} action put {} into play,{} return {}'s Hand".format(me,card,cardtoaction,card,me))#ArianneMartell
				if generalaction[d][2] == "1goldicon":
					choiceList = ['Military', 'Intrigue', 'Power']
					colorList = ['#ae0603' ,'#006b34','#1a4d8f']
					choice = askChoice("Which challenge do you want select?", choiceList,colorList)
					if choice == 0:
						actionforability(card,repass)
						return
					if choice == 1:
						cardmarkers(card,"milicon",1)
						addiconmil_turn.append(card)
						notify("{}'s {} action get a Military icon until the end of the phase.".format(me,card))#EdricDayne
					if choice == 2:
						cardmarkers(card,"inticon",1)
						addiconint_turn.append(card)
						notify("{}'s {} action get a Intrigue icon until the end of the phase.".format(me,card))#EdricDayne
					if choice == 3:
						cardmarkers(card,"powicon",1)
						addiconpow_turn.append(card)
						notify("{}'s {} action get a Power icon until the end of the phase.".format(me,card))#EdricDayne
				if generalaction[d][2] == "loseicon":
					cardmarkers(cardtoaction,"milicon",-1)
					cardmarkers(cardtoaction,"inticon",-1)
					cardmarkers(cardtoaction,"powicon",-1)
					subiconmil_turn.append(cardtoaction)
					subiconint_turn.append(cardtoaction)
					subiconpow_turn.append(cardtoaction)
					notify("{}'s {} action {} loses a [MIL], an [INT] and a [POW] icon.".format(me,card,cardtoaction))#Confinement
				if generalaction[d][2] == "d1cg1g":
					me.counters['Gold'].value += 1
					for incomecard in table:
						if incomecard.controller == me and incomecard.type == "Plot" and incomecard.filter == None:
							incomecard.markers[Gold] += 1
					notify("{}'s {} action gain 1 gold.".format(me,card))#OldForestHunter
				if generalaction[d][2] == "standlocation":
					cardtoaction.orientation = 0
					card.moveTo(me.piles['Dead pile'])
					notify("{}'s {} action Sacrifice {} to stand {}.".format(me,card,card,cardtoaction))#VeteranBuilder
				if generalaction[d][2] == "2gstandc":
					card.arrow(cardtoaction,False)
					cardtoaction.orientation = 0
					notify("{}'s {} action pay 2 gold to stand {}.".format(me,card,cardtoaction))#MagisterIllyrio
				if generalaction[d][2] == "standlady":
					cardtoaction.orientation = 0
					card.moveTo(me.piles['Dead pile'])
					notify("{}'s {} action Sacrifice {} to stand {}.".format(me,card,card,cardtoaction))#Handmaiden
				if generalaction[d][2] == "standtc":
					cardtoaction.orientation = 0
					notify("{}'s {} action to stand {}.".format(me,card,cardtoaction))#WakingtheDragon
					returntohand_turn.append(cardtoaction)
				if generalaction[d][2] == "5t3b":
					colorList = ['#1a4d8f','#ae0603']
					choiceList = ['{}'.format(me),'{}'.format(players[1])]
					choice = askChoice("select {}'s target.".format(card.name), choiceList,colorList)
					if choice == 0:
						actionforability(card,repass)
						return
					if choice == 1:
						if len(me.deck) >= 5:top5list = me.deck.top(5)
						else:top5list = me.deck.top(len(me.deck))
					if choice == 2:
						if len(players[1].deck) >= 5:top5list = players[1].deck.top(5)
						else:top5list = players[1].deck.top(len(players[1].deck))
					dlg = cardDlg(top5list, [])
					dlg.title = "These cards are you can moved"
					dlg.text = "place up to 3 of those cards on the bottom of that deck, and the others on top, in any order. click close button if none or cancel."
					dlg.label = "Top of the deck"
					dlg.bottomLabel = "bottom of the deck"
					dlg.min = 2
					dlg.max = 5
					cardmove = dlg.show()
					if cardmove != None:
						dlg.list.reverse()
						if choice == 1:
							remoteCall(me, "movedeckbottom", [dlg.bottomList])
							remoteCall(me, "movedeckbottom", [dlg.list])
							notify("{}'s {} action reorder {}'deck.".format(me,card,me))#TheBearandtheMaidenFair
						if choice == 2:
							remoteCall(otherplayer, "movedeckbottom", [dlg.bottomList])
							remoteCall(otherplayer, "movedecktop", [dlg.list])
							notify("{}'s {} action reorder {}'deck.".format(me,card,players[1]))#TheBearandtheMaidenFair
					else:notify("{}'s {} action cancel.".format(me,card))#TheBearandtheMaidenFair
				if generalaction[d][2] == "kneelfaction":
					for cardk in table:
						if cardk.type == "Faction" and cardk.controller == me:
							cardtoaction = cardk
					me.setGlobalVariable("reduceloyal_turn", "1")
					notify("{}'s {} action kneel {} to reduce the cost of the next loyal card marshal or play this phase by 1.".format(me,card,cardtoaction))#Fealty
				if generalaction[d][2] == "standicon":
					cardtoaction.orientation = 0
					card.markers[standIcon] = 0
					notify("{}'s {} action to stand {}.".format(me,card,cardtoaction))#PowerBehindtheThrone
				cardtoaction == []
				if not actioncardlimit.has_key(card._id):
					actioncardlimit[card._id] = 1
				else:actioncardlimit[card._id] += 1
				if actioncardlimit[card._id] == generalaction[d][4]:
					debug(actionattach)
					del actionattach[card._id]
					c = 1
		for d in dominanceaction:
			if card.model == dominanceaction[d][1] and card.controller == me:
				if dominanceaction[d][2] == "returndraw1":
					notify("{}'s {} action draw 1 card".format(me,card))#MessengerRaven
					card.moveTo(me.hand)
					draw(me.deck)
		if c == 0:
			actionattach[card._id] -= 1
			if actionattach[card._id] == 0:del actionattach[card._id]
		debug(repass)
		if repass == "generalaction":remoteCall(otherplayer, "action", ["general",1])
		if repass == "dominanceaction":remoteCall(otherplayer, "action", ["dominance",1])
		
def handview(vs):
	mute()
	me.hand.visibility = vs

def movedeckbottom(cardlist):
	mute()
	for card in cardlist:
		card.moveToBottom(me.Deck)

def movedecktop(cardlist):
	mute()
	for card in cardlist:
		card.moveTo(me.Deck)

def nextselectcard(selectlist,spass,deck = table,):
	mute()
	global sessionpass
	for card in deck:
		card.target(False)
	targetTuple = (selectlist, me._id)
	setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", "1")
	sessionpass = spass
	notify("**{} into selectmode**".format(me))
	return

def selectcardnext(selectlist,spass,deck = table,actioncard = [],player = "",button = 0,mode = 1):
	mute()
	global sessionpass
	global cardtmp
	attach = eval(getGlobalVariable("attachmodify"))
	for card in table:
		if player == "":
			if card.filter in (targetcardcolor,cantselectcardclor):card.filter = None
		else:
			if card.filter in (targetcardcolor,cantselectcardclor) and card.controller == player:card.filter = None
	for card in me.hand:
		if card.filter in (targetcardcolor,cantselectcardclor) and card.controller == player:card.filter = None

	if actioncard != []:
		cardtmp = actioncard
		cardtmp.filter = sourcecardcfilter
	else:cardtmp = []
	
	targetTuple = (selectlist, me._id)
	debug(selectlist)
	if me.getGlobalVariable("setupOk") in ("4","5") or me.getGlobalVariable("plotOk") == "ok" or me.getGlobalVariable("drawOk") == "ok":me.setGlobalVariable("tableTargets", str(targetTuple))
	else:setGlobalVariable("tableTargets", str(targetTuple))
	setGlobalVariable("selectmode", str(mode))
	sessionpass = spass
	for card in table:
		if card.type not in ("Internal"):
			if card._id not in targetTuple[0] and not attach.has_key(card._id):
				if player != "":
					if card.controller == player:
						if actioncard != []:
							if card._id != actioncard._id:card.filter = cantselectcardfilter
						else:card.filter = cantselectcardfilter
				else:
					if actioncard != []:
						if card._id != actioncard._id:card.filter = cantselectcardfilter
					else:card.filter = cantselectcardfilter
	for card in me.hand:
		if card._id not in targetTuple[0]:
			if actioncard != []:
				if card._id != actioncard._id:card.filter = cantselectcardfilter
			else:card.filter = cantselectcardfilter
	if button == 1:
		if me.isInverted:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,-250)
		else:table.create("584a37d7-5a30-4018-ae21-0ad325203fa0",-375,200)
	notify("**{} into selectmode**".format(me))
	return

def clearfilter(player = ""):
	mute()
	for card in table:
		if player == "":
			if card.filter in (targetcardcolor,cantselectcardclor,sourcecardcolor):card.filter = None
		else:
			if card.filter in (targetcardcolor,cantselectcardclor,sourcecardcolor) and card.controller == player:card.filter = None
	for card in me.hand:
		if card.filter in (targetcardcolor,cantselectcardclor,sourcecardcolor):card.filter = None

def cardmarkers(card,marker,add):
	mute()
	if marker == "milicon":
		addmodify = card.markers[MilitaryIcon] - card.markers[subMilitaryIcon] + add
		debug(addmodify)
		if addmodify > 0:card.markers[MilitaryIcon] = addmodify
		if addmodify < 0:card.markers[subMilitaryIcon] = abs(addmodify)
		if addmodify == 0:
			card.markers[MilitaryIcon] = 0
			card.markers[subMilitaryIcon] = 0
	if marker == "inticon":
		addmodify = card.markers[IntrigueIcon] - card.markers[subIntrigueIcon] + add
		debug(addmodify)
		if addmodify > 0:card.markers[IntrigueIcon] = addmodify
		if addmodify < 0:card.markers[subIntrigueIcon] = abs(addmodify)
		if addmodify == 0:
			card.markers[IntrigueIcon] = 0
			card.markers[subIntrigueIcon] = 0
	if marker == "powicon":
		addmodify = card.markers[PowerIcon] - card.markers[subPowerIcon] + add
		debug(addmodify)
		if addmodify > 0:card.markers[PowerIcon] = addmodify
		if addmodify < 0:card.markers[subPowerIcon] = abs(addmodify)
		if addmodify == 0:
			card.markers[PowerIcon] = 0
			card.markers[subPowerIcon] = 0

def checkchallengeicon(card,marker):
	mute()
	c = 0
	if marker == "milicon":
		if card.Military == "Yes":c = 1
		if card.markers[MilitaryIcon] - card.markers[subMilitaryIcon] + c > 0:return True
	if marker == "inticon":
		if card.Intrigue == "Yes":c = 1
		if card.markers[IntrigueIcon] - card.markers[subIntrigueIcon] + c > 0:return True
	if marker == "powicon":
		if card.Power == "Yes":c = 1
		if card.markers[PowerIcon] - card.markers[subPowerIcon] + c > 0:return True

def callplotleave(count):
	mute()
	plotleave(selectedcard,count)

def checkwinner(args):
	mute()
	if args.marker == "Power":
		i = 0 
		for card in table:
			if card.controller == me:
				i+=card.markers[Power]
		if i>=15:
			choiceList = ['You Win']
			colorList = ['#006b34']
			choice = askChoice("Game over", choiceList,colorList)

def checkactionattach(checkpass):
	mute()
	global actionattach
	actionattach = {}
	actiongeneral(3)
	if checkpass == "dominance":
		actiondominance(3)
	if checkpass == "standing":
		actionstanding(3)
	if checkpass == "taxation":
		actionstanding(3)
	actionattachtmp = actionattach.copy()
	debug("tmp")
	debug(actionattachtmp)
	for card in table:
		if card._id in actionattachtmp:
			for d in generalaction:
				if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "table":
					if "gold" in generalaction[d][5]:
						debug(generalaction[d][5][4])
						if me.counters['Gold'].value < int(generalaction[d][5][4]):
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == generalaction[d][4]:
							del actionattachtmp[card._id]
	for card in table:
		if card._id in actionattachtmp:
			for d in dominanceaction:
				if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "table":
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == dominanceaction[d][4]:
							del actionattachtmp[card._id]
	for card in me.hand:
		if card._id in actionattachtmp:
			for d in generalaction:
				if card.model == generalaction[d][1] and card.controller == me and generalaction[d][3] == "Hand":
					if card.type == "Event" and card.cost != "X":
						cost=int(card.Cost)
						if me.getGlobalVariable("firstevent") == "0":
							if checkpr(me) and card.type == "Event":
								cost=int(card.Cost)-1
						if card.loyal == "Yes":
							cost -= int(me.getGlobalVariable("reduceloyal_turn"))
						if me.counters['Gold'].value < cost:
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == generalaction[d][4]:
							del actionattachtmp[card._id]
	for card in me.hand:
		if card._id in actionattachtmp:
			for d in dominanceaction:
				if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "Hand":
					if card.type == "Event" and card.cost != "X":
						cost=int(card.Cost)
						if me.getGlobalVariable("firstevent") == "0":
							if checkpr(me) and card.type == "Event":
								cost=int(card.Cost)-1
						if card.loyal == "Yes":
							cost -= int(me.getGlobalVariable("reduceloyal_turn"))
						if me.counters['Gold'].value < cost:
							actionattachtmp[card._id] -= 1
							if actionattachtmp[card._id] == 0:del actionattachtmp[card._id]
					if actioncardlimit.has_key(card._id) and actionattachtmp.has_key(card._id):
						if actioncardlimit[card._id] == dominanceaction[d][4]:
							del actionattachtmp[card._id]
	debug(actionattachtmp)
	return actionattachtmp

def check511():
	mute()
	for card in table:
		if card.type == "Plot" and card.filter == None and card.model == "79877d2a-5b23-4c16-86df-9453c065835b":
			return True

def manualprocess(card,propass):
	mute()
	global manualpropass
	global manualcard
	
	manualcard = card
	manualpropass = propass
	if me.isInverted:table.create("90942683-91d6-414c-832d-5f6f0e495995",-375,-250)
	else:table.create("90942683-91d6-414c-832d-5f6f0e495995",-375,200)

def resumeprocess():
	mute()
	global manualpropass
	global manualcard
	global sessionpass
	sessionpass = ""
	c = 0
	for cardn in table:
		if cardn.name == "manualbutton" and cardn.controller == me:
			cardn.delete()
	if manualpropass == "plotability":
		manualpropass = ""
		manualcard = []
		if getGlobalVariable("reavelplot") == "1":
			setGlobalVariable("reavelplot","2")
			remoteCall(players[1], "reavelplot", table)
			return
		if getGlobalVariable("reavelplot") == "2":
			resetplot()
			remoteCall(players[1], "resetplot", [])
			if fplay(1) == me:actiongeneral(1)
			else:remoteCall(players[1], "actiongeneral", 1)
			return
	if manualpropass == "generalaction":
		for d in generalaction:
			if manualcard.model == generalaction[d][1] and manualcard.controller == me:
				if not actioncardlimit.has_key(manualcard._id):
					actioncardlimit[manualcard._id] = 1
				else:actioncardlimit[manualcard._id] += 1
				if actioncardlimit[manualcard._id] == generalaction[d][4]:
					debug(actionattach)
					del actionattach[manualcard._id]
					c = 1
		if c == 0:
			actionattach[manualcard._id] -= 1
			if actionattach[manualcard._id] == 0:del actionattach[manualcard._id]
		manualcard = []
		remoteCall(players[1], "action", ["general",1])
	if manualpropass == "dominanceend":
		for d in dominanceend:
			if manualcard.model == dominanceend[d][1] and manualcard.controller == me:
				if not reactioncardlimit.has_key(manualcard._id):
					reactioncardlimit[manualcard._id] = 1
				else:reactioncardlimit[manualcard._id] += 1
				if reactioncardlimit[manualcard._id] == dominanceend[d][4]:
					debug(reactionattach)
					del reactionattach[manualcard._id]
					c = 1
		if c == 0:
			reactionattach[manualcard._id] -= 1
			if reactionattach[manualcard._id] == 0:del reactionattach[manualcard._id]
		manualcard = []
		remoteCall(players[1], "reaction", ["dominanceend",1])
	if manualpropass == "dominance":
		for d in dominanceaction:
			if manualcard.model == dominanceaction[d][1] and manualcard.controller == me:
				if not actioncardlimit.has_key(manualcard._id):
					actioncardlimit[manualcard._id] = 1
				else:actioncardlimit[manualcard._id] += 1
				if actioncardlimit[manualcard._id] == dominanceaction[d][4]:
					debug(actionattach)
					del actionattach[manualcard._id]
					c = 1
		if c == 0:
			actionattach[manualcard._id] -= 1
			if actionattach[manualcard._id] == 0:del actionattach[manualcard._id]
		if manualcard.type == "Event":disc(manualcard)
		manualcard = []
		remoteCall(players[1], "action", ["dominance",1])

def dominancephasestart(count):
	mute()
	if me.isInverted:table.create("bd153c97-1108-4e65-bd46-88852ec7d5bc",-375,-250)
	else:table.create("bd153c97-1108-4e65-bd46-88852ec7d5bc",-375,200)
	if count == 1:remoteCall(players[1], "dominancephasestart", [2])

def dominancenext():
	mute()
	for cardn in table:
		if cardn.name == "dominancenextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("dominancephase") == "0":
		setGlobalVariable("dominancephase", "1")
		return
	if getGlobalVariable("dominancephase") == "1":
		if fplay(1) == me:dominancestartreaction(1)
		else: remoteCall(players[1], "dominancestartreaction", [1])

def dominancestartreaction(count):
	mute()
	global reactionattach
	for card in table:
		for d in dominancestart:
			if card.model == dominancestart[d][1] and card.controller == me and dominancestart[d][3] == "table":
				if dominancestart[d][2] == "stand" and card.orientation == 1:
					if not reactionattach.has_key(card._id):
						reactionattach[card._id] = 1
					else:reactionattach[card._id] += 1
					

	if len(reactionattach) > 0:setGlobalVariable("dominancestart", "1")
	if count == 1:remoteCall(players[1], "dominancestartreaction", [2])
	else:
		if getGlobalVariable("dominancestart") == "1":
			setGlobalVariable("dominancestart", "2")
			if fplay(1) == me:reaction("dominancestart",1)
			else: remoteCall(players[1], "reaction", ["dominancestart",1])
		else:
			if fplay(1) == me:dominance(table)
			else: remoteCall(players[1], "dominance", [table])

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
		setGlobalVariable("dominancewinplayer",players[winner]._id)
		for housecard in table:
			if housecard.type == "Faction" and housecard.controller == players[winner]:
				addPower(housecard)
	if fplay(1) == me:dominancewinreaction(1)
	else:remoteCall(players[1], "dominancewinreaction", [1])

def dominancewinreaction(count):
	mute()
	global reactionattach
	for card in table:
		for d in dominancewin:
			if card.model == dominancewin[d][1] and card.controller == me and dominancewin[d][3] == "table":
				if getGlobalVariable("dominancewinplayer") == str(me._id):
					if dominancewin[d][2] == "2power":
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1
					if dominancewin[d][2] == "move1pow" and checkhousepow(players[1]) > 0:
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1
					if dominancewin[d][2] == "returniron" and checkcardstatus(deck = me.piles['Dead pile'],traits = "Ironborn"):
						if not reactionattach.has_key(card._id):
							reactionattach[card._id] = 1
						else:reactionattach[card._id] += 1

	if len(reactionattach) > 0:setGlobalVariable("dominancewin", "1")
	if count == 1:remoteCall(players[1], "dominancewinreaction", [2])
	else:
		if getGlobalVariable("dominancewin") == "1":
			setGlobalVariable("dominancewin", "2")
			if fplay(1) == me:reaction("dominancewin",1)
			else: remoteCall(players[1], "reaction", ["dominancewin",1])
		else:
			if fplay(1) == me:actiondominance(1)
			else: remoteCall(players[1], "actiondominance", [1])

def dominanceendreaction(count):
	mute()
	global reactionattach
	for card in table:
		for d in dominanceend:
			if card.model == dominanceend[d][1] and card.controller == me and dominanceend[d][3] == "table":
				if dominanceend[d][2] == "cleartable":
					if not reactionattach.has_key(card._id):
						reactionattach[card._id] = 1
					else:reactionattach[card._id] += 1

	if len(reactionattach) > 0:setGlobalVariable("dominanceend", "1")
	if count == 1:remoteCall(players[1], "dominanceendreaction", [2])
	else:
		if getGlobalVariable("dominanceend") == "1":
			setGlobalVariable("dominanceend", "2")
			if fplay(1) == me:reaction("dominanceend",1)
			else: remoteCall(players[1], "reaction", ["dominanceend",1])
		else:
			dominancephaseend(table)
			remoteCall(players[1], "dominancephaseend", [table])

def dominancephaseend(group, x=0, y=0):
	mute()
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,-250)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,200)

def actiondominance(count):
	mute()
	if count < 3:actiongeneral(3)
	global actionattach
	for card in me.hand:
		for d in dominanceaction:
			if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "Hand":
				if dominanceaction[d][2] == "controll6" and checkcardstatus(deck = table,player = players[1],cardtype = "Character",cost = 6,unique = "No"):
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1

	for card in table:
		for d in dominanceaction:
			if card.model == dominanceaction[d][1] and card.controller == me and dominanceaction[d][3] == "table":
				if card.type == "Character" and check511():continue
				if dominanceaction[d][2] == "returndraw1" and len(me.deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1
				if dominanceaction[d][2] == "disctop" and len(players[1].deck) > 0:
					if not actionattach.has_key(card._id):
						actionattach[card._id] = 1
					else:actionattach[card._id] += 1



	debug(actionattach)
	if len(actionattach) > 0 and count < 3:setGlobalVariable("dominanceaction", "1")
	debug("dominanceaction1")
	debug(getGlobalVariable("dominanceaction"))
	if count == 1:remoteCall(players[1], "actiondominance", [2])
	if count == 2:

		if getGlobalVariable("dominanceaction") == "1":
			setGlobalVariable("dominanceaction", "2")
			debug("dominanceaction")
			debug(getGlobalVariable("dominanceaction"))
			if fplay(1) == me:action("dominance",1)
			else:remoteCall(otherplayer, "action", ["dominance",1])
		else:
			if fplay(1) == me:dominanceendreaction(1)
			else: remoteCall(players[1], "dominanceendreaction", [1])

def standingphasestart(count):
	mute()
	if me.isInverted:table.create("4d8aa7b0-f5ef-4584-be8c-601c45579dc6",-375,-250)
	else:table.create("4d8aa7b0-f5ef-4584-be8c-601c45579dc6",-375,200)
	if count == 1:remoteCall(players[1], "standingphasestart", [2])

def standingnext():
	mute()
	for cardn in table:
		if cardn.name == "standingnextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("standingphase") == "0":
		setGlobalVariable("standingphase", "1")
		return
	if getGlobalVariable("standingphase") == "1":
		if fplay(1) == me:standingstartreaction(1)
		else: remoteCall(players[1], "standingstartreaction", [1])

def standingstartreaction(count):
	mute()
	global reactionattach

					

	if len(reactionattach) > 0:setGlobalVariable("standingstart", "1")
	if count == 1:remoteCall(players[1], "standingstartreaction", [2])
	else:
		if getGlobalVariable("standingstart") == "1":
			setGlobalVariable("standingstart", "2")
			if fplay(1) == me:reaction("standingstart",1)
			else: remoteCall(players[1], "reaction", ["standingstart",1])
		else:
			if fplay(1) == me:standingphase(table)
			else:remoteCall(players[1], "standingphase", [table])

def standingphase(group, x=0, y=0):
	mute()
	if checkstannis():
		if fplay(1) == me:standcharacter("stand1")
		else:remoteCall(players[1], "standcharacter", ["stand1"])
	else:standingcard(1)

def standingcard(count):
	mute()
	myCards = (card for card in table  #restore all cards
		if card.controller == me)
	for card in myCards:
		if card.isFaceUp:
			card.orientation &= ~Rot90
			card.highlight = None
			card.target(False)
	if count == 1:remoteCall(players[1], "standingcard", [2])
	if count == 2:
		if fplay(1) == me:standingoverreaction(1)
		else:remoteCall(players[1], "standingoverreaction", [1])

def standcharacter(typep):
	mute()
	if typep == "stand1":
		if checkcardstatus(cardtype = "Character",stand = 1,player = me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me,stand = 1)
			selectcardnext(selectlist,"standcharacter1",table,[],me,1,2)
		else:remoteCall(players[1], "standcharacter", ["stand2"])
	if typep == "stand2":
		if checkcardstatus(cardtype = "Character",stand = 1,player = me):
			selectlist = checkcardid(deck = table,cardtype = "Character",player = me,stand = 1)
			selectcardnext(selectlist,"standcharacter2",table,[],me,1,2)

def standcharacterend(count):
	mute()
	for card in table:
		if card.filter == standcolor and card.controller == me:
			card.filter = None
			card.orientation = 0
	if count == 1:remoteCall(players[1], "standcharacterend", [2])
	if count == 2:
		if fplay(1) == me:standingoverreaction(1)
		else:remoteCall(players[1], "standingoverreaction", [1])

def checkstannis():
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	debug(attach)
	e = 0
	if not check511():
		for card in table:
			if card.model == "dfc85d0c-12a5-45b3-803a-98982c36d083":
				if checkcardattach(card):
					for d in attach:
						if attach[d] == card._id:
							debug(d)
							for cardatta in table:
								if cardatta._id == d:
									debug(cardatta.model)
									if cardatta.model != "a8bebc54-d01c-424d-8839-460ec09b733f":e = 1
				else:e = 1
	if e == 1:return True

def checkcardattach(card):
	mute()
	attach = eval(getGlobalVariable("attachmodify"))
	c = 0
	for card in table:
		for d in attach:
			if card._id == d:
				c = 1
				return True

def standingoverreaction(count):
	mute()
	global reactionattach

					

	if len(reactionattach) > 0:setGlobalVariable("standingover", "1")
	if count == 1:remoteCall(players[1], "standingoverreaction", [2])
	else:
		if getGlobalVariable("standingover") == "1":
			setGlobalVariable("standingover", "2")
			if fplay(1) == me:reaction("standingover",1)
			else: remoteCall(players[1], "reaction", ["standingover",1])
		else:
			if fplay(1) == me:actionstanding(1)
			else: remoteCall(players[1], "actionstanding", [1])

def actionstanding(count):
	mute()
	if count < 3:actiongeneral(3)

	debug(actionattach)
	if len(actionattach) > 0 and count < 3:setGlobalVariable("standingaction", "1")
	if count == 1:remoteCall(players[1], "actionstanding", [2])
	if count == 2:
		if getGlobalVariable("standingaction") == "1":
			setGlobalVariable("standingaction", "2")
			if fplay(1) == me:action("standing",1)
			else:remoteCall(otherplayer, "action", ["standing",1])
		else:
			if fplay(1) == me:standingendreaction(1)
			else: remoteCall(players[1], "standingendreaction", [1])


def standingendreaction(count):
	mute()
	global reactionattach
	
	if len(reactionattach) > 0:setGlobalVariable("standingend", "1")
	if count == 1:remoteCall(players[1], "standingendreaction", [2])
	else:
		if getGlobalVariable("standingend") == "1":
			setGlobalVariable("standingend", "2")
			if fplay(1) == me:reaction("standingend",1)
			else: remoteCall(players[1], "reaction", ["standingend",1])
		else:
			standingphaseend(table)
			remoteCall(players[1], "standingphaseend", [table])
			

def standingphaseend(group, x=0, y=0):
	mute()
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,-250)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,200)

def taxationphasestart(count):
	mute()
	if me.isInverted:table.create("c38f6f47-54dc-4853-8000-ff2da81370ee",-375,-250)
	else:table.create("c38f6f47-54dc-4853-8000-ff2da81370ee",-375,200)
	if count == 1:remoteCall(players[1], "taxationphasestart", [2])

def taxationnext():
	mute()
	for cardn in table:
		if cardn.name == "taxationnextbutton" and cardn.controller == me:
			cardn.delete()
	if getGlobalVariable("taxationphase") == "0":
		setGlobalVariable("taxationphase", "1")
		return
	if getGlobalVariable("taxationphase") == "1":
		if fplay(1) == me:taxationstartreaction(1)
		else: remoteCall(players[1], "taxationstartreaction", [1])

def taxationstartreaction(count):
	mute()
	global reactionattach

					
	if len(reactionattach) > 0:setGlobalVariable("taxationstart", "1")
	if count == 1:remoteCall(players[1], "taxationstartreaction", [2])
	else:
		if getGlobalVariable("taxationstart") == "1":
			setGlobalVariable("taxationstart", "2")
			if fplay(1) == me:reaction("taxationstart",1)
			else: remoteCall(players[1], "reaction", ["taxationstart",1])
		else:
			if fplay(1) == me:taxreturngold(1)
			else:remoteCall(players[1], "taxreturngold", [1])

def taxreturngold(count):
	mute()
	me.counters['Gold'].value = 0  #reset gold counters
	goldcard = (card for card in table
			if card.controller == me)
	for card in goldcard: 
		card.markers[Gold] = 0
	if count == 1:remoteCall(players[1], "taxreturngold", [2])
	if count == 2:
		if fplay(1) == me:taxationreturnoverreaction(1)
		else:remoteCall(players[1], "taxationreturnoverreaction", [1])

def taxationreturnoverreaction(count):
	mute()
	global reactionattach

					
	if len(reactionattach) > 0:setGlobalVariable("taxationreturn", "1")
	if count == 1:remoteCall(players[1], "taxationreturnoverreaction", [2])
	else:
		if getGlobalVariable("taxationreturn") == "1":
			setGlobalVariable("taxationreturn", "2")
			if fplay(1) == me:reaction("taxationreturnover",1)
			else: remoteCall(players[1], "reaction", ["taxationreturnover",1])
		else:
			if fplay(1) == me:taxationcheckhand(1)
			else:remoteCall(players[1], "taxationcheckhand", [1])

def taxationcheckhand(count):
	mute()
	getreserve(table)
	discAmount = None
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
			if count == 1:remoteCall(players[1], "taxationcheckhand", [2])
			else:
				if fplay(1) == me:taxationrcheckhandreaction(1)
				else:remoteCall(players[1], "taxationrcheckhandreaction", [1])
		else:
			taxationcheckhand(count)
			return
	else:
		notify("Hand size is ok.")
		if count == 1:remoteCall(players[1], "taxationcheckhand", [2])
		else:
			if fplay(1) == me:taxationrcheckhandreaction(1)
			else:remoteCall(players[1], "taxationrcheckhandreaction", [1])

def taxationrcheckhandreaction(count):
	mute()
	global reactionattach

					
	if len(reactionattach) > 0:setGlobalVariable("taxationrcheckhand", "1")
	if count == 1:remoteCall(players[1], "taxationrcheckhandreaction", [2])
	else:
		if getGlobalVariable("taxationrcheckhand") == "1":
			setGlobalVariable("taxationrcheckhand", "2")
			if fplay(1) == me:reaction("taxationcheckhandover",1)
			else: remoteCall(players[1], "reaction", ["taxationcheckhandover",1])
		else:
			if fplay(1) == me:actiontaxation(1)
			else:remoteCall(players[1], "actiontaxation", [1])

def actiontaxation(count):
	mute()
	if count < 3:actiongeneral(3)

	debug(actionattach)
	if len(actionattach) > 0 and count < 3:setGlobalVariable("actiontaxation", "1")
	if count == 1:remoteCall(players[1], "actiontaxation", [2])
	if count == 2:
		if getGlobalVariable("actiontaxation") == "1":
			setGlobalVariable("actiontaxation", "2")
			if fplay(1) == me:action("taxation",1)
			else:remoteCall(otherplayer, "action", ["taxation",1])
		else:
			if fplay(1) == me:taxationendreaction(1)
			else: remoteCall(players[1], "taxationendreaction", [1])

def taxationendreaction(count):
	mute()
	global reactionattach
	
	if len(reactionattach) > 0:setGlobalVariable("taxationend", "1")
	if count == 1:remoteCall(players[1], "taxationendreaction", [2])
	else:
		if getGlobalVariable("taxationend") == "1":
			setGlobalVariable("taxationend", "2")
			if fplay(1) == me:reaction("taxationend",1)
			else: remoteCall(players[1], "reaction", ["taxationend",1])
		else:
			taxationphaseend(table)
			remoteCall(players[1], "taxationphaseend", [table])

def taxationphaseend(group, x=0, y=0):
	mute()
	if me.isInverted:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,-250)
	else:table.create("cb48782b-3bdd-4024-af85-fb0eb65a8f51",-375,200)

def startnextphase(count):
	mute()
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
	me.setGlobalVariable("inmarshal","1")
	me.setGlobalVariable("firstevent", "0")
	me.setGlobalVariable("firstcharacter", "0")
	me.setGlobalVariable("firstll", "0")#A Noble Cause
	me.setGlobalVariable("turn", "0")
	me.setGlobalVariable("firstevent", "0")	
	me.setGlobalVariable("milcount","0")
	me.setGlobalVariable("milcountmax","1")	
	me.setGlobalVariable("intcount","0")
	me.setGlobalVariable("intcountmax","1")
	me.setGlobalVariable("powcount","0")
	me.setGlobalVariable("powcountmax","1")
	me.setGlobalVariable("active","0")
	me.setGlobalVariable("reduceloyal_turn", "0")
	me.setGlobalVariable("intwin", "0")
	me.setGlobalVariable("submilclaim", "0")
	me.setGlobalVariable("subintclaim", "0")
	me.setGlobalVariable("subpowclaim", "0")
	me.setGlobalVariable("limitchallenge", "0")
	me.setGlobalVariable("cantuseevent", "0")
	me.setGlobalVariable("cantuselocation", "0")
	me.setGlobalVariable("cantuseattach", "0")
	me.setGlobalVariable("plotOk","")
	me.setGlobalVariable("drawOk","")
	me.setGlobalVariable("setupOk","")

	if count == 1:remoteCall(players[1], "startnextphase", 2)
	if count == 2:
		setGlobalVariable("tableTargets", "")
		setGlobalVariable("insertre", "")
		setGlobalVariable("cantchallenge", "0")
		setGlobalVariable("bedefend", "")
		setGlobalVariable("aftcr", "")
		setGlobalVariable("aftcu", "")
		setGlobalVariable("dominancestart", "")
		setGlobalVariable("dominancewin", "")
		setGlobalVariable("dominancewinplayer","")
		setGlobalVariable("dominanceend", "")
		setGlobalVariable("standingstart", "")
		setGlobalVariable("standingover", "")
		setGlobalVariable("standingend", "")
		setGlobalVariable("taxationstart", "")
		setGlobalVariable("taxationreturn", "")
		setGlobalVariable("taxationrcheckhand", "")
		setGlobalVariable("taxationend", "")
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
		setGlobalVariable("reavelplot","1")
		setGlobalVariable("drawphase","0")
		setGlobalVariable("marshalphase","0")
		setGlobalVariable("firstreveal", "")
		setGlobalVariable("challengephase","0")
		setGlobalVariable("dominancephase","0")
		setGlobalVariable("standingphase","0")
		setGlobalVariable("taxationphase","0")
		setGlobalVariable("action","0")
		setGlobalVariable("activeplayer","")
		setGlobalVariable("winint","0")
		setGlobalVariable("challengeplayer","0")
		setGlobalVariable("Kingdomgold0","0")
		setGlobalVariable("Edictgold0","0")
		setGlobalVariable("plotdisc","0")
		setGlobalVariable("plotkill","0")
		setGlobalVariable("generalaction", "0")
		setGlobalVariable("dominanceaction", "0")
		setGlobalVariable("standingaction", "0")
		setGlobalVariable("actiontaxation", "0")
		notify("Taxation phase over")
		notify("A new turn start")
		notify("Plot phase start")
		plotphasestart(1)

def plotphasestart(count):
	mute()
	if me.isInverted:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,-250)
	else:table.create("62bad042-fbb0-4121-85d2-92149576308b",-375,200)
	if count == 1:remoteCall(players[1], "plotphasestart", [2])

def resetperturn():
	mute()
	global addiconmil_turn
	global addiconint_turn
	global addiconpow_turn
	global subiconmil_turn
	global subiconint_turn
	global subiconpow_turn
	global returntohand_turn
	global disc_turn
	for addmil in addiconmil_turn:
		cardmarkers(addmil,"milicon",-1)
	for addint in addiconint_turn:
		cardmarkers(addint,"inticon",-1)
	for addpow in addiconpow_turn:
		cardmarkers(addpow,"powicon",-1)
	for submil in subiconmil_turn:
		cardmarkers(addmil,"milicon",1)
	for subint in subiconint_turn:
		cardmarkers(addint,"inticon",1)
	for subpow in subiconpow_turn:
		cardmarkers(addpow,"powicon",1)
	for cardreturn in returntohand_turn:
		remoteCall(cardreturn.controller,"returncard",[cardreturn])
	for carddisc in disc_turn:
		remoteCall(carddisc.controller,"disc",[carddisc])

	addiconmil_turn = []
	addiconint_turn = []
	addiconpow_turn = []
	subiconmil_turn = []
	subiconint_turn = []
	subiconpow_turn = []
	returntohand_turn = []
	disc_turn = []
	
def checkcounter(args):
	mute()
	debug(args.counter)
	if args.counter == me.counters['Gold']:
		i = 0 
		for card in table:
			if card.controller == me and card.model == "390a8cf7-8bc4-45c1-bea5-e6a694e9f2d5":card.markers[STR_Up] += me.counters['Gold'].value-args.value#Tywin Lannister