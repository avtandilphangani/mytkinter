# ფანჯრები 

import tkinter
import config

def click():
# метод get возвращает текущее значение counter
# метод set устанавливает новое значение counter
    counter.set(counter.get() + 1)

window = tkinter.Tk()
window.title = "ხელოო უოლდ"
counter = tkinter.IntVar()
# Обнуляем созданный объект с помощью метода set
counter.set(0) 

frame = tkinter.Frame(window)
frame.pack()

button = tkinter.Button(frame, text='Click', command=click)
button.pack()
# Вид: в реальном времени обновляется содержимое виджета Label
label = tkinter.Label(frame, textvariable=counter)
label.pack()
# Можем изменять параметры фрейма:
frame2 = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame2.pack()
# Размещаем виджет в первом фрейме (frame)
first = tkinter.Label(frame, text='First label')
first.pack()
# Размещаем виджеты во втором фрейме (frame2)
second = tkinter.Label(frame2, text='Second label')
second.pack()
third = tkinter.Label(frame2, text='Third label')
third.pack()

data = tkinter.StringVar()
# Метод set класса StringVar позволяет изменить содержимое переменной:
data.set('Данные в окне')
# textvariable присваиваем ссылку на строковый объект из переменной data
label = tkinter.Label(window, textvariable=data)
label.pack()
var = tkinter.StringVar()
# Обновление содержимого переменной происходит в режиме реального времени
label = tkinter.Label(frame, textvariable=var)
label.pack()
# Пробуем набрать текст в появившемся поле для ввода
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()
window.mainloop()
