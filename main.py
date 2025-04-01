
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
        self.temperature_label = QLabel(self)
        self.emoji_label= QLabel(self) 
        self.description_label= QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("MAUSAM")
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
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
          QLabel, QPushButton{
                font-family: times new roman;           
                }
                QLabel#city_Label{
                           font-size: 39px;
                           font-style: italic;
                           }
                           QLineEdit#city_input{
                           font-size: 39px;
                           padding: 5px;
                           max-width: 400px;
                           }
                           QPushButton#get_weather_button{
                           font-size: 30px;
                           font-weight: bold;
                           }
                           QLabel#temperature_label{
                           font-size: 72px;
                           }
                           QLabel#emoji_label{
                           font-size: 99px;
                            font-family: "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", "Arial Unicode MS"; /* Fallback Options */
                            }
                           QLabel#description_label{
                           font-size: 51px;
                           }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
            api_key= "5a101c55fdffed7846583146e471d4d3"
            city = self.city_input.text()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            try:
                response = requests.get(url)
                response.raise_for_status()
                data= response.json()
                if data["cod"]== 200:
                 self.display_weather(data)
            except requests.exceptions.HTTPError as http_error:
                  match response.status_code:
                        case 400:
                              self.display_error ("Bad Request \n Please check your Provided City")
                        case 401:
                              self.display_error ("Unauthorized\n Invalid API Key")
                        case 403:
                              self.display_error ("Forbidden \n Please check your Provided City")
                        case 404:
                             self.display_error ("City Not found \n Please check your Provided City")
                        case 500:
                              self.display_error("Internal Server Error \n Please Try again later")
                        case 502:
                             self.display_error("Bad Gateway ")
                        case 503:
                              self.display_error ("Server Error \n Server Down")
                        case 504:
                              self.display_error("Gateway Timeout ")
                        case _:
                             self.display_error(f"HTTP Error occured \n{http_error}")
            except request.exceptions.ConnectionError:
                  self.display_error("Connection lost")
            except request.exceptions.Timeout:
                 self.display_error("Your request was timed out")
            except request.exceptions.TooManyRedirects:
                 self.display_error("Too Many Redirects")
            except request.exceptions.RequestException:
                  self.display_error("Request Error")
            
    
    def display_error(self, message):
            self.temperature_label.setStyleSheet("font-size: 33px;")
            self.temperature_label.setText(message)
    def display_weather(self, data):
            print(data)
        

if __name__ =="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
