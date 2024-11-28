#dataset
Hadoop MapReduce is powerful
MapReduce processes large datasets
Hadoop is scalable
# mapper.py
import sys

for line in sys.stdin:
    # Strip whitespace and split the line into words
    words = line.strip().split()
    for word in words:
        # Emit each word with a count of 1
        print(f"{word}\t1")
# reducer.py
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    # Split input line into word and count
    word, count = line.strip().split("\t", 1)
    count = int(count)

    # If the word changes, output the previous word's count
    if current_word and current_word != word:
        print(f"{current_word}\t{current_count}")
        current_count = 0

    # Accumulate counts for the current word
    current_word = word
    current_count += count

# Output the last word's count
if current_word:
    print(f"{current_word}\t{current_count}")
##testlocally
cat input.txt | python3 mapper.py | sort | python3 reducer.py
#op
HADOOP	2
IS	2
MAPREDUCE	2
POWERFUL	1
PROCESSES	1
LARGE	1
DATASETS	1
SCALABLE	1
#Move Dataset to HDFS
hdfs dfs -mkdir -p /user/input
hdfs dfs -put input.txt /user/input/
#Run the Hadoop MapReduce Job
hadoop jar /path/to/hadoop-streaming.jar \
    -input /user/input \
    -output /user/output \
    -mapper mapper.py \
    -reducer reducer.py
#Fetch the Output
hdfs dfs -cat /user/output/part-00000
