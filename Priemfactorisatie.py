delers = []
while True:
    getal=int(input("Typ het getal dat u wilt ontbinden in priemfactoren: "))
    for k in range(2, int(getal+1), 1):
        while getal%k == 0:
            delers.append(k)
            getal= getal/k
    print(delers)
    delers.clear()
