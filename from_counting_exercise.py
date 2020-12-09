fname = input("Enter file name: ")
fh = open("mbox-short.txt")
email_lst = list()

count = 0
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.strip().split()
        email_lst.append(words[1])
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
