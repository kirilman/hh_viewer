from parse_hh_data.parse import num_pages, resume
from parse_hh_data import download
from typing import Dict, List

def parse_vacances(area_id = '1255', specialization_id = '1.221', search_period = '30', num_pages = 1) -> List[Dict]:
    vacances = download.vacancy_search_page(area_id, specialization_id,search_period, num_pages)
    return vacances['items']

def save_vacances_to_csv(csv_name: str = 'hh.csv', vacances: List[Dict] = []):
    def to_line(vac, answer):
        for k,v in vac.items():
            if isinstance(v, dict):
                to_line(v, answer)
            else:
                if isinstance(v, list) and len(v) == 0:
                    answer[k] = None
                else:
                    answer[k] = v
    columns_names = set()

    # c = { for vac in vacances} 
    for vac in vacances:
        for key, v in vac.items():
            if isinstance(v, dict):
                for k_, v_ in v.items():
                    columns_names.add(k_)
            else:
                columns_names.add(key)
    
    print(len(columns_names))
    with open(csv_name,'w') as file:
        for vacancy in vacances:
            answer = {k:None for k in columns_names}
            to_line(vacancy, answer)
            for k,v in answer.items():
                file.write('{}={};'.format(k,v))
            file.write('\n')

