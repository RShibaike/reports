cnt = 1
with open('2.markdown_ori/13.md', mode='r', encoding='utf-8') as fi:
    for line in fi:
        if "<" in line:
            print(cnt)
        if ">" in line:
            print(cnt)
        if "textsuperscript" in line:
            print(cnt)

        cnt += 1

引用あるかみる！！
quate?
