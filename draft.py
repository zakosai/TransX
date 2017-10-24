__author__ = 'linh'
import os
import csv
import numpy as np
import random


def getBatch(dir="data/WN18", shuffle=True):
    train_path = os.path.join(os.getcwd(), dir, "valid_convert.csv")
    train_dataset = []
    with open(train_path, "r") as f:
        train_file = csv.reader(f, delimiter= ",",)
        for e in train_file:
            train_dataset.append(e)

    # if shuffle:
    #     np.random.shuffle(train_dataset)

    train_dataset = np.array(train_dataset)
    p_head = train_dataset[:,0]
    p_relation = train_dataset[:,1]
    p_tail = train_dataset[:, 2]

    n_head = random.sample(p_head, len(p_head))
    n_tail = random.sample(p_tail, len(p_tail))

    l_half = int(len(p_head)/2)
    n_head = np.concatenate((n_head[:l_half], p_head[l_half:]), axis=0)
    n_tail = np.concatenate((p_tail[:l_half],n_tail[l_half:]), axis=0)

    n_train = np.vstack((n_head, p_relation, n_tail))
    n_train = n_train.T
    np.random.shuffle(n_train)
    n_head = n_train[:,0]
    n_relation = n_train[:,1]
    n_tail = n_train[:,2]


    return p_head, p_relation, p_tail, n_head, n_relation, n_tail

if __name__ == '__main__':
    getBatch()
