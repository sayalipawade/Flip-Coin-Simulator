import random
print('Welcome to flip coin Simulator')

class Flip_coin_simulator:

    #Constants
    global HEAD
    TAIL=1

    #Variables
    no_of_coin=0
    no_of_time_flip=0

    #Checking head or tail
    def coin_flip(self,no_of_time_flip,no_of_coin):
        HEAD=0
        list_of_side=[]
        for index1 in range(0,no_of_time_flip):
            coin_side=""
            for index2 in range(0,no_of_coin):
                random_no=random.randint(0,1)
                if random_no == HEAD: 
                    coin_side=coin_side+"H"
                else: 
                    coin_side=coin_side+"T"
            list_of_side.append(coin_side)
        print(list_of_side)

    #Taking user input
    def take_user_input(self):
        global no_of_time_flip
        global no_of_coin
        try:
            no_of_coin=int(input("Enter no of coin you want to flip:"))
            no_of_time_flip=int(input("Enter no of times you want to flip:"))
        except ValueError:
            print("value should be valid")
    
#Object creation
flip_coin_simulator=Flip_coin_simulator()
flip_coin_simulator.take_user_input()
flip_coin_simulator.coin_flip(no_of_time_flip,no_of_coin)