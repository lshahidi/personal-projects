# take a mathematical expression in the form of a string as input
# print whether the expression is convex, concave, or affine

# build parse tree for expression (leaves are variables or constants/parameters)
# recursively parse string up to the innermost parenthesis, determine if concave, convex, affine, or unknown; then pass up

# next step: find next '(', call isConvex again passing in everything between next '(' and last ')'

import sys

def isConvex():

    return 'convex'
    
if __name__ == '__main__':
    functionString = str(sys.argv[1])
    convexity = isConvex()
    print('The function %s  is %s.' % (functionString, convexity))
