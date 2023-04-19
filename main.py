import random
from datacenter_api import *


if __name__ == '__main__':
    full_name = 'Иванов Иван'
    subject_title = 'Музыка'
    schoolkid = find_schoolkid(full_name)
    if not schoolkid:
        exit()
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(full_name, subject_title)
