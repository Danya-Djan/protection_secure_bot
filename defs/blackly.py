def modifyArr(arr):
    arr[1][0] *= arr[0][1]
    arr[1][2] *= arr[0][1]
    arr[1][0] -= arr[0][0] * arr[1][1]
    arr[1][2] -= arr[0][2] * arr[1][1]
    arr[1][1] = 0
    return arr
import numpy as np

def Gauss(A, F):
    n = len(A)
    a = np.concatenate((A, F), axis = 1)  #делаем расширенную матрицу 
    for i in range (n):             #прямой ход
        a[i] /= a[i][i]
        for j in range (i + 1, n):
            a[j] -= a[i] * a[j][i]

    for i in range (n - 1, -1, -1):  #обратный ход
        for j in range (i - 1, -1, -1):
            a[j] -= a[i] * a[j][i]

    ans = []
    for i in range (n):
        ans.append(a[i][n])
    return ans

#exp^-1 mod fi
def minusOneMod(exp, fi):
    #print('---промежуточный расчет {} ^-1 mod {} ---'.format(exp, fi))
    if fi == 0:
        #print('Нельзя брать по модулю 0')
        exit(0)
    if exp == 1:
        #print('1 mod {} = 1'.format(fi))
        #print('---промежуточный расчет закончен---')
        return 1
    if exp == 0:
        return 0
    r = 0
    g = 0
    y  = [0, 1]
    mod = fi
    expAns = exp
    coef_first = 0
    coef_second = 1

    #print('Распишем в таблице: (Элементы в () можно не писать)')
    #print('(Запишем y в столбце справа:)')
    #print('y[-2] =', y[0])
    #print('y[-1] =', y[1])

    while r != 1:
        g = fi // exp
        r = fi % exp
        y.append(y[coef_first] - y[coef_second]*g)
        #print('{} = (g{}){}*{} + r({}){} ,посчитаем y({}) = y({}){} - y({}){}*g({}){} = {}'
        #      .format(fi, coef_first, g, exp, coef_first, r, coef_first, coef_first - 2,
        #              y[coef_first], coef_second - 2, y[coef_second], coef_first, g, y[coef_second + 1]))
        fi = exp
        exp = r
        coef_first += 1
        coef_second += 1
    y[coef_second] %= mod
    #print('Ответ {}^-1 mod {} = {}'.format(expAns, mod, y[coef_second]))
    return y[coef_second]

def Gauss_finite(A, F, p):
    n = len(A)
    print("Применяем алгоритм Гаусса для решения, прямой ход:")
    a = np.hstack((A,F)) #делаем расширенную матрицу 
    print(a)
    for i in range (n):          #прямой ход
        print(f"a[{i}][{i}]^-1 = {minusOneMod(a[i][i], p)}")
        a[i] *= minusOneMod(a[i][i], p)
        a[i] = a[i] % p
        print("После умножения коэффециенты такие:", a[i])
        for j in range (i + 1, n):
            print(f"Вычитаем из {j}-й строчки {i}-ю")
            a[j] -= a[i] * a[j][i]
            a[j] = a[j] % p
            print(f"После вычитания из {j}-й строчки {i}-й: коэффициенты следующие ")
            print(a[j])


    print("Обратный ход: ")
    for i in range (n - 1, -1, -1):  #обратный ход
        for j in range (i - 1, -1, -1):
            # print("i,j", i,j)
            print(f"После подставления в {j}-ю строчку {i}-й: коэффициенты следующие ")
            a[j] -= a[i] * a[j][i]
            a[j] = a[j] % p
            print(a[j])
    # print(a)

    ans = []
    for i in range (n):
        ans.append(-a[i][n] % p)
    return ans

print('Введите модуль p:')
p = int(input())
# p = 11
print('Введите количество следов:')
n = int(input())
# n = 4
print('Введите количество цифр в следе:')
a = int(input())
# a = 3
print('Введите любые {} следа (через enter):'.format(a-1))
arr = [[0] * a for i in range(a-1)]
arr = np.asarray(arr)
for i in range(0, a - 1):
    for j in range (0, a):
        arr[i][j] = int(input())
# arr[0][0] = 8
# arr[0][1] = 1
# arr[0][2] = 4
# # arr[0][3] = 6

# arr[1][0] = 9
# arr[1][1] = 8
# arr[1][2] = 10
# # arr[1][3] = 1

# arr[2][0] = 4
# arr[2][1] = 2
# arr[2][2] = 1
# # arr[2][3] = 2
fs = np.zeros(a-1)
fs = fs.reshape(a-1,1)
print('Берем {} любые суперплоскости из следов (все вычисления в F{}):'.format(a - 1, p))

for i in range(0, a - 1):
    for j in range (0, a):
        if j != a - 1:
            print('{} * x{} + '.format(arr[i][j], j + 1), end = '')
        if j == a - 1:
            print(arr[i][j], end='')
    print(' = 0')

print('Выразив коэффициенты получаем:')
ans = Gauss_finite(arr, fs, p)
for i in range(a-1):
  print(f'x{i+1} = {ans[i]}')