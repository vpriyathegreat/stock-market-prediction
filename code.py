import yfinance as yf
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class StockRecommendationApp(App):
    def build(self):
        self.title = 'Stock Recommendation App'

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        title_label = Label(text='Stocks You Can Buy', font_size=36, color=(0, 0.5, 1, 1), size_hint=(1, 0.1))

        input_layout = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, 0.5))
        input_layout.border = (10, 10, 10, 10)

        input_layout.add_widget(Label(text='Amount in your bank (in dollars):', font_size=24))
        self.bank_input = TextInput(hint_text='Amount in dollars', input_type='number', font_size=24)
        input_layout.add_widget(self.bank_input)

        # Create a Spinner for stock symbols
        stock_symbols = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']  # Replace with your list of stock symbols
        self.stock_spinner = Spinner(text='Select a stock symbol', values=stock_symbols, font_size=24)
        input_layout.add_widget(self.stock_spinner)

        self.recommendation_label = Label(text='Recommendation will appear here', halign='center', font_size=24, color=(0, 0.5, 1, 1), size_hint=(1, 0.2))

        calculate_button = Button(text='Calculate', font_size=24, background_color=(0, 0.5, 1, 1), size_hint=(0.2, 0.1))
        calculate_button.bind(on_release=self.calculate_recommendation)

        layout.add_widget(title_label)
        layout.add_widget(input_layout)
        layout.add_widget(self.recommendation_label)
        layout.add_widget(calculate_button)

        return layout

    def calculate_recommendation(self, instance):
        available_funds = float(self.bank_input.text)
        stock_symbol = self.stock_spinner.text  # Get the selected stock symbol

        recommendation = self.get_stock_recommendation(stock_symbol, available_funds)
        self.recommendation_label.text = recommendation

    def get_stock_recommendation(self, stock_symbol, available_funds):
        stock_data = yf.Ticker(stock_symbol)
        current_price = stock_data.history(period="1d")["Close"].iloc[-1]
        shares_to_buy = available_funds / current_price

        return f'With ${available_funds:.2f} in your bank, you can buy {shares_to_buy:.2f} shares of {stock_symbol} at the current price of ${current_price:.2f} per share.'

if __name__== '__main__':
    StockRecommendationApp().run()
