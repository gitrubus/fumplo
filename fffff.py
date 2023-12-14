import random

def drink_cones_game():
    num_cones = int(input("Enter the number of cones: "))
    
    if num_cones <= 0:
        print("You need at least one cone to play!")
        return
    
    cones = ['Water', 'Juice', 'Soda', 'Milkshake', 'Smoothie']  # Types of cones/drinks
    
    print("Let's drink from the cones!")
    for cone in range(1, num_cones + 1):
        random_cone = random.choice(cones)
        print("Drink from cone {cone}: {random_cone}")
        input("Press Enter for the next cone...")
    
    print("All cones have been drunk from!")
     print("wait...")
print("ah ha we stole your money hehehe")
print("my master plan has worked you have been SCAMMED")
print("what you can't fight me hehe hehe")
print("i have AI you can't stop me")
print("comin soooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooon")
# Run the game
drink_cones_game()
