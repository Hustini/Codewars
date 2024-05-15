def main(data):
    return ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]


if __name__ == '__main__':
    print(main([(45, 12), (55, 21), (19, -2), (104, 20)]))
    print(f"solution: {['Open', 'Senior', 'Open', 'Senior']}")
