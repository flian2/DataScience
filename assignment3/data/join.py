import MapReduce
import sys
import json

# join
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: id
    # value: the record
    id = record[1]
    mr.emit_intermediate(id, record)

def reducer(key, list_of_values):
    # key: id
    # value: the entire record
    
    for record1 in list_of_values:
      if record1[0] == "order":
        for record2 in list_of_values:
          if record2[0] == "line_item":
            
            new_record = [];
            new_record.extend(record1); # extend(): append another iterable to the end of array
            new_record.extend(record2);
            mr.emit(new_record)

    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
