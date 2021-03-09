fo = open('3.text/6.txt', 'w', encoding='utf-8', newline='\n')


with open('2.markdown_ori/6.md', mode='r', encoding='utf-8') as fi:
    for line in fi:
        line = line.replace(">", "")
        line = line.lstrip("　")
        fo.write(line)

fo.close()
