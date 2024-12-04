import os
import shutil
import shlex


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
    list_of_content = os.listdir()
    if file_name.startswith('.'):
        count = 0
        file_extention = file_name
        for file in list_of_content:
            if file.endswith(file_extention):
                os.remove(file)
                count += 1
        if count == 0:
            print('File extension', file_extention, 'not found in this directory')
    if os.path.isfile(file_name):
        os.remove(file_name)
    if os.path.isdir(file_name):
        shutil.rmtree(file_name)
    elif file_name not in list_of_content and not file_name.startswith('.'):
        print("No such file or directory")


def mvb(users_input):
    result = users_input.split(' ')
    try:
        old_name = result[1]
        new_name = result[2]
        list_of_content = os.listdir()
        content_of_destination_folder = os.listdir(new_name)
        print('old name is', old_name)
        print(list_of_content)
        if new_name in list_of_content or old_name in content_of_destination_folder:
            print('The file or directory already exists')
        if old_name in list_of_content:
            print(old_name, 'it is in the file')
        if os.path.isfile(old_name):
            print('renamed', old_name, 'to', new_name)
        if os.path.isfile(old_name) and not os.path.isdir(new_name):
            os.rename(old_name, new_name)
            print('renamed', old_name, 'to', new_name)
            #print('one file')
        if os.path.isfile(old_name) and os.path.isdir(new_name):
            print('file and directory')
        #else:
        #    os.rename(old_name, new_name)
    except IndexError:
        print('Specify the current name of the file or directory and the new location and/or name')
    except FileNotFoundError:
        print('No such file or directory')


def mv(users_input):
    result = users_input.split(' ')
    try:
        old_name = result[1]
        new_name = result[2]
        if os.path.isfile(old_name) and not os.path.isdir(new_name):
            list_of_content = os.listdir()
            if new_name in list_of_content:
                print('The file or directory already exists')
            else:
                os.rename(old_name, new_name)
        if os.path.isdir(new_name):
            shutil.move(old_name, new_name)

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


def cp(input_from_user):
    result = shlex.split(input_from_user)
    try:

        file_path = result[1]
        dst_folder = result[2]
        split_file = file_path.split('/')
        file = split_file[-1]
        content_of_current_folder = os.listdir()
        content_of_destination_folder = os.listdir(dst_folder)

        if file not in content_of_current_folder:
            print('No such file or directory')
        elif file in content_of_destination_folder:
            print(file, 'already exists in this directory')
        else:
            shutil.copy(file_path, dst_folder)
    except IndexError:
        print('Specify the current name of the file or directory and the new location and/or name')
    except IsADirectoryError:
        print('Specify the current name of the file or directory and the new location and/or name')
    except FileNotFoundError:
        print('No such file or directory')


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
        print('Specify the current name of the file or directory and the new location and/or name')
    elif inp.startswith('mv '):
        mv(inp)
    elif inp == 'mkdir':
        print('Specify the name of the directory to be made')
    elif inp.startswith('mkdir '):
        mkdir(inp)
    elif inp == 'cp':
        print('Specify the file')
    elif inp.startswith('cp '):
        cp(inp)
    else:
        print('Invalid command')
