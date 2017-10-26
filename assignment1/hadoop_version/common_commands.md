hadoop fs -ls   # check hadoop file system
hadoop fs -put purchases.txt   # put file in cluster
hadoop fs -tail purchases.txt  # display end
hadoop fs -mv purchases.txt newname.txt # rename
hadoop fs -rm newname.txt   # delete file
head  -50 ../data/purchases.txt > testfile  # first 50 lines
cat testfile | ./mapper.py | sort | ./reducer.py
hs mapper.py reducer.py myinput output2
