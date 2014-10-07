# Opening the file and assigning the restaurant name and rating to lists.    

name = []
score = []

f = open("scores.txt")

for line in f:
    entries = line.split(':') 
    name.append(entries[0])
    score.append(entries[1])

dictionary = dict(zip(name,score))

keys_list = dictionary.keys()

keys_list.sort()

for restaurant in keys_list:
    print "Restaurant %s received a rating of %s." % (name, score)