'''Find the nth term of the series.

1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243,64, 729, 128, 2187 …'''

def main():
    n=int(input('Enter the no. of terms : '))
    o=e=0
    print('The series is as follows : ')
    for i  in range (n):
        if i%2 == 0 :
            print(pow(2,o),end=',')
            o=o+1
        else:
            print(pow(3,e),end=',')
            e=e+1

main()