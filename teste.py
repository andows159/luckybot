from time import sleep
from random import randint  
set = ["@diegocunha9","@_laerton2","@tavares_r_"]
  
def write_as_human():
    for account in set:
        print("QUEBRA")
        for letter in account:
            print(letter)
            sleep(randint(1, 5) / 15)


write_as_human()