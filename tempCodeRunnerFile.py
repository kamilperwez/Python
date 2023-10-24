#Scroll to look for Patterns
def main():
    while True:
        try:
            inp=int(input(('Enter the no. of Pattern to be Printed  or 0 For EXIT ')))
            if inp == 0:
                 print('Thanks')
                 break
            lines=int(input(('Enter no. of lines  :')))
            match inp:
                case 1 : pattern1(lines)
                case 2 : pattern2(lines)
                case _: print('No Pattern')
        except:
            print('Not A VALID INPUT')            

#Pattern1
'''* * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
        '''

def pattern1(n):
    for i in range(n):
        for j in range(n-i) :
            print('*',end=' ')
        print('\n',end=' '*(i+1))
    print('\n')

#Pattern 2
'''
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *

'''
def pattern2(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end=' ')
        print('\n',end=' '*((i+1)*2))
    print('\n')

if __name__=='__main__':
    main()
