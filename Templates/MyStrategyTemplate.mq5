//+------------------------------------------------------------------+
//|                                  MyStrategyTemplateWithTrailing |
//+------------------------------------------------------------------+
#property copyright "OpenAI"
#property version   "1.01"
#property strict

input double LotSize       = 0.1;
input int    SlPoints      = 500;   // SL in points
input int    TpPoints      = 1000;  // TP in points
input int    Slippage      = 10;
input int    MagicNumber   = 123456;
input int    TrailingStop  = 300;   // Trailing Stop in points
input int    TrailingStep  = 50;    // Step size to update SL

bool trailing_set = false;

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
{
   // No position → open one
   if(!PositionSelect(_Symbol))
   {
      double ask = NormalizeDouble(SymbolInfoDouble(_Symbol, SYMBOL_ASK), _Digits);

      MqlTradeRequest request = {};
      MqlTradeResult  result  = {};

      request.action   = TRADE_ACTION_DEAL;
      request.symbol   = _Symbol;
      request.volume   = LotSize;
      request.type     = ORDER_TYPE_BUY;
      request.price    = ask;
      request.sl       = 0.0;
      request.tp       = ask + TpPoints * _Point;
      request.deviation= Slippage;
      request.magic    = MagicNumber;

      if(OrderSend(request, result) && result.retcode == TRADE_RETCODE_DONE)
      {
         Print("✅ Buy order opened. Ticket: ", result.order);
         trailing_set = false;
      }
      else
      {
         Print("❌ Failed to open order. Code: ", result.retcode);
      }

      return;
   }

   // Trailing Stop logic
   ulong ticket = PositionGetInteger(POSITION_TICKET);
   double entry_price = PositionGetDouble(POSITION_PRICE_OPEN);
   double current_sl  = PositionGetDouble(POSITION_SL);
   double bid         = NormalizeDouble(SymbolInfoDouble(_Symbol, SYMBOL_BID), _Digits);
   double new_sl      = NormalizeDouble(bid - TrailingStop * _Point, _Digits);

   if(PositionGetInteger(POSITION_TYPE) == POSITION_TYPE_BUY)
   {
      // only trail if price is beyond threshold and SL is behind
      if(bid - entry_price > (TrailingStop + TrailingStep) * _Point)
      {
         if(current_sl < new_sl)
         {
            MqlTradeRequest slmod = {};
            MqlTradeResult  result = {};

            slmod.action   = TRADE_ACTION_SLTP;
            slmod.position = ticket;
            slmod.sl       = new_sl;
            slmod.tp       = PositionGetDouble(POSITION_TP);

            if(OrderSend(slmod, result) && result.retcode == TRADE_RETCODE_DONE)
            {
               Print("🔁 Trailing Stop updated. New SL: ", new_sl);
               trailing_set = true;
            }
         }
      }
   }
}
