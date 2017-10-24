#coding:utf-8
import tensorflow as tf
import numpy as np
import os
import csv
import random

class Data(object):
    def __init__(self, dir):

        # read head
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

        #read train
        train_path = os.path.join(os.getcwd(), dir, "train_convert.csv")
        train_dataset = []
        with open(train_path, "r") as f:
            train_file = csv.reader(f, delimiter= ",",)
            for e in train_file:
                e = list(map(int, e))
                train_dataset.append(e)


        self.head = head
        self.relation = relation
        self.tail = tail
        self.train_dataset = np.array(train_dataset)


    def getRelationTotal(self):
        return len(self.relation)

    def getHeadTotal(self):
        return len(self.head)

    def getTailTotal(self):
        return len(self.tail)

    def getTripleTotal(self):
        return len(self.train_dataset)

    def getBatch(self, shuffle=True):
        train_dataset = self.train_dataset[:]
        if shuffle:
            np.random.shuffle(train_dataset)

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


        return train_dataset, n_train




