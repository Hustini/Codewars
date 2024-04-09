result1 = {'r': 128, 'g': 255, 'b': 160}  # #80FFA0
result2 = {'r': 51, 'g': 187, 'b': 119}  # #3B7
result3 = {'r': 50, 'g': 205, 'b': 50}  # LimeGreen

PRESET_COLORS = {
    "red": "#FF0000",
    "blue": "#0000FF",
    "limegreen": "#32CD32",
    "green": "#008000",
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#FAEBD7"
}


def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def main(color):
    output_dict = {'r': 0, 'g': 0, 'b': 0}
    keys = list(output_dict.keys())
    counter = 0

    normalized_color = color.lower()
    if normalized_color in PRESET_COLORS:
        color = PRESET_COLORS[normalized_color]

    if len(color) == 7:
        value = color[1:]
        output_list = split_list(value, 2)
        for i in output_list:
            try:
                output_dict[keys[counter]] = int(i, 16)
            except ValueError:
                continue
            counter += 1
        return output_dict
    elif len(color) == 4:
        color = color[1:]
        color = split_list(color, 1)
        new_color = '#'
        for i in color:
            new_color += str(i) * 2
        return main(new_color)


if __name__ == '__main__':
    if main('limegreen') == result3:
        print('Named color test passed!')
    if main('#3B7') == result2:
        print('Short hex color test passed!')
    if main('#80FFA0') == result1:
        print('Full hex color test passed!')
