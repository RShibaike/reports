fo = open('3.text/2.txt', 'w', encoding='utf-8', newline='\n')


with open('2.markdown_ori/2.md', mode='r', encoding='utf-8') as fi:
    for line in fi:
        fo.write(line.lstrip("　"))

fo.close()
