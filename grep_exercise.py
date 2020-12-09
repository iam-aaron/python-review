fname = None
while True:
    try:
        if fname is None:
            fname = input("Enter file name: ")
        else:
            fname = input("File does not exist, try again or type 'quit' to exit: ")
            if fname == "quit":
                break
        fhandler = open(fname)
        break
    except:
        continue

if fname == "quit":
    exit()

spam_conf_total = 0
spam_conf_ave = 0
spam_count = 0
for line in fhandler:
    if line.startswith("X-DSPAM-Confidence"):
        spam_conf = line[line.find(":")+1:].lstrip()
        spam_conf_total = spam_conf_total + float(spam_conf)
        spam_count = spam_count + 1




print("Average spam confidence:",spam_conf_total/spam_count)
