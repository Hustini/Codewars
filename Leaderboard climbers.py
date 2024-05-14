def main(leaderboard, changes):
    new_changes = []
    for i in changes:
        new_data = i.split()
        new_changes.append(new_data)

    for person in new_changes:
        index = leaderboard.index(person[0])
        element = leaderboard.pop(index)
        leaderboard.insert(index - int(person[1]), element)

    return leaderboard


if __name__ == '__main__':
    case = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
    changes = ['Dave +1', 'Fred +4', 'Brian -1']
    answer = ['Fred', 'John', 'Dave', 'Brian', 'Jim']
    check = main(case, changes)
    print(check)
