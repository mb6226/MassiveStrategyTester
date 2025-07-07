import os
import argparse
import pandas as pd
from bs4 import BeautifulSoup

def extract_metrics_from_html(html_path):
    with open(html_path, 'r', encoding='utf-16') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    metrics = {
        'Strategy': os.path.basename(html_path).replace('.html', ''),
        'Total Trades': None,
        'Profit': None,
        'Drawdown': None,
        'Expected Payoff': None,
    }

    try:
        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) != 2:
                continue
            label = cols[0].text.strip()
            value = cols[1].text.strip()

            if 'Total trades' in label:
                metrics['Total Trades'] = int(value)
            elif 'Gross profit' in label:
                metrics['Profit'] = float(value.replace(',', ''))
            elif 'Maximal drawdown' in label:
                metrics['Drawdown'] = float(value.split(' ')[0].replace(',', ''))
            elif 'Expected payoff' in label:
                metrics['Expected Payoff'] = float(value.replace(',', ''))
    except Exception as e:
        print(f"❌ Error parsing {html_path}: {e}")
    
    return metrics

def parse_all_results(input_dir, output_file):
    data = []
    for file in os.listdir(input_dir):
        if file.endswith('.html'):
            html_path = os.path.join(input_dir, file)
            metrics = extract_metrics_from_html(html_path)
            data.append(metrics)
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"✅ Summary saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, required=True, help='Path to directory with MT5 HTML reports')
    parser.add_argument('--output_file', type=str, required=True, help='CSV file to save the summary')
    args = parser.parse_args()

    parse_all_results(args.input_dir, args.output_file)
