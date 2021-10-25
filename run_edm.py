import re
import random
import numpy as np
from sedm import EDM, sEDM
from data_fasttext import new_ft_dict
from ai2thor import data_dict_train, data_dict_test
from data_bert import match_most_similar, replace_kw, two_word_dict

# model = EDM()
model = sEDM()

###################################################################

for i, (k, v) in enumerate(data_dict_train.items()):
    goal_wv = []
    goal_wv_entire = []
    object_wv = []
    object_wv_entire = []
    instr_wv = []
    instr_wv_entire = []
    print(i)
    # if i == 6:
    #     break
    goals = v['goals']
    objects = v['objects']
    instr = v['instructions']
    for g in goals:
        go = g.split(" ")
        for w in go:
            w = re.sub('[\W_]+', '', w.lower())
            wvec = new_ft_dict[w]
            goal_wv.append(list(wvec))
        goal_wv_entire.append(goal_wv)
        goal_wv = []
    for o in objects:
        obj = o.split(" ")
        for w in obj:
            w = re.sub('[\W_]+', '', w.lower())
            wvec = new_ft_dict[w]
            object_wv.append(list(wvec))
        object_wv_entire.append(object_wv)
        object_wv = []
    for i in instr:
        ins = i.split(" ")
        for w in ins:
            w = re.sub('[\W_]+', '', w.lower())
            wvec = new_ft_dict[w]
            instr_wv.append(list(wvec))
        instr_wv_entire.append(instr_wv)
        instr_wv = []
    model.train(goal_wv_entire, object_wv_entire, instr_wv_entire)
print("done training")


pair_cos = match_most_similar(metric="cosine")
for pair in pair_cos:
    train_replace = False
    test_replace = False
    kw_pair = []
    goal_wv = []
    goal_wv_entire = []
    object_wv = []
    object_wv_entire = []
    test_order = pair[1]
    for k, v in two_word_dict.items():
        if k in test_order:
            test_order_new = test_order.replace(k, v)
            test_replace = True
    train_order = pair[2]
    for k, v in two_word_dict.items():
        if k in train_order:
            train_order_new = train_order.replace(k, v)
            train_replace = True
    test_obj = pair[3]
    train_obj = pair[4]
    if test_replace:
        if train_replace:
            test_kw = [x for x in test_order_new.split(" ") if x not in train_order_new.split(" ")]
        else:
            test_kw = [x for x in test_order_new.split(" ") if x not in train_order.split(" ")]
    else:
        if train_replace:
            test_kw = [x for x in test_order.split(" ") if x not in train_order_new.split(" ")]
        else:
            test_kw = [x for x in test_order.split(" ") if x not in train_order.split(" ")]
    if train_replace:
        if test_replace:
            train_kw = [x for x in train_order_new.split(" ") if x not in test_order_new.split(" ")]
        else:
            train_kw = [x for x in train_order_new.split(" ") if x not in test_order.split(" ")]
    else:
        if test_replace:
            train_kw = [x for x in train_order.split(" ") if x not in test_order_new.split(" ")]
        else:
            train_kw = [x for x in train_order.split(" ") if x not in test_order.split(" ")]
    print("Test order: {}".format(test_order))
    print("Train order: {}".format(train_order))
    for w in train_order.split(" "):
        w = re.sub('[\W_]+', '', w.lower())
        wvec = new_ft_dict[w]
        goal_wv.append(list(wvec))
    goal_wv_entire.append(goal_wv)
    goal_wv = []
    for o in train_obj:
        for w in o.split(" "):
            w = re.sub('[\W_]+', '', w.lower())
            wvec = new_ft_dict[w]
            object_wv.append(list(wvec))
        object_wv_entire.append(object_wv)
        object_wv = []
    sequence = model.test([goal_wv_entire, object_wv_entire])
    # print(sequence)
    final_seq = replace_kw(test_kw, train_kw, sequence)
    print("Test Sequence: ")
    print(final_seq)


