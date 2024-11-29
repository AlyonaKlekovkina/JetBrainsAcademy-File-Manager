import os


def change_directory():
    while True:
        inp = input()
        if inp == 'pwd':
            print(os.getcwd())
        elif inp == 'cd ..':
            os.chdir("..")
            current_directory = os.getcwd()
            print(os.path.basename(current_directory))
        elif inp.startswith('cd '):
            try:
                result = inp.split(' ')
                path = result[-1].strip()

                dir = '/Users/alyona/PycharmProjects/File Manager/File Manager/task/module/root_folder'
                #dir = os.path.dirname(__file__)
                print(dir)
                filename = os.path.join(dir, path)
                os.chdir(filename)
                current_directory = os.getcwd()
                print(os.path.basename(current_directory))
            except FileNotFoundError:
                print('not found')
        elif inp == 'quit':
            break
        else:
            print('Invalid command')


print('Input the command')
change_directory()

