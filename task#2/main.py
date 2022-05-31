import random

def hex_to_little_endian(number):
    temp = number
    if len(number) % 2 !=0:
        temp = '0' + number 
    temp = [temp[i: i+2] for i in range(0, len(temp), 2)]
    result =''
    i = len(temp) - 1
    while (i >= 0):
        result += temp[i]
        i -= 1
    return int('0x'  + result, 16)


def hex_to_big_endian(number):
    return int('0x' + number, 16)

def little_endian_to_hex(number, length):
    hex_str = hex(number)
    hex_str = hex_str[2:]
    temp = [hex_str[i: i+2] for i in range(0, len(hex_str), 2)]
    result = ''
    temp = temp[::-1]
    
    if temp[0][0] == '0':
        temp[0] = temp[0][1:]
    for i in range(len(temp)):
        result += temp[i]
    i = length - len(result) - 1
    while (i >= 0):
        result += '0'
        i -= 1
    return '0x' + result

def big_endian_to_hex(number, length):
    temp = hex(number)
    return temp

if __name__ == '__main__':
    """test #1"""
    num = 'ff00000000000000000000000000000000000000000000000000000000000000'
    print('Test #1:')
    print('Value:'+' '*20 + '0x'+(num))
    print('Number of bytes: ', len(num)/2)
    little_endian = hex_to_little_endian(num)
    big_endian = hex_to_big_endian(num)
    print('Little-endian: ', little_endian)
    print('Big-endian: ', big_endian)
    print('Value from little-edian: ', little_endian_to_hex(little_endian, len(num)))
    print('Value from big-edian:    ', big_endian_to_hex(big_endian, len(num)))
    """test #2"""
    num = 'aaaa000000000000000000000000000000000000000000000000000000000000'
    print('Test #2:')
    print('Value:'+' '*20 + '0x'+(num))
    print('Number of bytes: ', len(num)/2)
    little_endian = hex_to_little_endian(num)
    big_endian = hex_to_big_endian(num)
    print('Little-endian: ', little_endian)
    print('Big-endian: ', big_endian)
    print('Value from little-edian: ', little_endian_to_hex(little_endian, len(num)))
    print('Value from big-edian:    ', big_endian_to_hex(big_endian, len(num)))
    """test #3"""
    num = 'FFFFFFFF'
    print('Test #2:')
    print('Value:'+' '*20 + '0x'+(num))
    print('Number of bytes: ', len(num)/2)
    little_endian = hex_to_little_endian(num)
    big_endian = hex_to_big_endian(num)
    print('Little-endian: ', little_endian)
    print('Big-endian: ', big_endian)
    print('Value from little-edian: ', little_endian_to_hex(little_endian, len(num)))
    print('Value from big-edian:    ', big_endian_to_hex(big_endian, len(num)))
    """test #4"""
    num = 'F000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    print('Test #4:')
    print('Value:'+' '*20 + '0x'+(num))
    print('Number of bytes: ', len(num)/2)
    little_endian = hex_to_little_endian(num)
    big_endian = hex_to_big_endian(num)
    print('Little-endian: ', little_endian)
    print('Big-endian: ', big_endian)
    print('Value from little-edian: ', little_endian_to_hex(little_endian, len(num)))
    print('Value from big-edian:    ', big_endian_to_hex(big_endian, len(num)))
    """"""