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