"""Runnable examples for Standard Library Foundations."""

import math
import random
from datetime import datetime, timezone, timedelta
import os
from pathlib import Path
import sys
from collections import Counter, deque, defaultdict
from itertools import chain, islice
from functools import partial, reduce
import re
import json
import csv
import statistics

# 1. math
print("math:", math.sqrt(25), math.ceil(2.1))

# 2. random (not for security-sensitive secrets)
random.seed(1)
print("random:", random.randint(1, 10))

# 3. datetime
now = datetime.now(timezone.utc)
print("UTC datetime:", now)
print("tomorrow:", now + timedelta(days=1))

# 4. os
print("platform env example:", os.environ.get("PATH", "")[:20])

# 5. pathlib
path = Path("python") / "example.txt"
print("path:", path)

# 6. sys
print("Python version:", sys.version.split()[0])

# 7. collections
print("Counter:", Counter("banana"))
queue = deque([1, 2])
queue.append(3)
print("deque:", queue)

# 8. itertools
print("chain:", list(chain([1, 2], [3, 4])))
print("islice:", list(islice(range(10), 2, 7)))

# 9. functools
print("partial:", partial(pow, exp=2)(5))
print("reduce:", reduce(lambda a, b: a + b, [1, 2, 3]))

# 10. re
print("regex:", re.findall(r"[A-Z][a-z]+", "Python Standard Library"))

# 11. json
text = json.dumps({"device": "AGV", "enabled": True})
print("json:", json.loads(text))

# 12. csv
rows = [["name", "value"], ["temperature", "25"]]
print("CSV module available:", csv.reader(rows))

# 13. statistics
print("mean:", statistics.mean([10, 20, 30]))
