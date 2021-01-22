import pandas as pd 
import os

data =[]
if os.path.exists('sheet.xlsx'):
    data = pd.read_excel('sheet.xlsx')
    data = data.values.tolist()

for i in range(int(input('Enter the number of students : '))):
    to_append = list(map(str , input('Name USN T1 T2 T3 marks : ').split()))
    data.append(to_append[:5])

df = pd.DataFrame(data, columns=[ 'Name' , 'USN' , 'Test_1', 'Test_2', 'Test_3'])
df.to_excel('sheet.xlsx', index=None)

