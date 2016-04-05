import pickle

file_handle = open(r'banner.p', 'rb')
obj = pickle.load(file_handle)
file_store = open('file.txt', 'w')
for line in obj:
    for item in line:
        file_store.write(item[0] * item[1])
    file_store.write('\r\n')
