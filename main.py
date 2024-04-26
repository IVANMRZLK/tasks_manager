from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Главное окно")
window.state('zoomed')

window.option_add("*tearOff", FALSE)


# функции для исполняющих виджетов
def zagluschka():
    pass


def click_add_task_from_menu():
    window2 = Tk()
    window2.title("Добавление задач")
    window2.geometry("2500x500")
    label = ttk.Label(window2, text="Здесь когда-нибудь будут добаляться задачи")
    label.pack(anchor=CENTER, expand=1)


def click_add_project_from_menu():
    window3 = Tk()
    window3.title("Добавление задач")
    window3.geometry("2500x500")

    label_project_name = ttk.Label(window3, text="Название проекта")
    label_project_name.place(x=20, y=35)
    project_name = ttk.Entry(window3)
    project_name.place(x=20, y=60)

    label_project_type = ttk.Label(window3, text="Тип проекта")
    label_project_type.place(x=200, y=35)
    project_types = ['Фриланс', 'Поиск работы', 'Pet-проект', 'Обучение']
    project_type = ttk.Combobox(window3, values=project_types)
    project_type.place(x=200, y=60)

    label_project_cyclicality = ttk.Label(window3, text="Цикличность проекта")
    label_project_cyclicality.place(x=400, y=35)
    project_cyclicalities = ['Единоразовый', 'Ежедневный', 'Еженедельный']
    project_cyclicality = ttk.Combobox(window3, values=project_cyclicalities)
    project_cyclicality.place(x=400, y=60)

    label_new_project_task = ttk.Label(window3, text="Новая задача")
    label_new_project_task.place(x=20, y=115)
    new_project_task = ttk.Entry(window3)
    new_project_task.place(x=20, y=140)

    btn_append_new_task = ttk.Button(window3, text="Добавить задачу", command=zagluschka)
    btn_append_new_task.place(x=400, y=140)

    btn_create_project = ttk.Button(window3, text="Создать проект", command=zagluschka)
    btn_create_project.place(x=200, y=240)
    # label = ttk.Label(window3, text="Здесь когда-нибудь будут добаляться проекты")
    # label.pack(anchor=CENTER, expand=1)


def click_add_note_from_menu():
    window4 = Tk()
    window4.title("Добавление задач")
    window4.geometry("2500x500")
    label = ttk.Label(window4, text="Здесь когда-нибудь будут добаляться заметки")
    label.pack(anchor=CENTER, expand=1)
##########################################


main_menu = Menu()

task_menu = Menu()
task_menu.add_command(label="Добавить задачу", command=click_add_task_from_menu)
task_menu.add_command(label="Изменить задачу")
task_menu.add_command(label="Удалить задачу")
task_menu.add_separator()
task_menu.add_command(label="Удалить все задачи")

projects_menu = Menu()
projects_menu.add_command(label="Добавить проект", command=click_add_project_from_menu)
projects_menu.add_command(label="Изменить проект")
projects_menu.add_separator()
projects_menu.add_command(label="Удалить все проекты")

notes_menu = Menu()
notes_menu.add_command(label="Добавить заметку", command=click_add_note_from_menu)
notes_menu.add_separator()
notes_menu.add_command(label="Удалить все проекты")

main_menu.add_cascade(label="Задачи", menu=task_menu)
main_menu.add_cascade(label="Проекты", menu=projects_menu)
main_menu.add_cascade(label="Заметки", menu=notes_menu)

window.config(menu=main_menu)

window.mainloop()
