from hh_parser import parse_vacances, save_vacances_to_csv

vacances = parse_vacances()

save_vacances_to_csv('test_parse.csv', vacances)