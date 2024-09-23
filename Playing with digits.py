def main(n, p):
    tmp = [int(x) for x in str(n)]  # split numbers
    result = 0
    for i in tmp:
        result += i ** p
        p += 1

    if result % n == 0:
        return result // n
    else:
        return -1


if __name__ == '__main__':
    case = (46288, 3)
    solution = 51
    check = main(case[0], case[1])
    print(f'answer: {check}')
    print(f'solution: {solution}')
