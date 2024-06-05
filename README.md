# Stock-Data-API-Project
# AAPL Stock Analysis

This project is a web application built with Flask to provide live stock price data analysis for AAPL (Apple Inc.) using the Yahoo Finance API.

## Overview

The application fetches live stock price data from Yahoo Finance API and displays it in a tabular format on a webpage. It also includes a plot of the stock's closing prices along with its 50-day and 200-day moving averages. Users can download the data in CSV or PDF format.

## Features

- Displays live stock price data for AAPL.
- Provides a table view of the data along with moving averages.
- Renders a plot of closing prices and moving averages.
- Allows users to download the data in CSV or PDF format.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/aapl-stock-analysis.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the web application at `http://127.0.0.1:5000/` in your browser.

## Usage

- Upon accessing the web application, you will see live stock price data for AAPL displayed in a table format.
- You can download the data in CSV or PDF format by clicking the respective buttons.
- The plot of closing prices and moving averages is displayed below the table.

## Technologies Used

- Python
- Flask
- Pandas
- Matplotlib
- yfinance

## Author

[Chandresh Rajpoot](https://www.linkedin.com/in/chandreshrajpoot/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
