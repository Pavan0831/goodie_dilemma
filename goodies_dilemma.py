#opening file to read input

in_file =open("input.txt","r")

#opening output file for writing output

out_file = open("output.txt","w+")
goodies={}
out_list=[]


#reading the input file 

for f in in_file:
    readPrice=f.index(":")
    print(f[readPrice+1:].strip())
    print(f[:readPrice])
    goodies[f[:readPrice]]=f[readPrice+1:].strip()

print(goodies) 
sPrice=list(goodies.values())
sPrice=[int(i)for i in sPrice]

#To get prices to be distributed in order sorted list in decsending order 

sPrice.sort(reverse=True)
print(sPrice)


#getting inputs

No_of_emp=int(input("Enter number of employees: "))
conseideredLen=(len(sPrice)-No_of_emp)

print(conseideredLen)

#finding minimum difference between highest and lowest

for i in range(conseideredLen):
    priceMax=sPrice[i]
    priceMin=sPrice[No_of_emp+i]
    if i == 0:
        diff=priceMax-priceMin
        idx_choosen=i
    elif (priceMax-priceMin)<diff:
        diff=priceMax-priceMin
        idx_choosen=i

choosen_prices=sPrice[idx_choosen:No_of_emp+idx_choosen]


#differnce between high and low price


diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

count=0
for key,value in goodies.items():
    sPrice[count]
    print(value)
    if int(value)in choosen_prices and count<No_of_emp:
        str1=key+": "+value
        #preparing  list for output
        out_list.append(str1)
        count+=1
        print(str1)

#writing to output file

out_file.write("The goodies selected for distribution: ")

out_file.write("\n")

for i in out_list:
    out_file.write(i)
    out_file.write("\n")
out_file.write("And the difference between  chosen goodie with highest price and the lowest price are "+str(diff))

in_file.close()
out_file.close()