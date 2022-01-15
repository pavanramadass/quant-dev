from itertools import islice
import pandas as pd
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
from ta.trend import SMAIndicator, MACD

load_dotenv()


hour_delta = pd.Timedelta(1, unit='H')

holdings = 0


def main():
  api = REST()

  df = api.get_bars("AAPL", TimeFrame.Hour, "2021-10-01", "2021-11-01", adjustment='raw').df

  sma20 = SMAIndicator(df['close'], 20).sma_indicator()
  sma50 = SMAIndicator(df['close'], 50).sma_indicator()
  sma200 = SMAIndicator(df['close'], 200).sma_indicator()

  macd = MACD(df['close']).macd()

  for index, row in df.iterrows():
    if not (sma20[index] and sma50[index] and sma200[index] and macd[index]):
      continue

    if macd[index] > 0 and sma20[index] < sma50[index] < sma200[index]:
      if holdings == 0:
        buy()

    if macd[index] < 0 and sma20[index] > sma50[index] > sma200[index]:
      if holdings > 0:
        sell()


def buy():
  holdings += 100
  print("Buying")

def sell():
  holdings -= 100
  print("Selling")


if __name__ == "__main__":
  main()
