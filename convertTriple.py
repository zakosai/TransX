__author__ = 'linh'

import os
import csv

def convert(dir, tripleFile, writeFile):
    triple_path = os.path.join(os.getcwd(), dir, tripleFile)

    head_path = os.path.join(os.getcwd(), dir, "entity2id.txt")
    head = []
    with open(head_path, "r") as f:
        head_file = csv.reader(f, delimiter= "\t",)
        for e in head_file:
            head.append(e[0])

        #read relation
    relation_path = os.path.join(os.getcwd(), dir, "relation2id.txt")
    relation = []
    with open(relation_path, "r") as f:
        relation_file = csv.reader(f, delimiter= "\t",)
        for e in relation_file:
            relation.append(e[0])

        #read tail
    tail_path = os.path.join(os.getcwd(), dir, "entity2id.txt")
    tail = []
    with open(tail_path, "r") as f:
        tail_file = csv.reader(f, delimiter= "\t",)
        for e in tail_file:
            tail.append(e[0])

    triple = []
    with open(triple_path, "r") as f:
        trip_file = csv.reader(f, delimiter= "\t",)
        for t in trip_file:
            h_id = head.index(t[0])
            t_id = tail.index(t[1])
            r_id = relation.index(t[2])

            triple.append([h_id, r_id, t_id])

    write_path = os.path.join(os.getcwd(), dir, writeFile)
    with open(write_path, "w") as fout:
        wr = csv.writer(fout, delimiter=",")
        wr.writerows(triple)


if __name__ == '__main__':
    convert("data/WN18", "test.txt", "test_convert.csv")
