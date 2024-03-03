import os
from subprocess import check_output, CalledProcessError, STDOUT
import subprocess32 as subprocess



def rename():
    dir = os.path.abspath(os.curdir)#получим путь к папке откуда запускаем скрипт
    print(dir)
    #dir_list = sorted(os.listdir(dir), reverse=True)


    tree = os.walk(dir)# получим дерево каталогов

    for i in tree:
        if i[1] == ['ps', 'vs']: # если в папке есть и ps и vs, то это нужная папка
            print(f'В папке {i[0]}:')
            for file in i[2]: # пройдем по всем файлам в этой папке
                if file.endswith('.ts'): # если расширение ts, то это нужный файл
                    filename = f'{i[0]}/{file}' # соберем полный путь с именем файла
                    #соберем строку для запроса в коммандную строку
                    command = (f'"C:\\Users\\Ranger\\Downloads\\ffmpeg-2024-02-29-git-4a134eb14a-full_build\\ffmpeg-2024-02-29-git-4a134eb14a-full_build\\bin\\ffprobe.exe" -i {filename} -show_entries format=duration -v quiet -of csv="p=0"')
                    p = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    text = p.stdout.read() # получим текстовое значение продолжительности видеофайла
                    time_duration = format(float(text), ".3f")# преобразуем в число с 3 знакими после запятой
                    #retcode = p.wait()
                    print(f'{os.path.splitext(file)[0]} - {time_duration}')
                    base_name = os.path.splitext(file)[0].partition('T')[0]
                    print(f'{base_name}T{time_duration}\n')

        #Доработать бэкап файла. лучше заменой расширения




if __name__ == '__main__':
    rename()
    input("Нажмите Enter, чтобы закрыть консоль...")

