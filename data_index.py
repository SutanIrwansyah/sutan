list = [1,2,3,4,5]
list = ["Tony","Stark"]
#print(list[3] # hasilnya apa ? 4

for data in list:
    print(data)
	
# for with enumerate
for index, data in enumerate(list):
    print("index ke %i adalah %s"%(index,data))
	#print("index ke %i adalah %s"%(index,list[index]))