def read_hp(txt):
    file = open(txt, "r")
    n, arr = [x.strip() for x in file.readlines()]
    file.close()

    return [int(x) for x in arr.split()]


res = read_hp("rosalind_hs.txt")
ordered = sorted(res)

for num in ordered:
    print(num, end = " ")
