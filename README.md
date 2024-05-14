# Weather App

## Description
This Python CLI (Command Line Interface) weather app provides users with current weather information for a specified location or their current location if none is provided. The app leverages weather data from reliable sources to deliver accurate and up-to-date weather forecasts.

## Usage
To use the app, follow these steps:

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```
4. Run the weather CLI app with the following command:
```python
python weather.py [location]
```
5. Replace `[location]` with the desired location for which you want to retrieve weather information. If no location is provided, the app will use your current location.

## Features
- Retrieve current weather information for any specified location.
- Automatically detect and use the user's current location if no location is provided.
- Simple and intuitive command-line interface for easy usage.

## Requirements
- Python 3.x
- See `requirements.txt` for a list of Python packages required. Install these dependencies using `pip install -r requirements.txt`.

## Contributing
Contributions to the Weather App are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This app relies on third-party weather data sources and accuracy may vary depending on the availability and reliability of these sources. Use at your own discretion.

## Acknowledgements
Used open-meteo API: https://open-meteo.com/en/docs
