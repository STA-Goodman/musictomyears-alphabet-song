import winsound
import notes
import letters
import time
#Play the note b#

#Play the note c

#Play the note c#

#Play the note d

#Play the note d# 

#Play the note e
#mno

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0
while count < 3:
    for letter in alphabet:
        print(letter)
        exec("letters." + letter + "()")
        time.sleep(1)
        
        
    count +=1
