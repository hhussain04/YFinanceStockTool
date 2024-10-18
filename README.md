# YFinanceStockTool

YFinanceStockTool is a Flask web application that provides users with real-time access to stock market data using the Yahoo Finance API. The app features an intuitive interface that allows users to search for stock information, view historical price charts, and analyze market trends.

## Table of Contents
- [Description](#description)
- [Key Features](#key-features)
- [Languages Used](#languages-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

YFinanceStockTool is designed to help users easily access and analyze stock market data. With real-time updates and historical data analysis, users can make informed decisions based on the latest market trends.

## Key Features

- **Real-Time Stock Data:** Access the latest stock prices and market information
- **Historical Data Analysis:** View historical price charts for comprehensive analysis
- **Responsive Design:** Optimized for both desktop and mobile devices
- **Dynamic Search:** Easily search for stocks by name or ticker symbol
- **Lightweight and Fast:** Ensures quick loading times and efficient performance

## Languages Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **APIs:** Yahoo Finance API

## Installation Instructions

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/hhussain04/YFinanceStockTool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd YFinanceStockTool
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project directory and add the following:
   ```
   SECRET_KEY=your_secret_key
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
