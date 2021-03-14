from LAOlexer import *
from LAOParser import *
import sys

class BasicExecute:

    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and (isinstance(result, int) or  isinstance(result, float)):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)
    
    # ---- UTILITY FUNCTIONS ----
    def isFloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    # --------------------------------

    # MAIN IMPORTANT FUNCTION
    def walkTree(self, node):

            # EXIT IF NONE
            if node is None:
                return None

            # RE ENTER TREE
            if node[0] == 'program':
                if node[1] == None:
                    self.walkTree(node[2])
                else:
                    self.walkTree(node[1])
                    self.walkTree(node[2])

            # REM STATEMENT
            if node[0] == 'COMMENT STATEMENT':
                return ' '

            # GENERIC KEYWORDS
            if node[0] == 'KEYWORD':
                return node[1]

            if node == 'KEYWORD':
                return node
                
            # ---- DATA TYPES SECTION ---- 
            if node[0] == 'UNSIGNED_INTEGER':
                return node[1]
            
            if node[0] == 'UNSIGNED_REAL':
                return node[1]

            if node[0] == 'STRING':
                return node[1]


            # ---- CONDITIONAL STATMENTS SECTION ----
            if node[0] == 'IF STATEMENT':
                result = self.walkTree(node[1])
                if result:
                    return self.walkTree(node[2][1])
                if len(node) > 2:
                    if len(node[2]) > 2:
                        return self.walkTree(node[2][2])
                    else:
                        return self.walkTree(node[2][1])
                return self.walkTree(node[1])
            
            if node[0] == 'THEN STATEMENT':
                result = self.walkTree(node[1])
                if result:
                    return self.walkTree(node[2][1])
                return self.walkTree(node[2][2])

            if node[0] == 'EQUALS CONDITION':
                return self.walkTree(node[1]) == self.walkTree(node[2])

            if node[0] == 'OR CONDITION':
                return self.walkTree(node[1]) or self.walkTree(node[2])

            if node[0] == 'AND CONDITION':
                return self.walkTree(node[1]) and self.walkTree(node[2])

            if node[0] == 'NOT CONDITION':
                return self.walkTree(node[1]) != self.walkTree(node[2])

            if node[0] == 'GREATER THAN CONDITION':
                return self.walkTree(node[1]) > self.walkTree(node[2])

            if node[0] == 'LESS THAN CONDITION':
                return self.walkTree(node[1]) < self.walkTree(node[2])

            if node[0] == 'GREATER OR EQUAL CONDITION':
                return self.walkTree(node[1]) >= self.walkTree(node[2])

            if node[0] == 'LESS OR EQUAL CONDITION':
                return self.walkTree(node[1]) <= self.walkTree(node[2])

            if node[0] == 'NOT EQUAL CONDITION':
                return self.walkTree(node[1]) != self.walkTree(node[2])

            # ---- END OF CONDITIONAL STATMENTS SECTION ----

            # ARITHMETIC OPERATIONS
            if node[0] == 'ADDITION':
                return self.walkTree(node[1]) + self.walkTree(node[2])
            elif node[0] == 'SUBTRACTION':
                return self.walkTree(node[1]) - self.walkTree(node[2])
            elif node[0] == 'MULTPLICATION':
                return self.walkTree(node[1]) * self.walkTree(node[2])
            elif node[0] == 'DIVISION':
                return self.walkTree(node[1]) / self.walkTree(node[2])

            # ASSIGMENT OPERATION
            if node[0] == 'ASSIGNMENT_STATEMENT':
                self.env[node[1]] = self.walkTree(node[2])
                return node[1]
            
            # READ OPERATION
            if node[0] == 'READ STATEMENT':
                userInput = input()
                if userInput.isnumeric():
                    self.env[node[2]] = int(userInput)
                elif BasicExecute.isFloat(userInput):
                    self.env[node[2]] = float(userInput)
                else:
                    self.env[node[2]] = userInput
                return ' '

            # PRINT OPERATION
            if node[0] == 'PRINT_STATEMENT':
                if len(node) > 2:
                    print(self.walkTree(node[1]) and self.walkTree(node[2]))
                return ' '
            
            # END OF PROGRAM
            if node[0] == 'END STATEMENT':
                raise Exception('PROGRAM EXITED')

            if node == 'END STATEMENT':
                raise Exception('PROGRAM EXITED')

            # ASSIGNED VARIABLES
            if node[0] == 'VARIABLE':
                try:
                    return self.env[node[1]]
                except LookupError:
                    print("Undefined variable '"+node[1]+"' found!")
                    return ' '

            # ASSIGNED VARIABLES
            if node == 'VARIABLE':
                try:
                    return self.env[node]
                except LookupError:
                    print("Undefined variable '" + node + "' found!")
                    return ' '

            # STRING VARIABLES
            if node >= 'o' and node <= 'z' or node >= 'O' and node <= 'Z':
                try:
                    return self.env[node]
                except LookupError:
                    print("Undefined variable '" + node + "' found!")
                    return ' '

            # STRING VARIABLES
            if node[0] >= 'o' and node[0] <= 'z' or node[0] >= 'O' and node[0] <= 'Z':
                try:
                    return self.env[node[1]]
                except LookupError:
                    print("Undefined variable '" + node[1] + "' found!")
                    return ' '

            # REAL VARIABLES
            if node >= 'g' and node <= 'o' or node >= 'G' and node <= 'O':
                try:
                    return self.env[node]
                except LookupError:
                    print("Undefined variable '" + node + "' found!")
                    return ' '

            # REAL VARIABLES
            if node[0] >= 'g' and node[0] <= 'o' or node[0] >= 'G' and node[0] <= 'O':
                try:
                    return self.env[node[1]]
                except LookupError:
                    print("Undefined variable '"+node[1]+"' found!")
                    return ' '

            # INTEGER VARIABLES
            if  node >= 'a' and node < 'g' or node >= 'A' and node < 'G':
                try:
                    return self.env[node]
                except LookupError:
                    print("Undefined variable '" + node + "' found!")
                    return ' '

            # INTEGER VARIABLES
            if  node[0] >= 'a' and node[0] < 'g' or node[0] >= 'A' and node[0] < 'G':
                try:
                    return self.env[node[1]]
                except LookupError:
                    print("Undefined variable '" + node + "' found!")
                    return ' '

            # DEFAULT RETURN of Integer or String Values
            if isinstance(node, int):
                return node
            if isinstance(node, str):
                return node
# ------------------------------------        
# START OF PROGRAM - WILL RUN USING A EXTERNAL FILE TO READ THE CODE FROM AND INTERPRET IT
if __name__ == '__main__':
    lexer = LAOLexer()
    parser = LAOParser()
    env = {}
    # READ CODE FROM A EXTERNAL TEXT FILE
    fileName = sys.argv[1]
    with open(fileName) as file:
        try:
            for line in file:
                if line:
                    tree = parser.parse(lexer.tokenize(line))
                    BasicExecute(tree, env)
        except Exception as ex:
            print(ex)
            exit
