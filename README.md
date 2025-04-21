# WeatherPy

A Python desktop application that provides weather information based on user location input.

## Description

WeatherPy is a graphical desktop application built with PyQt5 that fetches and displays current weather data. This project uses the OpenWeatherMap API to retrieve real-time weather information for any city around the world.

## Features

- Get current weather conditions for any city
- Display temperature, humidity, wind speed, and weather description
- User-friendly graphical interface built with PyQt5
- Customizable temperature units (Celsius/Fahrenheit)
- Light and dark mode support

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/samko-1z/Weatherpy.git
   ```

2. Navigate to the project directory:
   ```
   cd Weatherpy
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) (Free tier available)

5. Insert your API key in the appropriate location in the code (see Usage section below)

## Usage

1. Add your OpenWeatherMap API key to the designated variable in the code.

2. Run the application using Python:
   ```
   python main.py
   ```

3. Use the graphical interface to enter a city name and view the weather information.

## Screenshots

### Light mode:
![Light mode](https://github.com/user-attachments/assets/8e06fa6b-221d-4764-8678-874a3830c220)

### Dark mode:
![Dark mode](https://github.com/user-attachments/assets/ce4f98bf-6b49-43c5-a192-f280dd6ea1e7)

## Technologies Used

- Python
- PyQt5 for the graphical user interface
- OpenWeatherMap API
- Requests library

## Future Improvements

- Add forecast data for upcoming days
- Implement location detection based on IP address
- Add support for more weather data points
- Implement weather alerts

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) for the GUI framework
- This is my first Python project. Feedback and contributions are welcome!
