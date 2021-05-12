import time
delers = []
while True:
    getal=int(input("Typ het getal dat u wilt ontbinden in priemfactoren: "))
    start=time.time()
    for k in range(2, int(getal+1), 1):
        while getal%k == 0:
            delers.append(k)
            getal= getal/k
    end=time.time()
    timer=end-start
    print("Delers: " + str(delers))
    print("Tijd: " + str(timer) + " seconden")
    delers.clear()
