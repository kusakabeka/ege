print('w x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(w <= (not (x <= y)))) and ((not x) <= ((not y) == z))) == False:
                    if x + y +z+ w == 3:
                        print(x, y, z, w)
                        #y w z x