import numpy as np
import matplotlib.pyplot as plt
#jellybeans = 10,000
#create a population of 10,000 jellybeans that are between 1 gram and 10 grams
population = np.random.uniform(1,10,10000)
#create a method to get random samples
def get_sample_beans(sample_size=30, num_samples=100):
    sample_averages = []
    for x in range(num_samples):
     sample = np.random.choice(population, size=sample_size)
     sample_averages.append(np.average(sample))
    return sample_averages

#get the sampling distribution of the jellybeans(mean/average)

average_size = get_sample_beans(sample_size=30, num_samples=100)

plt.hist(average_size, bins=30, edgecolor="black")
plt.show()