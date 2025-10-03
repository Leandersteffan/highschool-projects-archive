import math


def best_Version(listen):   # best_Version([["booki1", 2, 4], ["booki2", 3, 3]])
    bestVersionReturn = []
    for i in range(1, len(listen[0])):  # geht durch jede Wetbare Partei ohne den Namen
        bestForPosition = [listen[0][0], listen[0][i]]
        for j in range(1, len(listen)): # geht durch die anderen Bookis nicht den ersten
            if bestForPosition[1] < listen[j][i]:    # vergleicht andere angebote mit erstem
                bestForPosition = [listen[j][0], listen[j][i]]
        bestVersionReturn.append(bestForPosition)
    return bestVersionReturn

def abitrage_Calc(liste):
    try:
        x = liste[0][0]
        zwischenErgebnis = 0
        for i in range(len(liste)):
            zwischenErgebnis += (1 / liste[i][1])
        return zwischenErgebnis
    except:
        zwischenErgebnis = 0
        for i in range(len(liste)):
            zwischenErgebnis += (1 / liste[i])
        return zwischenErgebnis

def calculate_arbitrage_bet(returns, total_stake):
    implied_probabilities = [1 / r for r in returns]
    combined_implied_probability = sum(implied_probabilities)
    stakes = [(total_stake * p) / combined_implied_probability for p in implied_probabilities]
    profits = [r * s - total_stake for r, s in zip(returns, stakes)]
    overall_profit = max(profits)
    return stakes, overall_profit

def calculate_arbitrage_bet_with_max_profit(returns, total_stake, max_profit_stake):    # e.g.
    stakes = [0] * len(returns)
    stake_spent = 0
    for i in range(len(returns)):
        if not returns[i] == max_profit_stake:
            stakes[i] = total_stake / returns[i]
            stake_spent += total_stake / returns[i]
    for i in range(len(returns)):
        if not stakes[i]:
            stakes[i] = total_stake - stake_spent
    return stakes

def returns_without_booki(booki_returns_list):
    output_list = []
    for i in range(len(booki_returns_list)):
        output_this_list = []
        for j in range(1, len(booki_returns_list[0])):
            output_this_list.append(float(booki_returns_list[i][j]))
        output_list.append(output_this_list)
    for i in range(len(output_list)):
        output_list[i] = output_list[i][0]
    return output_list

def roundup(x, round_up_to):
    return int(math.ceil(x / round_up_to)) * round_up_to

def round_up_to_nicer_number(value, max_for_rounding):
    priority_list = [10, 5, 1, 0.5, 0.1, 0.05]
    for priority in priority_list:
        rounded_value = roundup(value, priority)
        if rounded_value - value <= max_for_rounding:
            return rounded_value

def check_if_always_profit(returns, stakes):
    total_stake = sum(stakes)
    for i in range(len(returns)):
        if stakes[i] * returns[i] < total_stake:
            return False
    return True

def calculate_arbitrage_bet_with_uprounded_stakes(returns, total_stake, extra_stake=10):
    implied_probabilities = [1 / r for r in returns]
    combined_implied_probability = sum(implied_probabilities)
    stakes = [(total_stake * p) / combined_implied_probability for p in implied_probabilities]
    extra_stake_for_each = extra_stake / len(returns)
    for i in range(len(stakes)):
        stakes[i] = round_up_to_nicer_number(stakes[i], extra_stake_for_each)
    if check_if_always_profit(returns, stakes):
        return stakes
    else:
        calculate_arbitrage_bet_with_uprounded_stakes(returns, total_stake, extra_stake-1)

def alles_wichtige_print(list_returns_bookis, total_stakes):
    print(f"best version: {best_Version(list_returns_bookis)}")
    print(f"Abitrage Vorteil: {abitrage_Calc(best_Version(list_returns_bookis))}")
    wetteinsaetze, profit = calculate_arbitrage_bet(returns_without_booki(best_Version(list_returns_bookis)), total_stakes)
    print(f"Abitrage Wetteinsätze: {wetteinsaetze}")
    print(f"Abitrage Profit: {profit}")
    print(f"Abitrage Wetteinsätze aufgerundet: {calculate_arbitrage_bet_with_uprounded_stakes(returns_without_booki(best_Version(list_returns_bookis)), total_stakes)}")

def alles_wichtige_return(list_returns_bookis, total_stakes):
    welcher_booki_welche_wette = best_Version(list_returns_bookis)
    abitrage_Vorteil = abitrage_Calc(best_Version(list_returns_bookis))
    wetteinsaetze, profit = calculate_arbitrage_bet(returns_without_booki(best_Version(list_returns_bookis)), total_stakes)
    abitrage_Wetteinsaetze_Aufgerundet = calculate_arbitrage_bet_with_uprounded_stakes(returns_without_booki(best_Version(list_returns_bookis)), total_stakes)
    return welcher_booki_welche_wette, abitrage_Vorteil, wetteinsaetze, profit, abitrage_Wetteinsaetze_Aufgerundet


if __name__ == "__main__":
    #test = best_Version([["booki1", 2, 4, 50], ["booki2", 3, 3, 80]])
    #print(test)
    #print(abitrage_Calc(test))
    #print(abitrage_Calc([1.9, 6.2, 4.1]))
    #print(calculate_arbitrage_bet([1.9, 6.2, 4.1], 300))
    #print(calculate_arbitrage_bet_with_max_profit([1.9, 6.2, 4.1], 300, 1.9))
    #print(calculate_arbitrage_bet_with_uprounded_stakes([1.9, 6.2, 4.1], 300))
    alles_wichtige_print([["booki1", 2, 4, 50], ["booki2", 3, 3, 80]], 300)
    #alles_wichtige_print([["booki1", 3, 1.4], ["booki2", 2, 1.8]], 100)
