X=['O','L','M','S','N','J','P','T','I','R','H','G']
Y=['S','N','H','P','T','I','O','R','L','M','G','J']
pair=list(set(X) & set(Y))
for i in pair:
    print("X[",X.index(i),"]=Y[",Y.index(i),"]")


    

