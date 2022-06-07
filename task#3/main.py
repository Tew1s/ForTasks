import numpy as np
import random
import hashlib

from pandas import array

l = 6
b = 25*(2**l)
rounds = 12 + 2*l 
print(rounds,' Rounds in SHA-3')
w = 2**l
r = 576
c = 1024
#Make from 1600 array to 3 dimension of 5*5*64

def _1Dto3D(array_input):
    array_output = np.zeros((5, 5, w ), dtype = int) # array 5*5*64 with zeros 
    
    for i in range(5):
        for j in range(5):
            for k in range(w):
                array_output[i][j][k] = array_input[(w)*(5 * j + i) + k]

    return array_output

def theta(array_input):
        array_output = np.zeros((5,5,(w)), dtype = int)  # array 5*5*(w) with zeros 
        C = {}
        for i in range(5):
            for k in range(w):
                temp_indx=(i, k)
                temp_res = (sum( [array_input[i][indx][k] for indx in range(5)]) % 2) # XOR = mod2 
                C[temp_indx] = temp_res
        D = {}
        for i in range(5):
            for k in range(w):
                temp_indx=(i, k)
                temp_res = ( C[(((i-1)%5), k)] + C[((i+1)%5), ((k-1) % w)]) % 2 #XOR=mod2 
                D[temp_indx] = temp_res
                #and one position "to the front" of the original bit
        for i in range(5):
            for j in range(5):
                for k in range(64):
                    array_output[i][j][k] = (array_input[i][j][k] + D[(i, k)]) % 2
        return array_output

#Rho : Each word is rotated by a fixed number of position according to table.
def rho(array_input):
    array_output = np.zeros((5,5,w), dtype = int)
    for k in range(w ):
        array_output[0][0][k] = array_input[0][0][k]
    i = 1
    j = 0
    for t in range(24):
        for k in range(w):
            array_output[i][j][k] = array_input[i][j][(k - ((t + 1)*(t + 2) // 2)) % w]
        i = j
        j = (2*i + 3*j) % 5
    return array_output

#Pi: Permutate the 64 bit words
def pi(array_input):
    array_output = np.zeros((5,5,w), dtype = int) # Initialize empty 5x5x64 array
    for i in range(5):
        for j in range(5):
            for k in range(64):
                array_output[i][j][k] = array_input[(i + 3*j) % 5][i][k]
    return array_output


def chi(array_input):
    array_output = np.zeros((5,5,w), dtype = int) # Initialize empty 5x5x64 array
    for i in range(5):
        for j in range(5):
            for k in range(64):
                array_output[i][j][k] = (array_input[i][j][k] + ((array_input[(i+1) % 5][j][k] + 1) % 2)*(array_input[(i+2) % 5][j][k])) % 2
    return array_output

#iota: add constants  to word (0,0)
# aout[i][j][k] = ain[i][j][k] ⊕ bit[i][j][k]
# for 0 ≤ ℓ ≤ 6, we have bit[0][0][2ℓ − 1] = rc[ℓ + 7ir]

def iota(array_input, round):
    # generate rc
    #print(array_input.shape)
    array_output = array_input.copy()
    shift_r = np.array([1,0,0,0,0,0,0,0], dtype = int)
    rc = np.zeros((255), dtype=int)

    rc[0] = shift_r[1]
    for i in range(1, 255): #7*24
        shift_r = [shift_r[1],shift_r[2],shift_r[3],shift_r[4],shift_r[5],shift_r[6],shift_r[7], (shift_r[0]+shift_r[4]+shift_r[5]+shift_r[6]) % 2]
        rc[i] = shift_r[0]

    for l in range(7):
        #print (l,' ', l+7*round, ' ', round)
        array_output[0][0][w - 1] = (array_output[0][0][w - 1] + rc[l + 7*round]) % 2

    return array_output

def _3Dto1D(array_input):
    array_output = np.zeros(1600, dtype = int) # Initialize empty array of size 1600
    for i in range(5):
        for j in range(5):
            for k in range((2**l)):
                array_output[(2**l)*(5 * j + i) + k] = array_input[i][j][k]
    return array_output

def keccak(Message):
    length = len(Message)
    array_3d = _1Dto3D(Message)

    for i in range(rounds):
        array_3d = iota(chi(pi(rho(theta(array_3d)))), rounds)
    
    result = _3Dto1D(array_3d)

    return result
def SHA3_512 (Message):
    message = hex(int.from_bytes(Message.encode(), 'big'))
    message = message[2:]
    if len(message + '81') % r == 0:
        message += '81'
    else:
        while len(message) % r != 0:
            if len(message + '80') % r == 0:
                message = message + '80'
                break
            message +='00' 
    array = []
    for i in range(0, len(message), 2):
        array.append(int(message[i:i+2], 16))
    for i in range(len(array), 1600):
        array.append(0)
    return keccak(array)



if __name__ == '__main__':
    s = SHA3_512('mem')
    sk = '0b'
    for i in range(64):
        sk += str(s[i])
    print(hex(int(sk, 2)))
    #test = np.random.randint(100, size =1600)
    #print ("Test ", test)
    #seq1 = sha3(test)
    #seq2 = sha3(test)
    #seq3 = sha3(test)
    #seq4 = sha3(test)
    #if np.array_equal(seq1, seq2) and np.array_equal(seq2, seq3) and np.array_equal(seq3, seq4):
    #    print("True")
    #for i in range(1600):
    #    print(test[i], end = ' ')
    #print(len(seq1))
    #result = ''
    #for i in range(len(seq1)):
    #    result += str(seq1[i])
    #print(hex(int(result, 2)))