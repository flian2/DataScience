import MapReduce
import sys
import json

# friend count
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: his friend
    key = record[0]
    mr.emit_intermediate(key, record[1])

def reducer(key, list_of_values):
    
    friend_list = list(set(list_of_values))
    count = len(friend_list)
    mr.emit((key,count))

    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
