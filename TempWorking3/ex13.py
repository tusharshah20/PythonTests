path = 'I:\\GitContent\\Datasets\\primer-dataset.json'
#open(path).readline()

import json
records = [json.loads(line) for line in open(path)]
records[0]