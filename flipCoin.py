import random
print('Welcome to flip coin Simulator')

#Constants
HEAD=0
TAIL=1
dict={}

class Flip_coin_simulator:
    #Checking head or tail
    def coin_flip(self,no_of_time_flip,no_of_coin):
        for i in range(0,no_of_time_flip):
            coin_side=""
            for j in range(0,no_of_coin):
                random_no=random.randint(0,1)
                if random_no == HEAD:
                    coin_side=coin_side+"H"
                else:
                    coin_side=coin_side+"T"
                dict={coin_side}
            print(dict)

#Object creation
flip_coin_simulator=Flip_coin_simulator()
try:
    no_of_coin=int(input("Enter no of coin you want to flip:"))
    no_of_time_flip=int(input("Enter no of times you want to flip:"))
except ValueError:
    print("Invalid value")
flip_coin_simulator.coin_flip(no_of_time_flip,no_of_coin)



