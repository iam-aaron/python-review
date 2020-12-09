fname = input("Enter file name: ")
fh = open(fname)
word_lst = list()

for line in fh:
    for words in line.strip().split():
        if words in word_lst:
            continue
        else:
            word_lst.append(words)


word_lst.sort()
print(word_lst)
