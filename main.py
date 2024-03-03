import os

def rename():
    dir = os.path.abspath(os.curdir)#получим путь к папке откуда запускаем скрипт
    print(dir)
    #dir_list = sorted(os.listdir(dir), reverse=True)

    #получить список всех папок
    dir_list = sorted(os.listdir(dir), reverse=True)
    print(dir_list)
    #циклом пороходим и ищем все папки
    for dir_el in dir_list:
        print(f'Открываем папку {dir_el}')
        dir_el_list = sorted(os.listdir(dir), reverse=True)#считываем содержимое
        ps_count = dir_el_list.count('ps')
        vs_count = dir_el_list.count('vs')
        if ps_count > 0 and vs_count > 0:
            pass#основной код


        #если нет напишем что папка не подходит для начала основного скрипта




if __name__ == '__main__':
    rename()
    input("Нажмите Enter, чтобы закрыть консоль...")

