def traverse(ast, visitor):
    def traverseArray(array, parent):
        for child in array:
            traverseNode(child, parent)

    def traverseNode(node, parent):
        entryFunction = visitor.get(node["type"])

        if entryFunction:
            # Call enter function
            entryFunction(node, parent)

        if (node["type"] == 'Program'):
            traverseArray(node["body"], node)
        elif (node["type"] == 'CallExpression'):
            traverseArray(node["params"], node)
        elif (node["type"] == 'NumberLiteral' or node["type"] == 'StringLiteral'):
            return
    
    traverseNode(ast, None)
