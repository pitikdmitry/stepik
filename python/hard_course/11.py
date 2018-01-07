import sys
import re

pattern = r"\s*cat\s*"

for line in sys.stdin:
    line = line.rstrip()
    match_object = re.match(pattern, line)
    print(match_object)
