def receive():#Function for inputting integer
    count=0
    while count==0:
        a=input('Enter the integer :')
        try:
            val=int(a)
            count+=1
            return val
        except ValueError:
            try:
                val=float(a)
                print('You entered a float. ')
            except ValueError:
                print('You did not enter a number. ')
my_list=[]
count=1
print('Creating the list')
while len(my_list)<7: #creating the list
    my_list.append(receive())
count_1=0 
while count_1==0:#inputting digit
    try:
        print('Enter the digit you want to find its number of repetitions')
        x=input(':')
        try:
            val=int(x)
            if val<=9 and val>=0:
                count_1+=1
            else:
                print('You did not enter a digit.')
        except ValueError:
            try:
                val=float(x)
                print('You entered a float.')
            except ValueError:
                print('You did not enter a number.')
def find_digit_in_array(x,array):#This function receives a list and a digit.Then,returns the number of repetition of this digit in the list.
    def find_digit_in_element(x,y):#This function  is defined in another function.It returns the number of repetition of the digit in the element.
        count_1=0  #A variable for counting the number of repetition of a digit in the element
        if y==0 and x==0:
            count_1+=1
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
ans=find_digit_in_array(val,my_list)
print('Digit',val,'is repeated',ans,'times in the list.')
        
                
          
        
