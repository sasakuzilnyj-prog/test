#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Студент
#
# Created:     13.02.2026
# Copyright:   (c) Студент 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, ttk
import random

class PythonFunctionsTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест по функциям Python")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')

        self.questions = self.create_questions()
        self.current_question = 0
        self.score = 0
        self.user_answers = []

        self.setup_ui()
        self.load_question()

    def create_questions(self):
        """Создание вопросов по теме функции"""
        return [
            {
                'question': 'Как объявить функцию в Python?',
                'options': [
                    'func my_function():',
                    'def my_function():',
                    'function my_function():',
                    'define my_function():'
                ],
                'correct': 1,
                'explanation': 'В Python функции объявляются с помощью ключевого слова def'
            },
            {
                'question': 'Что такое *args в параметрах функции?',
                'options': [
                    'Указатель на аргументы',
                    'Кортеж позиционных аргументов переменной длины',
                    'Словарь именованных аргументов',
                    'Обязательный аргумент'
                ],
                'correct': 1,
                'explanation': '*args позволяет передать произвольное количество позиционных аргументов'
            },
            {
                'question': 'Что вернет функция, если в ней нет return?',
                'options': [
                    '0',
                    'False',
                    'None',
                    'Ошибку'
                ],
                'correct': 2,
                'explanation': 'Функция без return возвращает None'
            },
            {
                'question': 'Какое ключевое слово нужно использовать, чтобы изменить глобальную переменную внутри функции??',
                'options': [
                    'nonlocal',
                    'global',
                    'outer',
                    'extern'
                ],
                'correct': 1,
                'explanation': 'global позволяет функции получить доступ к переменной, определенной на глобальном уровне (вне функции)'
            },
            {
                'question': 'Можно ли получить доступ к вложенной функции извне родительской функции?',
                'options': [
                    'Да, всегда',
                    'Нет, никогда',
                    'Да, если вернуть её из родительской функции',
                    'Да, используя специальный синтаксис'
                ],
                'correct': 2,
                'explanation': 'Вложенная функция по умолчанию недоступна снаружи.'
            },
            {
                'question': 'Что выведет код: def func(x, y=[]): y.append(x); return y?',
                'options': [
                    'Ошибку',
                    '[1]',
                    '[1, 2] при повторном вызове',
                    'Всегда новый список'
                ],
                'correct': 2,
                'explanation': 'Значение по умолчанию создается один раз и сохраняется между вызовами'
            },
            {
                'question': 'Какое ключевое слово используется для выхода из функции?',
                'options': [
                    'break',
                    'exit',
                    'return',
                    'stop'
                ],
                'correct': 2,
                'explanation': 'return используется для выхода из функции и возврата значения'
            },
            {
                'question': 'Что такое рекурсивная функция?',
                'options': [
                    'Функция, вызывающая саму себя',
                    'Функция с циклами',
                    'Функция без параметров',
                    'Встроенная функция Python'
                ],
                'correct': 0,
                'explanation': 'Рекурсивная функция - это функция, которая вызывает саму себя'
            },
            {
                'question': 'Как передать аргументы в функцию в произвольном порядке?',
                'options': [
                    'Использовать порядковые номера',
                    'Использовать именованные аргументы',
                    'Использовать ключевое слово order',
                    'Это невозможно'
                ],
                'correct': 1,
                'explanation': 'Обязательные позиционные аргументы должны идти до *args'
            },
            {
                'question': 'Что делает функция map()?',
                'options': [
                    'Создает карту местности',
                    'Применяет функцию к каждому элементу последовательности',
                    'Создает словарь',
                    'Сортирует последовательность'
                ],
                'correct': 1,
                'explanation': 'map() применяет указанную функцию к каждому элементу итерируемого объекта'
            }
        ]

    def setup_ui(self):
        """Настройка интерфейса"""
        # Заголовок
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x')

        title_label = tk.Label(title_frame, text="Тест по функциям Python",
                              font=('Arial', 20, 'bold'),
                              bg='#2c3e50', fg='white')
        title_label.pack(pady=20)

        # Основной контейнер
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Информация о прогрессе
        self.progress_label = tk.Label(main_frame,
                                      text="Вопрос 1/10",
                                      font=('Arial', 12),
                                      bg='#f0f0f0', fg='#34495e')
        self.progress_label.pack(pady=(0, 10))

        # Прогресс бар
        self.progress_bar = ttk.Progressbar(main_frame, length=600, mode='determinate')
        self.progress_bar.pack(pady=(0, 20))

        # Контейнер для вопроса
        question_container = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        question_container.pack(fill='x', pady=(0, 20))

        self.question_label = tk.Label(question_container,
                                      text="",
                                      font=('Arial', 14, 'bold'),
                                      bg='white', fg='#2c3e50',
                                      wraplength=600, justify='left')
        self.question_label.pack(padx=20, pady=20)

        # Контейнер для вариантов ответов
        options_container = tk.Frame(main_frame, bg='#f0f0f0')
        options_container.pack(fill='both', expand=True)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []

        for i in range(4):
            radio = tk.Radiobutton(options_container,
                                  text="",
                                  variable=self.radio_var,
                                  value=i,
                                  font=('Arial', 11),
                                  bg='#f0f0f0',
                                  activebackground='#f0f0f0',
                                  wraplength=550,
                                  justify='left')
            radio.pack(anchor='w', pady=5, padx=30)
            self.radio_buttons.append(radio)

        # Контейнер для кнопок
        button_container = tk.Frame(main_frame, bg='#f0f0f0')
        button_container.pack(fill='x', pady=(30, 0))

        # Кнопки
        self.next_btn = tk.Button(button_container,
                                 text="Следующий вопрос",
                                 command=self.next_question,
                                 font=('Arial', 11, 'bold'),
                                 bg='#3498db', fg='white',
                                 relief='flat', padx=20, pady=10,
                                 cursor='hand2')
        self.next_btn.pack(side='right', padx=5)

        self.prev_btn = tk.Button(button_container,
                                 text="Предыдущий вопрос",
                                 command=self.prev_question,
                                 font=('Arial', 11, 'bold'),
                                 bg='#95a5a6', fg='white',
                                 relief='flat', padx=20, pady=10,
                                 cursor='hand2')
        self.prev_btn.pack(side='right', padx=5)

        self.submit_btn = tk.Button(button_container,
                                   text="Завершить тест",
                                   command=self.submit_test,
                                   font=('Arial', 11, 'bold'),
                                   bg='#e74c3c', fg='white',
                                   relief='flat', padx=20, pady=10,
                                   cursor='hand2')
        self.submit_btn.pack(side='left', padx=5)

        # Метка с результатом
        self.result_label = tk.Label(main_frame,
                                    text="",
                                    font=('Arial', 12),
                                    bg='#f0f0f0', fg='#27ae60')
        self.result_label.pack(pady=20)

    def load_question(self):
        """Загрузка вопроса"""
        question = self.questions[self.current_question]
        self.question_label.config(text=f"{self.current_question + 1}. {question['question']}")

        # Загрузка вариантов ответов
        for i, option in enumerate(question['options']):
            self.radio_buttons[i].config(text=option)

        # Восстановление предыдущего ответа
        if len(self.user_answers) > self.current_question:
            self.radio_var.set(self.user_answers[self.current_question])
        else:
            self.radio_var.set(-1)

        # Обновление прогресса
        self.progress_label.config(text=f"Вопрос {self.current_question + 1}/{len(self.questions)}")
        self.progress_bar['value'] = ((self.current_question + 1) / len(self.questions)) * 100

    def next_question(self):
        """Следующий вопрос"""
        self.save_answer()
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()

    def prev_question(self):
        """Предыдущий вопрос"""
        self.save_answer()
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()

    def save_answer(self):
        """Сохранение ответа"""
        if self.radio_var.get() != -1:
            if len(self.user_answers) > self.current_question:
                self.user_answers[self.current_question] = self.radio_var.get()
            else:
                self.user_answers.append(self.radio_var.get())

    def submit_test(self):
        """Завершение теста и подсчет результатов"""
        self.save_answer()

        # Подсчет баллов
        self.score = 0
        wrong_answers = []

        for i, answer in enumerate(self.user_answers):
            if i < len(self.questions):
                if answer == self.questions[i]['correct']:
                    self.score += 1
                else:
                    wrong_answers.append(i + 1)

        # Показ результатов
        percentage = (self.score / len(self.questions)) * 100

        if percentage >= 80:
            grade = "Отлично!"
            color = "#27ae60"
        elif percentage >= 60:
            grade = "Хорошо!"
            color = "#f39c12"
        elif percentage >= 40:
            grade = "Удовлетворительно"
            color = "#e67e22"
        else:
            grade = "Нужно повторить тему"
            color = "#e74c3c"

        result_text = f"Результат: {self.score}/{len(self.questions)} ({percentage:.1f}%)\n"
        result_text += f"Оценка: {grade}\n\n"

        if wrong_answers:
            result_text += f"Ошибки в вопросах: {', '.join(map(str, wrong_answers))}"
        else:
            result_text += "Поздравляем! Все ответы верны!"

        self.result_label.config(text=result_text, fg=color)

        # Диалоговое окно с результатами
        messagebox.showinfo("Результаты теста",
                           f"Тест завершен!\n\n"
                           f"Правильных ответов: {self.score}/{len(self.questions)}\n"
                           f"Процент выполнения: {percentage:.1f}%\n"
                           f"{grade}")

    def reset_test(self):
        """Сброс теста"""
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        random.shuffle(self.questions)
        self.load_question()
        self.result_label.config(text="")
        self.progress_bar['value'] = 0

def main():
    root = tk.Tk()
    app = PythonFunctionsTest(root)

    # Меню
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Файл", menu=file_menu)
    file_menu.add_command(label="Новый тест", command=app.reset_test)
    file_menu.add_separator()
    file_menu.add_command(label="Выход", command=root.quit)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Помощь", menu=help_menu)
    help_menu.add_command(label="О программе",
                         command=lambda: messagebox.showinfo("О программе",
                                                            "Тест по функциям Python\nВерсия 1.0"))

    root.mainloop()

if __name__ == "__main__":
    main()