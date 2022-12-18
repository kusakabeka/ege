def F( n ):
    s = '*'
    print(s)
    if n >= 1:
        print(s)
        F(n-1)
        F(n//3)
        print(s)

    s.replace('8', '1')

F(280)