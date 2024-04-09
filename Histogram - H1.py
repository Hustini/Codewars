input_list = [7, 3, 10, 1, 0, 5]
input_list.reverse()
result = '6|##### 5\n5|\n4|# 1\n3|########## 10\n2|### 3\n1|####### 7\n'


def get_amount(value):
    output = ''
    for i in range(value):
        output += '#'
    return output


def main():
    counter = 6
    output = ''
    for i in input_list:
        if i == 0:
            output += f'{counter}|{get_amount(i)}\n'
        else:
            output += f'{counter}|{get_amount(i)} {i}\n'
        counter -= 1
    return output


if __name__ == '__main__':
    if main() == result:
        print(main())
