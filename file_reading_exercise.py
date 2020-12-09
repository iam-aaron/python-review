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

content = fhandler.read().strip().upper()

print(content)
