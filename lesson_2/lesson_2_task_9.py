# var_1 = 37
# var_2 = 99


# через функцию
def swap(var_1, var_2):
    var_3 = var_1
    var_1 = var_2
    var_2 = var_3
    print(var_1, var_2)

swap(37, 99)

# через инпут
var_1 = input("Введите первую переменную: ")
var_2 = input("Введите вторую переменную: ")

var_3 = var_1
var_1 = var_2
var_2 = var_3

print("Новое значение первой переменной: " + var_1)
print("Новое значение второй переменной: " + var_2)