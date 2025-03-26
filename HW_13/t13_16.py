class Var:
    def __init__(self, name):
        self.name = name

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# Precedence: Add = 1, Mul = 2, Var = 3.
def unparse(node, parent_prec):
    if isinstance(node, Var):
        prec = 3
        s = node.name
    elif isinstance(node, Mul):
        prec = 2
        s = unparse(node.left, prec) + unparse(node.right, prec)
    elif isinstance(node, Add):
        prec = 1
        s = unparse(node.left, prec) + "+" + unparse(node.right, prec)
    if prec < parent_prec:
        return "(" + s + ")"
    else:
        return s

def parse_E(s, i):
    node, i = parse_P(s, i)
    while i < len(s) and s[i] == '+':
        i += 1  # skip '+'
        right, i = parse_P(s, i)
        node = Add(node, right)
    return node, i

def parse_P(s, i):
    node, i = parse_F(s, i)
    while i < len(s) and (s[i].islower() or s[i] == '('):
        right, i = parse_F(s, i)
        node = Mul(node, right)
    return node, i

def parse_F(s, i):
    if s[i] == '(':
        i += 1
        node, i = parse_E(s, i)
        i += 1
        return node, i
    else:
        node = Var(s[i])
        i += 1
        return node, i

def parse_expression(s):
    node, i = parse_E(s, 0)
    return node

def solve():
    try:
        while True:
            line = input()
            if line is None:
                break
            line = line.strip()
            if line == "":
                continue
            ast = parse_expression(line)
            print(unparse(ast, 0))
    except EOFError:
        return

if __name__ == '__main__':
    solve()
