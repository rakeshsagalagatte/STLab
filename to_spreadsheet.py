import pandas as pd 

data = []
for i in range(2):
    to_append = list(map(str , input('Name USN T1 T2 T3 marks : ').split()))
    data.append(to_append[:5])

df = pd.DataFrame(data, columns=['Name' , 'USN' , 'Test_1', 'Test_2', 'Test_3'])
df.to_excel('sheet.xlsx')

