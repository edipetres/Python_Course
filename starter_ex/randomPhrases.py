import random

adjective = ['Adamant', 'unyielding', 'a very hard substance', 'Adroit', 'clever', 
          'resourceful', 'Amatory', 'sexual', 'Animistic', 'Antic', 'clownish', 
          'frolicsome', 'Arcadian', 'serene', 'Baleful', 'deadly', 'foreboding',
          'Bellicose', 'quarrelsome', 'Bilious', 'unpleasant', 'peevish',
          'Boorish', 'crude', 'insensitive', 'Calamitous', 'disastrous',
          'Caustic', 'corrosive', 'sarcastic', 'Cerulean', 'sky blue',]

noun = ["time", "year", "people", "way", "day", "man", "thing", "woman",
        "life", "child", "world", "school", "state", "family", "student", 
        "group", "country", "problem", "hand", "part", "place", "case", 
        "week", "company", "system", "program", "question", "work", 
        "government", "number", "night", "point", "home", "water", "room", 
        "mother", "area", "money", "story", "fact", "month", "lot", "right", 
        "study", "book", "eye", "job", "word", "business", "issue", "side", 
        "kind", "head", "house", "service", "friend", "father", "power", 
        "hour", "game", "line", "end", "member", "law", "car", "city", 
        "community", "name", "president", "team", "minute", "idea", "kid", 
        "body", "information", "back", "parent", "face", "others", "level", 
        "office", "door", "health", "person", "art", "war", "history", 
        "party", "result", "change", "morning", "reason", "research", "girl", 
        "guy", "moment", "air", "teacher", "force", "education"]




for i in range(1,10):
    randomAdj = random.choice(adjective)
    randomNoun = random.choice(noun)
    print((' ').join([randomAdj, randomNoun]))


