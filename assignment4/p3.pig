register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- First filter the data so you only have tuples whose subject matches 'rdfabout.com'.

filtered = FILTER ntriples BY (subject matches '.*business.*');
filtered2 = FOREACH filtered GENERATE ($0) as subject2, ($1) as predicate2, ($2) as object2 PARALLEL 50;

-- join the two copies
sextuples = JOIN filtered BY subject, filtered2 BY subject2;

-- remove duplicate tuples

results = DISTINCT sextuples;


-- store the results in the folder 
fs -mkdir /tmp;
store results into '/tmp/p3' using PigStorage();

-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';
