#!/usr/bin/env python

import json
from glob import glob
import gzip
import re
from collections import Counter, defaultdict

counts = defaultdict(Counter)

with open('revised-candidates.json', 'r') as f:
    pronouns = json.load(f)

pronouns_regex = re.compile('|'.join(pronouns) + "\b")

for filepath in glob("./*.gz"):
    print filepath

    with gzip.open(filepath, 'r') as file:
        
        for row in file:
            search = re.search(pronouns_regex, row)

            if search:
                pronoun = search.group(0)
                pairs = re.findall(r'([1-2]\d\d\d,\d+)', row)

                for pair in pairs:
                    year, count = tuple(int(v) for v in pair.split(','))
                    counts[pronoun].update({year: count})

with open('counts.json', 'w') as output:
    json.dump({k: v.most_common() for k, v in counts.items()}, output)

