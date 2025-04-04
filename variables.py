data = {}
the_keys = []
names = {}
const = 279146358279
months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
script_path = __file__[:__file__.rfind('\\')+1]
population = [0,
              1.7, 2.2, 3.0, 3.1, 2.9,
              1.6, 2.0, 2.9, 1.4, 2.1,
              1.3, 1.5, 3.6, 3.5, 1.0,
              2.5, 3.1, 2.6, 1.4, 1.6,
              1.5, 1.9, 1.3, 4.1, 3.0,
              2.4, 1.2, 2.7, 2.4, 2.0,
              3.6, 1.7, 1.1, 2.1, 3.4,
              1.7, 3.5, 1.0, 1.9, 1.8,
              1.7, 9.0]
population_backup = population[:]
for i in range(1, len(population)):
    population[i] = int(population[i]*10000)
counties = list(range(0, 43))
