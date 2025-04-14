import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.weather_image_label = QLabel(self)
        self.description_label = QLabel(self)
        self.setWindowIcon(QtGui.QIcon("icons/weather.png"))
        
        self.dark_mode_button = QPushButton(icon=QIcon("icons/night-mode.png"))
        self.light_mode_button = QPushButton(icon=QIcon("icons/light-mode.png"))
        
        self.dark_mode_button.setFixedSize(40, 40)
        self.light_mode_button.setFixedSize(40, 40)
      
        self.is_dark_mode = False
        
        self.temp_unit_group = QButtonGroup(self)
        self.celsius_radio = QRadioButton("Celsius (°C)")
        self.fahrenheit_radio = QRadioButton("Fahrenheit (°F)")
        self.kelvin_radio = QRadioButton("Kelvin (K)")
        
        self.celsius_radio.setChecked(True)
        
        self.temp_unit_group.addButton(self.celsius_radio)
        self.temp_unit_group.addButton(self.fahrenheit_radio)
        self.temp_unit_group.addButton(self.kelvin_radio)
        
        self.current_temp_k = None
        
        self.initUI()

    def initUI(self): 
        self.setWindowTitle("Weather App")
        self.setMinimumSize(500, 700)  

        temp_unit_layout = QHBoxLayout()
        temp_unit_layout.addWidget(self.celsius_radio)
        temp_unit_layout.addWidget(self.fahrenheit_radio)
        temp_unit_layout.addWidget(self.kelvin_radio)
        
        self.dark_mode_button.clicked.connect(self.enable_dark_mode)
        self.light_mode_button.clicked.connect(self.enable_light_mode)
        
        self.celsius_radio.toggled.connect(self.update_temperature_display)
        self.fahrenheit_radio.toggled.connect(self.update_temperature_display)
        self.kelvin_radio.toggled.connect(self.update_temperature_display)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.dark_mode_button)
        top_layout.addWidget(self.light_mode_button)
        top_layout.addStretch()  

        vbox = QVBoxLayout()
        vbox.addLayout(top_layout)  
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addSpacing(20)  
        vbox.addLayout(temp_unit_layout)
        vbox.addSpacing(20)  
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.weather_image_label)
        vbox.addSpacing(30)  
        vbox.addWidget(self.description_label)
        vbox.addStretch()  

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.weather_image_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setWordWrap(True)
        
        self.weather_image_label.setFixedHeight(150)
        
        self.description_label.setMinimumHeight(80)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.weather_image_label.setObjectName("weather_image_label")
        self.description_label.setObjectName("description_label")
        self.dark_mode_button.setObjectName("theme_button")
        self.light_mode_button.setObjectName("theme_button")
        
        self.celsius_radio.setObjectName("temperature_radio")
        self.fahrenheit_radio.setObjectName("temperature_radio")
        self.kelvin_radio.setObjectName("temperature_radio")
        
        self.apply_theme()

        self.get_weather_button.clicked.connect(self.get_weather)

    def enable_dark_mode(self):
        self.is_dark_mode = True
        self.apply_theme()

    def enable_light_mode(self):
        self.is_dark_mode = False
        self.apply_theme()

    def apply_theme(self):
        self.dark_mode_button.setVisible(not self.is_dark_mode)
        self.light_mode_button.setVisible(self.is_dark_mode)
        
        if self.is_dark_mode:
            self.setStyleSheet("""
                QWidget {
                    background-color: #1a1a2e;
                    font-family: Calibri, Arial, sans-serif;
                    color: #e0e0e0;
                }
                
                QLabel#city_label {
                    font-size: 40px;
                    font-style: italic;
                    color: #c0c0c0;
                    margin-top: 20px;
                }
                
                QLineEdit#city_input {
                    font-size: 40px;
                    border: 2px solid #00a3d9;
                    border-radius: 15px;
                    padding: 5px 15px;
                    margin: 10px 20px;
                    background-color: #2a2a3e;
                    color: #e0e0e0;
                }
                
                QPushButton#get_weather_button {
                    font-size: 30px;
                    font-weight: bold;
                    background-color: #00a3d9;
                    color: white;
                    border-radius: 15px;
                    padding: 10px 20px;
                    margin: 10px 50px;
                    border: none;
                }
                
                QPushButton#get_weather_button:hover {
                    background-color: #0088b3;
                }
                
                QPushButton#get_weather_button:pressed {
                    background-color: #00719c;
                }
                
                QPushButton#theme_button {
                    border-radius: 20px;
                    border: None;
                    padding: 5px;
                }
                
                QPushButton#theme_button:hover {
                    background-color: #3a3a4e;
                }
                
                QRadioButton#temperature_radio {
                    font-size: 20px;
                    color: #c0c0c0;
                    spacing: 12px;
                    padding: 5px;
                }
                
                QRadioButton#temperature_radio:checked {
                    color: #00a3d9;
                    font-weight: bold;
                }
                
                QRadioButton#temperature_radio::indicator {
                    width: 18px;
                    height: 18px;
                    border-radius: 10px;
                    border: 2px solid #00a3d9;
                }
                
                QRadioButton#temperature_radio::indicator:checked {
                    background-color: #00a3d9;
                    border: 2px solid #00a3d9;
                    width: 10px;
                    height: 10px;
                    border-radius: 6px;
                }
                
                QLabel#temperature_label {
                    font-size: 45px;
                    font-weight: bold;
                    color: #e0e0e0;
                    margin: 10px;
                }
                
                QLabel#weather_image_label {
                    margin: 0;
                    padding: 0;
                }
                
                QLabel#description_label {
                    font-size: 36px;
                    color: #c0c0c0;
                    font-style: italic;
                    margin-bottom: 20px;
                    padding: 0 20px;
                    line-height: 1.3;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #f0f8ff;
                    font-family: Calibri, Arial, sans-serif;
                }
                
                QLabel#city_label {
                    font-size: 40px;
                    font-style: italic;
                    color: #2c3e50;
                    margin-top: 20px;
                }
                
                QLineEdit#city_input {
                    font-size: 40px;
                    border: 2px solid #00c1ff;
                    border-radius: 15px;
                    padding: 5px 15px;
                    margin: 10px 20px;
                    background-color: white;
                }
                
                QPushButton#get_weather_button {
                    font-size: 30px;
                    font-weight: bold;
                    background-color: #00c1ff;
                    color: white;
                    border-radius: 15px;
                    padding: 10px 20px;
                    margin: 10px 50px;
                    border: none;
                }
                
                QPushButton#get_weather_button:hover {
                    background-color: #00a3d9;
                }
                
                QPushButton#get_weather_button:pressed {
                    background-color: #0088b3;
                }
                
                QPushButton#theme_button {
                    border-radius: 20px;
                    border: None;
                    padding: 5px;
                }
                
                QPushButton#theme_button:hover {
                    background-color: #949494;
                }
                
                QRadioButton#temperature_radio {
                    font-size: 20px;
                    color: #2c3e50;
                    spacing: 12px;
                    padding: 5px;
                }
                
                QRadioButton#temperature_radio:checked {
                    color: #00c1ff;
                    font-weight: bold;
                }
                
                QRadioButton#temperature_radio::indicator {
                    width: 18px;
                    height: 18px;
                    border-radius: 10px;
                    border: 2px solid #00c1ff;
                }
                
                QRadioButton#temperature_radio::indicator:checked {
                    background-color: #00c1ff;
                    border: 2px solid #00c1ff;
                    width: 10px;
                    height: 10px;
                    border-radius: 6px;
                }
                
                QLabel#temperature_label {
                    font-size: 45px;
                    font-weight: bold;
                    color: #2c3e50;
                    margin: 10px;
                }
                
                QLabel#weather_image_label {
                    margin: 0;
                    padding: 0;
                }
                
                QLabel#description_label {
                    font-size: 36px;
                    color: #34495e;
                    font-style: italic;
                    margin-bottom: 20px;
                    padding: 0 20px;
                    line-height: 1.3;
                }
            """)

    def get_weather(self):
        api_key = "" # Insert your own api key.
        city = self.city_input.text()
        
        if not city:
            self.display_error("Please enter a city name")
            return
            
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data.get("cod") == 200:
                self.display_weather(data)
            
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input.")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key.")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied.")
                case 404:
                    self.display_error("Not found:\nCity not found.")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later.")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid Response from the server.")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server.")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        
    def display_error(self, message):
        self.temperature_label.setText(message)
        self.weather_image_label.clear()
        self.description_label.clear()
        self.current_temp_k = None

    def display_weather(self, data):
        self.current_temp_k = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].capitalize()
        city_name = data["name"]
        country = data["sys"]["country"]

        image_path = self.get_weather_image(weather_id)
        
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.weather_image_label.setPixmap(pixmap)
        
        location_text = f"{city_name}, {country}"
        if len(location_text) > 20:
            description_text = f"{weather_description}\nin {location_text}"
        else:
            description_text = f"{weather_description} in {location_text}"
            
        self.description_label.setText(description_text)
        
        self.update_temperature_display()
    
    def update_temperature_display(self):
        if self.current_temp_k is None:
            return
            
        if self.celsius_radio.isChecked():
            temp_value = self.current_temp_k - 273.15
            unit = "°C"
        elif self.fahrenheit_radio.isChecked():
            temp_value = (self.current_temp_k * 9/5) - 459.67
            unit = "°F"
        else:  
            temp_value = self.current_temp_k
            unit = "K"
            
        self.temperature_label.setText(f"{temp_value:.0f}{unit}")
    
    @staticmethod
    def get_weather_image(weather_id):
        if 200 <= weather_id <= 232:
            return "weather-icons/thunderstorm.png"
        elif 300 <= weather_id <= 321:
            return "weather-icons/rainandsun.png"
        elif 500 <= weather_id <= 531:
            return "weather-icons/heavy-rain.png"
        elif 600 <= weather_id <= 632:
            return "weather-icons/snowflake.png"
        elif 701 <= weather_id <= 741:
            return "weather-icons/fog.png"
        elif 751 <= weather_id <= 761:
            return "weather-icons/dust.png"
        elif weather_id == 762:
            return "weather-icons/volcano.png"
        elif weather_id == 771:
            return "weather-icons/windy.png"
        elif weather_id == 781:
            return "weather-icons/tornado.png"
        elif weather_id == 800:
            return "weather-icons/sun.png"
        elif 801 <= weather_id <= 804:
            return "weather-icons/cloudy.png"
        else:
            return "images/weather.png"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())