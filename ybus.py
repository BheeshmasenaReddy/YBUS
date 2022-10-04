p=input('Enter line data in [[from_bus,to_bus,resistance,reactance]] :')
#p='[[1,2,0,0.2],[2,3,0,0.25],[1,3,0,0.25]]'
linedata=eval(p)
fb=[]
tb=[]
r=[]
x=[]
z=[]
y=[]

#for reading line data
try:
    for i in range(len(linedata)):
        for j in range(len(linedata[0])):
            if j==0:
                fb.append(linedata[i][j])
            elif j==1:
                tb.append(linedata[i][j])
            elif j==2:
                r.append(linedata[i][j])
            elif j==3:
                x.append(linedata[i][j])
except:
    print("There seems to be an error, Please enter linedata properly")
    exit()

#for calculating z and y
for k in range(len(r)):
    m=complex(r[k],x[k])
    z.append(m)
    y.append(1/m)
nbus=max(max(fb),max(tb))
nbranch=len(fb)
ybus=[]

#creating a ybus as null matrix
for i in range(nbus):
    ybus.append([0]*nbus)

#formation of mutual admittance
for i in range(nbranch):
    ybus[fb[i]-1][tb[i]-1]-=(y[i])
    ybus[tb[i]-1][fb[i]-1]=ybus[fb[i]-1][tb[i]-1]

#formation of self admittance
for m in range(nbus):
    for n in range(nbus):
        if (fb[n]-1)==m:
            ybus[m][m]+=y[n]
        elif (tb[n]-1)==m:
            ybus[m][m]+=y[n]

#function for printing ybus and linedata
def mat_print(lis):
    for i in range(nbus+1):
        for j in range(nbus+1):
            if i==0:
                if j==0:
                    print(' ',end='  ')
                elif j>0 and j<len(lis):
                    print(j,end='  ')
                else:
                    print(j)
            elif i==1:
                if j==0:
                    print(i,end=' ')
                elif j>0 and j<len(lis):
                    print(lis[i-1][j-1],end=' ')
                else:
                    print(lis[i-1][j-1])
            elif i==2:
                if j==0:
                    print(i,end=' ')
                elif j>0 and j<len(lis):
                    print(lis[i-1][j-1],end=' ')
                else:
                    print(lis[i-1][j-1])
            elif i==len(lis):
                if j==0:
                    print(i,end=' ')
                elif j>0 and j<len(lis):
                    print(lis[i-1][j-1],end=' ')
                else:
                    print(lis[i-1][j-1])

#making linedata
line_data=[]
data=[fb,tb,z]
for i in range(nbus):
    line_data.append([0]*nbus)
for i in range(nbus):
    for j in range(nbus):
        line_data[i][j]=data[j][i]

#printing output
print('Adjacency matrix [A] of the given power systems network:')
mat_print(line_data)
print('\nNo.of buses:',nbus)
print('\nNo. of transmission lines:',nbranch)
for i in range(len(z)):
    print(f'\nPrimitive impedance of line {i+1}:',z[i],'ohms')
print('\nBus admittance matrix:\nYBUS=')
mat_print(ybus)