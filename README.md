# Bertram-Capital-Coding-Challenge
Coding challenge for Bertram Capital

**GUIDE:**
-To build and run the program, open a new terminal and type in "python coffee_payment_gui.py". This will start the program and open the GUI interface.

**EXPLANATION:** 
-Inputting the names and prices is straightforward, as there will be seven rows where you can enter the information for each of the coffee consumers.

-With this program, you are allowed to save 3 different profiles. A profile consists of a group of 7 people maximum with the prices of their drinks. This eases the process of entering information as you can select a saved profile and click load to automatically fill in the information in one go.

-In order to save a profile, you can fill in the information in the boxes for the coffee consumers and click the save button for the profile you have selected. This will allow you to load that information right away when choosing that profile on another run.  

**ASSUMPTIONS:**
-This program determines fairness only through the prices of the coffees that were ordered.

-A person whose coffee is more expensive has a higher probability of being chosen to pay for coffee compared to someone with a less expensive drink.

-This is done by taking the prices of coffee for each person's order and putting them into a "weights" dictionary. This dictionary will be used for weightage in the random.choices() method in order to determine who gets chosen.
