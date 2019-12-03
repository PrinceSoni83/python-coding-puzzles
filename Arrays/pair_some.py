# given an integer array , output all unique pair that sum up to a specific value k

def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []
    #print("no pair sum is equal to the value provided")

print(sum_pairs([1,3,2,2],4))