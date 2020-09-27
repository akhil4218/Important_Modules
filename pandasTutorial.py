import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
"""

x={"XXX":[1,2,3,4,5],"first":[11,22,33,44,55],"SSS":[66,77,88,99,100]}
y={"YYY":[1,2,3,4,5],"second":[11,22,33,44,55],"lll":[66,77,88,99,100]}

df=pd.DataFrame(x)
df1=pd.DataFrame(y)
df2=pd.DataFrame(z)

"""



"""
#>>> Slicing

print(df.head(2))   #  df.head(n)-> to print first n numbers
print(df.tail(3))   #  df.tail(n)-> to print last n numbers
"""
"""
#>>> Merging

x={"XXX":[1,2,3,4,5],"first":[11,22,33,44,55],"SSS":[66,77,88,99,100]}
y={"XXX":[1,2,3,4,5],"second":[11,22,33,44,55],"lll":[66,77,88,99,100]}
z={"ZZZ":[21,22,23,24,25],"third":[114,224,334,444,554],"FFF":[661,717,88,199,100]}

df=pd.DataFrame(x)
df1=pd.DataFrame(y)
df2=pd.DataFrame(z)

m=pd.merge(df,df1,on="XXX")    
print(m)
"""

"""
#>>> joining

x={"XXX":[1,2,3,4,5],"first":[11,22,33,44,55],"SSS":[66,77,88,99,100]}
y={"xxx":[11,12,13,14,15],"first_first":[121,222,323,424,525],"SSS_sss":[636,773,838,399,310]}
z={"ZZZ":[21,22,23,24,25],"third":[114,224,334,444,554],"FFF":[661,717,88,199,100]}


df=pd.DataFrame(x,index=[11,12,13,14,16])
df1=pd.DataFrame(y,index=[11,12,13,14,15])
df2=pd.DataFrame(z)

j=df.join(df1)
print(j)

"""

"""
#>>> Changing Index and Coloumn Values

df=pd.DataFrame({"fir":[1,2,3],"sec":[4,5,6],"thi":[6,7,8]})
df.set_index("fir",inplace=True)   #index value name will be "fir"
df=df.rename(columns={"sec":"SEC"})    # to rename column names
print(df)
"""

"""
#>>>  Concatenation

df1=pd.DataFrame({"first":[1,2,3],"second":[11,22,33]},index=[1,2,3])
df2=pd.DataFrame({"first":[1,2,3],"second":[11,22,33]},index=[4,5,6])
c=pd.concat([df1,df2])   #to conctenation
print(c)

"""

#>>> DATA MUNGING
#fiir=pd.read_csv("C:\\Users\\NIKHIL\\Desktop\\Temporary\\y.csv",index_col=0)   # 2 theories -->index-col=0  means i dont wnt any index  ||   first row of index is coloumn name
#fiir.to_html("sooooo.html")   #to convert csv to html

















