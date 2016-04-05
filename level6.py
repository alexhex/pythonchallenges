import zipfile
import re

handle = zipfile.ZipFile('channel.zip', 'r')
info_handle = zipfile.ZipInfo('channel.zip', 'r')

current = '90052'
txt = handle.read('%s.txt' %current)
comment = []
# print txt
for i in range(2000):
    re_obj = re.match(r'.*?(\d+)$', txt)
    if re_obj:
        current = re_obj.group(1)
        print current
        txt = handle.read('%s.txt' %current)
        comment.append(info_handle.comment('%s.txt' %current))
    else:
        print txt
        print current
        print comment
        break
