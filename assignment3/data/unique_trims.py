import MapReduce
import sys
import json

# DNA trim
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[0]
    untrim = record[1]
    trim = untrim[:-10]
    mr.emit_intermediate(trim,1)
    

def reducer(key, list_of_values):
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
