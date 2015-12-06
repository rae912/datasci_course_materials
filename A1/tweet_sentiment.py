#coding:utf-8

import sys
import json

def main():
    input_file = open(sys.argv[2])
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    for line in input_file:
        data = line.split("\n")
        orgin = json.loads(data[0])
        words = orgin['text'].split(" ")
        sc = 0
        for word in words:
            try:
                sc += scores[word]
            except:
                pass
        print sc

if __name__ == '__main__':
    main()