import sys
import re

pattern = r"cat"

for line in sys.stdin:
    line = line.rstrip()
    match_object = re.findall(pattern, line)
    if len(match_object) >= 2:
        print(line)