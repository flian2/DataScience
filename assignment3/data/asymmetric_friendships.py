import MapReduce
import sys
import json

# friend count
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: first one in the sorted tuple (person, friend)
    # value: the person
    sorted_record = sorted(record)
    key = sorted_record[0]
    mr.emit_intermediate(key, record)
    
    

def reducer(key, list_of_values):
    # if there's tuple and flipped tuple in the list: symmetric
    person = []
    # print key
    # print list_of_values
    
    for record1 in list_of_values:
        symm = 0
        for record2 in list_of_values:
            if record1[0] == record2[1] and record1[1] == record2[0]:
                symm = 1
        if symm == 0:
            mr.emit((record1[1],record1[0]))
            



    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
