import tokenizer
import parsr
import transformer
import codeGenerator

#                  LISP                      C
#
#   2 + 2          (add 2 2)                 add(2, 2)
#   4 - 2          (subtract 4 2)            subtract(4, 2)
#   2 + (4 - 2)    (add 2 (subtract 4 2))    add(2, subtract(4, 2))

code = '(add 2 (subtract 4 2))'

tokens = tokenizer.tokenize(code)
ast = parsr.parseTokens(tokens)
newAst = transformer.transform(ast)

print("\n----------------- Code from new AST -----------------\n")
newCode = codeGenerator.generate(newAst)
print(newCode)
print()
