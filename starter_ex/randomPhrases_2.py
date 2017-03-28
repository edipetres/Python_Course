import random

adj = ["other", "new", "good", "high", "old", "great", "big", "American",
       "small", "large", "national", "young", "different", "black", "long"] 

articles = ["the", "a"] 

# https://www.espressoenglish.net/100-common-nouns-in-english/ 
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman",
         "life", "child", "world", "school", "state", "family", "student"] 

# https://www.espressoenglish.net/100-most-common-english-verbs/ 
verbs = ["call", "try", "ask", "need", "feel", "become", "leave", "put", 
         "mean", "keep", "let", "begin", "seem", "help", "talk", "turn"]

phrases = []

for article in articles:
    for adjective in adj:
        for noun in nouns:
            for verb in verbs:
                phrases.append((' ').join([article, adjective, noun, verb]))
                
for i in range(1,10):
    print(random.choice(phrases))
