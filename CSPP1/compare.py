varA=1234
varB="String"

if type(varA)==str or type(varB)==str:
    print("String is involved")
elif varA>varB:
    print("bigger")
elif varA==varB:
    print("equal")
else:
    print("smaller")
