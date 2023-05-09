import os
import sys
from csv import DictWriter

_cur_dir = os.path.dirname(os.path.realpath(__file__))
_par_dir = os.path.join(_cur_dir, os.path.pardir)
if _par_dir not in sys.path:
    sys.path.append(_par_dir)


def update_dict_recursively(dest, updated):
    """
    Update dictionary recursively.
    :param dest: Destination dict.
    :type dest: dict
    :param updated: Updated dict to be applied.
    :type updated: dict
    :return:
    """
    for k, v in updated.items():
        if isinstance(dest, dict):
            if isinstance(v, dict):
                r = update_dict_recursively(dest.get(k, {}), v)
                dest[k] = r
            else:
                dest[k] = updated[k]
        else:
            dest = {k: updated[k]}
    return dest


def number_to_ordinal(n):
    """
    Convert number to ordinal number string
    """
    return "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])


def write_csv(data, path):
    with open(path, 'w') as outfile:
        writer = DictWriter(outfile, list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
