import pandas as pd

def inspect_tick_file(file_path, num_lines=5):
    print(f"Inspecting file: {file_path}\n")
    
    try:
        with open(file_path, 'r') as f:
            for i in range(num_lines):
                line = f.readline().strip()
                print(f"Line {i+1}: {line}")
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    print("\nAttempting to load sample with pandas...")
    try:
        df = pd.read_csv(file_path, nrows=num_lines, header=None)
        print("\nDetected Columns:")
        print(df.head())
        print("\nSample types:")
        print(df.dtypes)
    except Exception as e:
        print(f"Pandas failed to load the file: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Inspect first lines of a tick data CSV file")
    parser.add_argument('--input', type=str, default='Data/EURUSD_mt5_ticks.csv', help='Path to tick CSV file')
    parser.add_argument('--lines', type=int, default=5, help='Number of lines to inspect')
    args = parser.parse_args()

    inspect_tick_file(args.input, args.lines)
