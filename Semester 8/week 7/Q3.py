import pandas as pd

data ={
    "A" :[10,20,30,40,50],
    "B":[5,10,15,20,25],
    "C" :[1,2,3,4,5],
    "D" :[4,8,12,16,20]
}

df = pd.DataFrame(data)
print(df,"\n")
#1 Average of the second column
avg = df.iloc[:,1].mean()
print("Average of 2nd column : ",avg  )

#2 Avg of first 5 rows and 3rd and 4th column
avg2=df.iloc[:5,2:4].mean()
print("Average of first 5 rows , columns 3 and 4 :\n",avg2)

#3Row-wise sum
row_sum=df.sum(axis=1)
print("Row-Wise sum : ",row_sum)

#4 MaX OF AVG VALUE IN A ROW
row_sums= df.mean(axis=1)
max_row = row_sums.max()
print("Maximum of row-wise averages: ", max_row)


