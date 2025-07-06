// MT5_Core/ResultsLogger.mqh

#include <Files\FileTxt.mqh>

void SaveResultToCSV(string filename, string strategy_name, double profit, double drawdown, double winrate, int trades) {
   int file = FileOpen(filename, FILE_WRITE | FILE_TXT | FILE_COMMON | FILE_READ);
   if (file == INVALID_HANDLE) {
      Print("Failed to open result file for writing");
      return;
   }

   // Go to end to append new result
   FileSeek(file, 0, SEEK_END);

   string line = StringFormat("%s,%.2f,%.2f,%.2f,%d\n",
                              strategy_name,
                              profit,
                              drawdown,
                              winrate,
                              trades);
   FileWriteString(file, line);
   FileClose(file);
}
