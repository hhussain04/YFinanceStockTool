from flask import Flask, render_template, request, redirect, url_for, flash, session
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

def get_ticker(query):
    query = query.upper()
    for name, ticker in ticker_mappings.items():
        if query in name or query == ticker:
            return ticker
    return None

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
    company_name = request.form['company_name'].strip().upper()
    if company_name:
        results = [(name, ticker) for name, ticker in ticker_mappings.items() if company_name in name or company_name == ticker]
        if not results:
            flash("No results found.", "error")
        elif len(results) == 1:
            ticker = results[0][1]
            if ticker not in selected_tickers:
                selected_tickers.append(ticker)
                flash(f"{ticker} added to the list.", "success")
            else:
                flash(f"{ticker} is already in the list.", "error")
            return redirect(url_for('index'))
        else:
            session['search_results'] = results
            return redirect(url_for('select_ticker'))
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
            'name': ticker  # Ensure the name is set correctly
        })

    return render_template('graph.html', graph_data=graph_data)

@app.route('/view_tickers')
def view_tickers():
    return render_template('view_tickers.html', tickers=selected_tickers)

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        search_query = request.form['search_query'].strip().upper()
        results = [(name, ticker) for name, ticker in ticker_mappings.items() if search_query in name or search_query == ticker]
        if not results:
            flash("No results found.", "error")
        elif len(results) == 1:
            ticker = results[0][1]
            if ticker not in selected_tickers:
                selected_tickers.append(ticker)
                flash(f"{ticker} added to the list.", "success")
            else:
                flash(f"{ticker} is already in the list.", "error")
            return redirect(url_for('index'))
        else:
            flash("Multiple matches found. Please refine your search.", "error")
    return render_template('search.html', results=results)

@app.route('/select_ticker', methods=['GET', 'POST'])
def select_ticker():
    if request.method == 'POST':
        selected_ticker = request.form['selected_ticker']
        if selected_ticker and selected_ticker not in selected_tickers:
            selected_tickers.append(selected_ticker)
            flash(f"{selected_ticker} added to the list.", "success")
        else:
            flash(f"{selected_ticker} is already in the list or invalid.", "error")
        return redirect(url_for('index'))
    results = session.get('search_results', [])
    return render_template('select_ticker.html', results=results)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)