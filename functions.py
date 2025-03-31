import random as rnd
from variables import *
from names_generator import generate_name


def hashed(val):
    total = 0
    while val > 10:
        total += val%10
        val //= 10
    return total%50

def add_cnp(val, name):
    key = (val%1000)//10
    if key not in data.keys():
        data[key] = []
    if key not in names.keys():
        names[key] = []
    hsh = hashed(val)
    while len(data[key]) < hsh+1:
        data[key].append([])
    while len(names[key]) < hsh+1:
        names[key].append([])
    found, _ = search(val)
    if found[0] == -1:
        data[key][hsh].append(val)
        names[key][hsh].append(name)
        return 1
    else:
        return 0

def remove(val):
    found, _ = search(val)
    if found[0] != -1:
        data[found[0]][found[1]].pop(found[2])
        names[found[0]][found[1]].pop(found[2])
        return 1
    return 0

def search(val):
    itr = 0
    key = (val%1000)//10
    hsh = hashed(val)
    for i in range(0, len(data[key][hsh])):
        itr += 1
        if data[key][hsh][i] == val:
            return [key, hsh, i], itr
    return [-1, -1, -1], -1

def generate_cnp():
    year = rnd.randint(1945, 2011)
    month = rnd.randint(1, 12)
    day = rnd.randint(1, months_days[month-1])
    gender = rnd.randint(1, 2) + (4 if year >= 2000 else 0)
    county = rnd.choice(counties[1:])
    population[county] -= 1
    if population[county] < 1:
        counties.remove(county)
    num = rnd.randint(0, 999)
    cnp = gender*(10**11) + (year%100)*(10**9) + month*(10**7) + day*(10**5) + county*(10**3) + num
    digits_sum = 0
    n = cnp
    c = const
    while n > 0:
        digits_sum += (n%10)*(c%10)
        n //= 10
        c //= 10
    cnp *= 10
    if digits_sum%11 == 10:
        cnp += 1
    else:
        cnp += digits_sum%11
    name = generate_name(style = 'capital')
    add_cnp(cnp, name)
    the_keys.append((cnp%1000)//10)
    return cnp, name

def thousand_search():
    itr_sum = 0
    min_itr = 1000001
    max_itr = 0
    for n in range(1000):
        rnd_key = rnd.choice(the_keys)
        list_length = len(data[rnd_key])
        idx = rnd.randint(0, list_length-1)
        if len(data[rnd_key][idx]) < 1:
            for i in range(idx, list_length):
                if len(data[rnd_key][i]) > 0:
                    idx = i
        cnp = rnd.choice(data[rnd_key][idx])
        print(f"{n+1}) Searching {cnp} ...")
        found, itr = search(cnp)
        print('Value found at:')
        print(f"            key - {found[0]}")
        print(f"     main index - {found[1]}")
        print(f"      sub index - {found[2]}")
        print(f"           name - {names[found[0]][found[1]][found[2]]}")
        print(f"     iterations - {itr}")
        if itr < min_itr:
            min_itr = itr
        if itr > max_itr:
            max_itr = itr
        itr_sum += itr
        print('\n')
    return itr_sum, min_itr, max_itr, itr_sum//1000