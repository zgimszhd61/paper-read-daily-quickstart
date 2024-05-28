fp = open("input.txt","r")
for line in fp.readlines():
    print('"' + line.strip() + '",')