from re import match


def division_message_into_blocks(message):
    message_len = len(message) + 1
    block_1 = message[0:message_len // 2]
    block_2 = message[message_len // 2:]

    return binary_presentation([block_1, block_2])


def chars_to_bites(value):
    match value.upper():
        case 'A':
            return '00000'
        case 'B':
            return '00001'
        case 'C':
            return '00010'
        case 'D':
            return '00011'
        case 'E':
            return '00100'
        case 'F':
            return '00101'
        case 'G':
            return '00110'
        case 'H':
            return '00111'
        case 'I':
            return '01000'
        case 'J':
            return '01001'
        case 'K':
            return '01010'
        case 'L':
            return '01011'
        case 'M':
            return '01100'
        case 'N':
            return '01101'
        case 'O':
            return '01110'
        case 'P':
            return '01111'
        case 'Q':
            return '10000'
        case 'R':
            return '10001'
        case 'S':
            return '10010'
        case 'T':
            return '10011'
        case 'U':
            return '10100'
        case 'V':
            return '10101'
        case 'W':
            return '10110'
        case 'X':
            return '10111'
        case 'Y':
            return '11000'
        case 'Z':
            return '11001'
        case '?':
            return '11010'
        case '!':
            return '11011'
        case '.':
            return '11100'
        case ',':
            return '11101'
        case '+':
            return '11110'
        case '-':
            return '11111'


def bites_to_chars(bits):
    match bits:
        case '00000':
            return 'A'
        case '00001':
            return 'B'
        case '00010':
            return 'C'
        case '00011':
            return 'D'
        case '00100':
            return 'E'
        case '00101':
            return 'F'
        case '00110':
            return 'G'
        case '00111':
            return 'H'
        case '01000':
            return 'I'
        case '01001':
            return 'J'
        case '01010':
            return 'K'
        case '01011':
            return 'L'
        case '01100':
            return 'M'
        case '01101':
            return 'N'
        case '01110':
            return 'O'
        case '01111':
            return 'P'
        case '10000':
            return 'Q'
        case '10001':
            return 'R'
        case '10010':
            return 'S'
        case '10011':
            return 'T'
        case '10100':
            return 'U'
        case '10101':
            return 'V'
        case '10110':
            return 'W'
        case '10111':
            return 'X'
        case '11000':
            return 'Y'
        case '11001':
            return 'Z'
        case '11010':
            return '?'
        case '11011':
            return '!'
        case '11100':
            return '.'
        case '11101':
            return ','
        case '11110':
            return '+'
        case '11111':
            return '-'


def binary_presentation(blocks_lst):
    binary_block_1, binary_block_2 = [], []

    for block in blocks_lst:
        if block == blocks_lst[0]:
            for value in block:
                binary_block_1.append(chars_to_bites(value))
        else:
            for value in block:
                binary_block_2.append(chars_to_bites(value))

    return [binary_block_1, binary_block_2]


def addition(val_bit, key_bit, operation):
    match operation:
        case 'and':
            if val_bit == '1' or key_bit == '1':
                return '1'
            else:
                return '0'
        case 'xor':
            if val_bit != key_bit:
                return '1'
            else:
                return '0'


def binary_and_addition(value, key):
    res = ''
    for bit in range(len(value)):
        res = res + (addition(value[bit], key[bit], 'and'))
    return res


def binary_xor_addition(l_block, right_block):
    res = []
    for i in range(len(l_block)):
        temp = ''
        for j in range(len(l_block[i])):
            temp = temp + (addition(l_block[i][j], right_block[i][j], 'xor'))
        res.append(temp)

    return res


def round_1(blocks_lst, key_h):
    left_block = []
    intermediate_result, round_1_result = '', ''

    for value in blocks_lst[0]:
        left_block.append(binary_and_addition(value, key_h))

    right_block = binary_xor_addition(left_block, blocks_lst[1])

    for bits in blocks_lst[1]:
        intermediate_result = intermediate_result + bites_to_chars(bits)

    for bits in right_block:
        round_1_result = round_1_result + bites_to_chars(bits)

    intermediate_result = intermediate_result + round_1_result

    print("Результат первого раунда:", intermediate_result)

    return round_1_result


def round_2(blocks_lst, left, key_p):
    right_block = []
    round_2_result = ''

    for value in blocks_lst:
        right_block.append(binary_and_addition(value, key_p))

    this_left = []
    for block in left:
        this_left.append(chars_to_bites(block))

    block = binary_xor_addition(right_block, this_left)

    for bits in block:
        round_2_result = round_2_result + bites_to_chars(bits)

    return round_2_result


def main():
    message = input("Введите сообщение для шифрования: ")

    blocks_lst = (division_message_into_blocks(message))

    keys = [chars_to_bites('H'), chars_to_bites('P')]

    left = round_1(blocks_lst, keys[0])
    right = round_2(blocks_lst[1], left, keys[1])

    print("Результат шифрования в латинском алфавите:", left+right)


if __name__ == '__main__':
    main()
