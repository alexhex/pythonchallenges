import re

big = re.compile(r'.*[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z].*')
file_open = open(r'F:\mystuff\pythonscripts\pythonchallenges\level3_src.txt', 'r')
file_wr = open(r'F:\mystuff\pythonscripts\pythonchallenges\level3_dest.txt', 'w')
# line = file_open.read()

line = file_open.readlines()
# line = ("\r\n").join(line)
# file_wr.write(line)
for sen in line:
    match_obj = big.match(sen)
    if match_obj:
        line_2 = match_obj.group(1)
    else:
        line_2 = ''
    file_wr.write(line_2)
    print line_2
# line_2 = re.sub(big, '\1', line, re.M)

# print line_2

file_open.close()
file_wr.close()
