import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QTextEdit, QPushButton, 
                             QTabWidget, QScrollArea, QFrame, QSplitter)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor


class FunctionTutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Учебник: Функции в Python')
        self.setGeometry(100, 100, 900, 700)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной layout
        main_layout = QVBoxLayout(central_widget)
        
        # Заголовок
        title_label = QLabel('📚 Функции в Python')
        title_label.setFont(QFont('Arial', 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('color: #2c3e50; padding: 10px;')
        main_layout.addWidget(title_label)
        
        # Разделитель
        splitter = QSplitter(Qt.Vertical)
        
        # Создаем вкладки
        self.tab_widget = QTabWidget()
        
        # Вкладка "Что такое функции?"
        self.create_intro_tab()
        
        # Вкладка "Создание функций"
        self.create_creation_tab()
        
        # Вкладка "Аргументы функций" - ИСПРАВЛЕНО: был неправильный отступ
        self.create_arguments_tab()
        
        # Вкладка "Применение функций"
        self.create_usage_tab()
        
        # Вкладка "Примеры"
        self.create_examples_tab()
        
        splitter.addWidget(self.tab_widget)
        
        # Область для вывода результатов
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setPlaceholderText('Здесь будут появляться результаты выполнения примеров...')
        self.result_area.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Courier New';
            }
        """)
        
        splitter.addWidget(self.result_area)
        splitter.setSizes([500, 200])
        
        main_layout.addWidget(splitter)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ecf0f1;
            }
            QTabWidget::pane {
                border: 1px solid #bdc3c7;
                background-color: white;
                border-radius: 5px;
            }
            QTabBar::tab {
                background-color: #3498db;
                color: white;
                padding: 8px 16px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #2980b9;
            }
            QTabBar::tab:hover {
                background-color: #5dade2;
            }
        """)
    
    def create_intro_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        content = """
        <h2 style="color: #2c3e50;">📖 Что такое функции?</h2>
        
        <p><b>Функция</b> — это именованный блок кода, который выполняет определенную задачу 
        и может быть многократно вызван из разных частей программы.</p>
        
        <h3 style="color: #3498db;">Синтаксис:</h3>
        <div>
        Для объявления функции используют ключевое слово def (от англ. define — определить, обозначить).<br>
          В общем виде объявление выглядит следующим образом:
        </div>
        
        <h3 style="color: #3498db;">Структура функции:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def имя_функции(аргументы):
    тело_функции
    return результат</pre>
        
        <div>
        Здесь:
        <ul>
        <li>имя_функции ― название, с помощью которого можно вызывать функцию в коде;</li>
        <li>аргументы ― значения, которые функция принимает на вход. Это поле может быть пустым;</li>
        <li>тело_функции ― набор инструкций, которые выполняются при вызове;</li>
         <li>результат ― значения, которые функция возвращает при завершении работы.</li>
        </ul>
        </div>
        
        <h3>Вызов функции</h3>
        <div>
        Функцию в Python можно создать один раз, а после вызывать её в коде <br>
          неограниченное количество раз. Это позволяет экономить время и сокращает <br>
            количество строк в проекте.
        </div>
        <p>Чтобы вызвать функцию, надо ввести её название и передать аргументы в скобках. В общем виде синтаксис вызова выглядит так:</p>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
        имя_функции(аргументы)
        </pre>
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Что такое функции?")
    
    def create_creation_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        content = """
        <h2 style="color: #2c3e50;">Область видимости функций</h2>
        
        <h3 style="color: #3498db;">1. Локальная область (local scope):</h3>
        <div>Внутри функции можно объявить временные переменные, которые помогают в промежуточных вычислениях. <br>
          Они существуют только внутри тела функции, их нельзя использовать в других местах проекта. <br> 
          Это и есть локальная область видимости.</div>
          <p>
          <div>В примере ниже переменная c объявлена внутри функции sum. <br> 
          Её можно использовать только внутри функции, если попробовать сделать это в другом месте, <br> 
          то Python выдаст ошибку:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def sum(a, b):
    c = a + b
    return c</pre>

        
        <h3 style="color: #3498db;">2. Область объемлющей функции (enclosing function scope):</h3>
        <div>
        Функции бывают вложенными, когда одна находится внутри другой как матрёшка. <br>
          В таком случае у внутренней функции есть доступ к переменным, определённым во внешней. Наоборот, это правило не будет работать.
        </div>
        <p>
        <div>
        Напишем код счётчика, который подсчитывает количество вызовов функции. Используем для этого вложенную архитектуру:
        </div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def make_counter():
    # Объявляем переменную count в объемлющей функции
    count = 0

    def counter():
        # Указываем, что count находится в объемлющей функции
        nonlocal count 
        count += 1
        return count

    return counter

# Создаём счётчик
call_counter = make_counter()

