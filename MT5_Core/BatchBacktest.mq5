// MT5_Core/BatchBacktest.mq5

#include <Files\FileTxt.mqh>
#include "ResultsLogger.mqh"

input string strategiesFile = "strategies.txt";

void OnStart() {
   int handle = FileOpen(strategiesFile, FILE_READ | FILE_TXT);
   if (handle == INVALID_HANDLE) {
      Print("Failed to open strategies file");
      return;
   }

   while (!FileIsEnding(handle)) {
      string line = FileReadString(handle);
      if (StringLen(line) == 0) continue;

      string parts[];
      StringSplit(line, ',', parts);
      if (ArraySize(parts) < 5) continue;

      int ema = (int)StringToInteger(parts[0]);
      int rsi = (int)StringToInteger(parts[1]);
      int atr = (int)StringToInteger(parts[2]);
      double tp = StringToDouble(parts[3]);
      double sl = StringToDouble(parts[4]);

      RunStrategy(ema, rsi, atr, tp, sl);
   }

   FileClose(handle);
}

void RunStrategy(int ema, int rsi, int atr, double tp, double sl) {
   // تنظیم ورودی‌های اکسپرت و اجرای تست (مثلاً با SetParameter یا ارسال ورودی به StrategyTemplate)
   PrintFormat("Testing strategy: EMA=%d RSI=%d ATR=%d TP=%.2f SL=%.2f", ema, rsi, atr, tp, sl);

   // این تابع باید Expert مربوطه رو با این پارامترها اجرا کنه (مثلاً با استفاده از تست خودکار)
   // و نتیجه را ذخیره کند. برای نمونه در فایل CSV توسط `ResultsLogger.mqh`
}
