# YFinanceStockTool

## Table of Contents
- [Description](#description)
- [Key Features](#key-features)
- [Languages Used](#languages-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description
YFinance Stocks is a Flask web application that provides users with real-time access to stock market data using the Yahoo Finance API. The app features an intuitive interface that allows users to search for stock information, view historical price charts, and analyze market trends.

## Key Features
- **Real-Time Stock Data:** Access the latest stock prices and market information.
- **Historical Data Analysis:** View historical price charts for comprehensive analysis.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Dynamic Search:** Easily search for stocks by name or ticker symbol.
- **Lightweight and Fast:** Ensures quick loading times and efficient performance.

## Languages Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **APIs:** Yahoo Finance API

## Installation Instructions
Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hhussain04/YFinanceStockTool.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd YFinanceStockTool
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your environment variables for API keys (if needed).**

5. Generate your own secret key and make a .env file in the root folder of the project, you can use pythons in-built **_secrets_** module for this:
     ```python
   import secrets
   secret_key = secrets.token_hex(32)
   print(secret_key)
   ```

7. **Run the application:**
   ```bash
   python app.py
   ```

## Usage
- Open your web browser and navigate to `http://127.0.0.1:5000` to access the app. (Alternatively if you have your own domain host you can just host this on there)
- Use the search bar to enter stock names or ticker symbols to get real-time data and historical charts.

## Contributing
Contributions are welcome! If you'd like to contribute to the project:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/xnewFeature`.
3. Make your changes and commit them: `git commit -m "Add x feature that does y"`.
4. Push to the branch: `git push origin feature/xnewFeature`.
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
