def permuta(s,s1=''):
    if len(s)==0:
        print(s1)
    else:
        for i in range(len(s)):
            permuta(s[:i]+s[i+1:],s1+s[i])
permuta('lucas')

