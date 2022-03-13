def zero(func = None): return 0 if func == None else eval(f'0{func[0]}{func[1]}')
def one(func = None): return 1 if func == None else eval(f'1{func[0]}{func[1]}')
def two(func = None): return 2 if func == None else eval(f'2{func[0]}{func[1]}')
def three(func = None): return 3 if func == None else eval(f'3{func[0]}{func[1]}')
def four(func = None): return 4 if func == None else eval(f'4{func[0]}{func[1]}')
def five(func = None): return 5 if func == None else eval(f'5{func[0]}{func[1]}')
def six(func = None): return 6 if func == None else eval(f'6{func[0]}{func[1]}')
def seven(func = None): return 7 if func == None else eval(f'7{func[0]}{func[1]}')
def eight(func = None): return 8 if func == None else eval(f'8{func[0]}{func[1]}')
def nine(func = None): return 9 if func == None else eval(f'9{func[0]}{func[1]}')

def plus(func): return '+', func
def minus(func): return '-', func
def times(func): return '*', func
def divided_by(func): return '/', func
print(seven(minus(five())))