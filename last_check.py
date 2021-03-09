cnt = 1
with open('8.tex_fix/D2/D2.tex', mode='r', encoding='utf-8') as fi:
    for line in fi:
        if "<" in line:
            print("<:"+str(cnt))
        if ">" in line:
            print(">:"+str(cnt))
        if "textsuperscript" in line:
            print("tsup:"+str(cnt))
        if "textsubscript" in line:
            print("tsub:"+str(cnt))
        if "quote" in line:
            print("q:"+str(cnt))
        if "http" in line:
            print("http:"+str(cnt))
        if "~" in line:
            print("~"+str(cnt))
        if "textasciitilde" in line:
            print("～2"+str(cnt))

        cnt += 1
