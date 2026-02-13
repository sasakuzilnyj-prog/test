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
def имя_функции (аргументы):
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
        <h2 style="color: #2c3e50;">🛠️ Создание функций</h2>
        
        <h3 style="color: #3498db;">1. Простая функция без параметров:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def приветствие():
    '''Функция выводит приветствие'''
    print("Привет, мир!")
    print("Добро пожаловать в Python!")

# Вызов функции
приветствие()</pre>
        <button onclick="app.execute_code('def приветствие():\\n    print(\\\"Привет, мир!\\\")\\n    print(\\\"Добро пожаловать в Python!\\\")\\n\\nприветствие()')">Запустить пример</button>
        
        <h3 style="color: #3498db;">2. Функция с параметрами:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def приветствие_имя(имя):
    '''Приветствие с именем'''
    print(f"Привет, {имя}!")

# Вызов с аргументом
приветствие_имя("Анна")
приветствие_имя("Иван")</pre>
        <button onclick="app.execute_code('def приветствие_имя(имя):\\n    print(f\\\"Привет, {имя}!\\\")\\n\\nприветствие_имя(\\\"Анна\\\")\\nприветствие_имя(\\\"Иван\\\")')">Запустить пример</button>
        
        <h3 style="color: #3498db;">3. Функция с возвращаемым значением:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def квадрат_числа(число):
    '''Возвращает квадрат числа'''
    результат = число ** 2
    return результат

# Использование возвращаемого значения
х = квадрат_числа(5)
print(f"Квадрат 5 равен {х}")</pre>
        <button onclick="app.execute_code('def квадрат_числа(число):\\n    результат = число ** 2\\n    return результат\\n\\nх = квадрат_числа(5)\\nprint(f\\\"Квадрат 5 равен {х}\\\")')">Запустить пример</button>
        
        <h3 style="color: #3498db;">4. Функция с несколькими параметрами:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def сложение(а, b):
    '''Складывает два числа'''
    return а + b

def приветствие_полное(имя, возраст):
    '''Приветствие с именем и возрастом'''
    return f"Привет, {имя}! Тебе {возраст} лет."

# Вызов функций
сумма = сложение(10, 20)
сообщение = приветствие_полное("Мария", 25)
print(сумма)
print(сообщение)</pre>
        <button onclick="app.execute_code('def сложение(а, b):\\n    return а + b\\n\\ndef приветствие_полное(имя, возраст):\\n    return f\\\"Привет, {имя}! Тебе {возраст} лет.\\\"\\n\\nсумма = сложение(10, 20)\\nсообщение = приветствие_полное(\\\"Мария\\\", 25)\\nprint(сумма)\\nprint(сообщение)')">Запустить пример</button>
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Создание функций")
    
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
        <button onclick="app.execute_code('def приветствие(имя=\\\"Гость\\\"):\\n    print(f\\\"Добро пожаловать, {имя}!\\\")\\n\\nприветствие()\\nприветствие(\\\"Алексей\\\")')">Запустить пример</button>
        
        <h3 style="color: #3498db;">2. Именованные аргументы:</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def информация_о_человеке(имя, возраст, город):
    '''Вывод информации о человеке'''
    print(f"Имя: {имя}")
    print(f"Возраст: {возраст}")
    print(f"Город: {город}")

# Можно передавать аргументы в любом порядке, если указывать имена
информация_о_человеке(возраст=30, город="Москва", имя="Петр")</pre>
        <button onclick="app.execute_code('def информация_о_человеке(имя, возраст, город):\\n    print(f\\\"Имя: {имя}\\\")\\n    print(f\\\"Возраст: {возраст}\\\")\\n    print(f\\\"Город: {город}\\\")\\n\\nинформация_о_человеке(возраст=30, город=\\\"Москва\\\", имя=\\\"Петр\\\")')">Запустить пример</button>
        
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
        <button onclick="app.execute_code('def сумма_чисел(*числа):\\n    сумма = 0\\n    for число in числа:\\n        сумма += число\\n    return сумма\\n\\nprint(сумма_чисел(1, 2, 3))\\nprint(сумма_чисел(10, 20, 30, 40, 50))')">Запустить пример</button>
        
        <h3 style="color: #3498db;">4. Произвольное количество именованных аргументов (**kwargs):</h3>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
