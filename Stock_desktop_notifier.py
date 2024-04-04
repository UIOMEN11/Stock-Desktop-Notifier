import datetime
import time
from plyer import notification
import yfinance as yf
msft = yf.Ticker("MSFT")
data = msft.info

while True:
    notification.notify(
        title = "MSFT data".format(datetime.date.today()),
        message = "Current Price = {cp} \n Day low = {dl} \n Day high = {dh}".format(
            cp = data["currentPrice"],
            dl = data["regularMarketDayLow"],
            dh = data["regularMarketDayHigh"]
        ),
        app_icon = "Alecive-Flatwoken-Apps-Notifications.ico",
        timeout = 5

    )
    time.sleep(10)
