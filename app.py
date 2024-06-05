#STOCK PRICE DETECTION by the help of API Calling in Python. We have used flask for web, pandas, yfinance, datetime, matplotlib, io, base64, FFPDF
from flask import Flask, render_template, jsonify, send_file
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
import io
import base64
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    # Define date range
    today = date.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")

    # Download stock data
    data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
    data["Date"] = data.index
    data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)

    # Calculate Moving Averages
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()

    # Plot the closing prices and moving averages
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.plot(data['Date'], data['50_MA'], label='50-Day Moving Average')
    plt.plot(data['Date'], data['200_MA'], label='200-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL Stock Price and Moving Averages')
    plt.legend()

    # Save the plot as a PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Convert data to JSON for table display
    data_json = data.to_json(orient='records')

    return render_template('index.html', plot_url=plot_url, data_json=data_json)

@app.route('/download_csv')
def download_csv():
    # Define date range
    today = date.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")

    # Download stock data
    data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
    data["Date"] = data.index
    data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)
    
    # Save CSV to a BytesIO object
    csv = io.BytesIO()
    data.to_csv(csv, index=False)
    csv.seek(0)
    return send_file(csv, mimetype='text/csv', attachment_filename='AAPL_stock_data.csv', as_attachment=True)

@app.route('/download_pdf')
def download_pdf():
    # Define date range
    today = date.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")

    # Download stock data
    data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
    data["Date"] = data.index
    data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)
    
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AAPL Stock Data", ln=True, align='C')

    # Add data to PDF
    for i in range(len(data)):
        pdf.cell(200, 10, txt=str(data.iloc[i].to_dict()), ln=True, align='L')

    # Save PDF to a BytesIO object
    pdf_bytes = io.BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)
    return send_file(pdf_bytes, mimetype='application/pdf', attachment_filename='AAPL_stock_data.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
