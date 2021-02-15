def deliveries(pizzaAmount, teamTwo, teamThree, teamFour, the_pizza_dict):
    
    print("FUNCTION DELIVERIES!")
    print("\nThe number of pizzas are:" + pizzaAmount)
    print("\nThe number of two people teams:" + teamTwo)
    print("\nThe number of three people teams:" + teamThree)
    print("\nThe number of four people teams:" + teamFour)
    print("the pizza dictionary")
    print(the_pizza_dict)

    numPizza = 0 
    max_pizza = pizzaAmount
    # THINK OF ANOTHER MORE EFFECIENT WAY TO DO THIS!!!!!!!!!
    order_list1 = []
    order_list2 = []
    order_list3 = []

    # total number of members in a team of two
    two_team_total = 2 * int(teamTwo)
    print("\nTWO TEAM TOTAL")
    print(two_team_total)

    # total number of members in a team of three
    three_team_total = 3 * int(teamThree)
    print("\nTHREE TEAM TOTAL")
    print(three_team_total)

    # total number of memebers in a team of four
    four_team_total = 4 * int(teamFour)
    print("\nFOUR TEAM TOTAL")
    print(four_team_total)
    

    # delivering pizza to each team
    for pizza in the_pizza_dict.keys():

        #delivering to teams of 2 
        if numPizza < two_team_total:

            order_list1.append(pizza) 
            pizzaAmount = int(pizzaAmount) - 1
            print("\nAmount of pizzas left: " + str(pizzaAmount))
            numPizza += 1


        # delivering to teams of 3
        # while numPizza != int(max_pizza):
        #     order_list2.append(the_pizza_dict[numPizza]) 
        #     pizzaAmount = int(pizzaAmount) - 1
        #     print("\nAmount of pizzas left: " + str(pizzaAmount))
        #     numPizza += 1

        # delivering teams of 4
        # while numPizza != int(max_pizza):
        #     order_list3.append(the_pizza_dict[numPizza])
        #     pizzaAmount = int(pizzaAmount) - 1
        #     print("\nAmount of pizzas left: " + str(pizzaAmount))
        #     numPizza += 1
        
    # No more pizza left
    # if int(pizzaAmount) == 0:
    #     print("Sorry, we could not deliver your pizza :(\n")


    # printing pizza per team
    
    print("\nTEAM TWO PIZZAS:")
    print(order_list1)


    print("\nTEAM THREE PIZZA:")
    print(order_list2)

    # print("\nTEAM FOUR PIZZA:")
    # print(order_list3)


    # # writing to a file to create an out file
    # with open("C:\\Users\\Windows\\Desktop\\Hashcode_Repo\\2021_EvenMorePizza\\output\\a_example.out", "w", encoding='utf8') as outputfile: # unicode transformation formatos xx
    #     outputfile.write(str(order_list1)) 
    #     outputfile.write("\n")

    #     outputfile.write(str(order_list2))
    #     outputfile.write("\n")
    
    #     outputfile.write(str(order_list3))


def main():
    details = []
    counter = 0

    pizza_dict = {}
    pizzaNum = 0

    # Reading the input file
    with open("C:\\Users\\Windows\\Desktop\\Hashcode_Repo\\2021_EvenMorePizza\\input\\a_example", "r") as file:
        
        for line in file.readline():
            for num in line.split(): 
                details.append(num)

        print(details)
        print("\n")

        availablePizza = details[0]

        twoPersonTeam = details[1]

        threePersonTeam = details[2]

        fourPersonTeam = details[3]
        
        print("Number of pizza available is: " + availablePizza)

        print("Number of two-Person teams is: " + twoPersonTeam)

        print("Number of three-Person teams is: " + threePersonTeam)

        print("Number of four-Person teams is: " + fourPersonTeam)
        print("\n")

        print("Pizza list:\n")

        for line in file:
            line = line.strip('\n') # strip removed the \n character from the line
            pizza_dict[pizzaNum] = line
            pizzaNum += 1
                
        print(pizza_dict)

        deliveries(availablePizza, twoPersonTeam, threePersonTeam, fourPersonTeam, pizza_dict)

if __name__ == '__main__':
    main()

