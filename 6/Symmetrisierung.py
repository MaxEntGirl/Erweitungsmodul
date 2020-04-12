import itertools

def parse(l):
    #parse the line into a alignment matrix
    alignments = set()
    l=l.split(' ')
    for i in range(0, len(l), 2):
        src_pos, tgt_pos = l[i],l[i+1]
        alignments.add((int(src_pos), int(tgt_pos)))

    return alignments

def grow_diag_final(e2f, f2e):
    #adds alignments in the neighborhood of alignments in the intersection and union
    neighbouring = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    alignments = e2f.intersection(f2e)
    alignment_union = e2f.union(f2e)
    e_len = max((e for e, f in alignment_union))
    f_len = max((f for e, f in alignment_union))

    for e, f in itertools.product(range(e_len+1), range(f_len+1)):
        if (e, f) in alignments:
            for e_new, f_new in ((e + E, f + F) for E, F in neighbouring):
                if e_new not in {e for e, f in alignments} and f_new not in {f for e, f in alignments} and (e_new, f_new) in alignment_union:
                    alignments.add((e_new, f_new))

    for e_new, f_new in itertools.product(range(e_len), range(f_len)):
        if e_new not in {e for e, f in alignments} and f_new not in {f for e, f in alignments} and (e_new, f_new) in alignment_union:
            alignments.add((e_new, f_new))

    return alignments

results= open('Alignierung.txt', 'w')

with open('english.txt', 'r') as f1:
    with open('german.txt', 'r') as f2:
        f1=f1.readlines()[1]
        f2 = f2.readlines()[1]
        al1 = parse(f1)
        al2 = parse(f2)
        alignments=grow_diag_final(al1, al2)
        alignments = ' '.join(list(str(e)+' '+ str(f) for (e,f) in alignments))
            #adapts the alignments into the format of the editor's file: source_index target_index
        results.write(alignments)

results.close()