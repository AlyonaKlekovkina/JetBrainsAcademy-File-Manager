import os


def change_directory(inp):
    try:
        result = inp.split(' ')
        path = result[-1].strip()
        dir = '/Users/alyona/PycharmProjects/File Manager/File Manager/task/module/root_folder'
        filename = os.path.join(dir, path)
        os.chdir(filename)
        current_directory = os.getcwd()
        print(os.path.basename(current_directory))
    except FileNotFoundError:
        print('not found')


def converter(bytes):
    if int(bytes) < 1024:
        return '{}B'.format(bytes)
    if 1024 <= int(bytes) < 1048576:
        kb = round(int(bytes) / 1024)
        return '{}KB'.format(kb)
    if 1048576 <= int(bytes) < 1073741824:
        mb = round(int(bytes) / 1048576)
        return '{}MB'.format(mb)
    if int(bytes) >= 1073741824:
        gb = round(int(bytes) / 1073741824)
        return '{}GB'.format(gb)


os.chdir('/Users/alyona/PycharmProjects/File Manager/File Manager/task/module/root_folder')
print('Input the command')
while True:
    inp = input()
    if inp == 'pwd':
        print(os.getcwd())
    elif inp == 'cd ..':
        os.chdir("..")
        current_directory = os.getcwd()
        print(os.path.basename(current_directory))
    elif inp.startswith('cd '):
        change_directory(inp)
    elif inp == 'quit':
        break
    elif inp == 'ls':
        list_of_content = os.listdir()
        file_list = []
        directory_list = []
        for item in list_of_content:
            if os.path.isfile(item):
                file_list.append(item)
            else:
                directory_list.append(item)
        for directory in directory_list:
            print(directory)
        for file in file_list:
            print(file)
    elif inp == 'ls -l':
        list_of_content = os.listdir()
        for file in list_of_content:
            if os.path.isfile(file):
                file_size = os.stat(file)
                print(file, file_size.st_size)
            else:
                print(file)
    elif inp == 'ls -lh':
        list_of_content = os.listdir()
        for file in list_of_content:
            if os.path.isfile(file):
                file_size = os.stat(file)
                h_reabable = converter(file_size.st_size)
                print(file, h_reabable)
            else:
                print(file)
    else:
        print('Invalid command')
