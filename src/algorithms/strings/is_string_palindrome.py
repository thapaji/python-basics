def main():
    str1 = 'racecar'
    str2 = 'nepal'
    str3 = 'madam'
    print(f'The string {str1} is palindrome??\n{is_palindrome(str1)}\n')
    print(f'The string {str2} is palindrome??\n{is_palindrome(str2)}\n')
    print(f'The string {str3} is palindrome??\n{is_palindrome(str3)}\n')


def is_palindrome(string):
    tmp_str = string[::-1]
    if string == tmp_str:
        return 'YES'
    return "NO"


main()
