print("welcome to treasure island game")
print("ur mission is to find the treasur")
side=input("u r at a cross road. where do u want to go? type left or right\n").lower()
if side=="left":
    lake=input("u came to a lake. there is an island in the middle of the lake. type 'wait' to wait for the boat or type 'swim' to swin across\n")
    if lake=="wait":
        door=input("u arrived at the island unharmed. there are 3 doors : red, yellow and blue. which one will u chose?\n")
        if door=='yellow':
            print("congratulations !! u won the treasure")
        else:
            print ("u lost, try again later.")
    else:
        print('you have entered in deep water and got eaten by sharks.')
else:
    print("u fell in a hole and died")