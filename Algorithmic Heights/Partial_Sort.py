def read_hp(txt):
    file = open(txt, "r")
    n, arr, k_s = [x.strip() for x in file.readlines()]
    file.close()

    cor_arr = [int(x) for x in arr.split()]
    k = int(k_s)

    return cor_arr, k


res, lim = read_hp("rosalind_ps.txt")
ordered = sorted(res)

for num in ordered[: lim]:
    print(num, end = " ")
