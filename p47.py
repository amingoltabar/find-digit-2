my_list=[]
for i in range(7):#creating the list
    a=float(input('Create your list.Enter the integer: '))
    while a!=int(a):
        a=float(input('You did not enter an integer.Enter the integer: '))
    a=int(a)
    my_list.append(a)
x=float(input('Enter the digit you want to find the number of its repetition in a list: '))
while x<0 or x>9 or x!=int(x):#Entered indexes must be integer and in the range of the list.
    x=float(input('Number you have entered is not a digit.Enter the digit again: '))
x=int(x)
def find_digit_in_array(x,array):#This function receives a list and a digit.Then,returns the number of repetition of this digit in the list.
    def find_digit_in_element(x,y):#This function  is defined in another function.It returns the number of repetition of the digit in the element.
        count_1=0#A variable for counting the number of repetition of a digit in the element
        if y==0 and x==0:
            count_1=1
        else:
            while(y!=0):
                r=y%10
                if r==x:
                    count_1+=1
                y=int(y/10)
        return count_1
    size=len(array)
    count=0 #A variable for counting the number of repetition of a digit in the list
    for i in range(size):
        count+=find_digit_in_element(x,array[i])
    return count
ans=find_digit_in_array(x,my_list)
print('Digit',x,'is repeated',ans,'times in the list.')
        
                
          
        
