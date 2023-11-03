'''
. The program will recieve 3 English words inputs from STDIN

    These three words will be read one at a time, in three separate line
    The first word should be changed like all vowels should be replaced by *
    The second word should be changed like all consonants should be replaced by @
    The third word should be changed like all char should be converted to upper case
    Then concatenate the three words and print them

Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h*wa@eYOU.

You can assume that input of each word will not exceed more than 5 chars
Test Cases
Case 1

Input

    how
    are
    you

Expected Output : h*wa@eYOU
Case 2

Input

    how
    999
    you

Expected Output : h*w999YOU
'''

def main():
    f=[x for x in(input('first '))]
    s=[x for x in(input('second '))]
    t=(input('Third ')).upper()
    for i in range(len(f)):
        if f[i] == 'a' or f[i] == 'e' or f[i] == 'i' or f[i] == 'o' or f[i] == 'u':
            f[i]='*'
    for i in range(len(s)):
        if (s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u') and (s[i].isalpha()):
            s[i]='@'
    st=''.join(x for x in f)
    sr=''.join(x for x in s)
    print(st+sr+t)

main()
    