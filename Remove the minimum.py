def main(numbers):
    return [element for i, element in enumerate(numbers) if i != numbers.index(min(numbers))]


if __name__ == '__main__':
    case = [1, 2, 3, 1, 1]
    answer = [2, 3, 1, 1]
    check = main(case)
    print(check)
