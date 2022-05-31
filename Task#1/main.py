import random
import time

from scipy import rand

def get_key_length( length : int) -> int:
    return 2**length

def random_key( length : int) ->int :
    temp = random.randint(0, length)

    return hex(random.getrandbits(temp))

def seach_key( length: int, search_num):
    temp = 0
    start_time = time.time()
    while( temp < int(search_num, 16) and temp.bit_length() - 2 <= length ):
        temp += 1
    end_time = time.time()
    if hex(temp) == search_num :
        print("Find num ", hex(temp)) 
    return (end_time - start_time) * 1000 #Millisecond


if __name__ == '__main__':


    print ("Print length of key: ")
    length_key = int(input())
    print("Number of different keys: ", get_key_length(length_key))

    random_num = random_key(length_key) 
    print("Random hex number : ",  random_num)
    print("Millisecond for search :", int(seach_key(length_key, random_num)))