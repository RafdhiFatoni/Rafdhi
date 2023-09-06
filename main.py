print("====INPUT====")
arah = input("arah : ")
besar = input("besar : ")


print("====OUTPUT====")
if arah == "maju":
    print("maju")
    print(besar)
else:
    if arah == "mundur":
        print("mundur")
        print(besar)
    else:
        if arah == "kanan":
            print("kanan")
            print(besar)
        else:
            if arah == "kiri":
                 print("kiri")
                 print(besar)
            else:
                if arah == "atas":
                    print("atas")
                    print(besar)
                else:
                    if arah == "bawah":
                         print("bawah")
                         print(besar)
                    else:
                        if arah == "rcc":
                            print("rotate counter clockwise")
                            print(besar)
                        else:
                            if arah == "rc":
                                 print("rotate clockwise")
                                 print(besar)
                            else:
                                print("tidak valid")


        