class Other:
    def __init__(self, content):
        self.content = content

class Braced:
    def __init__(self, inner):
        self.inner = inner

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

class Sequence:
    def __init__(self, elements):
        self.elements = elements

expr_str = ""
pos = 0
S = 0
D = 0

def skip_spaces():
    global pos
    while pos < len(expr_str) and expr_str[pos] == ' ':
        pos += 1

def parse_expression(end_char=None):
    global pos
    elements = []
    while pos < len(expr_str) and (end_char is None or expr_str[pos] != end_char):
        elements.append(parse_element())
    return Sequence(elements)

def parse_element():
    global pos
    skip_spaces()
    if pos < len(expr_str) and expr_str.startswith(r"\frac", pos):
        return parse_fraction()
    elif pos < len(expr_str) and expr_str[pos] == '{':
        return parse_braced()
    else:
        return parse_other()

def parse_fraction():
    global pos
    pos += len(r"\frac")
    numerator = parse_fraction_body(is_numerator=True)
    denominator = parse_fraction_body(is_numerator=False)
    return Fraction(numerator, denominator)

def parse_fraction_body(is_numerator):
    global pos
    skip_spaces()
    if pos < len(expr_str) and expr_str[pos] == '{':
        pos += 1
        node = parse_expression(end_char='}')
        pos += 1
        return node
    else:
        ch = expr_str[pos]
        pos += 1
        return Other(ch)

def parse_braced():
    global pos
    pos += 1
    node = parse_expression(end_char='}')
    pos += 1
    return Braced(node)

def parse_other():
    global pos
    start = pos
    while pos < len(expr_str) and expr_str[pos] not in " {}\\":
        pos += 1
    content = expr_str[start:pos]
    return Other(content)

def compute(node):
    if isinstance(node, Other):
        return (S, 0, False)
    if isinstance(node, Braced):
        return compute(node.inner)
    if isinstance(node, Fraction):
        t_num, b_num, hf_num = compute(node.numerator)
        t_den, b_den, hf_den = compute(node.denominator)
        top_eff = t_num if hf_num else S
        bottom_eff = b_den if hf_den else S
        return (top_eff, bottom_eff, True)
    if isinstance(node, Sequence):
        has_frac = False
        top_val = 0
        bottom_val = 0
        for el in node.elements:
            t, b, hf = compute(el)
            if hf:
                has_frac = True
                if t > top_val:
                    top_val = t
                if b > bottom_val:
                    bottom_val = b
            else:
                if S > top_val:
                    top_val = S
        if has_frac:
            return (top_val, bottom_val, True)
        else:
            return (S, 0, False)
    return (S, 0, False)

def solve():
    global expr_str, pos, S, D
    parts = input().split()
    S = int(parts[0])
    D = int(parts[1])
    expr_str = input().rstrip()
    pos = 0
    ast = parse_expression()
    top, bottom, hf = compute(ast)
    height = top + D + bottom if hf else S
    print(height)

if __name__ == '__main__':
    solve()
