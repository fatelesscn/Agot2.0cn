saveaction = dict( # save player card
             RisenfromtheSea =            ("Risen from the Sea", "0e42b4fb-8a0e-40d1-a398-fd9c0f7912a4", "Event", "Hand", "Greyjoy.", "Event"),
             Bodyguard =                  ("Bodyguard", "f5173e6f-1ec3-4ee0-8274-755160c57c0e", "sacrifice", "table", "all", "Attachment"),#没判断贵族
             MaesterAemon =               ("Maester Aemon", "157ee453-9a78-480a-bf0e-93d74c49dc88", "kneel", "table", "Night's Watch.", "Character"))

counterevent = dict( # cancel card
             Treachery =                  ("Treachery", "3fbc7d75-3d0b-49df-8841-c92566a8c6d3", "Event", "Hand","Location/Character/Attachment", "Lannister.","Yes","all"),
             TheHandsJudgment =           ("The Hand's Judgment", "c5d78fb6-ff52-4012-ac95-547ed9feec0f","Event", "Hand", "Event", "all","","opponent"),
             BranStark =                  ("Bran Stark", "9e56783a-c133-4f81-9914-4e81b92ba5d1", "sacrifice", "table", "Event", "all","","opponent"))

cardability = dict( # save card ability
             Bodyguard =                  ("Bodyguard", "f5173e6f-1ec3-4ee0-8274-755160c57c0e", "Attachment", "sacrifice", "", ""),
             RisenfromtheSea =            ("Risen from the Sea", "0e42b4fb-8a0e-40d1-a398-fd9c0f7912a4", "Attachment", "Greyjoy", "savetarget"))

cardkill = dict( # leave ability
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "me", "2 power"),
             SerDavosSeaworth =       ("Ser Davos Seaworth", "813fb666-b32f-4ae9-b2ac-3fe09adccf9a", "none", ""),
             ViserysTargaryen =       ("Viserys Targaryen", "6580b898-de89-4a6d-89b4-72cfc3b505e6", "all", "discard", "Attachment"),
             SerWaymarRoyce =         ("Ser Waymar Royce", "e65c6d16-075b-4634-a490-a200bb75e3be", "other", "discard", "card"),
             ShireenBaratheon =       ("Shireen Baratheon", "6967fd81-f9f9-4077-8d5a-c9ca189a5e41", "all", "kneel", "Character"),
             BastardDaughter =        ("Bastard Daughter", "fcba07e6-a15f-46d8-821c-8a14a4983284", "other", "discard", "other", "Bastard Daughter"),
             TheRedViper =            ("The Red Viper", "73a43b0f-8337-4e71-96b7-9553d5d57ddf", "link", "discard", "other", "", "Bastard Daughter"))
leavedeck = dict( # leave prosition
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "deck"),
             SerDavosSeaworth =       ("Ser Davos Seaworth", "813fb666-b32f-4ae9-b2ac-3fe09adccf9a", "deck"))

leavereacion = dict( # leave reaction
             JoffreyBaratheon =       ("Joffrey Baratheon", "df79718d-b01d-4338-8907-7b6abff58303", "Traits", "Lord./Lady.", "1 power", 3),
             RobbStark =              ("Robb Stark", "d892faa0-09c4-41ec-8705-abe2c1c87c83", "Faction", "Stark.", "stand", 1))

afterchallengereacion = dict( # 4.2 reaction
             TyrionLannister =       ("Tyrion Lannister", "102c0746-2205-425a-ab85-90dc41a031e3", "2", "all", "2 gold", 2),
             Ghost =                 ("Ghost", "9c0f0dce-2809-4ad9-bc27-ba5bb15484ee", "all", "", "stealth", 1),
             DornishParamour =       ("DornishParamour", "f70034a0-01a1-4e77-8dde-44c1cd7d3f40", "all", "", "makedefender", 1),
             EddardStark =           ("Eddard Stark", "aee0eeeb-97a7-4b48-82e7-03141663e346", "all", "defender", "stand", 1))

