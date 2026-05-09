# Expert System for Stock Market Trading

print("====================================")
print(" Stock Market Expert System ")
print("====================================")

market = input("Enter Market Trend (up/down/stable): ").lower()
risk = input("Enter Risk Level (low/high): ").lower()

print("\nTrading Suggestion:\n")

if market == "up" and risk == "high":

    print("Suggestion: BUY stocks")
    print("Reason: Market is rising")

elif market == "down" and risk == "low":

    print("Suggestion: HOLD or SELL stocks")
    print("Reason: Market is falling")

elif market == "stable":

    print("Suggestion: HOLD stocks")
    print("Reason: Market is stable")

else:

    print("Suggestion: Analyze market carefully before investing")