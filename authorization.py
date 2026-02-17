import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime

try:
    plugin_path = os.path.join(os.path.dirname(sys.executable), 'Lib', 'site-packages', 'PyQt5', 'Qt5', 'plugins')
    if os.path.exists(plugin_path):
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
except:
    pass

class User:
    """Класс для хранения данных пользователя"""
    def __init__(self):
        self.fio = ""
        self.group = ""
        self.login_time = ""
    
    def set_data(self, fio, group):
        self.fio = fio
        self.group = group
        self.login_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    def get_data(self):
        return f"ФИО: {self.fio}\nГруппа: {self.group}\nВремя: {self.login_time}"

class AuthWindow(QWidget):
    def __init__(self, user_object):
        super().__init__()
        self.user = user_object
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Авторизация")
        self.resize(400, 250)
        
        title = QLabel("Авторизация")
        
        self.fio_label = QLabel("ФИО:")
        self.fio_input = QLineEdit()
        self.fio_input.setPlaceholderText("Введите ФИО")
        
        self.group_label = QLabel("Группа:")
        self.group_input = QLineEdit()
        self.group_input.setPlaceholderText("Введите группу")
        
        self.login_btn = QPushButton("Войти")
        self.show_btn = QPushButton("Показать данные")
        
        fio_layout = QHBoxLayout()
        fio_layout.addWidget(self.fio_label)
        fio_layout.addWidget(self.fio_input)
        
        group_layout = QHBoxLayout()
        group_layout.addWidget(self.group_label)
        group_layout.addWidget(self.group_input)
        
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.show_btn)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addLayout(fio_layout)
        main_layout.addLayout(group_layout)
        main_layout.addLayout(btn_layout)
        
        self.setLayout(main_layout)
        
        self.login_btn.clicked.connect(self.login)
        self.show_btn.clicked.connect(self.show_data)
    
    def login(self):
        fio = self.fio_input.text().strip()
        group = self.group_input.text().strip()
        
        if fio and group:
            self.user.set_data(fio, group)
            QMessageBox.information(self, "Успешно", f"Добро пожаловать, {fio}!")
            self.show_data()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
    
    def show_data(self):
        if self.user.fio and self.user.group:
            QMessageBox.information(self, "Сохраненные данные", self.user.get_data())
        else:
            QMessageBox.warning(self, "Внимание", "Нет сохраненных данных!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    user = User()
    window = AuthWindow(user)
    window.show()
    sys.exit(app.exec_())