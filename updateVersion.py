import os

if __name__ == '__main__':
    with open('./.version', encoding='utf-8') as file:
        version = int(file.read())
    number = str(version)
    while len(number) < 3:
        number = "0" + number
    list_num = list(number)
    for i in range(len(list_num)-1, len(list_num)-3, -1):
        list_num.insert(i, ".")
    with open(os.getenv('GITHUB_ENV'), "a") as file:
        file.write("VERSION=" + ''.join(list_num))
    with open('./.version', "w", encoding='utf-8') as file:
        file.write(str(version+1))
        