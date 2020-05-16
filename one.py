from heapq import heapify, heappop

'''two-sum'''
def two_sum(number_array, target_value):
    for i, number in enumerate(number_array):
        for j, other_number in enumerate(number_array):
            if number + other_number == target_value:
                if i!= j:
                    return number, other_number
    return None

def two_sum_set(number_array, target_value):
    read = set() #lol like left on read
    for number in number_array:
        if target_value - number in read:
            return number, target_value - number
        read.add(number)
    return None

'''k-largest'''
def k_largest(number_array, k):
    return sorted(number_array, reverse=True)[:k]

def k_heap(number_array, k):
    max_heap = [-number for number in number_array]
    heapify(max_heap)
    return [-heappop(max_heap) for _ in range(k)]


hello=[5, 3, 6, 8, 2, 4, 7]
hi=10

goodbye=[5, 1, 3, 6, 8, 2, 4, 7]
peace_out=3

if __name__ == "__main__":
    print("TWO SUM")
    print(two_sum(hello, hi))
    print(two_sum_set(hello, hi))
    print("K-LARGEST")
    print(k_largest(goodbye, peace_out))
    print(k_heap(goodbye, peace_out))