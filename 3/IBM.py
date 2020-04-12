# coding=utf-8
# Read File to pairs

fp_en = open('en', 'r')
fp_cn = open('fr', 'r')

iters = 1
pairDic = {}
countPair = 0


for line_cn, line_en in zip(fp_cn, fp_en):

    f = line_cn.split()
    e = line_en.split()
    for w1 in f:
        for w2 in e:
            pairDic[countPair] = (w1, w2)
            countPair += 1
    iters += 1

fp_en.close()
fp_cn.close()

lst = list(set(pairDic.values()))
NewpairDic = {}
i = 0
foreign, english = [], []

for _tuple in lst:
    NewpairDic[i] = _tuple
    i += 1

t = {}
for key in NewpairDic.values():
    t[key] = 1/len(NewpairDic.values())  # initialize t(e|f) uniformly

print("t0=", t)
K = 0

while K <= 5:

    fp_en = open('en', 'r')
    fp_cn = open('fr', 'r')
    count, total = {}, {}
    for key in NewpairDic.values():
        count[key] = 0

    for _tuple in NewpairDic.values():
        total[_tuple[0]] = 0

    s_total = {}

    for ee, ff in zip(fp_en, fp_cn):

        # compute normalization
        for e in ee.split():
            s_total[e] = 0
            for f in ff.split():
                s_total[e] += t[(f, e)]
        # collect counts
        for e in ee.split():
            for f in ff.split():
                count[(f, e)] += t[(f, e)] / s_total[e]
                total[f] += t[(f, e)] / s_total[e]

    # estimate probabilities

    for f, e in NewpairDic.values():
        t[(f, e)] = count[(f, e)] / total[f]
    # end of while
    K += 1
    fp_en.close()
    fp_cn.close()

    print("t%d=" % K)
    for it in t.items():
        print(it)


