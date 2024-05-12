def main(case):
    words = []
    case_split = case.split()
    for i in range(len(case_split)):
        words.append('')

    for i in range(1, 10):
        for j in range(len(case_split)):
            if str(i) in case_split[j]:
                words[i - 1] = case_split[j]

    result = ' '.join(words)

    return result


if __name__ == '__main__':
    case1 = 'is2 Thi1s T4est 3a'
    answer1 = 'Thi1s is2 3a T4est'
    case2 = '4of Fo1r pe6ople g3ood th5e the2'
    answer2 = 'Fo1r the2 g3ood 4of th5e pe6ople'
    check = main(case1)
    print(answer1)
    print(check)
