import re

def w19():
    p = re.compile('\d{1,2}[-]\d|\d{1,2}[-][A-Z]')

    init = True
    with open('./19w.txt','r') as f:
        with open('./parsed/19w.txt','w') as w:
            for line in f:
                if line!='\n':
                    if p.match(line):
                        if init:
                            init = False
                            tmp = []
                        else:
                            w.write("".join(tmp)+"\n")
                            tmp = []
                    else:
                        tmp.append(line.replace('\n',''))
            w.write("".join(tmp))

def td19():
    p = re.compile('[A-Z]\w*')
    t = re.compile('Mini Test')
    ex = re.compile('Exercise \d{2}')

    with open('./19t_d.txt','r') as f:
        with open('./parsed/19td.txt','w') as w:
            for line in f:
                if line is not '\n':
                    if p.match(line) and not ex.match(line) and not t.match(line):
                        w.write(line)

if __name__ == "__main__":
    # w19()
    # td19()
