import random


s_nouns = ["A dude", "My mom", "The king", "Some......guy", "A rabid cat", "A sloth", "Your homie", "Superman", "The hacker", "The literal piece of human garbage", "A dev", "The VB Developer"]
p_nouns = ["These dudes", "Both of my moms","My two fathers", "Some guys", "Your homies", "Supermen", "Michael Bay", "Shahan", "David Awad", "Faiq", "The neckbeards", "The Brogrammers", "The intern", "The Android users", "All iPhone users" ]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "flees from", "tries to automate", "explodes", "eats", "breaks into"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode", "maul", "kill", "break", "treat", "fuck", "brogrammed", "gank", "hug"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology.", "to make the world flat.", "to fill a cup.", "in order to live.", "to hack the planet.", "to move.", "to port to windows", "to leran to smell.", "to code in VB.", "to eat protein.", "to die.", "for art."]

def get_sentence():
    rand_sentence = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
    while len(rand_sentence) > 140:
        rand_sentence = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
    return ' '.join(rand_sentence)

