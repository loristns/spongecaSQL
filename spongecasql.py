import sys

if __name__ == '__main__':
    filename = sys.argv[-1]

    with open(filename) as input_file:
        input_code = input_file.read()

    output_code = ""

    is_string = False
    is_inline_comment = False
    is_multiline_comment = False
    
    upper = False
    prev_char = ""

    for char in input_code:
        is_comment = is_inline_comment or is_multiline_comment
        is_special = is_comment or is_string
        two_char = prev_char + char

        if char == '\'' and not is_comment:
            is_string = not is_string
        
        elif two_char == '--' or char == "#" and not is_special:
            is_inline_comment = True
        
        elif two_char == '/*' and not is_special:
            is_multiline_comment = True

        elif char == '\n' and is_inline_comment:
            is_inline_comment = False
        
        elif two_char == '*/' and is_multiline_comment:
            is_multiline_comment = False

        if not is_special:
            if upper:
                output_code += char.upper()
            else:
                output_code += char.lower()

            upper = not upper
        else:
            output_code += char

        prev_char = char

    with open('sPoNgeCaSeD_' + filename, 'w') as output_file:
        output_file.write(output_code)
