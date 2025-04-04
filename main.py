from variables import *
from functions import *
import time as t


def generate():
    start_time = t.time()
    population = population_backup
    with open(script_path+'cnp-uri.csv', 'w', newline = '') as csvfile:
        for _ in range(1000000):
            thingy = generate_cnp()
            csvfile.write(f"{thingy[0]}, {thingy[1]}\n")
    print(f"\nGeneration took {t.time() - start_time:2} seconds!\n")

print('Please wait until generation is finished...')
generate()
print('\nType \'help\' to see a list of commands\n')

cmd = ''
while True:
    cmd = input('Input Command: ')
    print('\n')
    if cmd == 'show cnp':
        for key, value in data.items():
            print(f"{key:3} - ", end = '')
            first = 1
            for i in range(0, len(data[key])):
                if len(data[key][i]) > 0:
                    print(f"{'' if first else '      '}{i+1:2}:{data[key][i]}")
                    first = 0
            print()
    elif cmd == 'show names':
        for key, value in names.items():
            print(f"{key:3} - ", end = '')
            first = 1
            for i in range(0, len(names[key])):
                if len(names[key][i]) > 0:
                    print(f"{'' if first else '      '}{i+1:2}:{names[key][i]}")
                    first = 0
            print()
    elif cmd == 'add':
        inpt = input('Input a 13 digit CNP: ')
        if inpt.isnumeric():
            if len(inpt) == 13:
                inpt = int(inpt)
                ad = add_cnp(inpt)
                if ad:
                    print(f"Added {inpt} to dictionary:")
                    key = inpt//10%1000
                    hsh = hashed(inpt)
                    print(f"           name - {names[key][hsh][len(data[key][hsh])-1]}")
                    print(f"            key - {key}")
                    print(f"     main index - {hsh}")
                    print(f"      sub index - {len(data[key][hsh])-1}")
                else:
                    print('Value already exists!!!')
            else:
                print('Input must be 13 digits long!!!')
        else:
            print('Input numbers only!!!')
    elif cmd == 'remove':
        inpt = input('Input a 13 digit CNP: ')
        if inpt.isnumeric():
            if len(inpt) == 13:
                rmv = remove(inpt)
                if rmv:
                    print(f"Removed {inpt} from dictionary!")
                else:
                    print('Value doesn\'t exist!!!')
            else:
                print('Input must be 13 digits long!!!')
        else:
            print('Input numbers only!!!')
    elif cmd == 'search':
        inpt = input('Input a 13 digit CNP: ')
        if inpt.isnumeric():
            if len(inpt) == 13:
                found, iterations = search(inpt)
                if found[0] == -1:
                    print('Value not found!!!')
                else:
                    print('Value found at:')
                    print(f"            key - {found[0]}")
                    print(f"     main index - {found[1]}")
                    print(f"      sub index - {found[2]}")
                    print(f"           name - {names[found[0]][found[1]][found[2]]}")
                    print(f"     iterations - {iterations}")
                print()
            else:
                print('Input must be 13 digits long!!!')
        else:
            print('Input numbers only!!!')
    elif cmd == 'thousand':
        thingy = thousand_search()
        print('Iterations info: ')
        print(f"    - total: {thingy[0]}")
        print(f"    - min: {thingy[1]}")
        print(f"    - max: {thingy[2]}")
        print(f"    - average: {thingy[3]}")
    elif cmd in ['generate', 'regenerate']:
        generate()
    elif cmd == 'help':
        print('Available commands:')
        print('                   \'help\' - brings up this help page')
        print('                   \'show cnp\' - shows a list all generated cnp')
        print('                   \'show names\' - shows a list of all names associated with a cnp')
        print('                   \'add\' - adds a CNP to the list, if input is valid and doesn\'t already exist\'')
        print('                   \'remove\' - removes a CNP from the list, if input is valid and already exists\'')
        print('                   \'search\' - searches for a CNP, if input is valid, and returns its exact location in the list')
        print('                   \'thousand\' - searched 1000 random CNP, showing the min, max, average and total iterations for those')
        print('                   \'generate/regenerate\' - generates a new list of CNP, which replaces the older list')
        print('                   \'quit/q/exit\' - exits the program')
        print('Anything else will be considered an invalid command, and will ask for your input again')
    elif cmd in ['quit', 'q', 'exit']:
        print('Goodbye')
        break
    else:
        print('Not a valid command!')
    print('\n')
