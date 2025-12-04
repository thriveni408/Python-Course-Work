import random

p1 = input("Enter the player-1: ")
p2 = input("Enter the player-2: ")

winning_point=100
p1_sc=0
p2_sc=0
snakes={7:1,18:8,35:14,56:40,70:50,99:2}
ladders={5:30,9:21,25:45,48:88,66:97,80:94}

while p1_sc <winning_point and p2_sc <winning_point:
    
    p1_st=input(f"{p1} want to continue the game (y) or (n):")
    if p1_st=='y':
        p1_dice= random.randint(1,6)
        print(f"{p1}: Your dice score: {p1_dice}")
        p1_sc+=p1_dice
        
        if p1_sc in snakes:
            p1_sc=snakes[p1_sc]
            print(f"{p1}: You bitten by the snake.-------------\nYour total score: {p1_sc}")

        elif p1_sc in ladders:
            p1_sc=ladders[p1_sc]
            print(f"{p1}: You got the ladder.*************\nYour total score: {p1_sc}")    

        else:
            print(f"{p1}: Your total score: {p1_sc}")

        if p1_sc >= winning_point:
            print(f'Congrates!!!\n{p1} You win the game')
            break

            
    else:
        print(f'Congrates!!!\n{p2} You win the game')
        break


    p2_st=input(f"{p2} want to continue the game (y) or (n):")
    if p2_st=='y':
        p2_dice= random.randint(1,6)
        print(f"{p2}: Your dice score: {p2_dice}")
        p2_sc+=p2_dice
        if p2_sc in snakes:
            p2_sc=snakes[p2_sc]
            print(f"{p2}: You bitten by the snake.-------------\nYour total score: {p2_sc}")

        elif p2_sc in ladders:
            p2_sc=ladders[p2_sc]
            print(f"{p2}: You got the ladder.*************\nYour total score: {p2_sc}")    

        else:
            print(f"{p2}: Your total score: {p2_sc}")

        if p2_sc >= winning_point:
            print(f'Congrates!!!\n{p2} You win the game')
            break
    else:
        print(f'Congrates!!!\n{p1} You win the game')
        break

      
    
    