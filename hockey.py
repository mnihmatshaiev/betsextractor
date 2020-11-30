import common
from data_normalization.name.hockey import name_matcher
from data_filtering.name.hockey import filter_special_names, filter_special_events, filter_special_leagues


def normalize_file(input_file, output_file, append):
    common.normalize_file(input_file, output_file, append, name_matcher, ['league_name', 'date', 'event_type', 'owner', 'guest', 'score'])


def filter_file(input_file, output_file):
    common.filter_file(input_file, output_file, {'league_name': filter_special_leagues,
                                                 'event_type': filter_special_events,
                                                 'owner': filter_special_names,
                                                 'guest': filter_special_names},
                       ['event_type'])
