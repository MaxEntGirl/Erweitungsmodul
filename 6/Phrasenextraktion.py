
def extract_all(es, fs, alignment):
    BP = set()
    len_es = len(es)
    for e_start in range(1, len_es+1):
        for e_end in range(e_start, len_es+1):
            f_start, f_end = (len(fs), 0)
            for (e, f) in alignment:
                if e_start <= e <= e_end:
                    f_start = min(f, f_start)
                    f_end = max(f, f_end)
            BP.update(extract(es, fs, e_start, e_end, f_start, f_end, alignment))

    return BP


def extract(es, fs, f_start, f_end, e_start, e_end, alignment):
    if f_end == 0:
        return {}
    for (e, f) in alignment:
        if (f_start <= f <= f_end) and (e < e_start or e > e_end):
            return {}
    E = set()
    f_s = f_start
    while True:
        f_e = f_end
        while True:
            E.add((e_start, e_end, f_s, f_e))
            f_e += 1
            if f_e > len(fs) or f_e in list(zip(*alignment))[1]:
                break
        f_s -= 1
        if f_s == 0 or f_s in list(zip(*alignment))[1]:
            break

    return E

es= open('english.txt','r')
es= es.readline()[0]

fs=open('german.txt','r')
fs=fs.readline()[0]

with open('Alignierung.txt','r') as f:
    f=f.readline()
    alignments = set()
    l = f.split(' ')
    for i in range(0, len(l), 2):
        src_pos, tgt_pos = l[i], l[i + 1]
        alignments.add((int(src_pos), int(tgt_pos)))

    phrasen=extract_all(es,fs,alignments)
    print(phrasen)
