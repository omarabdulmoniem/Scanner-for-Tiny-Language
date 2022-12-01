def scan(code):
    code = code.strip() + " "
    reserved_tokens = {'if', 'then', 'else', 'end', 'repeat', 'until', 'read', 'write'}
    special_chars = {
        '+': 'PLUS',
        '-': 'MINUS',
        '*': 'MULT',
        '/': 'DIV',
        '=': 'EQUAL',
        '<': 'LESSTHAN',
        '(': 'OPENBRACKET',
        ')': 'CLOSEDBRACKET',
        ';': 'SEMICOLON',
        ':=': 'ASSIGN'
    }
    tokens, tokens_type = [], []
    state = 'start'
    token = ""
    i = 0
    code_length = len(code)
    while i < code_length:
        char = code[i]
        if state == 'start':
            if char == '{':
                state = 'in_comment'

            elif char.isdigit():
                token += char
                state = 'in_number'

            elif char.isalpha():
                token += char
                state = 'in_identifier'

            elif char == ':':
                state = 'in_assign'

            elif char != ' ' and char != '\n':
                tokens.append(char)
                if char in special_chars:
                    tokens_type.append(special_chars[char])
                else:
                    tokens_type.append('Unknown')

            i += 1

        elif state == 'in_comment':
            if char == '}':
                state = 'start'

            i += 1

        elif state == 'in_identifier':
            if char.isalpha():
                token += char
                i += 1
            else:
                tokens.append(token)
                if token in reserved_tokens:
                    tokens_type.append(token.upper())
                else:
                    tokens_type.append('IDENTIFIER')
                token = ''
                state = 'start'

        elif state == 'in_number':
            if char.isdigit():
                token += char
                i += 1
            else:
                tokens.append(token)
                tokens_type.append('NUMBER')
                token = ''
                state = 'start'

        else:
            if char == '=':
                tokens.append(':=')
                tokens_type.append('ASSIGN')
            else:
                tokens.append(':')
                tokens_type.append('Unknown')

            state = 'start'
            i += 1

    tokens_list = []

    outfile = open("scanned_table.txt","w")
    outfile.write('-'*43)
    outfile.write("\n|")
    outfile.write(' '*4)
    outfile.write("TOKEN VALUE")
    outfile.write(' '*(16-len("Token value")))
    outfile.write("|      ")
    outfile.write("TOKEN TYPE")
    outfile.write(' '*(9-len("Token type")+5))
    outfile.write("|\n")
    outfile.write('-'*43)
    outfile.write("\n")

    print('-'*50)
    print("|",' '*4,"TOKEN VALUE",' '*(16-len("Token value")),"|      ","TOKEN TYPE",' '*(9-len("Token type")+5),"|")
    print('-'*50)
    for x, y in zip(tokens, tokens_type):
        if y != 'Unknown':
            outfile.write("|")
            outfile.write(' '*6)
            outfile.write(x)
            outfile.write(' '*(14-len(x)))
            outfile.write("|      ")
            outfile.write(y)
            outfile.write(' '*(9-len(y)+5))
            outfile.write("|")
            outfile.write("\n")
            outfile.write('-'*43)
            outfile.write("\n")

            print("|",' '*6,x, ' '*(14-len(x)),"|      ", y,' '*(9-len(y)+5),"|")
            print('-'*50)
            tokens_list.append({"token_value": x, "token_type": y})

    return tokens_list


#codee = """
#{Sample program in TINY language - computes factorial}
#read x; {input an integer}
#if 0 < x then  {don't compute if x <= 0}
#	fact := 231;
#	repeat
#		fact := fact * x;
#		x := x - 1
#	until x = 0;
#	write fact {output factorial of x}
#end
#"""

if __name__ == "__main__":
    repeat = "yes"
    while 1 :
        code = ""
        if repeat == "yes":
            print("Please enter the code file name: ")
            filename = input()
            text_file = open(filename, "r")
            code = text_file.read()
            scan(code.strip())
            print("Do you want to scan another file? (yes/no)")
            repeat = input()
        else:
            break
