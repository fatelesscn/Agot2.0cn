saveaction = dict( # A dictionary which holds all cards action
             RisenfromtheSea =            ("Risen from the Sea", "0e42b4fb-8a0e-40d1-a398-fd9c0f7912a4", "Event", "Hand", "Greyjoy.", "Event"),
             Bodyguard =                  ("Bodyguard", "f5173e6f-1ec3-4ee0-8274-755160c57c0e", "sacrifice", "table", "all", "Attachment"),
             MaesterAemon =               ("Maester Aemon", "157ee453-9a78-480a-bf0e-93d74c49dc88", "kneel", "table", "Night's Watch.", "Character"))

counterevent = dict( # A dictionary which holds all cards action
             Treachery =                  ("Treachery", "3fbc7d75-3d0b-49df-8841-c92566a8c6d3", "Event", "Hand","Location/Character/Attachment", "Lannister.","Yes","all"),
             TheHandsJudgment =           ("The Hand's Judgment", "c5d78fb6-ff52-4012-ac95-547ed9feec0f","Event", "Hand", "Event", "all","","opponent"),
             BranStark =                  ("Bran Stark", "9e56783a-c133-4f81-9914-4e81b92ba5d1", "sacrifice", "table", "Event", "all","","opponent"))

cardability = dict( # A dictionary which holds all cards action
             RisenfromtheSea =            ("Risen from the Sea", "0e42b4fb-8a0e-40d1-a398-fd9c0f7912a4", "Attachment", "Greyjoy", "savetarget"))

cardkill = dict( # A dictionary which holds all cards action
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "me", "2 power"),
             SerDavosSeaworth =       ("Ser Davos Seaworth", "813fb666-b32f-4ae9-b2ac-3fe09adccf9a", "none", ""),
             ViserysTargaryen =       ("Viserys Targaryen", "6580b898-de89-4a6d-89b4-72cfc3b505e6", "all", "discard", "Attachment"),
             SerWaymarRoyce =         ("Ser Waymar Royce", "e65c6d16-075b-4634-a490-a200bb75e3be", "other", "discard", "card"),
             ShireenBaratheon =       ("Shireen Baratheon", "6967fd81-f9f9-4077-8d5a-c9ca189a5e41", "all", "kneel", "Character"),
             BastardDaughter =        ("Bastard Daughter", "fcba07e6-a15f-46d8-821c-8a14a4983284", "other", "discard", "other", "Bastard Daughter"),
             TheRedViper =            ("The Red Viper", "73a43b0f-8337-4e71-96b7-9553d5d57ddf", "link", "discard", "other", "", "Bastard Daughter"))
leavedeck = dict( # A dictionary which holds all cards action
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "deck"),
             SerDavosSeaworth =       ("Ser Davos Seaworth", "813fb666-b32f-4ae9-b2ac-3fe09adccf9a", "deck"))

leavereacion = dict( # A dictionary which holds all cards action
             JoffreyBaratheon =       ("Joffrey Baratheon", "df79718d-b01d-4338-8907-7b6abff58303", "Traits", "Lord./Lady.", "1 power", 3),
             RobbStark =              ("Robb Stark", "d892faa0-09c4-41ec-8705-abe2c1c87c83", "Faction", "Stark.", "stand", 1))

afterchallengereacion = dict( # A dictionary which holds all cards action
             TyrionLannister =       ("Tyrion Lannister", "102c0746-2205-425a-ab85-90dc41a031e3", "2", "all", "2 gold", 2),
             Ghost =                 ("Ghost", "9c0f0dce-2809-4ad9-bc27-ba5bb15484ee", "all", "", "stealth", 1),
             DornishParamour =       ("DornishParamour", "f70034a0-01a1-4e77-8dde-44c1cd7d3f40", "all", "", "makedefender", 1),
             EddardStark =           ("Eddard Stark", "aee0eeeb-97a7-4b48-82e7-03141663e346", "all", "defender", "stand", 1))

aftercalculate = dict( # A dictionary which holds all cards action
             RattleshirtsRaiders =   ("Rattleshirt's Raiders", "be9304f2-bb5d-4d19-8fbe-4efb6ee24f29", "all", "attacker", "disotherattachment", 1, "table", ""),
             PuttotheSword =         ("Put to the Sword", "38dd5d15-7214-4c68-9cc4-0d2abd1b2140", "1", "attacker", "kill", 1, "Hand", 5),
             PuttotheTorch =         ("Put to the Torch", "997f1584-7092-4895-ac40-fc9fd98891bc", "1", "attacker", "disotherloaction", 1, "Hand", 5))

def debug(str):
	mute()
	global debugMode
	if debugMode:
		whisper("Debug Msg: {}".format(str))
