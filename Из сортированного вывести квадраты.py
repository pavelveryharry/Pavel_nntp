vvod = [int(a) for a in input().split()] # ввод строки
posit = []
negat = []
for i in range(len(vvod)): # сортируем: из положительных и отрицательных
    if vvod[i]>=0:          # делаем два разных списка
        posit.append(vvod[i]**2)
    else:
        negat.append(vvod[i]**2)
negat = negat[::-1]
ind_negat = 0
ind_posit = 0
answer = []
while len(answer) != len(vvod): # пока не заполним ответ целиком, т.е. не возьмём все элементы
    if negat[ind_negat] >= posit[ind_posit]:
        answer.append(posit[ind_posit])
        if ind_posit != len(posit)-1:
            ind_posit += 1
        else:
            answer.extend(negat[ind_negat:]) # если элементы одного массива кончились, добавляем в ответ числа из другого
    else:
        answer.append(negat[ind_negat])
        if ind_negat != len(negat)-1:
            ind_negat += 1
        else:
            answer.extend(posit[ind_posit:])
print(*answer)

print('positive',*posit)
print('negative',*negat)