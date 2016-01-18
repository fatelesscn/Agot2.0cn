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
WaitColor = "#D8D8D8" # Grey
PlayColor = "#FFA6F7" # Yellow
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
attachmodify = {}
countusedplot = 0
Heartsbaneused = 0
countmil = 0
challengetype = 0
winplayer = []
attacker = []
defender = []
unopposed = 0
otherplayer = []
import re

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
	global otherplayer
	global challengetype
	stealth = ""
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
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = MilitaryColor
			if c.model != "a8854084-67e5-4955-89db-3d9cb1337789":
				if c.model == "09903f79-6155-4a63-9b52-e10fb2e69898":
					f = c.name+str(c.position)
					for cards in table:
						if cards.model == "99a12a9c-6e83-43bd-8947-0cc47ffcd02a":
							targetatt = cards.name+str(cards.position)
							if f == attachmodify[targetatt] and countmil != 0:
								c.orientation = 1
							else:c.orientation = 0
				elif c.model != "09903f79-6155-4a63-9b52-e10fb2e69898" :c.orientation = 1
				if re.search(r'stealth',c.keywords,re.I):   #stealth
					stealth = "0"
		notify("**{} declares MIL attackers.**".format(me))
		attacker = me
		challengetype = 1
		remoteCall(otherplayer, "getattacker", [attacker,challengetype])
		if stealth == "0":
			choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
			if choice == True:
				notify("{} is ready to use the stealth keyword.".format(me))
			else:
				notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
	else:
		whisper("You must declare at least 1 character to attack.")
	countmil += 1

def announceInt(group, x = 0, y = 0):
	mute()
	global attacker
	global otherplayer
	global challengetype
	stealth = ""
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
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
		notify("**{} declares INT attackers.**".format(me))
		attacker = me
		challengetype = 2
		remoteCall(otherplayer, "getattacker", [attacker,challengetype])
		if stealth == "0":
			choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
			if choice == True:
				notify("{} is ready to use the stealth keyword.".format(me))
			else:
				notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
	else:
		whisper("You must declare at least 1 character to attack.")

def announcePow(group, x = 0, y = 0):
	mute()
	global attacker
	global otherplayer
	global challengetype
	stealth = ""
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
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
			if re.search(r'stealth',c.keywords,re.I):   #stealth
				stealth = "0"
		notify("**{} declares POW attackers.**".format(me))
		attacker = me
		challengetype = 3
		remoteCall(otherplayer, "getattacker", [attacker,challengetype])
		if stealth == "0":
			choice = confirm("Character with the stealth keyword has been declared as an attacker, do you want to chooses its stealth target?")
			if choice == True:
				notify("{} is ready to use the stealth keyword.".format(me))
			else:
				notify("{} renounces the use of the stealth keyword.".format(me))
			stealth = "1"
	else:
		whisper("You must declare at least 1 character to attack.")

def holdOn(group, x = 0, y = 0):
	mute()
	notify("**Please wait.  {} has an action/question.**".format(me))

def announceOpp(group, x = 0, y = 0):
	mute()
	global attacker
	global challengetype
	global otherplayer
	global defender
	if attacker != []:
		notify("**{} responds: Opposed/Defend.**".format(me))
		if challengetype == 1:
			choiceList = ['Military', 'No defenders']
			colorList = ['#ae0603' ,'#D8D8D8']
			choice = askChoice("Opposed or defend?", choiceList,colorList)
			if choice == 1:
				defMil(table)
			elif choice == 2:
				notify("{} declares no defenders.".format(me))
				defender = me
				remoteCall(otherplayer, "getdefender", [me])
		if challengetype == 2:
			choiceList = ['Intrigue', 'No defenders']
			colorList = ['#006b34' ,'#D8D8D8']
			choice = askChoice("Opposed or defend?", choiceList,colorList)
			if choice == 1:
				defInt(table)
			elif choice == 2:
				notify("{} declares no defenders.".format(me))
				defender = me
				remoteCall(otherplayer, "getdefender", [me])
		if challengetype == 3:
			choiceList = ['Power', 'No defenders']
			colorList = ['#1a4d8f','#D8D8D8']
			choice = askChoice("Opposed or defend?", choiceList,colorList)
			if choice == 1:
				defPow(table)
			elif choice == 2:
				notify("{} declares no defenders.".format(me))
				defender = me
				remoteCall(otherplayer, "getdefender", [me])
		else:return
	else:notify("No challenge happened.")
		
