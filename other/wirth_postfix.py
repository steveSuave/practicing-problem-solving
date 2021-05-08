# Convert a simple expression into its corresponding postfix form

# expression = term {("+"|"-") term}.
# term       = factor {("*"|"/") factor}.
# factor     = letter | "(" expression")"|"[" expression "]".

theinput=""
i = -1; j = 0
ch = ""

def expression():
    global ch
    def term():
        global ch
        def factor():
            global ch
            if ch == "(":
                ch = readch()
                expression()
                while ch != ")":
                    ch = readch()
            elif ch == "[":
                ch = readch()
                expression()
                while ch != "]":
                    ch = readch()
            else:
                while ch < "a" or ch > "z":
                    ch = readch()
                print(ch, end = "")
            ch = readch()
        # term
        factor()
        while ch == "*" or ch == "/":
            mulop = ch
            ch = readch()
            factor()
            print(mulop, end = "")
    # expression
    term()
    while ch == "+" or ch == "-":
        addop = ch
        ch = readch()
        term()
        print(addop, end = "")

def readch():
    global i, j
    i += 1; j += 1
    return theinput[i:j]

def parse(s):
    global i, j, ch, theinput
    theinput = s
    ch = readch()
    while j <= len(s):
        expression()
        print()
        ch = readch()
    i = -1; j = 0


parse("a+b")          # ab+
parse("a*b+c")        # ab*c+
parse("a+b*c")        # abc*+
parse("a*(b/[c-d])")  # abcd-/*
