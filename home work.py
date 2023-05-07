#------------------- السوال الاول  الجزئية رقم واحد -----------------------
def aab(x,y):
    odd_num=[]      # list الفردي
    even_num=[]     # list  الزوجي
    for num in range (x,y):
        if num % 2 == 0:        # هذا المعادلة تستخدم للحصول على رقم زوجي
            even_num.append(num)
        else:
            odd_num.append(num)
    print ('ood number:',odd_num) 
    print ('Even number:',even_num)  

aab(5,9)             
#----------------------------- السوال الثاني--------
def divided(x,y):
       for s in range(1,101):
            if s % x == 0 and s % y ==0:
             print(s)
       
divided(3,5)  

#--------------- السوال الثالث--------
def  multi(x,y):
    for cc in range(x,y+1):
        print("Multi table",cc)
        for j in range (1,11):
            print(cc ,'x',j, '=',cc*j)
        print("----------")    
multi(2,4)        

#-------------------السوال الرابع--------
def remove_dup(sentence):
    words= sentence.split()
    rr = set(words)
    nn=' '.join(rr)
    print(nn)

remove_dup('hello fadi hello saif')    

#-----------------السوال الخامس ---------
def withot_duplicat (sentence):
    a = sentence.split()
    print(len(a))

withot_duplicat('hi majid where are you') 

#------------------السوال السادس----------
def remove_sen(sentence,word):
    a = sentence.split()
    a = [w for w in a if w !=word]
    new_sen = ' '.join(a)
    return new_sen
sentence='hi majid how are you do'
word = "do"
new_sen=remove_sen(sentence,word)
print(new_sen)  

#-------------------السوال السابع----------
def count_word(sentence, word):
    count = 0
    for w in sentence.split():
        if w == word:
            count += 1
    print(f"the word {word} appear {count} times in the sentence")        
sentence="Hi son where did you go last weak ? son say"
word = "son"
count_word(sentence,word)
#------------------------السوال الثامن------------
def divide_dd(x,y):
    for i in range (x,101):
        if i % y == 0:
            print(i)
print(divide_dd(5,3))            