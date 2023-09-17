string='codelocked'
quit_command = 0
while quit_command not in ["q","QUIT"]:
    substring=input('Enter the substring which you want to search : ')
    if substring in string:
        print(f'Congratulation!!! "{ substring }" Substring is present in "{string}" string.' )
        print('q TO QUIT and ENTER to continue...')
        quit_command=input()
    else:
        print('Please try again!! no such string found!!!')
        print('q TO QUIT and ENTER to continue...')
        quit_command=input()