aftercalculate = dict( # 4.2.2 reaction
             RattleshirtsRaiders =   ("Rattleshirt's Raiders", "be9304f2-bb5d-4d19-8fbe-4efb6ee24f29", "all", "attacker", "disotherattachment", 1, "table", ""),
             PuttotheSword =         ("Put to the Sword", "38dd5d15-7214-4c68-9cc4-0d2abd1b2140", "1", "attacker", "kill", 1, "Hand", 5),
             PuttotheTorch =         ("Put to the Torch", "997f1584-7092-4895-ac40-fc9fd98891bc", "1", "attacker", "disotherloaction", 1, "Hand", 5),
             SuperiorClaim =         ("Superior Claim", "8e9b06da-991e-4608-a16b-caf96209641a", "3", "all", "2 power", 1, "Hand", 5),
             TearsofLys =            ("Tears of Lys","b29c7bb5-7b84-4e94-a30b-8332fad51c2a","2","attacker","addmarker",1,"Hand",""),
             AshaGreyjoy =           ("Asha Greyjoy","41367a9d-b751-4632-9973-97d2e4df7087","all","attacker","stand",1,"table","uo"),
             EuronCrowsEye = ("Euron Crow's Eye","912e5447-89b3-4896-903c-6f5ed78113e1","all","both","放置进场",1,"table",""),
             TheonGreyjoy =          ("Theon Greyjoy","9a29f7bb-baa9-4475-8e35-55b845618822","all","attacker","addpowself",1,"table","uo"),
             GreatKraken =           ("Great Kraken","014da37c-9903-418d-a043-ee2191b9d169","all","attacker","drawcardorpower",1,"table","uo"),
             ThrowingAxe =           ("Throwing Axe","c3eeb001-e6a1-48ae-b310-cbd0d2c84653","all","attacker","attkilldef",1,"table",""),
             WeDoNotSow =            ("We Do Not Sow","62570a84-3203-468d-9529-37dbbc6d191c","all","attacker","disotherloactionattachment",1,"Hand","uo"),
             Lannisport =            ("Lannisport","5702d5f9-ae1e-435b-ae86-01c14817431a","2","all","drawcard",1,"table",""),
             MaesterCaleotte =       ("Maester Caleotte","4f58fa4d-7172-4466-86eb-32b2bb91b516","all","all","submarker",1,"table",""),
             TheRedViper =           ("The Red Viper","73a43b0f-8337-4e71-96b7-9553d5d57ddf","all","attacker","5pwinpow",1,"table",5),
             GhastonGrey =           ("Ghaston Grey","982acc7e-86c0-4bdd-84da-3b05e53dffa1","all","defender","returndefender",1,"table",""),
             Sunspear =              ("Sunspear","f2772a6e-2ed4-4fb9-8699-5497aee496e3","all","defender","addclaim",1,"table",""),
             DoransGame =            ("Doran's Game","427a5213-1be5-4b36-94be-04a5b3486575","2","all","addusedplotpow",1,"Hand",5),
             UnbowedUnbentUnbroken = ("Unbowed, Unbent, Unbroken","ad97966b-2d52-4b03-a8f4-f51c8a63a8c9","all","defender","cant1challenge",1,"Hand",""),
             TheSwordintheDarkness = ("The Sword in the Darkness","18715d47-dbe1-4f02-a5b3-e1d7f6943287","all","defender","cantchallenge",1,"Hand",5),
             LikeWarmRain =          ("Like Warm Rain","ef7d8bdf-1c56-4895-be9a-7a3ed059dcd3","2","defender","losekill",1,"Hand",""),
             Rhaegal =               ("Rhaegal","ac263d0d-d7db-49e7-bdc4-2e131d95aad4","all","all","standstm",1,"table",""),
             PlazaofPunishment =     ("Plaza of Punishment","06803230-d3a4-46f7-935a-1a7314839b9e","3","all","subability2",1,"table",""),
             DothrakiSea =           ("Dothraki Sea","1916c9ad-78da-42c7-9d22-8f059438dadc","3","all","addplayer",1,"table",""),
             MaesterLomys =          ("Maester Lomys","54111e34-4bec-4415-a562-fbd3f1ebbb77","2","defender","discard",1,"table",""),
             TheQueenofThorns =      ("The Queen of Thorns","0b5ca49f-5270-4b9f-84d4-391b59a2d4bc","2","all","addplayer6",1,"table",""),
             TheMander =             ("The Mander","bf44916f-cc99-4f0a-87f0-b529a426df7b","all","all","draw2card",1,"table","5"),
             OlennasCunning =        ("Olenna's Cunning","3fd0054d-0a3c-4ab9-9ea5-96b0a1ac4628","23","all","addhand",1,"Hand",""),
             Ice =                   ("Ice","e6059d34-2c23-41a1-a1c2-f299dee662e7","1","all","kill",1,"table",""))

def debug(str):
	mute()
	global debugMode
	if debugMode:
		whisper("Debug Msg: {}".format(str))
