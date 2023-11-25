from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

def txt_to_pdf(input_file, output_file):
    # Открываем файлы
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        # Создаем объект canvas для работы с pdf
        pdf_buffer = BytesIO()

        c = canvas.Canvas(pdf_buffer)
        pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
        c.setFont('FreeSans', 12)
        # Читаем содержимое файла txt
        txt_content = txt_file.read()

        # Разбиваем текст на строки и выводим его на страницу pdf
        lines = txt_content.split('\n')
        y = 750  # Начальная позиция по вертикали
        for line in lines:
            if y < 50:
                # Если страница заполнена, создаем новую страницу
                c.showPage()
                y = 750  # Начальная позиция по вертикали на новой странице
            c.drawString(50, y, line)
            y -= 20  # Сдвигаем позицию по вертикали для следующей строки

        # Завершаем создание pdf
        c.showPage()
        c.save()

    # Записываем буфер в файл
    with open(output_file, 'wb') as pdf_file:
        pdf_file.write(pdf_buffer.getvalue())

    print(f"Файл {input_file} успешно преобразован в {output_file}.")

# Пример использования
input_file = "test.txt"
output_file = "Report_PDF.pdf"
txt_to_pdf(input_file, output_file)