def информация(**детали):
    '''Принимает произвольные именованные аргументы'''
    for ключ, значение in детали.items():
        print(f"{ключ}: {значение}")

информация(имя="Анна", возраст=25, профессия="инженер")
информация(студент="Иван", курс=3, университет="МГУ")</pre>
        <button onclick="app.execute_code('def информация(**детали):\\n    for ключ, значение in детали.items():\\n        print(f\\\"{ключ}: {значение}\\\")\\n\\nинформация(имя=\\\"Анна\\\", возраст=25, профессия=\\\"инженер\\\")\\nинформация(студент=\\\"Иван\\\", курс=3, университет=\\\"МГУ\\\")')">Запустить пример</button>
        
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
        <button onclick="app.execute_code('def приветствие(имя):\\n    return f\\\"Привет, {имя}!\\\"\\n\\ndef прощание(имя):\\n    return f\\\"До свидания, {имя}!\\\"\\n\\ndef обработка_имени(имя, функция):\\n    return функция(имя)\\n\\nprint(обработка_имени(\\\"Мария\\\", приветствие))\\nprint(обработка_имени(\\\"Мария\\\", прощание))')">Запустить пример</button>
        """
        
        label = QLabel(content)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        
        scroll = QScrollArea()
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        
        layout.addWidget(scroll)
        self.tab_widget.addTab(widget, "Применение функций")
    
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
        <button onclick="app.execute_code('import math\\n\\ndef площадь_круга(радиус):\\n    return math.pi * радиус ** 2\\n\\ndef факториал(число):\\n    if число == 0:\\n        return 1\\n    результат = 1\\n    for i in range(1, число + 1):\\n        результат *= i\\n    return результат\\n\\nprint(f\\\"Площадь круга с радиусом 5: {площадь_круга(5):.2f}\\\")\\nprint(f\\\"Факториал 5: {факториал(5)}\\\")')">Запустить пример</button>
        
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
        <button onclick="app.execute_code('def обратная_строка(текст):\\n    return текст[::-1]\\n\\ndef статистика_текста(текст):\\n    слов = len(текст.split())\\n    символов = len(текст)\\n    букв = sum(1 for символ in текст if символ.isalpha())\\n    return слов, символов, букв\\n\\nтекст = \\\"Python - прекрасный язык программирования\\\"\\nprint(f\\\"Обратная строка: {обратная_строка(текст)}\\\")\\nслова, символы, буквы = статистика_текста(текст)\\nprint(f\\\"Слов: {слова}, Символов: {символы}, Букв: {буквы}\\\")')">Запустить пример</button>
        
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
        <button onclick="app.execute_code('def фильтрация_чисел(числа, порог):\\n    return [число for число in числа if число > порог]\\n\\ndef поиск_максимума(список):\\n    if not список:\\n        return None\\n    максимум = список[0]\\n    for элемент in список[1:]:\\n        if элемент > максимум:\\n            максимум = элемент\\n    return максимум\\n\\nчисла = [1, 5, 3, 8, 2, 7]\\nprint(f\\\"Числа больше 3: {фильтрация_чисел(числа, 3)}\\\")\\nprint(f\\\"Максимальное число: {поиск_максимума(числа)}\\\")')">Запустить пример</button>
        
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
        <button onclick="app.execute_code('def числа_фибоначчи(количество):\\n    if количество <= 0:\\n        return []\\n    elif количество == 1:\\n        return [0]\\n    elif количество == 2:\\n        return [0, 1]\\n    последовательность = числа_фибоначчи(количество - 1)\\n    следующий = последовательность[-1] + последовательность[-2]\\n    последовательность.append(следующий)\\n    return последовательность\\n\\nprint(f\\\"Первые 10 чисел Фибоначчи: {числа_фибоначчи(10)}\\\")')">Запустить пример</button>
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