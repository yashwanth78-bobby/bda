#numbers.txt
10
20
30
40
50
#mapper
# mapper_avg.py
import sys

for line in sys.stdin:
    num = int(line.strip())
    print(f"sum\t{num}")
    print(f"count\t1")
# reducer_avg.py
import sys

sum_total = 0
count_total = 0

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    value = int(value)
    
    if key == "sum":
        sum_total += value
    elif key == "count":
        count_total += value

if count_total > 0:
    print(f"Average\t{sum_total / count_total}")
#run locally
cat numbers.txt | python3 mapper_avg.py | sort | python3 reducer_avg.py
#op
Average	30.0
