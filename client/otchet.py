import os
import subprocess
import re

from flask import Flask, send_file

app = Flask(__name__)
FILENAME = "report.txt"

def check_info(command, commandslist):
    # Выполняем команду и получаем результат
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Указываем путь
    separator = 120 * "#"
    pattern = r"\b(?!libreoffice\b)lib\.*"

    if error:
        print(f"Ошибка: {error.decode()}")
    else:
        description = commandslist.get(command)
        with open(FILENAME, "a") as file:
            lines = output.decode().splitlines()
            file.write(separator)
            file.write("\n")
            file.write(description)
            for line in lines:
                if re.match(pattern, line):
                    continue  # Пропустить запись строки, если соответствует шаблону
                file.write(line)
                file.write("\n")
            file.write("\n")
        print(f'Данные успешно записаны в файл {FILENAME}')

def execute_commands():
    commands = ["hostname", "uname -r", "cat /etc/os-release", "lshw -short", "sudo dmidecode -t system", "lsusb", "apt-mark showmanual"]
    commandslist = {
    "hostname": "\n Имя компьютера:\n- ",
    "uname -r": "\n Версия ядра ОС:\n- ",
    "cat /etc/os-release": "\n Информация об операционной системе:\n",
    "lshw -short":"\n Информация об аппартном обеспечении:\n",
    "sudo dmidecode -t system":"\n Информация о системе и сведения о компьютере:\n",
    "lsusb":"\n Подключенные USB-устройства:\n",
    "apt-mark showmanual":"\n Список установленного ПО:\n"}

    for command in commands:
        check_info(command, commandslist)

@app.route('/')
def send_report():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        
    execute_commands()
    return send_file(FILENAME)

@app.route('/ping')
def ping():
    return "ping"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)