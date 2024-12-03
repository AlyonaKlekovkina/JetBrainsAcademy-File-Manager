import os
import shutil


def change_directory(input_from_user):
    try:
        result = input_from_user.split(' ')
        path = result[-1].strip()
        dir = '/Users/alyona/PycharmProjects/File Manager/File Manager/task/module/root_folder'
        filename = os.path.join(dir, path)
        os.chdir(filename)
        current_directory = os.getcwd()
        print(os.path.basename(current_directory))
    except FileNotFoundError:
        print('not found')


def converter(raw_info_bytes):
    if int(raw_info_bytes) < 1024:
        return '{}B'.format(raw_info_bytes)
    if 1024 <= int(raw_info_bytes) < 1048576:
        kb = round(int(raw_info_bytes) / 1024)
        return '{}KB'.format(kb)
    if 1048576 <= int(raw_info_bytes) < 1073741824:
        mb = round(int(raw_info_bytes) / 1048576)
        return '{}MB'.format(mb)
    if int(raw_info_bytes) >= 1073741824:
        gb = round(int(raw_info_bytes) / 1073741824)
        return '{}GB'.format(gb)


def ls():
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


def lsl():
    list_of_content = os.listdir()
    for file in list_of_content:
        if os.path.isfile(file):
            file_size = os.stat(file)
            print(file, file_size.st_size)
        else:
            print(file)


def lslh():
    list_of_content = os.listdir()
    for file in list_of_content:
        if os.path.isfile(file):
            file_size = os.stat(file)
            h_reabable = converter(file_size.st_size)
            print(file, h_reabable)
        else:
            print(file)


def rm(input_from_user):
    result = input_from_user.split(' ')
    file_name = result[-1]
    if os.path.isfile(file_name):
        os.remove(file_name)
    elif os.path.isdir(file_name):
        shutil.rmtree(file_name)
    else:
        print("No such file or directory")


def mv(users_input):
    result = users_input.split(' ')
    try:
        old_name = result[1]
        new_name = result[2]
        list_of_content = os.listdir()
        if new_name in list_of_content:
            print('The file or directory already exists')
        else:
            os.rename(old_name, new_name)
    except IndexError:
        print('Specify the current name of the file or directory and the new name')
    except FileNotFoundError:
        print('No such file or directory')


def mkdir(input_from_user):
    result = input_from_user.split(' ')
    directory = result[-1]
    try:
        os.mkdir(directory)
    except FileExistsError:
        print('The directory already exists')


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
        ls()
    elif inp == 'ls -l':
        lsl()
    elif inp == 'ls -lh':
        lslh()
    elif inp == 'rm':
        print("Specify the file or directory")
    elif inp.startswith('rm '):
        rm(inp)
    elif inp == 'mv':
        print('Specify the current name of the file or directory and the new name')
    elif inp.startswith('mv '):
        mv(inp)
    elif inp == 'mkdir':
        print('Specify the name of the directory to be made')
    elif inp.startswith('mkdir '):
        mkdir(inp)
    else:
        print('Invalid command')
