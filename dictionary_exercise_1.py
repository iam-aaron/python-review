
#fname = input("Enter file name: ")
fh = open("mbox-short.txt")
senders_time = dict()

for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.strip().split()
        senders_time[words[5].split(":")[0]] = senders_time.get(words[5].split(":")[0],0) + 1

#senders_time_sorted = sorted([(k,v) for (k,v) in senders_time.items()])
#print(senders_time_sorted)

for (k,v) in sorted(senders_time.items()):
    print(k,v)
