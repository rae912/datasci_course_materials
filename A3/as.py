import MapReduce
import sys

"""
Asymmetric Friendships using the Simple Python MapReduce Framework

Test Input: friends.json
Test Output: asymmetric_friendships.json
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: a sorted tuple of a person and one of his friend
    # value: simply 1. Then we can count in reduce if the total count is 2, which
    #        indicates asymmetric friendship
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(tuple(sorted((person, friend))), 1)

def reducer(key, list_of_values):
    # key: a sorted tuple of a person and one of his friend
    # value: list of occurrence counts
    # output: (person, friend) and (friend, person) for each asymmetric relationships
    total = 0
    for v in list_of_values:
        total += v
    if total == 1:
        mr.emit(key)
        mr.emit(key[::-1])

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