# Пример использования счётчика
print(call_counter())  # Вывод: 1
print(call_counter())  # Вывод: 2
print(call_counter())  # Вывод: 3</pre>
        <br>
        <div>
        В этом примере вложенная функция использует переменную count для вычислений. <br>
          Чтобы программа не приняла переменную за локальную, как в примере выше, используют ключевое слово nonlocal. <br>
            Это полезно, если, как здесь, мы хотим обновить значение переменной только внутри вложенной функции.
        </div>
        <h3 style="color: #3498db;">3. Глобальная область (global scope):</h3>
        <div>
        Переменные, определённые вне функций, находятся в глобальной области видимости. Это значит, что они видны во всей программе и доступны всем функциям. Если надо изменить значение глобальной функции внутри функции, то необходимо использовать ключевое слово global.
        </div>
        <pre>
        <div>
        Например, нам нужно написать программу для кондитерской, которая ведёт учёт изготовленных тортов. Каждый раз, когда мы продаём новые торты, мы будем изменять переменную cake:
        </div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
# Глобальная переменная, которая обозначает количество сделанных тортов
cake_count = 10

def modify_cake():
    global cake_count
    # Изменяем значение глобальной переменной
    cake_count = 15

modify_cake()
print(cake_count)  # Вывод: 15  <!-- ИСПРАВЛЕНО: было print(modify_cake) -->
        </pre>
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Область видимости функций")
    
    # ИСПРАВЛЕНО: название метода и отступ
    def create_arguments_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        content = """
        <h2 style="color: #2c3e50;">🚀 Аргументы функций</h2>
        
        <h3 style="color: #3498db;">Типы аргументов в Python:</h3>
        
        <h4>1. Позиционные аргументы (positional arguments):</h4>
        <div>Аргументы, которые передаются в функцию в правильном порядке:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def greet(name, greeting):
    return f"{greeting}, {name}!"

print(greet("Alice", "Hello"))  # Hello, Alice!</pre>
        
        <h4>2. Именованные аргументы (keyword arguments):</h4>
        <div>Аргументы, которые передаются с указанием имени параметра:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def describe_pet(name, animal_type="dog"):
    print(f"I have a {animal_type} named {name}")

describe_pet(animal_type="cat", name="Whiskers")</pre>
        
        <h4>3. Аргументы по умолчанию (default arguments):</h4>
        <div>Параметры, которые имеют значение по умолчанию:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # 9 (3 в квадрате)
print(power(3, 4)) # 81 (3 в 4-й степени)</pre>
        
        <h4>4. Произвольное количество аргументов (*args):</h4>
        <div>Позволяет передавать любое количество позиционных аргументов:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15</pre>
        
        <h4>5. Произвольное количество именованных аргументов (**kwargs):</h4>
        <div>Позволяет передавать любое количество именованных аргументов:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")</pre>
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Аргументы функций")
    
    def create_usage_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        content = """
        <h2 style="color: #2c3e50;">🚀 Применение функций</h2>
        
        <h3 style="color: #3498db;">1. Параметры по умолчанию:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def приветствие(имя="Гость"):
    '''Функция с параметром по умолчанию'''
    print(f"Добро пожаловать, {имя}!")

# Разные способы вызова
приветствие()           # Используется значение по умолчанию
приветствие("Алексей")  # Передается свое значение</pre>
        
        <h3 style="color: #3498db;">2. Именованные аргументы:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def информация_о_человеке(имя, возраст, город):
    '''Вывод информации о человеке'''
    print(f"Имя: {имя}")
    print(f"Возраст: {возраст}")
    print(f"Город: {город}")

# Можно передавать аргументы в любом порядке, если указывать имена
информация_о_человеке(возраст=30, город="Москва", имя="Петр")</pre>
        
        <h3 style="color: #3498db;">3. Произвольное количество аргументов (*args):</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def сумма_чисел(*числа):
    '''Суммирует произвольное количество чисел'''
    сумма = 0
    for число in числа:
        сумма += число
    return сумма

# Можно передавать разное количество аргументов
print(сумма_чисел(1, 2, 3))
print(сумма_чисел(10, 20, 30, 40, 50))</pre>
        
        <h3 style="color: #3498db;">4. Произвольное количество именованных аргументов (**kwargs):</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def информация(**детали):
    '''Принимает произвольные именованные аргументы'''
    for ключ, значение in детали.items():
        print(f"{ключ}: {значение}")

информация(имя="Анна", возраст=25, профессия="инженер")
информация(студент="Иван", курс=3, университет="МГУ")</pre>
        
        <h3 style="color: #3498db;">5. Функции как объекты:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def приветствие(имя):
    return f"Привет, {имя}!"

def прощание(имя):
    return f"До свидания, {имя}!"

# Функция может принимать другую функцию как параметр
def обработка_имени(имя, функция):
    return функция(имя)

# Использование
print(обработка_имени("Мария", приветствие))
print(обработка_имени("Мария", прощание))</pre>
        
                <h3 style="color: #3498db;">Функции можно передавать другим функциям</h3>
        <div>
        Поскольку функции являются объектами, их можно передавать в качестве аргументов другим функциям. Вот функция greet, которая форматирует строку greeting, используя переданный ей объект функции, а затем выводит ее:
        </div>
        
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)</pre>
        <br>
        <div>
        Приветствие, которое получается в результате, можно изменить, передавая различные функции. Вот что произойдет, если передать в greet функцию yell:
        </div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
