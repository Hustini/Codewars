def main(st):
    state_dict = {'AZ': ['Arizona'],
                  'CA': ['California'],
                  'ID': ['Idaho'],
                  'IN': ['Indiana'],
                  'MA': ['Massachusetts'],
                  'OK': ['Oklahoma'],
                  'PA': ['Pennsylvania'],
                  'VA': ['Virginia']}

    tmp_list = st.split('\n')
    curr = []

    for item in tmp_list:  # gets everything to one person in a list
        curr.append(item.split(','))

    for state in list(state_dict.keys()):  # adds everything to one person to the according state
        for item in curr:
            if state in item[2]:
                key = item[2]
                item[2] = item[2][:-2]
                state_dict[key[-2:]].append(item)

    result = ''
    for state in state_dict:  # prints data according to the assignment
        if len(state_dict[state]) == 1:
            continue
        else:
            result += state_dict[state][0] + '\n'
            for data in state_dict[state][1:]:
                result += '..... ' + ''.join(data) + state_dict[state][0] + '\n'

    return result[:-1]


if __name__ == '__main__':
    case0 = """John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Sal Carpenter, 73 6th Street, Boston MA"""
    answer = 'Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n..... Sal Carpenter 73 6th ' \
             'Street Boston Massachusetts\r\nVirginia\r\n..... Alice Ford 22 East Broadway Richmond Virginia'
    check = main(case0)
    print(check)
    print('------------------------------------------------------------')
    print(answer)
