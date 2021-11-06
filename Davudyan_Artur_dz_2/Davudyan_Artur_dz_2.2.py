my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздух', 'была', '+5', 'градусов']
new_list = []
for item in my_list:
    number = ''
    diff1 = ''
    diff2 = ''
    for s in item:
        if s in '1234567890':
            number += s
        else:
            if number:
                diff2 += s
            else:
                diff1 += s
    if not number:
        new_list.append(item)
        continue
    nubmer = f'{diff1}{int(number):02d}{diff2}'
    new_list.append('"')
    new_list.append(nubmer)
    new_list.append('"')
print(new_list)
res = ' '.join(new_list)
print(res)
res2 = ''
i = 0
while i < len(res):
    if res[i] == '"' and i < len(res) - 3 and res[i + 1] == ' ' and res[i + 2] in '1234567890+-':
        res2 += '"'
        i += 1
    elif res[i] == '"' and i > 1 and res[i - 1] == ' ' and res[i - 2] in '1234567890':
        res2 = res2[:-1] + '"'
    else:
        res2 += res[i]
    i += 1
print(res2)



