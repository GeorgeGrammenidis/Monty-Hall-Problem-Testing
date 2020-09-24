# Monty-Hall-Problem-Testing
This is a simple description of the Monty Hall problem from Wikipedia:  "Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"  This project attempts to examine both approaches (switching and not switching) empirically. This is done by generating 3 variables representing the 3 doors  where one randomly is assigned a true value while the others are false. The program each time picks one door at random, then it "opens" one of  the other two which is always false and the first 100 times the computer switches its choice and picks the remaining third door, while the other 100 times it sticks with the initial choice.  At the end the program prints how many times it found the correct door by switching vs how many times it found it by maintaining the initial choice. The most common answer of the Monty Hall problem is that you have a 2/3 chance of winning if you always switch, and interestingly all the times I personally tried the program it printed around 62-68/100 (Around 2/3) wins by switching and 31-36/100 (around 1/3) by not switching. Obviously when it comes to luck based problems like this, empiricism can only get us so far and would never be as valid as  a proper mathematical proof, but it's still valuable to see how the data in a simulation such as this seem to confirm the "switching has a 2/3 chance" hypothesis. 
