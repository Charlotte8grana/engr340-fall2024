import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
### YOUR CODE HERE
#df is the name of the loaded text in pandas to the dataframe
path_to_file = "../../data/drop-jump/all_participant_data_rsi.csv"
df = pd.read_csv(path_to_file)
"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE
#Only want to look at column 1(force plate) and 2(acceleration)
#For a normal distribution, mu (mean) and sigma (standard deviation) values are needed (information from class slides)

#Following class slides and examples for the information below

#DISTRIBUTION PARAMETERS
#Ideal Mu
mu = 0
print('The mean used to develop each distribution graph is ' + str(mu))
#Ideal standard deviation
std = 1
print('The standard deviation used to develop each distribution graph is ' + str(std))
#Changed number of samples from 10, to 50, to 100 to get the best fit distribution after sampling more values
number_samples = 100

##FORCE PLATE NORMAL DISTRIBUTION VS IDEAL DISTRIBUTION
#change force plate data from pandas to numpy
FP_Samples_numpy = df['force_plate_rsi'].to_numpy()

#Making normal distribution with those values
normal_samples_FP = np.random.normal(loc=mu, scale=std, size=number_samples)
#Calculating the mean and standard deviation of that distribution
sample_mean_FP = np.mean(normal_samples_FP)
print('The actual mean for the force plate data is ' + str(sample_mean_FP))
sample_std_FP = np.std(normal_samples_FP)
print('The actual standard deviation for the force plate data is ' + str(sample_std_FP))

#Finding a probability distribution function
space_x_FP = np.linspace(start=-3, stop=3, num=10000)
space_y_FP = norm.pdf(space_x_FP, loc=sample_mean_FP, scale=sample_std_FP)
#Plotting the distribution
plt.plot(space_x_FP, space_y_FP, label='Fitted Normal Distribution of Force Plate Data')
plt.title('Fitted Normal Distribution for ' + str(number_samples) + ' Force Plate Samples')
plt.xlabel('Value')
plt.ylabel('Probability of Value')

space_x_FP = np.linspace(start=-3, stop=3, num=10000)
space_y_FP = norm.pdf(space_x_FP, loc=mu, scale=std)
plt.plot(space_x_FP, space_y_FP, label='Ideal Normal Distribution of Force Plate Data')
plt.legend()
plt.show()

#ACCELERATION NORMAL DISTRIBUTION VS IDEAL DISTRIBUTION
#change acceleration data from pandas to numpy
ACCEL_Samples_numpy = df['accelerometer_rsi'].to_numpy()
#Doing the same here as what was done with the force plate data
#Making normal distribution with those values
normal_samples_ACCEL = np.random.normal(loc=mu, scale=std, size=number_samples)
#Calculating the mean and standard deviation of that distribution
sample_mean_ACCEL = np.mean(normal_samples_ACCEL)
print('The actual mean for the acceleration data is ' + str(sample_mean_ACCEL))
sample_std_ACCEL = np.std(normal_samples_ACCEL)
print('The actual standard deviation for the acceleration data is ' + str(sample_std_ACCEL))

#Finding a probability distribution function
space_x_ACCEL = np.linspace(start=-3, stop=3, num=10000)
space_y_ACCEL = norm.pdf(space_x_ACCEL, loc=sample_mean_ACCEL, scale=sample_std_ACCEL)
#Plotting the distribution
plt.plot(space_x_ACCEL, space_y_ACCEL, label='Fitted Normal Distribution of Acceleration Data')
plt.title('Fitted Normal Distribution for ' + str(number_samples) + ' Acceleration Samples')
plt.xlabel('Value')
plt.ylabel('Probability of Value')

space_x_ACCEL = np.linspace(start=-3, stop=3, num=10000)
space_y_ACCEL = norm.pdf(space_x_ACCEL, loc=mu, scale=std)
plt.plot(space_x_ACCEL, space_y_ACCEL, label='Ideal Normal Distribution of Acceleration Data')
plt.legend()
plt.show()



"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), with the 10th bin encompassing [2,inf). An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

alpha = 0.05

"""
Acceleration
"""
### YOUR CODE HERE

#Creating 10 bins from 0 to 2
bins = np.linspace(0, 2, 9)  # Create 10 bins

#making the last bin go to infinity
bins = np.r_[-np.inf, bins, np.inf]

#Find the expected probability using the code from lecture example
expected_prob = np.diff(norm.cdf(bins, loc=mu, scale=std))

#Frequencey of each count (following lecture example)
expected_counts = expected_prob * len(ACCEL_Samples_numpy)

# putting the values in bins for the histogram
counts, edges = np.histogram(ACCEL_Samples_numpy, bins=bins, density=False)

# Conduct chi2 test
# Reduce the degrees of freedom as the normal distribution has two parameters
(chi_stat_ACCEL, p_value_ACCEL) = chisquare(f_obs=counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat for acceleration data: ', chi_stat_ACCEL, 'p-value for acceleration data: ', p_value_ACCEL)

if p_value_ACCEL < alpha:
    print('Reject null hypothesis. ACCEL Counts are not equal.')
else:
    print('Accept null hypothesis. ACCEL Counts are equal')

"""
Force Plate
"""
### YOUR CODE HERE

#Creating 10 bins from 0 to 2
bins = np.linspace(0, 2, 9)  # Create 10 bins

#making the last bin go to infinity
bins = np.r_[-np.inf, bins, np.inf]

#Find the expected probability using the code from lecture example
expected_prob = np.diff(norm.cdf(bins, loc=mu, scale=std))

#Frequencey of each count (following lecture example)
expected_counts = expected_prob * len(FP_Samples_numpy)

# putting the values in bins for the histogram
counts, edges = np.histogram(FP_Samples_numpy, bins=bins, density=False)

# Conduct chi2 test
# Reduce the degrees of freedom as the normal distribution has two parameters
(chi_stat_FP, p_value_FP) = chisquare(f_obs=counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat for force plate data: ', chi_stat_FP, 'p-value for force plate data: ', p_value_FP)

if p_value_FP < alpha:
    print('Reject null hypothesis. FP Counts are not equal.')
else:
    print('Accept null hypothesis. FP Counts are equal')

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE
#Want to determine if the means of accel and fp are equivalent so this is a 2-sample t test

(stat_2Sample_Test, p_value_2Sample_Test) = ttest_ind(normal_samples_FP, normal_samples_ACCEL, alternative='two-sided')
print('The calculated p value from the 2 sample test is ' + str(p_value_2Sample_Test))
if p_value_2Sample_Test < alpha:
    print('Reject hypothesis, sample means are not equal')
else:
    print('Accept hypothesis, sample means are equivalent')

"""
Question 4 (Bonus): Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE
#Calculating error between the force plate and acceleration data as per lecture slide examples
error = FP_Samples_numpy - ACCEL_Samples_numpy
plt.hist(error, bins=16, label='RSI ACCEL and FP Error')
plt.xlabel('RSI Error')
plt.ylabel('Counts')
plt.title('RSI Error Distribution')

#FIT THE ERROR TO A NORMAL DISTRIBUTION
(fitted_mean, fitted_std) = norm.fit(error)
plt.show()