from flask import Flask, render_template, request, redirect, url_for, flash
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go # type: ignore
from dotenv import load_dotenv
import os
import csv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


# Global variable to store tickers
selected_tickers = []

ticker_mappings = {}
with open('tickers.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header row
    for rows in reader:
        ticker_mappings[rows[0].strip().upper()] = rows[1].strip().upper()

def get_ticker(company_name):
    return ticker_mappings.get(company_name.upper())

def get_data(tickers, period):
    combined_df = pd.DataFrame()
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)
            hist['Company'] = ticker
            hist.reset_index(inplace=True)
            combined_df = pd.concat([combined_df, hist], ignore_index=True)
            print(f"Fetched data for {ticker}: {hist.head()}")  # Debugging: Print fetched data
        except Exception as e:
            flash(f"An error occurred while fetching data for {ticker}: {e}", "error")
    return combined_df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_ticker', methods=['POST'])
def add_ticker():
    company_name = request.form['company_name'].strip()
    if company_name:
        ticker = get_ticker(company_name)
        if ticker and ticker not in selected_tickers:
            selected_tickers.append(ticker)
            flash(f"{ticker} added to the list.", "success")
        else:
            flash(f"{company_name} is already in the list or invalid.", "error")
    else:
        flash("Please enter a company name or ticker.", "error")
    return redirect(url_for('index'))

@app.route('/clear_tickers')
def clear_tickers():
    selected_tickers.clear()
    flash("Ticker list cleared.", "success")
    return redirect(url_for('index'))

@app.route('/show_graph/<period>')
def show_graph(period):
    if not selected_tickers:
        flash("Please add at least one stock/company.", "error")
        return redirect(url_for('index'))

    combined_df = get_data(selected_tickers, period)
    if combined_df.empty:
        flash("No valid data found for the selected stocks.", "error")
        return redirect(url_for('index'))

    graph_data = []
    for ticker in selected_tickers:
        stock_data = combined_df[combined_df['Company'] == ticker]
        graph_data.append({
            'x': stock_data['Date'].tolist(),
            'y': stock_data['High'].tolist(),
            'mode': 'lines',
            'name': ticker
        })

    return render_template('graph.html', graph_data=graph_data)

@app.route('/view_tickers')
def view_tickers():
    return render_template('view_tickers.html', tickers=selected_tickers)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)