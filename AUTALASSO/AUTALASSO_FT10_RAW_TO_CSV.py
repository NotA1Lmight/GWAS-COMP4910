import pandas as pd

data = pd.read_csv("C:\Projects\PycharmProjects\GWAS\PLink\p1.raw", sep=' ', header='infer', engine = 'python',iterator=True)

loop = True
chunkSize = 100
chunks = []
index=0
while loop:
    try:
        print(index)
        chunk = data.get_chunk(chunkSize)
        chunks.append(chunk)
        index+=1

    except StopIteration:
        loop = False
        print("Iteration is stopped.")
print('Merge Chunks')
data = pd.concat(chunks, ignore_index= True)
print('Merge Chunks End')
print('Delete the first six columns ')
data = data.drop(data.columns[[0, 1, 2, 3, 4, 5]], axis=1)
e=data.iloc[:3,:3]
print(e)

print('Get the  phenotypes FT10')
first_column = pd.read_csv('C:\Projects\PycharmProjects\GWAS\PLink\phenotypes.pheno', header='infer', usecols=[30], sep=' ')

print(first_column)

print('insert the  phenotypes FT10 into genotype')
idx = 0
data.insert(loc=idx,column='FT10',value=first_column)
f=data.iloc[:5,:5]
print(f)
print('Delete the line containing Nan ')
data = data.dropna(subset=['FT10'])#Delete the line containing Nan
g=data.iloc[:5,:5]
print(g)
print('Write raw file')
data.to_csv('C:\Projects\PycharmProjects\GWAS\PLink\_p1.csv', sep=',', header=None, index=None)
