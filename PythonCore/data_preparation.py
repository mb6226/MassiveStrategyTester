import pandas as pd

def load_raw_data(file_path):
    # خواندن فایل CSV خام
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # حذف ردیف‌های ناقص یا پرکردن مقادیر گم‌شده
    df = df.dropna()
    # اصلاح فرمت تاریخ، تایم‌استمپ و...
    df['Date'] = pd.to_datetime(df['Date'])
    # سایر اصلاحات لازم
    return df

def standardize_data(df):
    # اطمینان از ستون‌های مورد نیاز و ترتیب آنها
    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df[required_columns]
    # مرتب‌سازی بر اساس تاریخ
    df = df.sort_values(by='Date')
    return df

def save_prepared_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Prepared data saved to {output_path}")

if __name__ == "__main__":
    raw_file = "Data/raw_data.csv"
    prepared_file = "Data/prepared_data.csv"

    df_raw = load_raw_data(raw_file)
    df_clean = clean_data(df_raw)
    df_std = standardize_data(df_clean)
    save_prepared_data(df_std, prepared_file)
