def calculate_saving_plan_value(monthly_saving, annual_growth_rate, years, beginningvalue = 0):
    """
    Calculate the future value of a savings plan with constant monthly savings and annual growth.

    :param monthly_saving: Amount saved each month (float)
    :param annual_growth_rate: Annual growth rate of the ETF in percentage (float, e.g., 5 for 5%)
    :param years: Number of years to calculate (int)
    :return: Total savings value after the given time (float)
    """
    total_months = years * 12
    monthly_growth_rate = (1 + annual_growth_rate / 100) ** (1 / 12) - 1
    total_value = beginningvalue

    for _ in range(total_months):
        total_value = total_value * (1 + monthly_growth_rate) + monthly_saving

    return total_value


# Example usage
#monthly_save = 500  # Save 500 each month
#annual_growth = 7  # Annual growth rate of 7%
#time_years = 20  # Calculate for 20 years

monthly_save = 6000  # Save x each month
annual_growth = 11  # Annual growth rate of x%
time_years = 30-19  # Calculate for x years
beginningcash = 20000  # The Amount of Money you start with which will keep growing. (0 is a valid input)

future_value = calculate_saving_plan_value(monthly_save, annual_growth, time_years, beginningcash)
future_value_inoneyearplus = calculate_saving_plan_value(monthly_save, annual_growth, time_years + 1, beginningcash)
print(f"The future value of your savings plan is: €{future_value:.2f}\n")
print(f"The future value generated in {time_years} years plus 1 (one year): €{future_value_inoneyearplus - future_value:.2f}\n")
print(f"The future value generated in {time_years} years plus 1 (one year) WITHOUT SAVING ONLY INTEREST: €{future_value*(1+ annual_growth / 100)-future_value:.2f}\n")
