import re

str_in = open('in.txt', 'r')
str_out = open('out.txt', 'w')
line = '1'
line_2 = ''
while(line):
    line = str_in.readline()
    line_2 = re.sub("\W", "", line)
    line_2 = re.sub("_", "", line_2)
    str_out.write(line_2)
str_out.close()
str_in.close()

# out.txt shows equality
