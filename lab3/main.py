from nltk.corpus import wordnet as wn
import time


def info(word):
    print(word.name(), word.pos(), word.definition(), word.lemmas())


def important_relation(synset):
    synset.hypernyms()
    synset.hyponyms()
    synset.instance_hyponyms()
    synset.substance_holonyms()
    synset.part_meronyms()
    return 0


def potential_all(synset):
    li = []
    for i in synset.hypernyms(): li.append(i)
    for i in synset.instance_hypernyms(): li.append(i)
    for i in synset.hyponyms(): li.append(i)
    for i in synset.instance_hyponyms(): li.append(i)
    for i in synset.member_holonyms(): li.append(i)
    for i in synset.substance_holonyms(): li.append(i)
    for i in synset.part_holonyms(): li.append(i)
    for i in synset.member_meronyms(): li.append(i)
    for i in synset.substance_meronyms(): li.append(i)
    for i in synset.part_meronyms(): li.append(i)
    for i in synset.attributes(): li.append(i)
    for i in synset.entailments(): li.append(i)
    for i in synset.causes(): li.append(i)
    for i in synset.also_sees(): li.append(i)
    for i in synset.verb_groups(): li.append(i)
    for i in synset.similar_tos(): li.append(i)
    return li


def potential_all_conections(synset):
    li = []
    for i in synset.hypernyms(): li.append([synset, 'hypernyms', i])
    for i in synset.instance_hypernyms(): li.append([synset, 'instance_hypernyms', i])
    for i in synset.hyponyms(): li.append([synset, 'hyponyms', i])
    for i in synset.instance_hyponyms(): li.append([synset, 'instance_hyponyms', i])
    for i in synset.member_holonyms(): li.append([synset, 'member_holonyms', i])
    for i in synset.substance_holonyms(): li.append([synset, 'substance_holonyms', i])
    for i in synset.part_holonyms(): li.append([synset, 'part_holonyms', i])
    for i in synset.member_meronyms(): li.append([synset, 'member_meronyms', i])
    for i in synset.substance_meronyms(): li.append([synset, 'substance_meronyms', i])
    for i in synset.part_meronyms(): li.append([synset, 'part_meronyms', i])
    for i in synset.attributes(): li.append([synset, 'attributes', i])
    for i in synset.entailments(): li.append([synset, 'entailments', i])
    for i in synset.causes(): li.append([synset, 'causes', i])
    for i in synset.also_sees(): li.append([synset, 'also_sees', i])
    for i in synset.verb_groups(): li.append([synset, 'verb_groups', i])
    for i in synset.similar_tos(): li.append([synset, 'similar_tos', i])
    return li


def find_all(base_synsets, iterat):
    if iterat == 0: return []
    iterat -= 1
    next_list_Synset = []
    for i in base_synsets:
        next_list_Synset.append(i)
        list_synset = potential_all(i)
        for new_synset in list_synset:
            if (new_synset in next_list_Synset) == False and new_synset != wn.synset('entity.n.01'):
                next_list_Synset.append(new_synset)
    new_list = find_all(next_list_Synset, iterat)
    for new_synset in new_list:
        if (new_synset in next_list_Synset) == False:
            next_list_Synset.append(new_synset)
    return next_list_Synset


def find_first_connections(li, synset2find, iterat):
    if iterat == 0: return []
    iterat -= 1
    for synset in li:
        if synset[2] == synset2find:
            return [synset]
        next_list_Synset = potential_all_conections(synset[2])
        str = find_first_connections(next_list_Synset, synset2find, iterat)
        if len(str) != 0:
            str.append(synset)
            return str
    return []


def find_all_connections(li, synset2find, iterat):
    if iterat == 0: return li
    iterat -= 1
    next_list_Synset = []
    for synset in li:
        next_list_Synset.append(synset)
        list_synset = potential_all_conections(synset[2])
        for new_synset in list_synset:
            if (new_synset in next_list_Synset) == False:
                next_list_Synset.append(new_synset)
    new_list = find_all_connections(next_list_Synset, synset2find, iterat)
    for new_synset in new_list:
        if (new_synset in next_list_Synset) == False:
            next_list_Synset.append(new_synset)
    return next_list_Synset


start = time.time()
# find_all([wn.synset('hospital.n.02')], 5)
# find_first_connections([[wn.synset('hospital.n.02'), " ", wn.synset('hospital.n.02')]], wn.synset('staff.n.01'), 5)
# find_all_connections([[wn.synset('hospital.n.02'), " ", wn.synset('hospital.n.02')]], wn.synset('staff.n.01'), 5)

# a
list_of_synset = [wn.synset('hospital.n.02'), wn.synset('staff.n.01'), wn.synset('doctor.n.01'),
                  wn.synset('nurse.n.01'), wn.synset('physician.n.01'),
                  wn.synset('operate.v.07'), wn.synset('aseptic.s.01'), wn.synset('injured.a.01'),
                  wn.synset('patient.n.01'), wn.synset('treat.v.03')]

# b
for i in list_of_synset:
    for x in find_all([i], 1):
        print(x)
    #    info(i)
    print("----------")

# c
for i in list_of_synset:
    for j in list_of_synset:
        if i == j: continue
        lis = find_first_connections([["", "", i]], j, 6)
        for k in lis:
            print(k)
        print("----------")

end = time.time()
print('Execution time:', round((end - start), 3), "s")

lis = find_first_connections([["", "", wn.synset('patient.n.01')]], wn.synset('hospital.n.02'), 11)
for k in lis:
    print(k)
print("----------")