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
    # sorted_record = sorted(record)
    # key = sorted_record[0]
    # mr.emit_intermediate(key, sorted_record)
    mr.emit(record[0],record[1])
    

def reducer(key, list_of_values):
    
    dic = {}
    for record in list_of_values:
    	tup = (record[0],record[1])
    	if not (tup in dic):
    		# asymetric
    		dic[tup] = 0 
    	else:
    		# symmetric
    		dic[tup] = 1

    for tup in dic:
    	if dic[tup] == 0:
          mr.emit((record[0],record[1]))
    	  mr.emit((record[1],record[0]))

    

    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
