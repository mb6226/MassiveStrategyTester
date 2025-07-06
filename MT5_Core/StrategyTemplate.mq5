// MT5_Core/StrategyTemplate.mq5

#property strict
input int emaPeriod = 50;
input int rsiPeriod = 14;
input int atrPeriod = 14;
input double takeProfit = 50;
input double stopLoss = 30;

double ema, rsi, atr;

int OnInit() {
   return(INIT_SUCCEEDED);
}

void OnTick() {
   ema = iMA(NULL, 0, emaPeriod, 0, MODE_EMA, PRICE_CLOSE, 0);
   rsi = iRSI(NULL, 0, rsiPeriod, PRICE_CLOSE, 0);
   atr = iATR(NULL, 0, atrPeriod, 0);

   if (ema > iClose(NULL, 0, 1) && rsi < 30) {
      OpenBuy();
   }

   if (ema < iClose(NULL, 0, 1) && rsi > 70) {
      OpenSell();
   }
}

void OpenBuy() {
   if (PositionsTotal() == 0) {
      double lot = 0.1;
      double sl = Bid - stopLoss * _Point;
      double tp = Bid + takeProfit * _Point;
      trade.Buy(lot, _Symbol, Bid, sl, tp);
   }
}

void OpenSell() {
   if (PositionsTotal() == 0) {
      double lot = 0.1;
      double sl = Ask + stopLoss * _Point;
      double tp = Ask - takeProfit * _Point;
      trade.Sell(lot, _Symbol, Ask, sl, tp);
   }
}