def defMil(group, x = 0, y = 0):
	mute()
	global defender
	global otherplayer
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
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = MilitaryColor
			c.orientation = 1
		notify("**{} declares MIL defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	defender = me
	remoteCall(otherplayer, "getdefender", [defender])

def defInt(group, x = 0, y = 0):
	mute()
	global defender
	global otherplayer
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
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = IntrigueColor
			c.orientation = 1
		notify("**{} declares INT defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	defender = me
	remoteCall(otherplayer, "getdefender", [defender])

def defPow(group, x = 0, y = 0):
	mute()
	global defender
	global otherplayer
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
	if cards != None:
		for c in cards:
			c.target(True)
			c.highlight = PowerColor
			c.orientation = 1
		notify("**{} declares POW defenders.**".format(me))
	else:
		notify("{} declares no defenders.".format(me))
	defender = me
	remoteCall(otherplayer, "getdefender", [defender])
		
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
	if (card.model == "f97ccf1a-5b0d-490f-9968-78330e92171c" or card.model == "4c8a114e-106c-4460-846b-28f73914fc11") and card.orientation == 0:
		if not confirm("Do you want to use {}'s ability?".format(card.name)): return
		attach = card.name+str(card.position)
		for cards in table:
			f = cards.name+str(cards.position)
			if attachmodify != {}:
				if f == attachmodify[attach]:
					if card.model == "4c8a114e-106c-4460-846b-28f73914fc11":#just for Heartsbane
						global Heartsbaneused
						cards.markers[STR_Up] += 3
						card.orientation ^= Rot90
						Heartsbaneused = 1	
						return
					if cards.orientation != 0:
						cards.orientation ^= Rot90
						card.orientation ^= Rot90
					else:
						notify("{} is standing, you cannot stand it.".format(cards))
						return
	else:notify("{} s already knelt.".format(card))
	if card.model not in ("f97ccf1a-5b0d-490f-9968-78330e92171c" ,"4c8a114e-106c-4460-846b-28f73914fc11"):		
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
			for u in table:
				if u.name == card.name:
					if u.name not in uniquecards:
						if u.controller == me and u.unique == "Yes":
							uniquecards.append(u.name)
							for cards in table:
								if cards.name == u.name and cards.index != u.index:
									x, y = u.position
									if me.isInverted: 
										cards.moveToTable(x-8,y-8)
									else:
										cards.moveToTable(x+8,y+8)
									notify("{} plays {}'s duplicate.".format(me,card))
									card.sendToBack()
									card.filter = WaitColor

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
	for housecard in table:
		if housecard.type == "Faction" and housecard.controller == me:
			addPower(housecard)

def subhousepow(ok = 1):
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
	
	if not confirm("Are you sure you want to Mulligan?"): return
	if draw == None: draw = askInteger("How many cards would you like to draw for your Mulligan?", len(me.hand))
	if draw == None: return
	
	for card in group:
		card.moveToBottom(me.deck)
			
	me.deck.shuffle()
		
	for card in me.deck.top(draw):
		card.moveTo(me.hand)
	notify("{} mulligans and draws {} new cards.".format(me, draw))


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
	if drawAmount == None: drawAmount = askInteger("Draw how many cards?", 7)
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
	notify("{} randomly moves {} from their discard to thier hand.".format(me, card))

#---------------------------------------------------------------------------
# New actions
#---------------------------------------------------------------------------
# New Table group actions
#---------------------------------------------------------------------------
def setup(group, x = 0, y = 0):
	mute()
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
				c.moveToTable(300,-100)			
			else:
				c.moveToTable(-320,0)
		if c.Type == "Agenda":
			if me.isInverted: 
				c.moveToTable(220,-100)			
			else:
				c.moveToTable(-240,0)
	me.deck.shuffle()
	for card in me.deck.top(7):
		card.moveTo(me.hand)
	if me.isInverted: 
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",300,-200)
	else:
		table.create("656f69c4-c506-4014-932b-9dff4422f09e",-280,100)
	if confirm ("Need the quickbar?"):
		if me.isInverted: 
			table.create("342dd044-b0f7-4eef-a021-5b755397f9d4",-280,-50)
			table.create("6a34f431-c468-4d31-8d8c-51aac6a66f89",-320,-50)
			table.create("338370f8-3952-46a7-a3b9-a462a326e7bb",-360,-50)
			table.create("9936a519-785c-4058-b060-4ca0a01258ea",-280,-90)
			table.create("91e2e6b3-9929-4365-93b2-3d143a20e6ff",-280,-130)
			table.create("c237b30d-6511-4646-a93a-49b63ff4aa22",-320,-130)
			table.create("d6ac416d-0956-403f-a1bc-ed6e8c5ba4a9",-360,-130)
			table.create("dac3d665-1af7-427e-9f50-36d77b93513c",-280,-170)
			table.create("08e6fe74-098f-4429-9076-71235a67c9b0",-280,-210)
			table.create("be7113f0-d44a-4923-bbc2-a2b3ad4cd948",-400,-50)
			table.create("7e3783d4-150a-46dd-8bd7-ef3680744d8c",-400,-90)
		else:
			table.create("342dd044-b0f7-4eef-a021-5b755397f9d4",300,20)
			table.create("6a34f431-c468-4d31-8d8c-51aac6a66f89",340,20)
			table.create("338370f8-3952-46a7-a3b9-a462a326e7bb",380,20)
			table.create("9936a519-785c-4058-b060-4ca0a01258ea",300,60)
			table.create("91e2e6b3-9929-4365-93b2-3d143a20e6ff",300,100)
			table.create("c237b30d-6511-4646-a93a-49b63ff4aa22",340,100)
			table.create("d6ac416d-0956-403f-a1bc-ed6e8c5ba4a9",380,100)
			table.create("dac3d665-1af7-427e-9f50-36d77b93513c",300,140)
			table.create("08e6fe74-098f-4429-9076-71235a67c9b0",300,180)
			table.create("be7113f0-d44a-4923-bbc2-a2b3ad4cd948",420,20)
			table.create("7e3783d4-150a-46dd-8bd7-ef3680744d8c",420,60)
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
		otherplayer = players[1]
		remoteCall(players[1], "getotherplayer", me)
	placesetupcards()

def placesetupcards():
	mute()
	list = []
	for p in me.hand:list.append(p)
	dlg=cardDlg(list)
	dlg.title = "Choose your setup cards."
	dlg.text = "You may place up to 8 gold cost worth cards as setup cards."
	dlg.min = 0
	dlg.max = len(list)
	cards = dlg.show()
	uniquecards = [] #Duplicates
	cost = 0
	limit = 0
	countcards=20
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
			confirm("You may only place up 1 limit card.")
			place = "NOTOK"
		if place == "NOTOK":
			placesetupcards()
		if place == "OK":
			for card in cards:
				if me.isInverted:
					card.moveToTable(countcards,-100,True)
				else:
					card.moveToTable(countcards,0,True)
				countcards=countcards-80
				card.peek()
			for drawcard in me.deck.top(7-len(me.hand)):
				drawcard.moveTo(me.hand)
			notify("{} is ready to begin.".format(me))
	else:
		if me.getGlobalVariable("setupOk") == "2":
			placesetupcards()
		else:
			mulligan(me.hand)
			me.setGlobalVariable("setupOk","2")
			placesetupcards()

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
	for c in table: 
		if c.Type == "Plot" and c.controller == me:
			if len(me.piles['Plot Deck']) > 0:
				c.moveTo(me.piles['Used Plot Pile'])
			else:
				shuffleToPlot(me.piles['Used Plot Pile'])
				c.moveTo(me.piles['Used Plot Pile'])
	global countusedplot
	oldcountusedplot = countusedplot
	countusedplot = len(me.piles['Used Plot Pile'])
	for card in table:
		if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":#just for Dawn
			attach = card.name+str(card.position)
			for cards in table:
				f = cards.name+str(cards.position)
				if f == attachmodify[attach]:cards.markers[STR_Up] += countusedplot-oldcountusedplot
	me.counters['Reserve'].value = 0
	me.counters['Initiative'].value = 0
	me.counters['Str'].value = 0
	me.setGlobalVariable("turn", "0")
	global countmil
	countmil = 0
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
						if card.controller == me and card.type == "Plot"]
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
				if card.Initiative and int(card.Initiative) > 0:
					if card.Unique != "Yes":
						person.counters['Initiative'].value += int(card.Initiative)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Initiative'].value += int(card.Initiative)	
		for card in plotlist:
			person.counters['Initiative'].value += int(card.plotInitiative)
			break
		plotlist.reverse()
		notify("{}'s Initiative value is {}.".format(person,person.counters['Initiative'].value))
	return

def fp(group, x = 0, y = 0):
	mute()
	if getGlobalVariable("numplayer") == "2":
		getInit(table)
		if players[0].counters['Initiative'].value == players[1].counters['Initiative'].value:
			notify("{}'s initiative value is same as {}.".format(players[0],players[1]))
			recalcPower(table)
			if players[0].counters['Power'].value == players[1].counters['Power'].value:
				if not confirm("Are you sure to decide who wins the initiative randomly?"): return
				n = rnd(1, 2)
				if n == 1:
					notify("**{} flips heads,and wins the initiative.**".format(players[0]))
					notify("**{} decides who is the first player.**".format(players[0]))
					setGlobalVariable("firstplay","{}".format(me._id))
				else:
					notify("**{} flips heads,and wins the initiative.**".format(players[1]))
					notify("**{} decides who is the first player.**".format(players[1]))
					setGlobalVariable("firstplay","{}".format(players[1]._id))
			if players[0].counters['Power'].value > players[1].counters['Power'].value:
				notify("**{} wins the initiative.**".format(players[1]))
				notify("**{} decides who is the first player.**".format(players[1]))
				setGlobalVariable("firstplay","{}".format(players[1]._id))
			if players[0].counters['Power'].value < players[1].counters['Power'].value:
				notify("**{} wins the initiative.**".format(players[0]))
				notify("**{} decides who is the first player.**".format(players[0]))
				setGlobalVariable("firstplay","{}".format(me._id))
		elif players[0].counters['Initiative'].value > players[1].counters['Initiative'].value:
			notify("{} wins the initiative.".format(players[0]))
			notify("**{} decides who is the first player.**".format(players[0]))
			setGlobalVariable("firstplay","{}".format(me._id))
		else:
			notify("{} wins the initiative.".format(players[1]))
			notify("**{} decides who is the first player.**".format(players[1]))
			setGlobalVariable("firstplay","{}".format(players[1]._id))
		if not confirm("Continue to decide who is the first player?"): return
		decidefirstplayer(table)
	else:
		notify("Only supported for Joust format.")
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
	for person in players:
		person.counters['Str'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		uniquecards = []
		for card in personCards:
			if card.isFaceUp:
				if card.orientation != Rot90:
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
				if card.dominance and int(card.dominance) > 0:
					if card.Unique != "Yes":
						person.counters['Str'].value += int(card.dominance)
					elif card.name not in uniquecards:
						uniquecards.append(card.name)
						person.counters['Str'].value += int(card.dominance)
				if card.markers[Gold] > 0:
					person.counters['Str'].value += card.markers[Gold]
		notify("{}'s total for dominance is {}.".format(person,person.counters['Str'].value))
	if not confirm("Confirm to proceed?"): return
	if getGlobalVariable("numplayer") == "2":
		if players[0].counters['Str'].value == players[1].counters['Str'].value:
			notify("No one wins dominance.")
		elif players[0].counters['Str'].value > players[1].counters['Str'].value:
			notify("{} wins the dominance.".format(players[0]))
			for housecard in table:
				if housecard.type == "Faction" and housecard.controller == players[0]:
					addPower(housecard)
		else:
			notify("{} wins the dominance.".format(players[1]))
			for housecard in table:
				if housecard.type == "Faction" and housecard.controller == players[1]:
					addPower(housecard)
	else:
		notify("Only supported for Joust format.")
	return

def challenge(group, x=0, y=0):
	mute()
	global challengetype
	global winplayer
	global attacker
	global defender
	global unopposed
	global otherplayer
	if attacker == []:
		notify("Please announce a attacker.")
		return
	if defender == []:
		notify("Please announce a defender.")
		return
	#choiceList = ['Military', 'Intrigue', 'Power']
	#choice = askChoice("To which challenge do you want to calculate? ", choiceList)
	choice = challengetype
	for person in players:
		person.counters['Str'].value = 0
		personCards = (card for card in table
						if card.controller == person)
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
	if getGlobalVariable("numplayer") == "2":
		if players[0].counters['Str'].value == players[1].counters['Str'].value:
			if players[0] == attacker:
				notify("attacker 1{} wins this challenge.".format(players[0]))
				winplayer = attacker
				if players[1].counters['Str'].value == 0:unopposed = 1
			else:
				notify("attacker 2{} wins this challenge.".format(players[1]))
				winplayer = players[1]
				if players[0].counters['Str'].value == 0:unopposed = 1
		elif players[0].counters['Str'].value > players[1].counters['Str'].value:
			if players[0] == attacker:
				notify("attacker 3{} wins this challenge.".format(players[0]))
				winplayer = players[0]
				if players[1].counters['Str'].value == 0:unopposed = 1
			else:
				notify("defender1 {} wins this challenge.".format(players[1]))
				winplayer = [0]
		else:
			if players[0] == attacker:
				notify("defender2 {} wins this challenge.".format(players[1]))
				winplayer = [0]
			else:
				notify("attacker 4{} wins this challenge.".format(players[1]))
				winplayer = players[1]
				if players[0].counters['Str'].value == 0:unopposed = 1
		remoteCall(otherplayer, "getwinner", [winplayer,unopposed,challengetype])
		balancechallenge(choice,winplayer,1)
	else:
		notify("Only supported for Joust format.")
	global Heartsbaneused
	for card in table:
		if card.model == "4c8a114e-106c-4460-846b-28f73914fc11" and Heartsbaneused == 1:#just for Heartsbane
			attach = card.name+str(card.position)
			for cards in table:
				f = cards.name+str(cards.position)
				if f == attachmodify[attach]:
					cards.markers[STR_Up] -=3
					Heartsbaneused = 0

def balancechallenge(challenge,winplayer,checkcount):
	mute()
	global otherplayer
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
			balancechallengefinish(challenge,winplayer)
		else:
			notify("2ndplayer want to action") 
			return

def getotherplayer(player):
	global otherplayer
	otherplayer =  player

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
	global challengetype
	global winplayer
	if winplayer != []:
		balancechallenge(challengetype,winplayer,1)
	else:
		notify("No challenge happened.")

def balancechallengefinish(challenge,winplay):
	mute()
	global winplayer
	global attacker
	global defender
	global unopposed
	global otherplayer
	global challengetype
	if winplayer != [0]:
		if unopposed != 0:
			notify("{} add 1 pow from unopposed.".format(winplay))
			if winplay == me:
				addhousepow(1)
			else:
				remoteCall(otherplayer, "addhousepow", 1)
		if challenge == 1:Militarychallenge(1)
		if challenge == 2:
			if winplay != me:
				randomDiscard(me.hand)
			else:
				remoteCall(otherplayer, "randomDiscard", [otherplayer.hand])  
		if challenge == 3:
			if winplay == me:
				if otherplayer.counters['Power'].value > 0:
					remoteCall(otherplayer, "subhousepow", 1)
					addhousepow(1)
			else:
				if me.counters['Power'].value > 0:
					subhousepow(1)
					remoteCall(otherplayer, "addhousepow", 1)
	for card in table:
		card.highlight = None
		card.target(False)
	notify("challenge balance over.")
	winplayer = []
	attacker = []
	defender = []
	unopposed = 0
	challengetype = 0
	remoteCall(otherplayer, "getwinner", [winplayer,unopposed,challengetype])
	remoteCall(otherplayer, "getattacker", [attacker,challengetype])
	remoteCall(otherplayer, "getdefender", [defender])

def challengeAnnounce(group, x=0, y=0):
	mute()
	global attacker
	if attacker ==[]:
		choiceList = ['Military', 'Intrigue', 'Power', 'No challenge and Pass']
		colorList = ['#ae0603' ,'#006b34','#1a4d8f','#D8D8D8']
		choice = askChoice("Which challenge do you want to initiate?", choiceList,colorList)
		if choice == 1:
			announceMil(table)
		elif choice == 2:
			announceInt(table)
		elif choice == 3:
			announcePow(table)
		elif choice == 4:
			notify("{} has no challenge to initiate.".format(me))
		else:return
	else:
		notify("challenge already happened.")

def Militarychallenge(claim):
	list = []
	for card in table:
		if card.type == "Character" and card.controller == me:
			if card.unique == 'Yes':
				if card not in list:
					list.append(card)
			else:
				list.append(card)
	if len(list) == 0:
		Militarychallenge(1)
	dlg = cardDlg(list)
	dlg.title = "These cards are in your table:"
	dlg.text = "Declares at least 1 character to be killed."
	dlg.min = 1
	dlg.max = 1
	cards = dlg.show()
	for card in cards:
		card.moveTo(me.piles['Dead pile'])

def revealplot(group, x = 0, y = 0):
	mute()
	me.piles['Plot Deck'].addViewer(me)
	dlg=cardDlg([c for c in me.piles['Plot Deck']])
	dlg.title = "These cards are in your unused-plot pile:"
	dlg.text = "Select a plot card to reveal."
	cards = dlg.show()
	if cards != None:
		for card in cards:
			if me.isInverted: 
				card.moveToTable(120,-80,True)
			else:
				card.moveToTable(-120,0,True)
			me.setGlobalVariable("turn","1")
			list = [card for card in table
						if card.Type == "Plot" and card.controller == me]
			count = len(list)
			for p in list:
				if count > 1:
					p.moveTo(me.piles['Used Plot Pile'])
					count -= 1
				if count == 1:
					break
			if len(me.piles['Plot Deck']) == 0:
				shuffleToPlot(me.piles['Used Plot Pile'])
			if len(players) > 1:
				if me.getGlobalVariable("turn") == players[1].getGlobalVariable("turn") == "1":
					flipplotcard(card)
					d = (card for card in table 
							if card.type == "Plot" and card.controller != me)
					for c in d:
						remoteCall(players[1], "flipplotcard", c)
					if not confirm("Continue to calculate initiative?"): return
					fp(table)
			if len(players) == 1:
				flipplotcard(card)
	else:
		return

		
def decidefirstplayer(group, x = 0, y = 0):
	mute()
	if getGlobalVariable("firstplay") == "{}".format(me._id):  
		askfirstplayer(table)
	else: 
		remoteCall(players[1], "askfirstplayer", table)     


def askfirstplayer(group, x = 0, y = 0):
	mute()
	choiceList = ['{}'.format(getGlobalVariable("AID")),'{}'.format(getGlobalVariable("BID"))]
	choice = askChoice("Decide who is First player.", choiceList)
	if choice == 1:
		notify("**{} is firstplayer.**".format(getGlobalVariable("AID")))
		setGlobalVariable("firstplay","True")
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:    
				moveFP(card)
			else:                        
				remoteCall(players[1], "moveFP", card)
	elif choice == 2:
		notify("**{} is firstplayer.**".format(getGlobalVariable("BID")))
		setGlobalVariable("firstplay","False")
		f = (card for card in table  
			if card.name == "1st Player Token")
		for card in f:
			if card.controller == me:   
				moveFP(card)
			else:                       
				remoteCall(players[1], "moveFP", card)
	else:
		return

#---------------------------------------------------------------------------
# New Table card actions
#---------------------------------------------------------------------------
def displayCardText(card, x = 0, y = 0):
	mute()
	
	notify('{} - Card Text:'.format(card))
	notify('{}'.format(card.Text))


def displayErrata(card, x = 0, y = 0):
	mute()
	
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
	if card.type == "Plot":
		card.moveTo(me.piles['Used Plot Pile'])
		notify("{} move {} to used plot pile.".format(me, card))
	elif card.type == "Faction" or card.type ==  "Agenda":
		whisper("You can't discard {} card.".format(card.type))
	elif card.type == "Internal":
		whisper("You can't discard {}.".format(card.name))
	elif card.type == "Attachment":
		for targetcard in table:
			g = targetcard.name+str(targetcard.position)
			f = card.name+str(card.position)
			b=attachmodify.copy()
			for key in b:
				if key == f and b[key] == g:
					del attachmodify[key]
					#rollback
					if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
						targetcard.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
					if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and targetcard.model == "df79718d-b01d-4338-8907-7b6abff58303":targetcard.markers[MilitaryIcon] -= 1#096小乔
					if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
						stradd = re.search('\+\d\sSTR', card.Text).group()
						targetcard.markers[STR_Up] -= int(stradd[1])
					if re.search('\[INT]\sicon', card.Text):targetcard.markers[IntrigueIcon] -= 1
					if re.search('\[POW]\sicon', card.Text):targetcard.markers[PowerIcon] -= 1
					if re.search('\[MIL]\sicon', card.Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":targetcard.markers[MilitaryIcon] -= 1
		card.moveTo(me.piles['Discard pile'])
	elif card.type == "Character":
		for attachcard in table:
			f = card.name+str(card.position)
			g = attachcard.name+str(attachcard.position)
			b=attachmodify.copy()
			whisper("g{}".format(g))
			whisper("f{}".format(f))
			whisper("{}".format(attachmodify))
			for key in b:
				if key == g and b[key] == f:
					attachcard.moveTo(me.hand)
					del attachmodify[key]
		card.moveTo(me.piles['Discard pile'])
		notify("{} discard {}.".format(me, card))

def defaultAction(card, x = 0, y = 0):
	mute()
	# Default for Done button is playerDone
	if card.Type == "Internal": 
		if card.name == "Done Token":
			DoneButton(card)
		if card.name == "1st Player Token":
			moveFP(card)
		if card.name == "quickrevealplot":
			revealplot(Table)
		if card.name == "quickgetInit":
			getInit(Table)
		if card.name == "quickfp":
			fp(Table)
		if card.name == "quickcountincome":
			countincome(Table)
		if card.name == "quickchallengeAnnounce":
			challengeAnnounce(Table)
		if card.name == "quickannounceOpp":
			announceOpp(Table)
		if card.name == "quickchallenge":
			challenge(Table)
		if card.name == "quickdominance":
			dominance(Table)
		if card.name == "quickendturn":
			endturn(Table)
		if card.name == "quickgetreserve":
			getreserve(Table)
		if card.name == "quickrecalcPower":
			recalcPower(Table)
	elif card.Type == "Plot":
		countincome(table)
	elif len(me.piles['Plot Deck']) == 7 and card.Type == "Attachment" and card.isFaceUp == True:
		play(card)
	elif not card.isFaceUp: #Face down card - flip
		flipcard(card, x, y)
	else:
		kneel(card, x, y)

def moveFP(card):
	mute()
	for person in players:
		if players != me:
			otherplayer = person
	if person.name == getGlobalVariable("AID"):
		playera = person
	if person.name == getGlobalVariable("BID"):
		playerb = person
	if getGlobalVariable("firstplay") == "True":
		if me.isInverted: 
			card.moveToTable(380,-100)
			card.controller = me
		else:
			card.moveToTable(-360,0)
			card.controller = me
	elif getGlobalVariable("firstplay") == "False":
		if me.isInverted: 
			card.moveToTable(-360,0)
			card.controller = otherplayer
		else:
			card.moveToTable(380,-100)
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
	c = 0
	if card.cost == "" : 
		whisper("You can't play this card")
		return
	if card.Cost == "X": cost=askInteger("How much do you want to pay to play {} ? ".format(card.name),0)
	else : cost=int(card.Cost)
	uniquecards = []
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
					cards = dlg.show()
				if cards != None:
					for choose in cards:
						if len(me.piles['Plot Deck']) != 7:
							reduc=askInteger("Reduce Cost by ?",0)
							if reduc == None or cost == None: return
							if reduc>cost: reduc=cost
							cost-=reduc
							if me.counters['Gold'].value < cost :
								whisper("You don't have enough Gold to pay for {}.".format(card))
								return
							me.counters['Gold'].value -= cost
							for incomecard in table:
								if incomecard.controller == me and incomecard.markers[Gold] > 0:
									incomecard.markers[Gold] -= cost
						cx,cy = choose.position
						x,y = attachat(cx+15,cy+15,table)
						card.moveToTable(x,y)
						attach = card.name+str(card.position)
						attachmodify[attach] = choose.name+str(choose.position)
						if card.model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and choose.model == "df79718d-b01d-4338-8907-7b6abff58303":choose.markers[MilitaryIcon] += 1#096小乔
						if card.model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":choose.markers[STR_Up] += countusedplot
						if re.search('\+\d\sSTR', card.Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', card.Text).group()
							choose.markers[STR_Up] += int(stradd[1])
						if re.search('\[INT]\sicon', card.Text):choose.markers[IntrigueIcon] += 1
						if re.search('\[POW]\sicon', card.Text):choose.markers[PowerIcon] += 1
						if re.search('\[MIL]\sicon', card.Text) and card.model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":choose.markers[MilitaryIcon] += 1
						card.sendToBack()
						card.highlight = PlayColor
						if len(me.piles['Plot Deck']) == 7:
							notify("{} plays {} and attachs to {}.".format(me,card,choose))
						else:
							notify("{} plays {} and attachs to {} for {} Gold (Cost reduced by {}).".format(me,card,choose,cost,reduc))
				else:
					whisper("Attachment cards must be attached to another card or game element.")
					return
		else:
			reduc=askInteger("Reduce Cost by ?",0)
			if reduc == None or cost == None: return
			if reduc>cost: reduc=cost
			cost-=reduc
			if me.counters['Gold'].value < cost :
				whisper("You don't have enough Gold to pay for {}.".format(card))
				return		
			if card.type == "Character":
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
			else:
				if me.isInverted: card.moveToTable(150,-230)
				else: card.moveToTable(-130,130)
			card.highlight = PlayColor
			notify("{} plays {} for {} Gold (Cost reduced by {}).".format(me,card,cost,reduc))
			me.counters['Gold'].value -= cost
			for incomecard in table:
				if incomecard.controller == me and incomecard.markers[Gold] > 0:
					incomecard.markers[Gold] -= cost
	else:
		if me.isInverted: 
			card.moveToTable(x-8,y-8)
		else:
			card.moveToTable(x+8,y+8)
		notify("{} plays {}'s duplicate.".format(me,card))
		card.sendToBack()
			
#------------------------------------------------------------------------------
# New Pile Actions
#------------------------------------------------------------------------------
def checkdeck():
	mute()
	notify (" -> Checking deck of {} ...".format(me))
	attachmodify.clear()
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
def onloaddeck(args):
	mute()
	c = int(getGlobalVariable("numplayer"))+1
	setGlobalVariable("numplayer","{}".format(c))
	if me._id == 1:
		setGlobalVariable("AID","{}".format(me))
	else:
		setGlobalVariable("BID","{}".format(me))
	player = args.player
	notify("players{}".format(getGlobalVariable("numplayer")))
	if player==me:
		checkdeck()
		setup(table)
		
def onmoved(args):
	mute()
	index = 0
	for card in args.cards:
		movecard = args.cards[index]
		d = args.cards[index].name+'('+str(args.xs[index])+'.0, '+str(args.ys[index])+'.0)'#(-255.0, 110.0)
		for key in attachmodify:
			if attachmodify[key] == d:
				attachmodify[key] = args.cards[index].name+str(args.cards[index].position)
			if key == d and args.cards[index].position != (0.0, 0.0):
				e = attachmodify[key]
				del attachmodify[key]
				attach = args.cards[index].name+str(args.cards[index].position)
				attachmodify[attach] = e
		if card.type == "Attachment" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.owner == me:
			for card in table:
				f = args.cards[index].name+'('+str(args.xs[index])+'.0, '+str(args.ys[index])+'.0)'
				g = card.name+str(card.position)
				b=attachmodify.copy()
				for key in b:
					if key == f and b[key] == g:
						del attachmodify[key]
						#rollback
						if args.cards[index].model == "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c":
							card.markers[STR_Up] -= len(me.piles['Used Plot Pile'])
						if args.cards[index].model == "4dd074aa-af6c-4897-b7b2-bff3493bcf9e" and card.model == "df79718d-b01d-4338-8907-7b6abff58303":card.markers[MilitaryIcon] -= 1#096小乔
						if re.search('\+\d\sSTR', args.cards[index].Text) and card.model != "9e6bf142-159b-4a3b-9d4c-d8bf233a6f0c" and card.model != "4c8a114e-106c-4460-846b-28f73914fc11":
							stradd = re.search('\+\d\sSTR', args.cards[index].Text).group()
							card.markers[STR_Up] -= int(stradd[1])
						if re.search('\[INT]\sicon', args.cards[index].Text):card.markers[IntrigueIcon] -= 1
						if re.search('\[POW]\sicon', args.cards[index].Text):card.markers[PowerIcon] -= 1
						if re.search('\[MIL]\sicon', args.cards[index].Text) and args.cards[index].model != "4dd074aa-af6c-4897-b7b2-bff3493bcf9e":card.markers[MilitaryIcon] -= 1
		if args.cards[index].type == "Character" and args.toGroups[index].name != "Table" and args.fromGroups[index].name == "Table" and card.owner == me:
			for card in table:
				g = args.cards[index].name+'(0.0, 0.0)'
				f = card.name+str(card.position)
				b=attachmodify.copy()
				for key in b:
					if key == f and b[key] == g:
						del attachmodify[key]
						card.moveTo(me.hand)
		index += 1