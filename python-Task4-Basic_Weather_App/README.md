# 🌤️ Basic Weather App

A simple Python application that fetches real-time weather information for any city using the **OpenWeatherMap API**. This project demonstrates API integration, JSON parsing, input validation, and exception handling.

## 📌 Features

- 🌍 Search weather by city name
- 🌡️ Display temperature in Celsius and Fahrenheit
- 💧 Display humidity percentage
- ☁️ Show weather condition and description
- 💨 Display wind speed
- ✅ Input validation for empty or invalid city names
- ⚠️ Handles API errors gracefully
- 🌐 Handles network connection and timeout errors

## 🛠️ Technologies Used

- Python 3
- Requests Library
- Python Dotenv
- OpenWeatherMap API

## 📂 Project Structure

```
python-Task4-Basic_Weather_App/
│── get_weather.py
│── .env
│── .gitignore
│── requirements.txt
└── README.md
```

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/OIBSIP.git
```

2. Navigate to the project folder:

```bash
cd OIBSIP/python-Task4-Basic_Weather_App
```

## 🔑 API Key Setup

Create a file named `.env` in the project folder and add your OpenWeatherMap API key:

```env
API_KEY=YOUR_OPENWEATHERMAP_API_KEY
```

> **Note:** Never upload your `.env` file to GitHub. It is already ignored using `.gitignore`.

## ▶️ Run the Program

```bash
python get_weather.py
```

## 💻 Example Output

```
Enter city name: Surat

City Name: Surat
Weather: Clouds
Weather Condition: Broken Clouds
Temperature: 31.5°C
Temperature: 88.7°F
Humidity: 74%
Wind Speed: 4.2 m/s
```

## 📚 Concepts Used

- Variables
- User Input
- Loops
- Conditional Statements
- Input Validation
- Functions
- HTTP Requests
- JSON Parsing
- Exception Handling
- Environment Variables (.env)

## 📋 Error Handling

The application handles:

- Empty city name
- Invalid city name
- Invalid API key
- Internet connection issues
- Request timeout
- Unexpected errors

## 👨‍💻 Author

**Deep Savani**

Information Technology Student | Python Developer

## 📜 License

This project is created for learning purposes as part of the **Oasis Infobyte Python Programming Internship**.