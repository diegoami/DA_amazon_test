
def getMinimumDifference(a, b):
    result = []

    for i in range(len(a)):
        ax, bx = a[i], b[i]
        if (len(ax) == len(bx)):
            ad = dict()
            diff = 0
            for x in ax:
                ad[x] = ad.get(x,0) + 1
            for x in bx:
                c =  ad.get(x,0)
                if c <= 0:
                    diff += 1
                ad[x] = c - 1
            result.append(diff)
        else:
            result.append(-1)
    return result

print(getMinimumDifference(["a","jk", "abb", "mn", "abc"], ["bb", "kj", "bbc", "op", "def"]))
assert(getMinimumDifference(["a","jk", "abb", "mn", "abc"], ["bb", "kj", "bbc", "op", "def"])) == [-1,0,1,2,3]
