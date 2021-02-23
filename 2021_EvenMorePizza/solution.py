import sys 

def deliveries(pizzaAmount, team_of_Two, team_of_Three, team_of_Four):

    """
        This method will deliver pizzas to the different teams.
        ---
        Attributes:
        -----------
            pizzaNum : int
            Counter for keeping track of pizzas given away

            teamNumber : int
            Counter to count the amount of teams

            order_list2 : list
            The list of pizza for the team of two

            order_list3 : list
            The list of pizza for the team of three

            order_list4 : list
            The list of pizza for the team of four

            team_of_Two_total : int
            Holds the total number of members in a team of two

            team_of_Three_total : int
            Holds the total number of members in a team of three

            team_of_Four_total : int
            Holds the total number of members in a team of four         
         

    """

    pizzaNum = 0 # counter is for keeping track of the pizza given 
    max_pizza = pizzaAmount
    teamNumber = 0 # counter variable, counts the amount of teams 
   
    teamTwo = 2
    teamThree = 3
    teamFour = 4

    # Pizza lists for each team 
    order_list2 = []
    order_list3 = []
    order_list4 = []

    # total number of members in a team of two
    team_of_Two_total = teamTwo * int(team_of_Two)

    # total number of members in a team of three
    team_of_Three_total = teamThree * int(team_of_Three)

    # total number of memebers in a team of four
    team_of_Four_total = teamFour * int(team_of_Four)
    
    ######################################### DELIVERING PIZZA TO THE TEAMS #################################################################

    # delivering pizza to each team

    for member in range(0, team_of_Two_total):
        if pizzaNum < int(max_pizza):
            order_list2.append(pizzaNum)
            pizzaAmount = int(pizzaAmount) - 1
            pizzaNum += 1

    # checks if there's enough pizza for team of 3 

    spare_pizza = int(pizzaAmount) % teamThree          # checks how many pizzas are left over
    remaining_pizza = pizzaAmount - spare_pizza         # removes extra pizza from the pizzas available
    enough_pizza = int(pizzaNum) + remaining_pizza      # total of pizzas that will be divided evenly for teams of 3

    for member in range(0, team_of_Three_total):
        if pizzaNum < enough_pizza:
            order_list3.append(pizzaNum)
            pizzaAmount = int(pizzaAmount) - 1
            pizzaNum += 1


    spare_pizza = int(pizzaAmount) % teamFour           # checks how many pizzas are left over
    remaining_pizza = pizzaAmount - spare_pizza         # removes extra pizza from the pizzas available
    enough_pizza = int(pizzaNum) + remaining_pizza      # total of pizzas that will be divided evenly for teams of 4

    for member in range(0, team_of_Four_total):
      
        if pizzaNum < enough_pizza:
            order_list4.append(pizzaNum)
            pizzaAmount = int(pizzaAmount) - 1
            pizzaNum += 1


    #################### SPLITTING PIZZA FOR SPEARATE TEAMS & PRINTING IN TERMINAL & CALCULATING THE AMOUNT OF TEAMS GET PIZZA #####################


    for pizzaNum in range(0, len(order_list2)): 

        if (pizzaNum % teamTwo) == 0:
            teamNumber += 1


    for pizzaNum in range(0, len(order_list3)): 

        if (pizzaNum % teamThree) == 0:
            teamNumber += 1


    for pizzaNum in range(0, len(order_list4)): 
    
        if (pizzaNum % teamFour) == 0:
            teamNumber += 1

    ################################################# writing to a file to create an out file #####################################################
    sys.argv[1] = sys.argv[1].strip('.in') #stripping the filename of original file extension that is read from the command line

    with open("C:\\Users\\Windows\\Desktop\\Hashcode_Repo\\2021_EvenMorePizza\\output\\" + sys.argv[1] + ".out", "w", encoding='utf8') as outputfile: # unicode transformation format
        outputfile.write(str(teamNumber)) # printing out the total number of teams who got pizza
      
        # printing out team twos pizza orders to output file
        for pizzaNum in range(0, len(order_list2)):

            if (pizzaNum % teamTwo) == 0:
                outputfile.write("\n")
                outputfile.write(str(teamTwo))
                outputfile.write(" ")
                outputfile.write(str(order_list2[pizzaNum])) # prints out VALUE of pizza
            else : 
                
                outputfile.write(" ")
                outputfile.write(str(order_list2[pizzaNum])) 

        # printing out team threes pizza orders to output file
        for pizzaNum in range(0, len(order_list3)):
    
            if (pizzaNum % teamThree) == 0:
                outputfile.write("\n")
                outputfile.write(str(teamThree))
                outputfile.write(" ")
                outputfile.write(str(order_list3[pizzaNum])) # prints out VALUE of pizza
            else : 
                
                outputfile.write(" ")
                outputfile.write(str(order_list3[pizzaNum])) 

        # printing out team fours pizza orders to output file
        for pizzaNum in range(0, len(order_list4)):
        
            if (pizzaNum % teamFour) == 0:
                outputfile.write("\n")
                outputfile.write(str(teamFour))
                outputfile.write(" ")
                outputfile.write(str(order_list4[pizzaNum])) # prints out VALUE of pizza
            else : 
                
                outputfile.write(" ")
                outputfile.write(str(order_list4[pizzaNum])) 

        outputfile.write("\n")


##################################################################### MAIN ########################################################################
def main():

    """
        This method is the main method which reads in input files.
        Files are read from the command line. 
        The first line separates the integers and put into a list called details.
        A variable was created for each integer in details. 
        These variables are passed to the deliveries method.
        ...
        
        Attributes:
        ----------
            details : list
            Holds the numbers from the first line in the input file.

            availablePizza : str
            This variable is used to hold the total number of pizzas avaliable.

            twoPersonTeam : int
            A variable used to hold the number of people in a team of two

            threePersonTeam : int
            A variable used to hold the number of people in a team of two

            fourPersonTeam : int
            A variable used to hold the number of people in a team of two

    """

    if len(sys.argv) < 2:
        sys.stderr.write("filename missing\n")
        sys.exit()

    # Reading the input file
    with open("C:\\Users\\Windows\\Desktop\\Hashcode_Repo\\2021_EvenMorePizza\\input\\" + sys.argv[1], "r") as file:
    
        line = file.readline()

        details = line.split() # line.split puts the read in line from the input file into a ready made list 

        availablePizza = details[0]

        twoPersonTeam = details[1]

        threePersonTeam = details[2]

        fourPersonTeam = details[3]
      
        deliveries(availablePizza, twoPersonTeam, threePersonTeam, fourPersonTeam)

if __name__ == '__main__':
    main()
