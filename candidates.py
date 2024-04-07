#!/usr/bin/env python

from glob import glob
import gzip
import re
import json
from collections import Counter, defaultdict

counts = defaultdict(Counter)

for filepath in glob("./*.gz"):
    print filepath

    with gzip.open(filepath, 'r') as file:
        
        for row in file:
            search = re.search(r'([^ \t\/]+)[^ \t]+PRP/dobj', row)

            if search:
                pronoun = search.group(1)
                pairs = re.findall(r'([1-2]\d\d\d,\d+)', row)

                for pair in pairs:
                    year, count = tuple(int(v) for v in pair.split(','))
                    counts[pronoun].update({year: count})

with open('counts.json', 'w') as output:
    json.dump({k: v.most_common() for k, v in counts.items()}, output)
