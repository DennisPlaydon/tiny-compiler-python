def generate(node):
    if (node["type"] == 'Program'):
        return '\n'.join(list(map(generate, node["body"])))

    elif (node["type"] == 'ExpressionStatement'):
        return generate(node["expression"])

    elif (node["type"] == 'CallExpression'):
        return (
            generate(node["callee"]) +
            '(' +
            ', '.join(list(map(generate, node["arguments"]))) +
            ')'
        )

    elif (node["type"] == 'Identifier'):
        return node["name"]
    
    elif (node["type"] == 'NumberLiteral'):
        return node["value"]
    
    elif (node["type"] == 'StringLiteral'):
        return '"' + node["value"] + '"'
    else:
        raise TypeError('I dont know node this is:', node)