....
def yell(text):
    return text.upper() + '!'
        ....
        >>> greet(yell)
'HI, I AM A PYTHON PROGRAM!'
        </pre>
         <div>
        Чтобы сгенерировать другой вид приветствия, можно определить новую функцию, Например, функция whisper может работать лучше, если вы не хотите, чтобы программы на Python звучали так, словно их автор Оптимус Прайм:
        </div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
        def whisper(text):
    return text.lower() + '...'

>>> greet(whisper)
'hi, i am a python program...'
        </pre>
         <h3 style="color: #3498db;">Функции могут быть вложенными</h3>
        <div>
        Python позволяет определять функции внутри других функций. Их часто называют вложенными или внутренними функциями. Вот пример:
        </div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
        def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

>>> speak('Hello, World')
'hello, world...'
        </pre>
        <div>Каждый раз, когда вы вызываете speak, он определяет новую внутреннюю функцию whisper и затем вызывает ее.

И вот в чем загвоздка — whisper не существует вне speak:</div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
        >>> whisper('Yo')
NameError: "name 'whisper' is not defined"

>>> speak.whisper
AttributeError: "'function' object has no attribute 'whisper'"
        </pre>
        <div>
        Но что, если вы действительно хотите получить доступ к вложенной функции whisper из внешней функции speak? Ну, функции являются объектами — можно вернуть внутреннюю функцию вызывающей родительской функции.

Например, вот функция, определяющая две внутренние функции. В зависимости от аргумента, переданного функции верхнего уровня, она выбирает и возвращает вызывающему одну из внутренних функций:
        </div>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
        def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper
        </pre>
        
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Применение функций")
    
    # ИСПРАВЛЕНО: отступ метода
    def create_examples_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        content = """
        <h2 style="color: #2c3e50;">📊 Примеры функций</h2>
        
        <h3 style="color: #3498db;">1. Математические функции:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
import math

def площадь_круга(радиус):
    '''Вычисляет площадь круга'''
    return math.pi * радиус ** 2

def факториал(число):
    '''Вычисляет факториал числа'''
    if число == 0:
        return 1
    результат = 1
    for i in range(1, число + 1):
        результат *= i
    return результат

# Использование
print(f"Площадь круга с радиусом 5: {площадь_круга(5):.2f}")
print(f"Факториал 5: {факториал(5)}")</pre>
        
        <h3 style="color: #3498db;">2. Работа со строками:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def обратная_строка(текст):
    '''Возвращает строку в обратном порядке'''
    return текст[::-1]

def статистика_текста(текст):
    '''Анализирует текст'''
    слов = len(текст.split())
    символов = len(текст)
    букв = sum(1 for символ in текст if символ.isalpha())
    return слов, символов, букв

# Использование
текст = "Python - прекрасный язык программирования"
print(f"Обратная строка: {обратная_строка(текст)}")
слова, символы, буквы = статистика_текста(текст)
print(f"Слов: {слова}, Символов: {символы}, Букв: {буквы}")</pre>
        
        <h3 style="color: #3498db;">3. Работа со списками:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def фильтрация_чисел(числа, порог):
    '''Фильтрует числа больше порога'''
    return [число for число in числа if число > порог]

def поиск_максимума(список):
    '''Находит максимальный элемент в списке'''
    if not список:
        return None
    максимум = список[0]
    for элемент in список[1:]:
        if элемент > максимум:
            максимум = элемент
    return максимум

# Использование
числа = [1, 5, 3, 8, 2, 7]
print(f"Числа больше 3: {фильтрация_чисел(числа, 3)}")
print(f"Максимальное число: {поиск_максимума(числа)}")</pre>
        
        <h3 style="color: #3498db;">4. Рекурсивная функция:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def числа_фибоначчи(количество):
    '''Генерирует числа Фибоначчи'''
    if количество <= 0:
        return []
    elif количество == 1:
        return [0]
    elif количество == 2:
        return [0, 1]
    
    последовательность = числа_фибоначчи(количество - 1)
    следующий = последовательность[-1] + последовательность[-2]
    последовательность.append(следующий)
    return последовательность

print(f"Первые 10 чисел Фибоначчи: {числа_фибоначчи(10)}")</pre>
        
        <h3 style="color: #3498db;">5. Функция с возвратом:</h3>
        
<div>В Python ключевое слово return используется для возврата значения из функции. <br>
Полученное значение можно дальше использовать в программе.<br>
В примере ниже функция add принимает два аргумента a и b, складывает их и с помощью return возвращает сумму a + b:</div>
<pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Вывод: 8</pre>
<p>Если не использовать в функции ключевое слово return, она по умолчанию вернёт None.</p>
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Примеры")

def main():
    app = QApplication(sys.argv)
    tutorial = FunctionTutorial()
    tutorial.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()