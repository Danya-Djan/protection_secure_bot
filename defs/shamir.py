from docx import Document

def write_to_docx(text, file_path):
    try:
        document = Document(file_path)
    except:
        document = Document()
    
    document.add_paragraph(text)
    document.save(file_path)   

print('Введите модуль схемы Шамира p:')
p = int(input())
print('Введите первый многочлен (два числа первого следа через пробел):')
x1 = int(input())
y1 = int(input())
print('Введите второй многочлен:')
x2 = int(input())
y2 = int(input())
print('Введите третий многочлен:')
x3 = int(input())
y3 = int(input())

def minusOneMod(exp, fi):
    if fi == 0:
        print('Нельзя брать по модулю 0')
        exit(0)
    if exp == 1:
        return 1
    if exp == 0:
        return 0
    r = 0
    q = 0
    y  = [0, 1]
    mod = fi
    coef_first = 0
    coef_second = 1
    while r != 1:
        q = fi // exp
        r = fi % exp
        y.append(y[coef_first] - y[coef_second]*q)
        fi = exp
        exp = r
        coef_first += 1
        coef_second += 1
    y[coef_second] %= mod
    return y[coef_second]

arr = []

print('F(X) = Σl  li(x)yi\nli(x) = ∏j  x - xj/ xi - xj')

print('l1(x) = (x - x2)/(x1 - x2) * (x - x3)/(x1 - x3) = (x - {})/({} - {}) * (x - {})/({} - {}) ='
      .format(x2, x1, x2, x3, x1, x3))
znam = pow((x1- x2)*(x1-x3), 1, p)
a = 1
b = pow(-x2 -x3, 1, p)
c = pow((-x2)*(-x3),1 , p)
print('=1/{} * (({})x^2 + ({})x + {}) ='.format(znam,a, b, c))
znam = minusOneMod(znam, p)
a = pow(a*znam, 1, p)
b = pow(b*znam, 1, p)
c = pow(c*znam, 1, p)
print('=(({})x^2 + ({})x + {}'.format(a, b, c))
arr.append([a, b, c])

print('l2(x) = (x - x1)/(x2 - x1) * (x - x3)/(x2 - x3) = (x - {})/({} - {}) * (x - {})/({} - {}) ='
      .format(x1, x2, x1, x3, x2, x3))
znam = pow((x2 - x1)*(x2 - x3), 1, p)
a = 1
b = pow(-x1 -x3, 1, p)
c = pow((-x1)*(-x3),1 , p)
print('=1/{} * (({})x^2 + ({})x + {}) ='.format(znam,a, b, c))
znam = minusOneMod(znam, p)
a = pow(a*znam, 1, p)
b = pow(b*znam, 1, p)
c = pow(c*znam, 1, p)
print('=(({})x^2 + ({})x + {}'.format(a, b, c))
arr.append([a, b, c])

print('l3(x) = (x - x1)/(x3 - x1) * (x - x2)/(x3 - x2) = (x - {})/({} - {}) * (x - {})/({} - {}) ='
      .format(x1, x3, x1, x2, x3, x2))
znam = pow((x3 - x1)*(x3 - x2), 1, p)
a = 1
b = pow(-x1 -x2, 1, p)
c = pow((-x1)*(-x2),1 , p)
print('=1/{} * (({})x^2 + ({})x + {}) ='.format(znam,a, b, c))
znam = minusOneMod(znam, p)
a = pow(a*znam, 1, p)
b = pow(b*znam, 1, p)
c = pow(c*znam, 1, p)
print('=(({})x^2 + ({})x + {}'.format(a, b, c))
arr.append([a, b, c])

a = pow(arr[0][0]*y1 + arr[1][0]*y2 + arr[2][0]*y3, 1, p)
print('a = {}y1 + {}y2 + {}y3 = {}*{} + {}*{} + {}*{} = {} mod {} = {}'
      .format(arr[0][0], arr[1][0], arr[2][0], arr[0][0], y1, arr[1][0], y2, arr[2][0], y3, arr[0][0]*y1 + arr[1][0]*y2 + arr[2][0]*y3, p , a))

b = pow(arr[0][1]*y1 + arr[1][1]*y2 + arr[2][1]*y3, 1, p)
print('b = {}y1 + {}y2 + {}y3 = {}*{} + {}*{} + {}*{} = {} mod {} = {}'
      .format(arr[0][1], arr[1][1], arr[2][1], arr[0][1], y1, arr[1][1], y2, arr[2][1], y3, arr[0][1]*y1 + arr[1][1]*y2 + arr[2][1]*y3, p , b))

M = pow(arr[0][2]*y1 + arr[1][2]*y2 + arr[2][2]*y3, 1, p)
print('M = {}y1 + {}y2 + {}y3 = {}*{} + {}*{} + {}*{} = {} mod {} = {}'
      .format(arr[0][2], arr[1][2], arr[2][2], arr[0][2], y1, arr[1][2], y2, arr[2][2], y3, arr[0][2]*y1 + arr[1][2]*y2 + arr[2][2]*y3, p , M))

print('Ответ будет вида ax^2 + bx + m = {}x^2 + {}x + {} <= последний член - секрет'.format(a, b, M))



