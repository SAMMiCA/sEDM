import re
from sedm import EDM, sEDM
from data_fasttext import new_ft_dict
from data_bert import match_most_similar

# model = EDM()
model = sEDM()
model.load(filename="data.pickle")
pair_cos = match_most_similar(metric="cosine")
for pair in pair_cos:
    goal_wv = []
    goal_wv_entire = []
    object_wv = []
    object_wv_entire = []
    test_order = pair[1]
    train_order = pair[2]
    test_obj = pair[3]
    train_obj = pair[4]
    test_obj = [ob.replace('openable ', '') if 'openable' in ob else ob for ob in test_obj]
    train_obj = [ob.replace('openable ', '') if 'openable' in ob else ob for ob in train_obj]
    print("Test order: {}\n".format(test_order))
    # print("Train order: {}".format(train_order))
    if len(test_obj) == len(train_obj):
        diff_test_tr = [(i, j) for i, j in zip(test_obj, train_obj) if i != j]
    else:
        print("***sequence cannot be retrieved***")
        print("\n\n")
        continue
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
    # sequence = model.test(goal_wv_entire)
    # print(sequence)
    final_seq = []
    for seq in sequence:
        for kw in diff_test_tr:
            if kw[1] in seq:
                seq=seq.replace(kw[1], kw[0])
        final_seq.append(seq)
    print("Test Sequence: ")
    for s in final_seq:
        print(s)
    print("\n\n")



