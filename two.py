'''Twitter'''

from heapq import heapify, heappop

def similarity_score(handle_1, handle_2):
    h1_set = set([*handle_1.lower()])
    h2_set = set([*handle_2.lower()])
    return 3 * len(h1_set.intersection(h2_set)) - len(h1_set) - len(h2_set)

def name_twins(template_handle, global_handles, k=2):
    min_heap = []
    for handle in global_handles:
        score = similarity_score(template_handle, handle)
        min_heap.append((-score, handle))
    heapify(min_heap)
    return [heappop(min_heap)[1] for _ in range(k)]

handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']

if __name__ == "__main__":
    print(name_twins('iLoveDogs', handles, k=2))