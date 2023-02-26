a=80000
b=15000
anos=0
while(a<=b):
    a=a+a*0.03
    b=b+b*0.015
    anos=anos+1
print('A população A ultrapassa a população B em {}'.format(anos))

