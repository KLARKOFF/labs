# 1
def f1(name="example.txt", method='a'):
    file=open(name, 'r')
    if method == 'a':
        text=file.read()
        print(text)
    elif method == 's':
        for line in file:
            print(line.strip())
    else:
        print("Несуществующий метод чтения!")

f1(method=input("\nВыберите способ чтения ('a'/'s'):"))

#2

def f2():
    file=open("user_input.txt", 'a')
    user_input=str(input("\nВведите любой текст: "))
    file.write(user_input + "\n")
f2()

print("Содержимое файла user_input.txt: ") 
f1("user_input.txt", 'a')

#3

def f3(name="example.txt", method='a'):
    try:
        file=open(name, 'r')
        if method == 'a':
            text=file.read()
            print(text)
        elif method == 's':
            for line in file:
                print(line.strip())
        else:
            print("Несуществующий метод чтения!")
    except FileNotFoundError:
        print("Такого файла не существует!")

f3(input("Введите имя файла: ").strip(), input("\nВыберите способ чтения ('a'/'s'):")) 
