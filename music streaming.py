## We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
## create a dictionary called plays, and creates a song:playcount pair
plays = {key:value for key, value in zip(songs, playcounts)}
## print
print(plays)

## add a new entry to it
plays["Purple Haze"] = 1

## This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. 
plays["Respect"] = 94

## Create a dictionary called library that has two key: value pairs:
library = {"The Best Songs":plays, "Sunday Feelings":{}}

## print
print(library)
