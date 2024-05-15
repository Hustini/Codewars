def main(source_array):
    """Pseudocode
    get list of with odd numbers
    sort odd numbers
    using original list and enumerate() insert even numbers at the right place
    """
    odd_numbers = [item for item in source_array if item % 2 != 0]
    odd_numbers.sort()
    for index, value in enumerate(source_array):
        if value % 2 == 0:
            odd_numbers.insert(index, value)

    return odd_numbers


if __name__ == '__main__':
    case = [5, 3, 2, 8, 1, 4, 11]
    solution = [1, 3, 2, 8, 5, 4, 11]
    check = main(case)
    print(f'answer: {check}')
    print(f'solution: {solution}')
