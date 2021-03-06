# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

import yaml
from pprint import pprint
from draw_network_graph import draw_topology

def transform_topology(yaml_topology_file):
    topology_dict = {}
    with open(yaml_topology_file, encoding = 'UTF-8') as f:
        from_yaml_dict = yaml.safe_load(f)
    for key, value in from_yaml_dict.items():
        topology_dict.update({ (key, k): (kk, vv) for k, v in value.items() for kk, vv in v.items() })
    a = set(topology_dict.keys())
    b = set(topology_dict.values())
    c = list(a | b)
    topology_dict_new = {}
    for d in c:
        if d not in topology_dict_new.values():
            topology_dict_new.update({d: topology_dict[d]})
    draw_topology(topology_dict_new)
    return topology_dict

#testing
if __name__ == '__main__':
    pprint(transform_topology('topology.yaml'))