import random
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_Label= QLabel("Enter city Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel("32℃", self)
        self.emoji_label= QLabel("☀️", self) 
        self.description_label= QLabel("Sunny",self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Weather APP")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_Label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        self.city_Label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_Label.setObjectName("city_Label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button.")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        

if __name__ =="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
