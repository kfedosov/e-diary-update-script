from datacenter.models import *


def find_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print(f'Ученик с именем "{full_name}" не найден')
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено несколько учеников с именем "{full_name}". Уточните запрос.')
        return None
    return schoolkid


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def get_lessons(schoolkid, subject_title):
    subject = Subject.objects.get(title=subject_title)
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject,
    )
    if not lessons:
        print(f'Уроков по предмету "{subject_title}" для ученика {schoolkid.full_name} не найдено')
        return None
    return lessons


def create_commendation(full_name, subject_title):
    schoolkid = find_schoolkid(full_name)
    if not schoolkid:
        return
    lessons = get_lessons(schoolkid, subject_title)
    if not lessons:
        return
    lesson = random.choice(lessons)
    Commendation.objects.create(
        text=random.choice([
            'Молодец!',
            'Отлично!',
            'Хорошо!',
            'Гораздо лучше, чем я ожидал!',
            'Ты меня приятно удивил!',
        ]),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        lesson=lesson,
    )
    print(f'Похвала для ученика {full_name} по предмету "{subject_title}" успешно добавлена')
