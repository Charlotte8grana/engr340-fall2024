#initial thought: determine how much money must be deposited into an account with 5% interest to output the total tuition for instate
#instate tuition calculations
in_state_tuition = 30792 #instate tuition cost on JMU website for 2022-2023 school year
return_rate = 0.05 #given percentage (as a decimal) return rate at designated bank
in_state_gift = in_state_tuition / return_rate #calculation to find deposit amount
print('in_state_gift is' , in_state_gift) #print gift amount value

#out of state tuition calculations
out_state_tuition = 47882 #out of state tuition cost on JMU website for 2022-2023 school year
out_state_gift = out_state_tuition / return_rate #calculation to find deposit amount
print('out_state_gift is' , out_state_gift)

