#---------------- السوال الاول  الجزء الثاني
Names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
upper_words=[]
for name in ( Names):
   upper_words.append(name.upper())
print(upper_words) 


list_names=[name.upper() for name in (Names)] 
print(list_names)

upper_case=list(map(lambda x:x.upper(),Names))
print(upper_case)

#--------------------- السوال الثاني 

find_a=[]
for name in Names:
   if "a" in name:
      find_a.append(name)
print (find_a)    

find_a=[a for a in Names if "a"in a]
print(find_a)

find_aa=list(filter(lambda x: "a" in x,Names))
print(find_aa)

#------------------السوال الثالث
names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']

t_names = []
for name in names:
    if name[0] == 't':
        t_names.append(name)

print(t_names)

t_name=[name for name in t_names if name[0] == "t"]
print(t_name)    
        
t_name1=list(filter(lambda x:"t" in x[0],t_name))
print(t_name)

# ------------------السوال الرابع
letter_2=[]
for name in names:
   if name.count('a') >=2:
      letter_2.append(name)
print(letter_2)

letter_2=[name for name in names if name.count('a')>=2]
print(letter_2)

letter_2 = list(filter(lambda x: x.count("a") >=2 , names))
print(letter_2)

#------------------- السوال الخامس
len_list =[]
for name in names:
   list_names1=len(name)
   len_list.append(list_names1)
print (len_list)
   

len_list=[len(name) for name in names] 
print(len_list)  

len_list =list(map(lambda x:len(x),names))
print(len_list)

#-------------السوال السادس
# الجزيئة السابعة
names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']
a, *b = names    # قمنا بتعين a اول شخص في القائمة
print('a:',a)    # *b تم تعيينه على انها باقي القائمة
print('b:',b)
#الجزئية الثامنة
a ,*_ , b = names
print('a:',a)     # الاول a
print('b:',b)      # b الاخير,*_ من الثاني الى قبل الاخير
#الجزئية الثامنة
a , b , *_ = names
print('a:',a) # aالاول في القائمة
print("b:",b)# bالثاني في القائمة
              # *_ من الثالث الى الاخير