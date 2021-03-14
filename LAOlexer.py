from sly import Lexer

class LAOLexer(Lexer):

    # TOKENS OF OPERATIONS ALLOWED TO BE USED IN LEXER
    tokens = {ARROW, POSITIVE_SIGN, NEGATIVE_SIGN, GT, LT, EQ, GE, LE, NE,
              OR, AND, NOT, ADD, SUB, MUL, DIV, DECIMAL_PART, DECIMAL_POINT, UNSIGNED_REAL, REAL, NUMBER, DIGIT, ELSE,
              FOR, FUN,
              TO, COMMA, EQEQ, STRING, IF, THEN, READ, PRINT, END, EXPONENT, NAME, VARIABLE, LETTER, UNSIGNED_INTEGER,
              INTEGER, SIGNED_INTEGER,
              INTEGER_VARIABLE, REAL_VARIABLE, STRING_VARIABLE, REM, SEMICOLON
              }

    # IGNORE SPACES
    ignore = '\t '

    literals = {'=', '/', '*', '(', ')'}
    # (?i) CASE INSENSITIVE
    # Define tokens, regular Expression Rules for tokens.
    ARROW = r'->'
    GT = r'\.GT\.'
    LT = r'\.LT\.'
    EQ = r'\.EQ\.'
    GE = r'\.GE\.'
    LE = r'\.LE\.'
    NE = r'\.NE\.'
    OR = r'\.OR\.'
    AND = r'\.AND\.'
    NOT = r'\.NOT\.'
    ADD = r'\.ADD\.'
    SUB = r'\.SUB\.'
    MUL = r'\.MUL\.'
    DIV = r'\.DIV\.'
    END = r'END\.'
    DECIMAL_PART = r'\.+\d+'
    DECIMAL_POINT = r'^(\.)$'  # \.
    UNSIGNED_REAL = r'\d+\.\d+|\d+\.'
    REAL = r'\-\d+\.\d+|\+\d+\.\d+|\-\d+\.|\+\d+\.'
    UNSIGNED_INTEGER = r'\d+|\d'
    INTEGER = r'\+\d+|\d|\-\d+|\d'
    DIGIT = r'\d'
    SIGNED_INTEGER = r'\+\d|\-\d'
    POSITIVE_SIGN = r'\+'
    NEGATIVE_SIGN = r'\-'
    ELSE = r'(?i)ELSE'
    FOR = r'FOR'
    FUN = r'FUN'
    TO = r'TO'
    COMMA = r'\,'
    EQEQ = r'=='
    STRING = r'\".*?\"'
    IF = r'IF'
    THEN = r'THEN'
    READ = r'READ'
    PRINT = r'PRINT'
    REM = r'REM'
    EXPONENT = r'[e|E]'
    LETTER = r'[a-zA-Z]$'
    VARIABLE = r'[a-zA-Z][0-9_]$'
    # any character including a newline(character)
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    SEMICOLON = r'\;'

    def DECIMAL_POINT(self, t):
        t.value = "DECIMAL POINT"
        return t

    def DECIMAL_PART(self, t):
        t.value = float(t.value)
        return t

    # ---- CONDITIONAL TOKENS SECTION ----
    def GT(self, t):
        t.value = "RELATIONAL OPERATOR"
        return t

    def LT(self, t):
        t.value = "RELATIONAL OPERATOR"
        return t

    def EQ(self, t):
        t.value = "RELATIONAL OPERATOR"
        return t

    def GE(self, t):
        t.value = "RELATIONAL OPERATOR"
        return t

    def LE(self, t):
        t.value = "RELATIONAL OPERATOR"
        return t

    def NE(self, t):
        t.value = "RELATIONAL OPERATOR"
        return t

    def OR(self, t):
        t.value = "LOGICAL OPERATOR"
        return t

    def AND(self, t):
        t.value = "LOGICAL OPERATOR"
        return t

    def NOT(self, t):
        t.value = "LOGICAL OPERATOR"
        return t
    
    # ---- END OF CONDITIONAL TOKENS SECTION ----

    # ---- ARITHMETIC TOKENS SECTION ----
    def ADD(self, t):
        t.value = "ARITHMETIC OPERATOR"
        return t

    def SUB(self, t):
        t.value = "ARITHMETIC OPERATOR"
        return t

    def MUL(self, t):
        t.value = "ARITHMETIC OPERATOR"
        return t

    def DIV(self, t):
        t.value = "ARITHMETIC OPERATOR"
        return t
    
    # ---- END OF ARITHMETIC TOKENS SECTION ----

    # IF STATMENT TOKEN
    def IF(self, t):
        t.value = "KEYWORD"
        return t

    # THEN STATEMENT TOKEN
    def THEN(self, t):
        t.value = "KEYWORD"
        return t

    # READ USER INPUT TOKEN
    def READ(self, t):
        t.value = "KEYWORD"
        return t

    # PRINT STATEMENT TOKEN
    def PRINT(self, t):
        t.value = "KEYWORD"
        return t

    # REM COMMENT STATEMENT
    def REM(self, t):
        pass
        return t

    # EXIT PROGRAM TOKEN
    def END(self, t):
        t.value = "KEYWORD"
        return t

    # INDIVIDUAL LETTER TOKENS
    def LETTER(self, t):
        return t

    # VARIABLE TOKEN FOR ASSIGMENTS
    def VARIABLE(self, t):
        return t

    def NAME(self, t):
        return t

    def EXPONENT(self, t):
        t.value = "EXPONENT"
        return t

    # ---- DATA TYPES DEPENDING ON VARIABLE NAME ----
    def UNSIGNED_INTEGER(self, t):
        t.value = int(t.value)
        return t

    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    def UNSIGNED_REAL(self, t):
        t.value = float(t.value)
        return t

    def REAL(self, t):
        t.value = float(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')

    # HOW ERRORS ARE DETECTED WHEN ANALYZING TOKENS
    def error(self, t):
        print('Line %d: Illegal character %r at index %s' %
              (self.lineno, t.value[0], self.index))
        self.index += 1


if __name__ == '__main__':
    lexer = LAOLexer()
    env = {}
    while True:
        try:
            text = input('LEXER > ')
        except EOFError:
            break
        #  To ignore all Comments
        if text:
            try:
                lex = lexer.tokenize(text)
                for token in lex:
                    print(token)
            except Exception as ex:
                print(ex)
