import re


def str_to_list(str_exp):
    li_ch = re.split(r'\s*([()+*/-])\s*', str_exp)
    li_ch = list(filter((lambda el: el != ''), li_ch))
    li_zn = ['(', ')', '+', '*', '/', '-']
    li_ch = list(map((lambda el: float(el) if el not in li_zn else el), li_ch))

    return li_ch

def operation(math_operation, x, y):
    if math_operation == "+":
        return x + y
    elif math_operation == "-":
        return x - y
    elif math_operation == "/":
        return x / y
    elif math_operation == "*":
        return x * y

def calc(li_ch):
    while len(li_ch) > 1:
        while "/" in li_ch or "*" in li_ch:
            for el in li_ch:
                if el == '*' or el == '/':
                    res_i = li_ch.index(el)
                    li_ch[res_i - 1] = operation(el, li_ch[res_i - 1], li_ch[res_i + 1])
                    del li_ch[res_i:res_i + 2]

        while "+" in li_ch or "-" in li_ch:
            for el in li_ch:
                if el == '+' or el == '-':
                    res_i = li_ch.index(el)
                    li_ch[res_i - 1] = operation(el, li_ch[res_i - 1], li_ch[res_i + 1])
                    del li_ch[res_i:res_i + 2]

    return li_ch[0]

data = input('Введите выражение: ')
li_ch = str_to_list(data)
print(f'{data} = {calc(li_ch)}')
print(f'Расчет eval для проверки: {eval(data)}')