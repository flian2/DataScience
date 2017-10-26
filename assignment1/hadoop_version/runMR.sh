#!/bin/bash
#Defining program variables
DC="twitter_data/cache/AFINN-111.txt"
IP="twitter_data/output.txt"
OP="output4"
HADOOP_JAR_PATH="/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar"
MAPPER="mapper.py"
REDUCER="reducer.py"

hadoop jar $HADOOP_JAR_PATH \
-file $MAPPER -mapper $MAPPER \
-file $REDUCER -reducer "python reducer.py" -input $IP -output $OP \
-cacheFile $DC#afinn \
