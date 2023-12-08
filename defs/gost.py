from docx import Document

def write_to_docx(text, file_path):
    try:
        document = Document(file_path)
    except:
        document = Document()
    
    document.add_paragraph(text)
    document.save(file_path)  
    

def module(a):
    if a >= 0:
        return a
    else:
        return a - 2 * a

def MinusOneMod(exp, fi, filename):
    write_to_docx('---промежуточный расчет {} ^-1 mod {} ---'.format(exp, fi), filename)
    x = pow(exp, -1, fi)
    write_to_docx(f'ПОЛУЧИЛИ: {x}---промежуточный расчет закончен---', filename)
    return x

def findDotMainFunc(x, y, a, f, c, file_name):
    resX = x
    resY = y
    l = []
    l.append([x, y])
    for i in range(0, c):
        write_to_docx('Рассчет {}А:'.format(i + 1), file_name)
        write_to_docx('{}A + A = ({},{}) + ({},{})'.format(i + 1, resX, resY, x, y), file_name)
        if i == 0:
            p = module(a)
            ch = pow(3 * resX ** 2 - p, 1, f)
            write_to_docx('(3x^2 - p) mod F = (3*{}^2 + ({}) )mod {} = {}'.format(x, a, f, ch), file_name)
            zn = MinusOneMod(pow(2 * resY, 1, f), f, file_name)
            res = pow(ch * zn, 1, f)
            write_to_docx('lambda = ((3x^2 + а )/ 2y) mod F = ({} * {}) mod {} = {}'.format(ch, zn, f, res), file_name)
            resXPrev = resX
            resYPrev = resY
            resX = pow(res ** 2 - 2 * x, 1, f)
            resY = pow(-y + res * (x - resX), 1, f)
            write_to_docx('X{} = lambda^2 -2x mod F = {} mod {} = {}'.format(i + 1, res ** 2 - 2 * x, f, resX), file_name)
            write_to_docx('Y{} = -y + lambda*(X - X{}) mod F = {} mod {} = {}'.format(i + 1, i + 1,-y + res * (x - resX), f, resY), file_name)
            l.append([resX, resY])
        elif i >= 1:
            if resX == x:
                write_to_docx('x2 = x1 => деление на 0', file_name)
                write_to_docx('Значит, -Y0 == Y{} mod {}'.format(i, f), file_name)
                l.append(0)
                break
            ch = pow(resY - y, 1, f)
            write_to_docx('y{} - y{} mod F = ({} - {}) mod {} = {}'.format(i + 1, i, resY, y, f, ch), file_name)
            zn = MinusOneMod(pow(resX - x, 1, f), f, file_name)
            write_to_docx('(x{} - x{})^-1 mod F = ({} - {})^-1 mod {} = {}'.format(i + 1, i, resX, x, f, zn), file_name)
            res = pow(ch * zn, 1, f)
            write_to_docx('lambda = ({} * {}) mod {} = {}'.format(ch, zn, f, res), file_name)
            resXPrev = resX
            resYPrev = resY
            resX = pow(res ** 2 - resX - x, 1, f)
            resY = pow(-resY + res * (resXPrev - resX), 1, f)
            write_to_docx('X{} = (lambda^2 - x{} - x{}) mod F = ({} - ({}) - ({}))mod {} = {}'
                  .format(i + 1, i, x, res ** 2, resXPrev, x, f, resX), file_name)
            write_to_docx('Y{} = (-y{} + lambda*(X{} - X{})) mod F = ({} + {}) mod {} = {}'
                  .format(i + 1, i, i , i+1, -resYPrev, res * (resXPrev - resX), f, resY), file_name)
            l.append([resX, resY])
        write_to_docx('{}A + A = ({},{}) + ({},{}) = ({},{})'.format(i + 1,resXPrev, resYPrev, x, y,  resX, resY), file_name)
    return l


def gost(m, a, b, f, g_1, g_2, n, q_1, q_2, k, file_name):

    x = g_1
    y = g_2
    e = q_1
    d = q_2

    p = module(a)
    write_to_docx(f'Из у-я ЭП: p = {p}', file_name)
    write_to_docx('С = k*G = {}*G ='.format(k), file_name)

    c = findDotMainFunc(x, y, a, f, k - 1, file_name)
    c = c[len(c) - 1]
    write_to_docx(f'Откуда с = {c}', file_name)
    write_to_docx('\nНайдем закрытый ключ:\nq = d*G = ({},{}) = d*({},{})'.format(e, d, x, y), file_name)
    i = 1
    temp1 = x
    temp2 = y
    write_to_docx(f'{d}, {e}', file_name)
    while(e != temp1 or d != temp2):
        ans = findDotMainFunc(x,y , a, f, i, file_name)
        temp1 = ans[len(ans) - 1][0]
        temp2 = ans[len(ans) - 1][1]
        i += 1
    d = i
    write_to_docx(f"d = {d}", file_name)
    Sy = pow(c[0]*d + k * m ,1, n)
    write_to_docx('\nНайдем эл.подпись s: (Sy = ) (Xc*d + k*m) mod n = ({}*{} + {}*{}) mod {} = {}'
        .format(c[0], d, k, m, n, Sy), file_name)
    
    write_to_docx('\nОтвет: ({},{})'.format(c[0], Sy), file_name)
    
gost(5, -8, -5, 11, 8, 5, 15, 2, 3, 2, "gost_test.docx")