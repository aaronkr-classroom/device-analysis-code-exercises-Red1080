#list
my_list1=[1,2,'a',"hello"]
my_list2=[1,'a',3,67]
my_list1[1]=67
my_list2.append(89)

#tuple(cant modify)
my_t1=('Arnold',1984)
my_t23=(1991,2003)
print(my_t23[0])
my_t23=(100,1000)

#dictionary
my_dict={
    "name":"Red",
    "list":my_list1,
    "tup":(1,2,3),
    }
my_dict['tup']=(1,4,5)
my_dict['name']="brian"

#set
set1={1,2,'a',"hello"}
set2={2,3,'b',"hello"}
union_set= set1 | set2
intersection_set= set1 & set2
diff_set = set1-set2
sym_diff_set= set1^set2

print('u:',union_set)
print('i:',intersection_set)
print('d:',diff_set)
print('sd:',sym_diff_set)








