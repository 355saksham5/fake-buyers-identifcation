import pandas as pd
def f1():
   data = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
   j=0
   for i in range(0,3040):
    if(data.iloc[i]['Billing Zip']==data.iloc[i]['Shipping Zip'] and data.iloc[i]['Billing Zip']!="NaN"):
       print(data.iloc[i]['Order #'],"  ",data.iloc[i]['Shipping Zip'],"    ",data.iloc[i]['Billing Name'])
       j=j+1
   print("Total fake orders:   ",j)

def f2():
    data = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    s=list(data['LineItem Name'])
    j=0
    res = {i:s.count(i) for i in s}
    for i in res:
        if(res[i]>1):
            print(i,"   ",res[i])
            j=j+1
    print("Total fake orders:   ",j)
def f3():
    data = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    s=list(data['Total'])
    j=0
    for i in range(0,len(s)):
        str=float(s[i][2:].replace(',',''))
        if(str>=20000.00):
            print(data.iloc[i]['LineItem Name'],s[i])
            j=j+1
    print("Total fake orders:   ",j)
def f4():
    x=[]
    m=[]
    l=[]
    co=0
    data = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    for i in range(0,3040):
        l.append(data.iloc[i]['LineItem Name']+" "+str(data.iloc[i]['Shipping Street Address']))
        m.append(data.iloc[i]['Payment Method'])
    for i in range(0,3040):
        f=[]
        k=0
        for j in range(0,3040):
            if l[i] == l[j]:
                k=k+1
                f.append(j)
            if(k>1):
                h=set(f)
                if(len(h)==len(f)):
                  x.append(str(l[i])+"  "+str(m[i]))
    x=list(set(x))        
    for i in range(0,len(x)):
        print(x[i])    
    print("Total fake orders:   ",len(x))
def f5():
    data = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    j=0
    for i in range(0,3040):
        if(str(data.iloc[i]['Shipping State'])[0:2]!='IN'):
            print(data.iloc[i]['Order #'],data.iloc[i]['LineItem Name'],data.iloc[i]['Shipping Street Address'])
            j=j+1
    print("Total fake orders:   ",j)

print("Enter a choice:")
sp=int(input())
if(sp==1):
    f1()
elif(sp==2):
    f2()
elif(sp==3):
    f3()
elif(sp==4):
    f4()
elif(sp==5):
    f5()
i=input("enter 1 to exit")



