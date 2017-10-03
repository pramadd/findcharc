word_list = ['hello','world','my','name','is','Anna']
char ='o'
new_list=[]
for i in word_list:
    if char in str(i):
        new_list.append(i)
        #new_list += i
        print new_list