import json
import pandas as pd

data = open("data.txt","r")
pdata = data.read()
print(pdata)
processingData = json.loads(pdata)
json.dumps(processingData,sort_keys=True, indent=4)