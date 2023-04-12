mad1,mad2=0,0 # максимальное количество делителей
for n in range(586132, 586430+1):
	divs=[d for d in range(n,0,-1) if n%d==0] # "divs"- массив делителей числа n (от n до 1)
	if len(divs)>mad1:
		mad1=len(divs)
madivs1=divs
if len(divs)>=mad2: # нестрогое неравенство
mad2=len(divs)
madivs2=divs
print(mad1,*madivs1)
print(mad2,*madivs2)
print('Ответ:')
print(mad1,madivs1[1])
print(mad2,madivs2[1])

	