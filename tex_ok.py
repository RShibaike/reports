fo = open('8.tex_fix/14/14-2.tex', 'w', encoding='utf-8', newline='\n')

fo.write("\\documentclass[twoside]{jsarticle}\n")
fo.write("\\usepackage[dvipdfmx,hidelinks]{hyperref}\n")
fo.write("\\usepackage{pxjahyper}\n")
fo.write("\\usepackage[jis2004]{otf}\n")
fo.write("\\usepackage[dvipdfmx]{graphicx}\n")
fo.write("\\usepackage{url}\n")
fo.write("\\setcounter{page}{1}\n")
fo.write("\\usepackage{fancyhdr}\n")
fo.write("\\begin{document}\n")

fo.write(
    "\\title{None}\n\\author{None班\quad None}\n\\date{}\n\\maketitle\n\\tableofcontents\n\\clearpage\n")

fo.write("\\pagestyle{fancy}\n\\lhead[]{}\n\\rhead[]{\\leftmark}\n")

with open('7.tex_ori/14-2.tex', mode='r', encoding='utf-8') as fi:
    for line in fi:
        line = line.replace("①", "\\UTF{2460}")
        line = line.replace("②", "\\UTF{2461}")
        line = line.replace("③", "\\UTF{2462}")
        line = line.replace("④", "\\UTF{2463}")
        line = line.replace("⑤", "\\UTF{2464}")
        line = line.replace("⑥", "\\UTF{2465}")
        line = line.replace("⑦", "\\UTF{2466}")
        line = line.replace("⑧", "\\UTF{2467}")
        line = line.replace("⑨", "\\UTF{2468}")
        line = line.replace("⑴", "\\ajKakko{1}")
        line = line.replace("⑵", "\\ajKakko{2}")
        line = line.replace("⑶", "\\ajKakko{3}")
        line = line.replace("⑷", "\\ajKakko{4}")
        line = line.replace("⑸", "\\ajKakko{5}")
        line = line.replace("⑹", "\\ajKakko{6}")
        line = line.replace("Ⅰ", "\\ajRoman{1}")
        line = line.replace("Ⅱ", "\\ajRoman{2}")
        line = line.replace("Ⅲ", "\\ajRoman{3}")
        line = line.replace("Ⅳ", "\\ajRoman{4}")
        line = line.replace("Ⅴ", "\\ajRoman{5}")
        line = line.replace("Ⅵ", "\\ajRoman{6}")
        line = line.replace("<", "\\textless")
        line = line.replace(">", "\\textgreater")
        fo.write(line)

fo.write("\\end{document}")

fo.close()
