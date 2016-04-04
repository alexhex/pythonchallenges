import re

# match_obj = re.match(r'dog', 'This is not a dog.')
match_obj = re.search(r'(.*?) dog', 'This is not a dog.')

if match_obj:
    print "It is aber right!~"
    print match_obj.group(1)
else:
    print "Doch!"
