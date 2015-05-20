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
    # value: order + line item
    # new_record = []
    # print "==="
    # for record in list_of_values:
    #   print record
    # print "==="

    for record1 in list_of_values:
      if record1[0] == "order":
        for record2 in list_of_values:
          if record2[0] == "line_item":
            
            # print "==="
            # print record1
            # print record2
            new_record = [];
            new_record.extend(record1);
            new_record.extend(record2);
            mr.emit(new_record)

    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
