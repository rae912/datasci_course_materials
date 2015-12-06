import MapReduce
import sys

"""
Social Network dataset with friends counting in the Simple Python MapReduce Framework

Test Input: friends.json
Test Output: friend_count.json
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person A
    # value: just a single count indicating record[1] is a friend with 'key'
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: a person
    # value: and a list of 1s, whose sum is the number of friends the person has
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
