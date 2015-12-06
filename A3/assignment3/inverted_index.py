import MapReduce
import sys

"""
Inverted Index using Simple Python MapReduce Framework

Test Input: books.json
Test Output: inverted_index.json
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # record is a 2-element list
    # key: a word  
    # value: a document that the word appears in
    id = record[0]
    content = record[1]
    words = content.split()
    for w in words:
      mr.emit_intermediate(w, id)

def reducer(key, list_of_values):
    # key: a document word
    # value: a list of all the documents that 'key' is in, which
    #        can contain duplicates, so our job can be as simple
    #        as removing duplicates from list_of_values
    seen = set()
    add = seen.add
    mr.emit((key, [s for s in list_of_values if s not in seen and not add(s)]))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
