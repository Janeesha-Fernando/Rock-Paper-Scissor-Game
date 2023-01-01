play_again="yes"
while (play_again == "yes"):
    #Input the name of the player
    player_name=input("Enter your name: ")
    print("____________________________________________________________________________________________________________________________________________")
    print("                                                Hi",player_name,"Welcome to Rock Paper Scissor ")
    print("____________________________________________________________________________________________________________________________________________")
    print("\n")
    
    #Importing the function random to generate random index number.
    from random import randint

    #Creating a new list to store values of Rock/Paper/Scissor.
    code_breaker=[]
    
    #Create a list of play option.
    code_breaker=["Rock","rock","Paper","paper","Scissor","scissor"]

    #Assign a random play to the computer.
    computer=code_breaker[randint(0,5)]
    #print(computer)
    
    #Set player to True
    player=True

    while player == True:
        # Input the player guess
        player=input("Enter your guess (Rock/Paper/Scissor) : ")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You loose",computer,"cover the",player)   
            else:
                print("You win!",player,"smashes the",computer)  
        elif player == "rock":
            if computer == "paper":
                print("You loose",computer,"cover the",player)   
            else:
                print("You win!",player,"smashes the",computer)     
        elif player == "Rock":
            if computer == "paper":
                print("You loose",computer,"cover the",player)   
            else:
                print("You win!",player,"smashes the",computer)   
        elif player == "rock":
            if computer == "Paper":
                print("You loose",computer,"cover the",player)   
            else:
                print("You win!",player,"smashes the",computer) 
        elif player == "Paper":
            if computer == "Rock":
                print("You win!",player,"covers the",computer)       
            else:
                print("You loose",computer,"cut the",player)   
        elif player == "paper":
            if computer == "rock":
                print("You win!",player,"covers the",computer)       
            else:
                print("You loose",computer,"cut the",player)                                  
        elif player == "Paper":
            if computer == "rock":
                print("You win!",player,"covers the",computer)       
            else:
                print("You loose",computer,"cut the",player)   
        elif player == "paper":
            if computer == "Rock":
                print("You win!",player,"covers the",computer)       
            else:
                print("You loose",computer,"cut the",player)   
        elif player == "Scissor":
            if computer == "Paper":
                print("You win!",player,"cuts the",computer)
            else:
                print("You loose!",computer,"smashes the",player) 
        elif player == "scissor":
            if computer == "paper":
                print("You win!",player,"cuts the",computer)
            else:
                print("You loose!",computer,"smashes the",player) 
        elif player == "Scissor":
            if computer == "paper":
                print("You win!",player,"cuts the",computer)
            else:
                print("You loose!",computer,"smashes the",player) 
        elif player == "scissor":
            if computer == "Paper":
                print("You win!",player,"cuts the",computer)
            else:
                print("You loose!",computer,"smashes the",player) 
        else:
            print("Invalid input.Please check you spellings.")                                            
        
        player=False
        computer = code_breaker[randint(0,5)]
    play_again ="no"
    print("\n")
    play_again = str(input("Do you want to play another game (yes/no)? "))
    continue
print("Thankyou for playing the game.")









    


