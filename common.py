import pandas as pd
from data_normalization.score import score_matcher
from data_normalization.time import time_matcher_default
import string


def check_len(line):
    if len(line.split(',')) != 3:
        return False
    return True


def normalize_table(old_data, teams_normalization_func, columns_order):
    data = old_data.copy(deep=True)
    print(f'Delete NaN')
    data = data.dropna(axis=0)

    print(f'Update time')
    data['date'] = data['date'].map(time_matcher_default)

    print(f'Get teams')
    data['teams'] = data['teams'].map(teams_normalization_func)
    data = data[data.teams != False]
    data = data[data.teams.map(check_len) != False]
    data[['event_type', 'owner', 'guest']] = data['teams'].str.split(',', expand=True)
    data = data.drop(columns=['teams'])

    print(f'Update scores')
    data['score'] = data['score'].map(score_matcher)
    data = data[data.score != False]

    print(f'Reindex data')
    data = data.reindex(columns=columns_order)
    data = data.drop_duplicates()
    return data


def normalize_file(input_file, output_file, append, teams_normalization_func, columns_order):
    print(f'Read file')
    data = pd.read_csv(input_file, names=['league_name', 'date', 'teams', 'score'], sep=';')
    new_data = normalize_table(data, teams_normalization_func, columns_order)

    print(f'Write to file')
    if append:
        new_data.to_csv(output_file, index=False, mode='a', header=False, float_format='%.6f')
    else:
        new_data.to_csv(output_file, index=False, float_format='%.6f')


def filter_table(data, key_to_filter_func, keys_to_drop):
    for key in key_to_filter_func:
        print(f'Filter {key}')
        data = data[data[key].map(key_to_filter_func[key]) == True]

    print(f'Drop columns')
    data = data.drop(columns=keys_to_drop)
    return data


def filter_file(input_file, output_file, key_to_filter_func, keys_to_drop):
    print(f'Read file')
    data = pd.read_csv(input_file, header=0)
    new_data = filter_table(data, key_to_filter_func, keys_to_drop)
    print(f'Write to file')
    new_data.to_csv(output_file, index=False, float_format='%.6f')


def select_for_owner(data, owner_name):
    new_data = data.copy(deep=True)
    new_data_ex = new_data.loc[new_data['owner'] == owner_name]
    new_data_full = new_data.loc[(new_data['owner'] == owner_name) | (new_data['guest'] == owner_name)]
    return new_data_ex, new_data_full


def select_for_guest(data, guest_name):
    new_data = data.copy(deep=True)
    new_data_ex = new_data.loc[new_data['guest'] == guest_name]
    new_data_full = new_data.loc[(new_data['owner'] == guest_name) | (new_data['guest'] == guest_name)]
    return new_data_ex, new_data_full


def select_from_file(input_file, owner_name, guest_name):
    print(f'Read file')
    data = pd.read_csv(input_file, header=0)

    print(f'Select owner')
    owner_data, owner_full_data = select_for_owner(data, owner_name)

    print(f'Select guest')
    guest_data, guest_full_data = select_for_guest(data, guest_name)

    print(f'Write to file')
    owner_short_name = owner_name.translate({ord(c): None for c in string.whitespace})
    guest_short_name = guest_name.translate({ord(c): None for c in string.whitespace})
    owner_data.to_csv(f'{owner_short_name}_owner.csv', index=False)
    owner_full_data.to_csv(f'{owner_short_name}_full.csv', index=False)
    guest_data.to_csv(f'{guest_short_name}_guest.csv', index=False)
    guest_full_data.to_csv(f'{guest_short_name}_full.csv', index=False)