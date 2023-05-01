def aab(x,y):
    odd_num=[]
    even_num=[]
    for num in range (x,y):
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    print ('ood number:',odd_num) 
    print ('Even number:',even_num)  

aab(5,9)             