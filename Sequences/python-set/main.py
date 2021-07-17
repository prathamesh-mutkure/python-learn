

def print_data(tag, value):
    print(tag + " : " + str(value))


set1 = {"a", "b", "c", "d"}
set2 = set(["a", "b", "e", "f"])

print_data("set1", set1)
print_data("set2", set2)

print("------------------------------------")

union = set1.union(set2)
print_data("union", union)

intersection = set1.intersection(set2)
print_data("intersection", intersection)

diff = set1.difference(set2)
print_data("difference", diff)

diff_sym = set1.symmetric_difference(set2)
print_data("Symm Diff", diff_sym)

print("------------------------------------")

set3 = set1.copy()
set3.intersection_update(set2)
print_data("intersec update", set3)

set3 = set1.copy()
set3.difference_update(set2)
print_data("diff update", set3)

set3 = set1.copy()
set3.symmetric_difference_update(set2)
print_data("symm diff update", set3)

print("------------------------------------")

# set3.pop()
# print_data("pop", set3)
#
# set3.remove("d")
# print_data("remove", set3)
#
# set3.discard("f")
# print_data("discard", set3)

frozen_set = frozenset(["a", "b", "c", "d", "e", "f"])
print_data("frozenset", frozen_set)

print_data("frozen_set is super set of ", frozen_set.issuperset(set3))
print_data("set3 is sub set of frozen_set", set3.issubset(frozen_set))
