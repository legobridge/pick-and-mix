import csv
import pprint
import random
import time


practice_items_file_path = 'practice_items_template.csv'


def read_practice_items():
    with open(practice_items_file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        practice_items_to_minutes_map = {item['practice item']: int(item['minutes to practice']) for item in reader}
    return practice_items_to_minutes_map


def print_welcome(practice_items_to_minutes_map):
    print('Items for Practice:')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(practice_items_to_minutes_map)


def run_practice_loop(practice_item_map_list):
    practice_over = False
    while not practice_over:
        next_practice_item = random.choice(practice_item_map_list)
        item_name = next_practice_item[0]
        item_minutes = next_practice_item[1]
        print('Next Practice Item -\n{} - {} minutes\n'.format(item_name, item_minutes))
        print('Press Enter/Return to start.')
        input()
        for i in range(60 * item_minutes, -1, -1):
            minutes = i // 60
            seconds = i % 60
            if seconds < 10:
                seconds = '0' + str(seconds)
            print('Time Remaining - {}:{}'.format(minutes, seconds), end="\r", flush=True)
            time.sleep(1)
        print('\a')
        continue_practice_response = input('Continue practice? (y/n)')
        if continue_practice_response.lower() != 'y':
            practice_over = True
            print('Bye!')
        else:
            print()


def practice():
    practice_items_to_minutes_map = read_practice_items()
    practice_item_map_list = list(practice_items_to_minutes_map.items())
    # print_welcome(practice_items_to_minutes_map)
    run_practice_loop(practice_item_map_list)


if __name__ == '__main__':
    practice()
