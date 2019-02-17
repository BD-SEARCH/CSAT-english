# -*- coding: utf-8 -*-

import os
import re
from io import open


short_space = re.compile(r'[ ]{2,5}')
long_space = re.compile(r'[ ]{6,}')

os.makedirs('parsed', exist_ok=True)

with open('./parsed/19t.txt', 'w', encoding='utf-8') as outfile:
    with open('./19t.txt', 'rt', encoding='utf-8') as infile:
        prev_lines = ['', '', '']
        doc_state = False
        doc_lines = []

        while True:
            line = infile.readline()
            if line is None:
                break
            line = line.strip()

            del(prev_lines[0])
            prev_lines.append(line)

            if doc_state:
                if prev_lines[-1].startswith('①') or prev_lines[-1][:3] in ['[정답', '[해설']:
                    doc_state = False
                    doc_lines.pop()  # 마지막 빈 줄 제거
                    doc_string = ' '.join(doc_lines)

                    doc_string = long_space.sub(' ________________ ', doc_string)
                    doc_string = short_space.sub(' ', doc_string)
                    outfile.write(doc_string)
                    outfile.write('\n')
                    doc_lines = []
                else:
                    if not line.startswith('*'):
                        doc_lines.append(line)
            elif prev_lines[-1] == '' and prev_lines[-3] in ['[문제]', '[지문]']:
                doc_state = True
