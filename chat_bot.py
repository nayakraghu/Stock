from stock_analyzer import analyze_stock

def run_chat_bot():
    print("📈 Welcome to StockBot!")
    print("Type a stock ticker (e.g., AAPL, TSLA) or 'exit' to quit.")

    while True:
        user_input = input("You: ").strip().upper()
        if user_input == 'EXIT':
            print("👋 Goodbye!")
            break

        try:
            suggestion = analyze_stock(user_input)
            print(f"🤖 StockBot: Recommendation for {user_input}: {suggestion}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
