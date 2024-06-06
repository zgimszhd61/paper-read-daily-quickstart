fp = open("input.txt","r")
for line in fp.readlines():
    print('"' + "https://github.com"+ line.strip() + '",')