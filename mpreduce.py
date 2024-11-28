#mapper
# mapper.py
import sys

# Input comes from standard input
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Output each word with a count of 1
    for word in words:
        print(f"{word}\t1")
# reducer.py
import sys

current_word = None
current_count = 0
word = None

# Input comes from standard input
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Parse the input from mapper
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # If count is not a number, ignore the line
        continue

    # Aggregate counts for the same word
    if word == current_word:
        current_count += count
    else:
        if current_word:
            # Write the result to standard output
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
  #input.txt
  Hello world
Hello Hadoop
Welcome to the world of Hadoop
Move Input File to HDFS:
hdfs dfs -mkdir -p /wordcount/input
hdfs dfs -put input.txt /wordcount/input
Run the Hadoop Streaming Job
hadoop jar /path/to/hadoop-streaming.jar \
  -input /wordcount/input \
  -output /wordcount/output \
  -mapper mapper.py \
  -reducer reducer.py
Retrieve Output
hdfs dfs -cat /wordcount/output/part-00000


output:
Hadoop	2
Hello	2
Welcome	1
of	1
the	1
to	1
world	2

