import pandas as pd

df = pd.read_excel(input('Enter the existing excel filename : '), )
toUpdate = []
L = df.values.tolist()#[['Test_1' , 'Test_2' , 'Test_3']]
for i in range(len(L)):
    if int(L[i][len(L[i]) - 1]) < 60:
        toUpdate.append(L[i])
        continue
    if int(L[i][len(L[i])-2]) < 60:
        toUpdate.append(L[i])
        continue
    if int(L[i][len(L[i])-3]) < 60:
        toUpdate.append(L[i])

df = pd.DataFrame(toUpdate, columns=['sl','Name' , 'USN' , 'Test_1', 'Test_2', 'Test_3'])
df.to_excel('toUpdate.xlsx', index=None)
