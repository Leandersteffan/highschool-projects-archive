# Define the investment strategy
investment_strategy_old = [
    ["Welt ETF", 35, [["MSCI World", 20], ["ACWI", 15]]],
    ["S&P 500", 21],
    ["Crypto", 15, [["Bitcoin", 10], ["Microstrategy", 5]]],
    ["Gold (ETF or Physical)", 10],
    [
        "Regional/EM Diversification", 19, [
            ["China", 3],
            ["India", 2],
            ["Southeast Asia", 2],
            ["Brazil", 1],
            ["Middle East", 3],
            ["South Africa", 1],
            ["Russia", 2],
            ["Poland", 1],
            ["Germany", 1],
            ["Global Small-Cap Stocks", 3]
        ]
    ]
]

investment_strategy = [
    ["Welt ETF", 35, [["MSCI World", 20], ["ACWI", 15]]],
    ["S&P 500", 21],
    ["Crypto", 15, [["Bitcoin", 10], ["Microstrategy", 5]]],
    ["Gold (ETF or Physical)", 10],
    [
        "Regional/EM Diversification", 19, [
            ["core msci em imi usd acc", 10],
            ["iShares Core MSCI Europe EUR (acc)", 7],
            ["Global Small-Cap Stocks", 2]
        ]
    ]
]

investment_strategy_without_crypto = [
    ["Welt ETF", 39, [["MSCI World", (20+2)], ["ACWI", (15+2)]]],
    ["S&P 500", (21+3)],
    #["Crypto", 15, [["Bitcoin", 10], ["Microstrategy", 5]]],
    ["Gold (ETF or Physical)", 10+4],
    [
        "Regional/EM Diversification", 23, [
            ["core msci em imi usd acc", 10+3],
            ["iShares Core MSCI Europe EUR (acc)", (7+3)],
            #["Global Small-Cap Stocks", 2]
        ]
    ]
]

def calculate_allocation(strategy, total_investment):
    allocations = {}

    def allocate(category, percentage, subcategories=None):
        amount = (percentage / 100) * total_investment
        if subcategories:
            for sub in subcategories:
                sub_amount = (sub[1] / percentage) * amount
                allocations[sub[0]] = round(sub_amount, 2)
        else:
            allocations[category] = round(amount, 2)

    for item in strategy:
        category = item[0]
        percentage = item[1]
        subcategories = item[2] if len(item) > 2 else None
        allocate(category, percentage, subcategories)

    return allocations

def main():
    try:
        total_investment = float(input("Enter the total amount you want to invest: "))
        allocation_result = calculate_allocation(investment_strategy_without_crypto, total_investment) #here change the strat!!
        print("\nInvestment Allocation:")
        for asset, amount in allocation_result.items():
            print(f"{asset}: {amount} EUR")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
