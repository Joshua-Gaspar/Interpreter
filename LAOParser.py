from LAOlexer import *
from sly import Parser


class LAOParser(Parser):
    tokens = LAOLexer.tokens

    # HOW TOKENS ARE EVALUATED
    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('right', 'NOT'),
        ('left', 'EQ', 'NE'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'ADD', 'SUB'),
        ('left', 'MUL', 'DIV')
    )
    
    def __init__(self):
        self.env = {}

    # IGNORE EMPYT STRINGS
    @_('')
    def statement(self, p):
        pass
    
    # ---- CONDITIONALS SECTION ----
    @_('IF condition')
    def statement(self, p):
        return ('IF STATEMENT', p.condition)

    @_('IF condition THEN statement')
    def statement(self, p):
        return ('IF STATEMENT', p.condition, ('THEN STATEMENT', p.statement))

    @_('IF NOT condition')
    def statement(self, p):
        return ('IF STATEMENT, (NOT CONDITION', p.condition)

    @_('IF NOT condition THEN statement')
    def statement(self, p):
        return ('IF STATEMENT, (NOT CONDITION', p.condition, ('THEN STATEMENT', p.statement))

    @_('condition OR condition')
    def condition(self, p):
        return ('OR CONDITION', p.condition0, p.condition1)

    @_('expr OR expr')
    def condition(self, p):
        return ('OR CONDITION', p.expr0, p.expr1)

    @_('condition AND condition')
    def condition(self, p):
        return ('AND CONDITION', p.condition0, p.condition1)

    @_('condition NOT condition')
    def condition(self, p):
        return ('NOT CONDITION', p.condition0, p.condition1)

    @_('expr GT expr')
    def condition(self, p):
        return ('GREATER THAN CONDITION', p.expr0, p.expr1)

    @_('expr LT expr')
    def condition(self, p):
        return ('LESS THAN CONDITION', p.expr0, p.expr1)

    @_('expr EQ expr')
    def condition(self, p):
        return ('EQUALS CONDITION', p.expr0, p.expr1)

    @_('expr GE expr')
    def condition(self, p):
        return ('GREATER OR EQUAL CONDITION', p.expr0, p.expr1)

    @_('expr LE expr')
    def condition(self, p):
        return ('LESS OR EQUAL CONDITION', p.expr0, p.expr1)

    @_('expr NE expr')
    def condition(self, p):
        return ('NOT EQUAL CONDITION', p.expr0, p.expr1)

    # ---- END OF CONDITIONALS SECTION ----

    # REM COMMENT STATEMENT
    @_('COMMENT_STATEMENT')
    def statement(self, p):
        return p.COMMENT_STATEMENT

    # ASSIGMENT OPERATION
    @_('ASSIGNMENT_STATEMENT')
    def statement(self, p):
        return p.ASSIGNMENT_STATEMENT

    # PRINT OPERATION
    @_('PRINT_STATEMENT')
    def statement(self, p):
        return p.PRINT_STATEMENT

    # READ USER INPUT OPERATION
    @_('READ_STATEMENT')
    def statement(self, p):
        return p.READ_STATEMENT

    # EXIT PROGRAM FUNCTIONALITY
    @_('END_STATEMENT')
    def statement(self, p):
        return p.END_STATEMENT

    # REM COMMENT STATEMENT
    @_('REM')
    def COMMENT_STATEMENT(self, p):
        return ('COMMENT STATEMENT', p[0])

    # REM COMMENT STATEMENT
    @_('REM VARIABLE',
       'REM NAME',
       'REM STRING')
    def COMMENT_STATEMENT(self, p):
        return ('COMMENT STATEMENT', p[0], p[1])

    # PRINT OPERATION
    @_('PRINT')
    def PRINT_STATEMENT(self, p):
        return ('PRINT_STATEMENT', p[0])

    # PRINT OPERATION AND VALUES ACCEPTED
    @_('PRINT NAME',
       'PRINT VARIABLE',
       'PRINT UNSIGNED_INTEGER',
       'PRINT UNSIGNED_REAL',
       'PRINT INTEGER',
       'PRINT REAL',
       'PRINT STRING',
       'PRINT LETTER')
    def PRINT_STATEMENT(self, p):
        return ('PRINT_STATEMENT', p[0], p[1])

    # REM AND VALUES ACCEPTED FOR A COMMENT
    @_('READ VARIABLE',
       'READ NAME',
       'READ LETTER')
    def READ_STATEMENT(self, p):
        return ('READ STATEMENT', p[0], p[1])

    # EXIT PROGRAM
    @_('END')  
    def END_STATEMENT(self, p):
        return ('END STATEMENT', p[0])

    @_('NAME "=" expr',
       'VARIABLE "=" expr')
    def ASSIGNMENT_STATEMENT(self, p):
        return ('ASSIGNMENT_STATEMENT', p[0], p.expr)

    # ASSIGMMENT OPERATION
    @_('NAME "=" STRING',
       'VARIABLE "=" STRING')
    def ASSIGNMENT_STATEMENT(self, p):
        return ('ASSIGNMENT_STATEMENT', p[0], p.STRING)

    # ---- ARITHMETIC OPERATIONS SECTION ----
    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('expr ADD expr')
    def expr(self, p):
        return ('ADDITION', p.expr0, p.expr1)

    @_('expr SUB expr')
    def expr(self, p):
        return ('SUBTRACTION', p.expr0, p.expr1)

    @_('expr MUL expr')
    def expr(self, p):
        return ('MULTPLICATION', p.expr0, p.expr1)

    @_('expr DIV expr')
    def expr(self, p):
        return ('DIVISION', p.expr0, p.expr1)
    
    # ---- END OF ARITHMETIC OPERATIONS SECTION ----

    # DECLARATION OF VARIABLES
    @_('NAME',
       'VARIABLE',
       'LETTER')
    def expr(self, p):
        return ('VARIABLE', p[0])

    # ---- DATA TYPES SECTION ----
    @_('INTEGER')
    def expr(self, p):
        return ('NEGATIVE_SIGN_INTERGER', p[0])

    @_('UNSIGNED_INTEGER')
    def expr(self, p):
        return ('UNSIGNED_INTEGER', p[0])

    @_('REAL')
    def expr(self, p):
        return ('NEGATIVE_SIGN_REAL', p[0])

    @_('UNSIGNED_REAL')
    def expr(self, p):
        return ('UNSIGNED_REAL', p[0])

    @_('STRING')
    def expr(self, p):
        return ('STRING', p[0])

    # ---- END OF DATA TYPES SECTION ----


# ------------------------------------
# START OF PROGRAM - WILL RUN USING THE TERMINAL LINE BY LINE
if __name__ == '__main__':
    lexer = LAOLexer()
    parser = LAOParser()
    env = {}
    while True:
        try:
            text = input('PARSER > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
