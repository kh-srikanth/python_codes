f = open("C://Users//PC//Documents//funny.txt", "r")
f_w = open("C://Users//PC//Documents//funny_len.txt", "w")
'''print(f.read())'''
print(type(f))
for line in f:
    a = line.split(' ')
    '''print(a)'''
    f_w.write("word count: " + str(len(a)) + " "+line)
f.close()
f_w.close()


