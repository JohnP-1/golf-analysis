import pandas as pd
import numpy as np
import seaborn as sns
import os.path as path
import matplotlib.pyplot as plt


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
        shots = pd.DataFrame([], columns=['Date', 'Club', 'Club Speed (MPH)', 'Ball-Speed (MPH)', 'Smash Factor', 'Total (yard)'])
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
            text_input = get_input('Give the index of the club you would like to remove: ')

            try:
                clubs = clubs.drop([int(text_input)])
                clubs.to_csv(path.join(data_path, 'clubs.csv'), index=False)
            except:
                text_input = get_input('Index not valid! Enter command to execute (hint: type \"help\" for more information): ')
            text_input = get_input('Enter command to execute (hint: type \"help\" for more information): ')


        elif text_input == 'input shot':
            data = []
            text_input = get_input('Enter date: ')
            data.append(text_input)
            text_input = get_input('Enter club: ')
            data.append(text_input)
            text_input = get_input('Enter the club speed (MPH): ')
            data.append(float(text_input))
            text_input = get_input('Enter the ball-speed (MPH): ')
            data.append(float(text_input))
            text_input = get_input('Enter smash factor: ')
            data.append(float(text_input))
            text_input = get_input('Enter club total distance(yards): ')
            data.append(float(text_input))

            shots = pd.read_csv(path.join(data_path, 'shots.csv'))
            data_temp = pd.DataFrame([data], columns=shots.columns)

            try:
                shots = pd.concat([shots, data_temp], axis=0).reset_index(drop=True)
                shots.to_csv(path.join(data_path, 'shots.csv'), index=False)
            except:
                print('Shot already entered')
                text_input = get_input('Enter command to execute (hint: type \"help\" for more information): ')

        elif text_input == 'analyse distances':
            clubs = pd.read_csv(path.join(data_path, 'clubs.csv'))
            clubs = clubs.rename(columns={"Name": "Club"})
            shots = pd.read_csv(path.join(data_path, 'shots.csv'))
            shots['Date'] = pd.to_datetime(shots['Date'])
            data = pd.merge(clubs, shots, on='Club')

            text_input = get_input('Enter clubs to analyse (separate clubs with a \",\"):')
            if ',' not in text_input:
                if text_input == 'all':
                    club_list = list(data['Club'].unique())
                else:
                    club_list = [text_input]
            else:
                club_list = text_input.strip(' ').split(',')

            data = data[data['Club'].isin(club_list)]

            print(data.dtypes)

            text_input = get_input('Enter date range to analyse (separate clubs with a \",\"):')

            # print(text_input)

            if text_input != 'None':
                date = pd.to_datetime(text_input)
                data = data[data['Date']==date]

            fig, axes = plt.subplots(2, 2, figsize=(18, 18))
            fig.suptitle('Shot Statistics')

            sns.boxplot(data=data, x="Club", y="Total (yard)", ax=axes[0, 0])
            sns.swarmplot(data=data, x='Club', y='Total (yard)', color="grey", ax=axes[0, 0])

            sns.boxplot(data=data, x="Club", y="Club Speed (MPH)", ax=axes[0, 1])
            sns.swarmplot(data=data, x='Club', y='Club Speed (MPH)', color="grey", ax=axes[0, 1])

            sns.boxplot(data=data, x="Club", y="Ball-Speed (MPH)", ax=axes[1, 0])
            sns.swarmplot(data=data, x='Club', y='Ball-Speed (MPH)', color="grey", ax=axes[1, 0])

            sns.boxplot(data=data, x="Club", y="Smash Factor", ax=axes[1, 1])
            sns.swarmplot(data=data, x='Club', y='Smash Factor', color="grey", ax=axes[1, 1])

            plt.show()

            fig, axes = plt.subplots(2, 2, figsize=(18, 18))
            fig.suptitle('Shot Statistics')

            sns.scatterplot(data=data, x="Club Speed (MPH)", y="Total (yard)", hue="Club", ax=axes[0, 0])
            # sns.regplot(data=data, x="Club Speed (MPH)", y="Total (yard)", hue="Club", ax=axes[0, 0])
            sns.scatterplot(data=data, x="Ball-Speed (MPH)", y="Total (yard)", hue="Club", ax=axes[0, 1])
            sns.scatterplot(data=data, x="Smash Factor", y="Total (yard)", hue="Club", ax=axes[1, 0])

            # sns.boxplot(data=data, x="Club", y="Smash Factor",, hue="Club", ax=axes[1, 1])

            plt.show()


        else:
            text_input = get_input('Input not recognised, please enter a different command to execute (hint: type \"help\" for more information): ')


if __name__ == "__main__":
    main()


