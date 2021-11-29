def parseTokens(tokens):
    current = 0

    def walk():
        nonlocal current
        token = tokens[current]

        if (token["type"] == 'number'):
            current += 1
            return { 'type': 'NumberLiteral', 'value': token["value"]}

        if (token["type"] == 'string'):
            current += 1
            return { 'type': 'StringLiteral', 'value': token["value"]}

        if (token["type"] == 'paren' and token["value"] == "("):
            # Skip over first open parenthesis (
            current += 1
            token = tokens[current]

            node = { 'type': 'CallExpression', 'name': token["value"], 'params': []}

            # Get the next token so we can process the children of the function
            current += 1
            token = tokens[current]

            # Process the children or nested functions
            while (token["type"] != 'paren' or (token["type"] == 'paren' and token["value"] != ")")):
                node["params"].append(walk())
                token = tokens[current]

            current+=1

            return node

        raise TypeError(token["type"])

    ast = {
        "type": 'Program',
        "body": []
    }

    while (current < len(tokens)):
        ast["body"].append(walk())

    return ast