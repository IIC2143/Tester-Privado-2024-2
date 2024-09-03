import os
import sys
import json
from pathlib import Path

from test_1A import test_1A
from test_1B import test_1B
from test_1C import test_1C

from test_2A import test_2A
from test_2B import test_2B
from test_2C import test_2C

from test_3A import test_3A



def main():


    file_path = 'results.json'



    #tests = [test_1A,]

    tests = [
        test_1A, test_1B, test_1C,
        test_2A, test_2B, test_2C,
        test_3A, 
    ]

    #student_user = input('Enter student username: ')

    #if not os.path.exists(student_user):
    #    os.mkdir(student_user)
    all_results = {}

    for test in tests:
        results = test()
        #path = Path(student_user) / f'{test.__name__}.json'
        #with open(path, 'w') as f:
        #    json.dump(results, f, indent=4)


        all_results[test.__name__] = results

        #score = sum(results.values())
        #total = len(results)

        #print(f'{test.__name__}: {score}/{total}')

    #print(all_results["test_1C"])
    data = all_results
    new_data = {}

    totalCorrect = 0
    total = 0

    for key in data:
        #print(f'{key}:')
        count = 0
        for k in data[key]:
            if data[key][k][0] == True:
                count += 1
 
        #print(f'{count}/{len(data[key])}')
        new_data[key] = f'{count}'f'/{len(data[key])}'
        totalCorrect += count
        total += len(data[key])

    new_data['Total'] = f'{totalCorrect}/{total}'
    #print(f'Total: {totalCorrect}/{total}')
    #print(new_data)

    with open(file_path, 'w') as f:
        json.dump(new_data, f, indent=4)

if __name__ == '__main__':
    main()
