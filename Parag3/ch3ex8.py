def gouhi(namae, kokugo, sansu, rika, syakai):
    print(namae, ":", end="")
    if kokugo>60:
        print("国語合格")
    else:
        print("国語不合格")
    if sansu>60:
        print("算数合格")
    else:
        print("算数不合格")
    if rika>60:
        print("理科合格")
    else:
        print("理科不合格")
    if syakai>60:
        print("社会合格")
    else:
        print("社会不合格")
    return

#クラスの定義