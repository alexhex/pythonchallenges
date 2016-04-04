import urllib
import re
import time

url_handle = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579', 'r')
file_handle = open('temp_re.txt', 'w')


for i in range(2000):
    time.sleep(0.5)
    line = url_handle.read()
    file_handle.write(line+'\r\n')
    # print line
    num_obj = re.match(r'.*?(\d+)', line)
    if num_obj:
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num_obj.group(1)
        print url
        url_handle = urllib.urlopen(url, 'r')
    else:
        print "no"
        break

file_handle.close()
url_handle.close()
