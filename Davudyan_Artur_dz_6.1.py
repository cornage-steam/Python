f_logs = 'nginx_logs.txt'
f_trans = 'logs.txt'

q = []
with open(f_logs, 'r', encoding='utf-8') as logs:
    data = logs.read()
    for el in data.split('\n'):
        i = [i for i in el.split()]
        x = i[0], i[5], i[6]
        q.append(x)

print(q)