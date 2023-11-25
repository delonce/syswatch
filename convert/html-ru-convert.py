

def Correcting_report():
    translate = ['Кодовое имя ОС', 'Краткое имя', 'Имя', 'Домашняя ссылка', 'Цветовой код имени ОС', 'Идентификатор схожих ОС', 'Поддержка', 'Логотип', 'Версия ОС',
                 'Уникальный идентификатор', 'Производитель', 'Имя продукта', 'Версия', 'Серийный номер', 'Идентификатор ОС', 'Тип включения', 'Идентификатор товара', 'Семья']

    original = ['VERSION_CODENAME','PRETTY_NAME', 'NAME', 'HOME_URL', 'ANSI_COLOR', 'ID_LIKE', 'SUPPORT_URL', 'LOGO', 'VERSION_ID',
                'UUID', 'Manufacturer', 'Product Name', 'Version', 'Serial Number', 'ID', 'Wake-up Type', 'SKU Number', 'Family']

    no_need = ['# dmidecode 3.3', 'Getting SMBIOS data from sysfs.', 'SMBIOS 2.5 present.','Handle 0x0001, DMI type 1, 27 bytes', 'System Information']

    i = 0

    # Открываем файл для чтения и чтения данных
    with open('report.txt', 'r', encoding='utf-8') as file:
        # Читаем данные из файла
        file_data = file.read()

    for i in range(len(translate)):
        new_file_data = file_data.replace(original[i],  translate[i])
        file_data = new_file_data

    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write(new_file_data)

    with open("test.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()

    with open("test.txt", "w", encoding='utf-8') as file:
        for line in lines:
            if line.strip("\n") in no_need:
                continue
            file.write(line)

def html_report():
    with open('test.txt', 'r', encoding='utf-8') as input_file:
        with open('output.html', 'w') as output_file:
            # Записываем заголовок HTML документа
            output_file.write('<html>\n<head>\n<title>Мой HTML документ</title>\n</head>\n<body>\n')

            # Читаем содержимое текстового файла и записываем его в HTML документ
            for line in input_file:
                output_file.write('<p>' + line.strip() + '</p>\n')

            # Записываем закрывающие теги HTML документа
            output_file.write('</body>\n</html>')

if __name__ == "__main__":
    Correcting_report()
    html_report()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
