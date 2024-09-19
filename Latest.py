import numpy as np

import matplotlib.pyplot as plt

lions = np.array([15, 16, 17, 20, 19, 21, 23, 24, 25, 27])

elephants = np.array([50, 52, 54, 53, 55, 56, 57, 59, 60, 62])

zebras = np.array([100, 98, 95, 97, 96, 94, 95, 93, 92, 90])

def totalpop(species):

print(" total population for a species over 10 years : ")

return np.sum(species)

def avg_grow(species):

print(" the average yearly population growth for a species. :")

growth = np.diff(species)

avg_growth = np.mean(growth)

return avg_growth

sname = ['Lions', 'Elephants', 'Zebras']

sdata = [lions, elephants, zebras]

for sname, spec in zip(sname, sdata):

print(f"Total population of {sname} over 10 years: {totalpop(spec)}")

print(f"Average yearly population growth for {sname}: {avg_grow(spec):.2f}")

def yearly_grow(spec):

growth_rate = np.diff(spec) / spec[:-1] * 100

return growth_rate

for sname, spec in zip(sname, sdata):

growth_rate = yearly_grow(spec)

print(f"Yearly growth rate of {sname}: {growth_rate}")

years = np.arange(1, 11)

plt.figure(figsize=(10, 6))
plt.plot(years, lions, label='Lions', marker='o')

plt.plot(years, elephants, label='Elephants', marker='o')

plt.plot(years, zebras, label='Zebras', marker='o')

plt.xlabel('Year')

plt.ylabel('Population (in thousands)')

plt.title('Population Trends of Lions, Elephants, and Zebras Over 10 Years')

plt.legend()

plt.grid(True)

plt.show()

def highest_avg():

growth_rates = [avg_grow(lions), avg_grow(elephants), avg_grow(zebras)]

max_growth_index = np.argmax(growth_rates)

return sname[max_growth_index]

print(f"Species with the highest average growth rate: {highest_avg()}")

end_population = [lions[-1], elephants[-1], zebras[-1]]

plt.figure(figsize=(8, 5))

plt.bar(species_names, end_population, color=['gold', 'gray', 'black'])

plt.xlabel('Species')

plt.ylabel('Population at Year 10 (in thousands)')

plt.title('Total Population of Species at the End of 10 Years')

plt.show()
