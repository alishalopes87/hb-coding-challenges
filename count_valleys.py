# A mountain is a sequence of consecutive steps above sea level, 
# starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea level.

# Given Gary's sequence of up and down steps during his last hike, 
# find and print the number of valleys he walked through.

#s = [DDUUUUDD]
#START AT SEA LEVEL
#TAKE TWO STEPS DOWN- 1 STEP IS DOWN FROM SEA LEVEL, 1 STEP INTO VALLEY
#TAKES TWO STEPS UP - 1 STEP OUT OF VALLEY, 1 STEP INTO SEA LEVEL
#TAKES TWO STEPS UP - 1 STEP OUT OF SEAL LEVEL, 1 STEP UP MOUNTAIN
#TWO STEPS DOWN - 1 STEP DOWN FROM MOUNTAIN, 1 STEP INTO SEA LEVEL

#3 = [UDDDUDUU]
#START AT SEA LEVEL
#TAKE ONE STEP - UP FROM SEA LEVEL
# TAKE 3 STEPS DOWN - ONE STEP DOWN TO SEA LEVEL, TWO STEPS DOWN TO VALLEY
#ONE STEP UP UP TO SEA LEVEL 
# ONE STEP DOWN TO SEA LEVEL
##TWO STEPS UP TO MOUNTAIN 

#VAR SEA_LEVEL 
#VAR VALLEY 
#VAR MOUNTAIN
#COUNT = 0

#ITERATE OVER STRING SEA LEVEL = TRUE
#IF U INCREMENT COUNT
#IF THERES A D DECREMENT COUNT
#IF COUNT < -1 valley += abs(count /2)
#count > 1 count += count /2
#return mountain 

def count_valleys(n,s):
    inValley = False
    vallies = 0
    hgt = 0
    
    for step in s:
        print("THESE ARE VALLIES",vallies)
        if step == 'U':
            hgt += 1
        else:
            hgt -= 1
            
        if not inValley:
            if hgt < 0:
                inValley = True
        elif hgt == 0:
            inValley = False
            vallies += 1
            
    return vallies

print(count_valleys(8, "UDDDUDUU"))
print(count_valleys(100,"DDUUDDDUDUUDUDDDUUDDUDDDUDDDUDUUDDUUDDDUDDDUDDDUUUDUDDDUDUDUDUUDDUDUDUDUDUUUUDDUDDUUDUUDUUDUUUUUUUUU"))



