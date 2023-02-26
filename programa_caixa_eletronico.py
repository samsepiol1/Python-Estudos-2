print('='*30)
print('{:^30}'.format('BANCO E-CORP'))
print('='*30)
saque=int(input('QUAL O VALOR DO SAQUE?:'))
total=saque
ced=100
total_ced=0
while True:
 if total>=ced:
    total=total-ced
    total_ced=total_ced+1
 else:
    print(f'TOTAL DE {total_ced} CEDULAS DE R${ced}')
    if ced==100:
        ced=50
    elif ced==50:
        ced=10
    elif ced==10:
        ced=5
    elif ced==5:
        ced=1
    total_ced=0
    if total==0:
       break






