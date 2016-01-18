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
             ViserysTargaryen =       ("Viserys Targaryen", "6580b898-de89-4a6d-89b4-72cfc3b505e6", "all", "discard", "Attachment"),
             SerWaymarRoyce =         ("Ser Waymar Royce", "e65c6d16-075b-4634-a490-a200bb75e3be", "other", "discard", "card"),
             ShireenBaratheon =       ("Shireen Baratheon", "6967fd81-f9f9-4077-8d5a-c9ca189a5e41", "all", "kneel", "Character"),
             BastardDaughter =        ("Bastard Daughter", "fcba07e6-a15f-46d8-821c-8a14a4983284", "Bastard Daughter/The Red Viper", "discard", "card"))
leavedeck = dict( # A dictionary which holds all cards action
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "deck"))


eventinsert = 0
eventcard = []

def debug(str):
	mute()
	global debugMode
	if debugMode:
		whisper("Debug Msg: {}".format(str))
