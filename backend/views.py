from django.shortcuts import render
import os
import datetime
import sys

path_exec = os.getcwd()  # 项目根目录hello-vue-django


def index(request):
    return render(request, 'index.html')


def test(request):
    # 将mysql的bin目录追加到系统路径中
    sys.path.append('/usr/local/mysql/bin/')
    # path_exec = os.getcwd();
    print(path_exec)
    if not os.path.exists(path_exec+'/backend/db_dumpfile'):
        os.makedirs(path_exec+'/backend/db_dumpfile')
    os.chdir(path_exec+'/backend/db_dumpfile')
    print(path_exec)
    result = os.system("mysqldump -uperch fortest>backup"+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+".sql")
    if not result:
        print('backup success')
    else:
        print('backup fail')

    rm_backup(path_exec+'/backend/db_dumpfile', 2)
    print('dd')
    return render(request, 'index.html')


# 自动保留最近的几个文件
def rm_backup(rm_path, nums):
    files_list = os.listdir(rm_path)
    list = []
    dict = {}
    for i in files_list:
        all_path = os.path.join(rm_path,i)
        ctime = os.path.getctime(all_path)
        dict[all_path] = ctime
    all_path_ctime_list = sorted(dict.items(), key=lambda item:item[1])
    if len(all_path_ctime_list) <= nums:
        pass
    else:
        for i in range(len(all_path_ctime_list) - nums):
            os.remove(all_path_ctime_list[i][0])
