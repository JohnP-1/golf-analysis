import pandas as pd
import numpy as np
import seaborn as sns
import os.path as path


def get_data_path():
    return path.join(path.dirname(__file__), 'Data')


def get_input(input_text):

    return input(input_text)


def check_club_db():
    if path.exists(path.join(get_data_path(), 'clubs.csv')) is False:
        clubs = pd.DataFrame([], columns=['Name', 'Type', 'Brand', 'Model', 'Length', 'Loft', 'Lie'])
        clubs.to_csv(path.join(get_data_path(), 'clubs.csv'), index=False)


def check_shot_db():

    if path.exists(path.join(get_data_path(), 'shots.csv')) is False:
        shots = pd.DataFrame([], columns=['Date', 'Club', 'Club Speed (MPH)', 'Ball-Speed (MPH)', 'Smash Factor', 'Carry (yard)'])
        shots.to_csv(path.join(get_data_path(), 'shots.csv'), index=False)


def main():
    data_path = get_data_path()
    check_shot_db()
    check_club_db()
    exit_flag = False

    text_input = get_input('Enter command to execute (hint: type \"help\" for more information): ')

    while exit_flag is False:

        if text_input == 'help':
            print("Placeholder for help")
            text_input = get_input('Enter command to execute (hint: type \"help\" for more information): ')
        elif text_input == 'exit':
            exit_flag = True
        elif text_input == 'add club':
            data = []
            text_input = get_input('Enter club name: ')
            data.append(text_input)
            text_input = get_input('Enter club type: ')
            data.append(text_input)
            text_input = get_input('Enter the brand: ')
            data.append(text_input)
            text_input = get_input('Enter the model: ')
            data.append(text_input)
            text_input = get_input('Enter club length: ')
            data.append(float(text_input))
            text_input = get_input('Enter club loft: ')
            data.append(float(text_input))
            text_input = get_input('Enter club lie: ')
            data.append(float(text_input))

            clubs = pd.read_csv(path.join(data_path, 'clubs.csv'))
            data_temp = pd.DataFrame([data], columns=clubs.columns)

            try:
                clubs = pd.concat([clubs, data_temp], axis=0).reset_index(drop=True)
                clubs.to_csv(path.join(data_path, 'clubs.csv'), index=False)
            except:
                print('Club already in your bag')
                text_input = get_input('Enter command to execute (hint: type \"help\" for more information): ')

        elif text_input == 'remove club':
            clubs = pd.read_csv(path.join(data_path, 'clubs.csv'))
            print(clubs)
            text_input = get_input('Give the index of the club you would like to remove: ')

            try:
                clubs = clubs.drop([int(text_input)])
                clubs.to_csv(path.join(data_path, 'clubs.csv'), index=False)
            except:
                text_input = get_input('Index not valid! Enter command to execute (hint: type \"help\" for more information): ')
            text_input = get_input('Enter command to execute (hint: type \"help\" for more information): ')


        elif text_input == 'input shot':
            pass
        else:
            text_input = get_input('Input not recognised, please enter a different command to execute (hint: type \"help\" for more information): ')


if __name__ == "__main__":
    main()


