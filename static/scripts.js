async function addTicker() {
    const companyName = document.getElementById('companyName').value;
    const response = await fetch('/add_ticker', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ company_name: companyName })
    });
    const data = await response.json();
    if (response.ok) {
        const tickerList = document.getElementById('tickerList');
        const listItem = document.createElement('li');
        listItem.textContent = companyName;
        tickerList.appendChild(listItem);
    } else {
        alert(data.message);
    }
}

async function fetchData(period) {
    const response = await fetch('/fetch_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ period: period })
    });
    const data = await response.json();
    if (response.ok) {
        plotGraph(data);
    } else {
        alert(data.message);
    }
}

function plotGraph(data) {
    const graphDiv = document.getElementById('graph');
    const traces = [];
    const groupedData = data.reduce((acc, item) => {
        if (!acc[item.Company]) {
            acc[item.Company] = [];
        }
        acc[item.Company].push(item);
        return acc;
    }, {});

    for (const [company, values] of Object.entries(groupedData)) {
        traces.push({
            x: values.map(item => item.Date),
            y: values.map(item => item.Close),
            type: 'scatter',
            mode: 'lines',
            name: company  // Ensure the name is set correctly
        });
    }

    Plotly.newPlot(graphDiv, traces, { title: 'Stock Prices' });
}

function navigateTo(url) {
    window.location.href = url;
}