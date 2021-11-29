import sys

def tokenize(input):
    current = 0
    tokens = []

    while (current < len(input)):
        char = input[current]

        if (char == "("):
            token = { 'type': 'paren', 'value': '('}
            tokens.append(token)
            current+=1
            continue

        if (char == ")"):
            token = { 'type': 'paren', 'value': ')'}
            tokens.append(token)
            current+=1
            continue

        if (char == " "):
            current+=1
            continue

        if (char.isdigit()):
            value = ""

            while (char.isdigit()):
                value += char
                current+=1
                char = input[current] if current < len(input) else ''
        
            token = { 'type': 'number', 'value': value}
            tokens.append(token)
            continue

        if (char == '"'):
            value = ""
            
            # Skip over first quote
            current += 1
            char = input[current]

            while (char != '"'):
                value += char
                current+=1
                char = input[current]
        
            # Skip over the last quote
            current += 1
            char = input[current] if current < len(input) else ''

            token = { 'type': 'string', 'value': value}
            tokens.append(token)
            continue

        if (char.isalpha()):
            value = ""
            
            while (char.isalpha()):
                value += char
                current+=1
                char = input[current]
        
            token = { 'type': 'name', 'value': value}
            tokens.append(token)
            continue

        raise TypeError('I dont know what this character is: ' + char);

    return tokens


if __name__ == "__main__":
    toProcess = "(add 2 (subtract 4 2))"
    print(tokenize(toProcess))
