"""
Etapa 1 - Situación Problema 1: Resaltador de sintaxis

A01753179  Abner Maximiliano Lecona Nieves 
---------------------------------------------------------
S -> var '=' E C
E -> A B
A -> (E) | var | float | int
B - > op E B | 𝜀
C -> com | 𝜀
"""

import re
from termcolor import colored
 
def tokenizer(line):
    float_re = re.compile(r'\d*\.\d*')
    int_re = re.compile(r'\d+')
    op_re = re.compile(r'[+\-*/^]')
    var_re = re.compile(r'[a-zA-Z]+\w*')
    equal_re = re.compile(r'\=')
    opar_re = re.compile(r'\(')
    cpar_re = re.compile(r'\)')
    
    i = 0
    while i < len(line):
        if line[i].isspace():
            i += 1
            continue        
        if line[i:i+2] == '//':
            tokens.append(('com', line[i:].strip()))
            break        
        match = None
        for regex, token_type in [(float_re, 'float'), (int_re, 'int'), (op_re, 'op'), (var_re, 'var'), (equal_re, '='), (opar_re, '('), (cpar_re, ')')]:
            match = regex.match(line[i:])
            if match:
                tokens.append((token_type, match.group()))
                i += len(match.group())
                break      
        if not match:
            raise Exception()

#S -> var '=' E C
def S():
    if t < len(tokens):
        if tokens[t][0] == 'var':
            match('var')
            match('=')
            E() 
            C()
        else:
            raise Exception

#E -> A B
def E():
    if t < len(tokens):
        A()
        B()

#A -> (E) | var | float | int
def A():
    if t < len(tokens):
        if tokens[t][0] == '(':
            match('(')
            E()
            match(')')
        elif tokens[t][0] == 'var':
            match('var')
        elif tokens[t][0] == 'float':
            match('float')
        elif tokens[t][0] == 'int':
            match('int')
        else:
            raise Exception

#B - > op E B | 𝜀
def B():
    if t < len(tokens):
        if tokens[t][0] == 'op':
            match('op')
            E()
            B()
        else:
            pass

#C -> com | 𝜀
def C():
    if t < len(tokens):
        if tokens[t][0] == 'com':
            match('com')
        else: 
            pass
 
def match(c):
    global t
    if t < len(tokens) and tokens[t][0] == c:
        t += 1
    else:
        raise Exception

def colorize_tokens(tokens):
    tag_map = {
        'float': 'span class="float"',
        'int': 'span class="int"',
        'op': 'span class="op"',
        'var': 'span class="var"',
        '=': 'span class="asig"',
        '(': 'span class="opb"',
        ')': 'span class="opc"',
        'com': 'span class="com"',
    }

    result = ''
    for token_type, token_value in tokens:
        tag = tag_map.get(token_type, 'span') 
        result += f'<{tag}>{token_value}</span>'
    return result



def start(file_path):
    global tokens
    global t
    tokens = []
    t = 0
    with open(file_path, 'r') as file:
        with open('output.html', 'w') as output_file:
            output_file.write('<html lang="en">\n<head>\n<title>Etapa 1</title>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\n<style>\n')
            output_file.write('.error { text-decoration: underline red; }\n')
            output_file.write('.float { color: blue; }\n')
            output_file.write('.int { color: green; }\n')
            output_file.write('.op { color: cyan; }\n')
            output_file.write('.var { color: yellow; }\n')
            output_file.write('.com { color: purple;}\n')
            output_file.write('.asig {color: magenta;}\n')
            output_file.write('.opb {color: orange;}\n')
            output_file.write('.opc {color: orange;}\n')
            output_file.write('body { font-family: Arial; white-space: pre; background-color: black; color: white}\n')
            output_file.write('</style>\n</head>\n<h1>Etapa 1 - Situación Problema 1: Resaltador de sintaxis</h1>\n<body class="w3-container w3-pale-white">\n<p>A01753179 &nbsp;Abner Maximiliano Lecona Nieves <br>A01754887 &nbsp;Ernesto Juárez Torres <br>A01748640 &nbsp;Juan Carlos Carro Cruz</p>\n')
            for line in file:
                try:
                    tokenizer(line)
                    S()
                    if t < len(tokens):
                        raise Exception
                    output_file.write(colorize_tokens(tokens) + '<br>\n')
                except Exception:
                    output_file.write('<span class="error">' + line.strip() + '</span><br>\n')
                tokens = []
                t = 0
            output_file.write('</body>\n</html>')

start('syntax_test.txt')
