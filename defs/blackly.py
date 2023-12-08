from docx import Document

def write_to_docx(text, file_path):
    try:
        document = Document(file_path)
    except:
        document = Document()
    
    document.add_paragraph(text)
    document.save(file_path)   


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

def minusOneMod(exp, fi, filename):
    write_to_docx('---промежуточный расчет {} ^-1 mod {} ---'.format(exp, fi), filename)
    if fi == 0:
        write_to_docx('Нельзя брать по модулю 0', filename)
        exit(0)
    if exp == 1:
        write_to_docx('1 mod {} = 1'.format(fi), filename)
        write_to_docx('---промежуточный расчет закончен---', filename)
        return 1
    if exp == 0:
        return 0
    r = 0
    q = 0
    y = [0, 1]
    mod = fi
    coef_first = 0
    coef_second = 1

    write_to_docx('Запишем в таблице: (Элементы в () можно не писать)', filename)
    write_to_docx('(Запишем y в столбце справа:)', filename)
    write_to_docx('y[-2] =' + str(y[0]), filename)
    write_to_docx('y[-1] =' + str(y[1]), filename)

    while r != 1:
        q = fi // exp
        r = fi % exp
        y.append(y[coef_first] - y[coef_second] * q)
        write_to_docx(
            '{} = (q{}){}*{} + r({}){} ,посчитаем y({}) = y({}){} - y({}){}*q({}){} = {}'
                .format(fi, coef_first, q, exp,coef_first, r, coef_first, coef_first - 2, y[coef_first],
                        coef_second - 2, y[coef_second], coef_first, q, y[coef_second + 1]), filename)
        fi = exp
        exp = r
        coef_first += 1
        coef_second += 1

    y[coef_second] %= mod
    write_to_docx('---промежуточный расчет закончен---', filename)
    return y[coef_second]

def Gauss_finite(A, F, p, filename):
    n = len(A)
    write_to_docx("Применяем алгоритм Гаусса для решения, прямой ход:", filename)
    a = np.hstack((A,F)) #делаем расширенную матрицу 
    write_to_docx(str(a), filename)
    for i in range (n):          #прямой ход
        write_to_docx(f"a[{i}][{i}]^-1 = {minusOneMod(a[i][i], p, filename)}", filename)
        a[i] *= minusOneMod(a[i][i], p, filename)
        a[i] = a[i] % p
        write_to_docx("После умножения коэффециенты такие:" + str(a[i]), filename)
        for j in range (i + 1, n):
            write_to_docx(f"Вычитаем из {j}-й строчки {i}-ю", filename)
            a[j] -= a[i] * a[j][i]
            a[j] = a[j] % p
            write_to_docx(f"После вычитания из {j}-й строчки {i}-й: коэффициенты следующие ", filename)
            write_to_docx(str(a[j]), filename)


    write_to_docx("Обратный ход: ", filename)
    for i in range (n - 1, -1, -1):  #обратный ход
        for j in range (i - 1, -1, -1):
            # print("i,j", i,j)
            write_to_docx(f"После подставления в {j}-ю строчку {i}-й: коэффициенты следующие ", filename)
            a[j] -= a[i] * a[j][i]
            a[j] = a[j] % p
            write_to_docx(str(a[j]), filename)
    # print(a)

    ans = []
    for i in range (n):
        ans.append(-a[i][n] % p)
    return ans


def blackly(p, n, numbers_in_sled, two_dimension, filename):
    a = numbers_in_sled
    arr = two_dimension #np.asarray
    fs = np.zeros(a-1)
    fs = fs.reshape(a-1,1)
    write_to_docx('Берем {} любые суперплоскости из следов (все вычисления в F{}):'.format(a - 1, p), filename)
    for i in range(0, a - 1):
        for j in range (0, a):
            if j != a - 1:
                write_to_docx('{} * x{} + '.format(arr[i][j], j + 1) + str("здесь нет переноса строки"), filename)
            if j == a - 1:
                write_to_docx(str(arr[i][j]) + str(" здесь нет переноса строки"), filename)
        write_to_docx(' = 0', filename)

    write_to_docx('Выразив коэффициенты получаем:', filename)
    ans = Gauss_finite(arr, fs, p, filename)
    for i in range(a-1):
        write_to_docx(f'x{i+1} = {ans[i]}', filename)
    return ans

blackly(11, 4, 4, [[5, 10, 3, 4], [6, 7, 8, 3], [6,8,7,8]],"blackly_test.docx")