"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###

## initial thought: use compound interest formula to calculate the final amount of money made
## after both a 10 year and 20 year investment

principal = 33000000000 # amount initially invested
# ten year investment
rate_ten_year = 3.96 # interest rate as a percentage (not decimal) for 10 year bond
n_ten = 10 # number of years
ten_year_final = principal * ((1 + (rate_ten_year / 100)) ** n_ten) # calculation of final amount after 10 years
print('The final amount after 10 years is' , ten_year_final)
# twenty year investment
rate_twenty_year = 4.32 # interest rate as a percentage (not decimal) for 20 year bond
n_twenty = 20 # number of years
twenty_year_final = principal * ((1 + (rate_twenty_year / 100)) ** n_twenty) # calculation of final amount after 20 years
print('The final amount after 20 years is' , twenty_year_final)

# final answer for 10-year
#ten_year_final = None

# final answer for 20-year
#twenty_year_final = None
