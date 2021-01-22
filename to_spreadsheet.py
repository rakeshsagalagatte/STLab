import pandas as pd 
import os

data =[]
filename = input('Entre the excel filename : ')
if os.path.exists(filename):
    data = pd.read_excel(filename)
    data = data.values.tolist()

for i in range(int(input('Enter the number of students : '))):
    to_append = list(map(str , input('Name USN T1 T2 T3 marks : ').split()))
    data.append(to_append[:5])

df = pd.DataFrame(data, columns=[ 'Name' , 'USN' , 'Test_1', 'Test_2', 'Test_3'])
df.to_excel(filename, index=None)

