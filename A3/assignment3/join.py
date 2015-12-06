import MapReduce
import sys

"""
Relational Join using Simple Python MapReduce Framework

Test Input: records.json
Test Output: join.json
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # record is database records. Specifically for the provided dataset:
    #    First item(index 0) in each record identifies which table the record originates from
    #       'line_item' indicates that the record is a line item
    #       'order' indicates that the record is an order
    #    Second element is the order id that we want to join on
    # LineItem records have 17 elements including the identifier string
    # Order records have 10 elements including the identifier string
    #
    # key - the order id 
    # value - the entire record, for joining purpose
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: order id
    # value: a list of records with the order id 'key'
    for v1 in list_of_values:
        for v2 in list_of_values:
            if v1[0] > v2[0]: # we use a common SQL trick to filter duplicate data
                res = v1 + v2 
                mr.emit(res)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
