import datetime
def redact_nothes_titul():
    index = int(input("Какой заголовок хотите поменять(укажите его индекс): "))
    current_datetime = datetime.datetime.now()

    with open('file.txt', 'r', encoding='utf-8') as f:
         tituls = f.readlines()
         if index < 0 or index >= len(tituls):
            print("Некоректный ввод")
            return

         for i,elem in enumerate(tituls):
            elements = elem.split(",")

            if elements[0] == tituls[index]:
                new_tituls = input("Введите новый заголовок: ")
                tituls[i] = f"({current_datetime}) - " + "Заголовок: " + new_tituls.upper() + "\n"

                with open('file.txt', 'w', encoding='utf-8') as f_out:
                    f_out.writelines(tituls)
                    print("Заголовок успешно обнавлён!!")
                    return


def redact_nothes():
    index = int(input("Какую заметку вы хотите редактировать "
                      "(введите номер заголовка по порядку)(если заметка находится в первом заголовке напишите 1 и тд): "))


    with open('file.txt', 'r', encoding='utf-8') as f:
        notes = f.readlines()
        if index < 0 or index >= len(notes):
            print("Некорректный ввод индекса")
            return

        for i, elem in enumerate(notes):
            elements = elem.split(",")

            if elements[0] == notes[index].split(",")[0]:
                new_note = input("Введите новую заметку: ")
                notes[i] = "Ваша заметка" + ": " + f"{new_note}" + "\n"

                with open("file.txt", "w", encoding="utf-8") as f_out:
                    f_out.writelines(notes)
                print("Заметка успешно обновлена")
                return




def nothes():
    str = input("Введите заметку: ")
    return str


def read_nothes():
    with open("file.txt", "r", encoding="utf-8") as f:
        for string in f:
            print(*string.strip().split(";"))




def delete_notes():
    count = int(input("Какую заметку вы хотите удалить (введите просто номер заметки)(если заметка первая, введите 0, "
                      "если вторая, введите 2 и т.д.): "))

    with open("file.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    if count < 0 or count >= len(lines):
        print("Некорректный ввод")
        return

    del lines[count]
    del lines[count]

    with open('file.txt', 'w', encoding="utf-8") as nf:
        nf.writelines(lines)

    print("Заметка удалена!!")
def write_nothes():
    with open('file.txt', 'a', encoding='utf-8') as f:
         titul = input("Введите заголовок заметки: ")
         current_datetime = datetime.datetime.now()
         f.write(f"({current_datetime}) - " +
                 "Заголовок: " + titul.upper() + "\n")
         f.write("Тело заметки" + ": "  + f"{nothes()}" + "\n")

    print('Заметка добавлена!!')

def main():
    while True:
        n = input("Что вы хотите сдлеать:(add) - записать заметку, (delete) - удлаить заметку,(redact) - редактировать заметку,"
                      " (read) - прочитать заметки, (over) - закончить работу с заметками: ")
        current_datetime = datetime.datetime.now()

        if n == "add":
            write_nothes()


        elif n == "delete":
            delete_notes()
            break


        elif n == "redact":
            stroka = int(input("Что вы хотите поменять: (1)- Заголовок, (2)- Заметку: "))
            if stroka == 1:
                redact_nothes_titul()
            elif stroka == 2:
                redact_nothes()



        elif n == "read":
            read_nothes()

        elif n == "over":
            print("Работа закончена!!" + "\n" +
                  "Приятно с вами работать!))" + "\n" + "Дата и время:" + f"{current_datetime}")
            break
        else:
            print("Некорректный ввод")




if __name__ == '__main__':
    main()
