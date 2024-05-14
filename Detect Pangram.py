def main(st):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    count = 0
    for letter in alphabet:
        if letter in st.lower():
            count += 1
    if count == 26:
        return True
    else:
        return False


if __name__ == '__main__':
    case = 'The quick brown fox jumps over the lazy dog'
    answer = True
    check = main(case)
    print(check)
