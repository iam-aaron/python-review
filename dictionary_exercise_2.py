fname = input("Enter file name: ")
fh = open("mbox-short.txt")
senders = dict()

for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.strip().split()
        senders[words[1]] = senders.get(words[1],0) + 1

sender_leading = None
sender_count = None

for key,value in senders.items():
    if sender_count is None or value > sender_count:
        sender_count =  value
        sender_leading = key

print(sender_leading," ",sender_count)
