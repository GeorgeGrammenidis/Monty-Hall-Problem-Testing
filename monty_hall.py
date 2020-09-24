import random
def door_picking (strategy):
    pick = random.randrange(1,4)
    if pick==1 :
        door1 = True
        door2 = False
        door3 = False
    elif pick==2:
        door1 = False
        door2 = True
        door3 = False
    elif pick==3:
        door1 = False
        door2 = False
        door3 = True
    doors = [door1 , door2 , door3]
    guess = random.randrange(1,4)
    if guess==1:
        left_out1 = 1
        left_out2 = 2
    elif guess==2:
        left_out1 = 0
        left_out2 = 2
    elif guess==3:
        left_out1 = 0
        left_out2 = 1
    if strategy == "switch":
        if doors[left_out1]==False and doors[left_out2] == False:
            last = random.randrange(1,3)
            if last==2:
                return doors[left_out1]
            elif last==1:
                return doors[left_out2]
        elif doors[left_out1]==False:
            return doors[left_out2]
        elif doors[left_out2]==False:
            return doors[left_out1]
    elif strategy=="keep":
        return doors[guess-1]
switch=0
keep=0
for i in range (100):
    if door_picking("switch"):
        switch= switch + 1
for i in range (100):
    if door_picking("keep"):
        keep= keep + 1
print ("Wins by switching: " , switch)
print ("Wins by keeping : " , keep)
        
