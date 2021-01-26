import re
import pandas as pd

df = pd.read_excel(input('Enter xlsx file name : '))
for i,d in df.iterrows():
    if not re.search('(.*[0-9]+.*-){4}.*[0-9]+.*', d[1]):
        print(d[i])