word = input()
cro = ["dz=","c=","c-","d-","lj","nj","s=","z="]
cnt = len(word)

cnt = cnt -word.count("dz=")- word.count("c=")-word.count("c-")-word.count("d-")-word.count("lj")-word.count("nj")-word.count("s=")-word.count("z=")
print(cnt)
