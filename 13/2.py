s = 'АБВГ БВД ВДЖ ГВЕ ЕЖК ЖЛ ДИЛ КЛ Л'
d = {w[0]: w[1:] for w in s.split()}
f = lambda a, b : (a == b) + sum(f(c, b) for c in d[a])
print(f(*'АЛ'))