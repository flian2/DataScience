import MapReduce
import sys
import json

# matrix multiplication
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	for k in range(5):
		if record[0] == "a":
			key = (record[1],k) # (i,k)
			value = ("a", record[2], record[3]) # (matrix,j,value)
		else:
			key = (k,record[2]) # (k,j)
			value = ("b", record[1], record[3]) # (matrix,i,value)
		# print key, value
		mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    sum = 0
	# key is j in a(i,j) b(j,k), value is a(i,j)*b(j,k) when both exist
	# value is a(i,j) or b(j,k) when only single exists
    dic = {}
    for tup in list_of_values:
    	if not (tup[1] in dic):
    		dic[tup[1]] = tup[2]
    	else:
    		prod = dic[tup[1]] * tup[2]
    		dic[tup[1]] = prod
    		sum += prod

    mr.emit((key[0],key[1],sum)) 







# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
