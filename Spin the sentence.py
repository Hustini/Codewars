def main(sentence):
    new_sentence = sentence[:-1]
    list_words = new_sentence.split()
    output_list = []
    output_str = ''
    for i in list_words:
        if len(i) > 6 or i.lower().count('t') >= 2 or ',' in i:
            if ',' in i and len(i) == 7:
                new_word = i[:-1]
                output_list.append(new_word.upper() + ',')
            elif ',' in i and len(i) <= 6:
                new_word = i[:-1]
                output_list.append(new_word.upper() + ',')
            elif ',' in i and len(i) >= 6:
                new_word = i[:-1]
                output_list.append(new_word[::-1] + ',')
            else:
                output_list.append(i[::-1])
        elif len(i) == 2:
            output_list.append(i.upper())
        elif len(i) == 1:
            output_list.append('0')
        else:
            output_list.append(i)
    for i in output_list:
        output_str += i + ' '
    return output_str[:-1] + '.'


if __name__ == '__main__':
    sentence = 'If a man does not keep pace with his companions, perhaps it is because he hears a different drummer.'
    sentence2 = 'As Grainier drove along in the wagon behind a wide, slow, sand-colored mare, clusters of orange ' \
                'butterflies exploded off the purple blackish piles of bear sign and winked and winked and fluttered ' \
                'magically like leaves without trees.'
    sentence3 = 'Action is indeed, commmmmmmming.'

    result = 'IF 0 man does not keep pace with his snoinapmoc, spahrep IT IS esuaceb HE hears 0 tnereffid remmurd.'
    result2 = 'AS reiniarG drove along IN the wagon behind 0 WIDE, SLOW, deroloc-dnas MARE, sretsulc OF orange ' \
              'seilfrettub dedolpxe off the purple hsikcalb piles OF bear sign and winked and winked and derettulf ' \
              'yllacigam like leaves tuohtiw trees. '
    result3 = 'Action IS INDEED, gnimmmmmmmmoc.'

    check = main(sentence)
    print(f'is: {check}')
    print(f'sh: {result}')
