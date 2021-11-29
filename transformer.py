import traverser

# Take one type of AST (e.g. a lisp syntax tree) and convert to another type
def transform(ast):
    newAst = {
        "type": 'Program',
        "body": []
    }

    ast["_context"] = newAst["body"]

    def NumberLiteralEnter(node, parent):
        parent["_context"].append({
            "type": 'NumberLiteral',
            "value": node["value"]
        })

    def StringLiteralEnter(node, parent):
        parent["_context"].append({
            "type": 'StringLiteral',
            "value": node["value"]
        })

    def CallExpressionEnter(node, parent):
        expression = {
            "type": 'CallExpression',
            "callee": {
                "type": 'Identifier',
                "name": node["name"]
            },
            "arguments": [],
        }

        node["_context"] = expression["arguments"]

        if (parent["type"] != expression["arguments"]):
            expression = {
                "type": "ExpressionStatement",
                "expression": expression
            }

        parent["_context"].append(expression)

    visitorFunctions = {
        "NumberLiteral": NumberLiteralEnter,
        "StringLiteral": StringLiteralEnter,
        "CallExpression": CallExpressionEnter
    }
    traverser.traverse(ast, visitorFunctions)

    return newAst