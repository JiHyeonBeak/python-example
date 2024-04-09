import json
import pandas as pd

# 정렬할 데이터(txt)를 받아온다.
data = open("data.txt","r")
pdata = data.read()

# 데이터 확인
print(pdata)

# txt파일을 json으로 변환한다.
processingData = json.loads(pdata)

# 정렬
json.dumps(processingData,sort_keys=True, indent=4)