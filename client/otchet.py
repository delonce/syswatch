import os
import subprocess
import json

from flask import Flask, send_file

app = Flask(__name__)
FILENAME = "report.txt"

def check_info(commands, commandslist):
    dct_res = {}
    for command in commands:
        # Выполняем команду и получаем результат
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        if "dmidecode" in command:
            command_key = "dmidecode"
        else:
            command_key = command.split()[0]

        if error:
            dct_res[command_key] = f"Error: {error.decode()}"
        else:
            dct_res[command_key] = output.decode()

    json_dump = json.dumps(dct_res)

    with open(FILENAME, "w") as file:
        file.write(json_dump)

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

    check_info(commands, commandslist)

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