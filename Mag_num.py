import random
        
magic = [random.randint(0, 9), random.randint(0, 9)]

def ask_check():    #This allows user to enter their guess and check if correct
    user_num = int(input("Enter a number between 0 and 9: "))
    if user_num in magic:
        return "ABRACADABRA!"
    if user_num not in magic:
        return "HOCUS BOGUS!"


def run_program_x_times(chances):
    for i in range(chances): #range(chances_ is [0, 1, 2]
        print("This is attempt {}".format(i))
        print(ask_check())
        
attempts = int(input("How many times do you want to try?: "))
run_program_x_times(attempts)
