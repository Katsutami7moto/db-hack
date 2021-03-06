import random

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import (Schoolkid, Mark, Chastisement, Lesson,
                               Commendation)


def get_kid_by_name() -> Schoolkid:
    while True:
        kid_name = input('Введите имя ученика: ')
        try:
            kid = Schoolkid.objects.get(full_name__contains=kid_name)
        except MultipleObjectsReturned:
            print('Существует несколько учеников с таким именем.')
            print('Пожалуйста, введите более точное имя.')
            continue
        except ObjectDoesNotExist:
            print('Ученика с таким именем не существует.')
            continue
        else:
            print(f'Ученик по имени "{kid.full_name}" найден.')
            return kid


def get_subject_last_lesson() -> Lesson:
    while True:
        subject_name = input('Введите название предмета: ').capitalize()
        class_number = int(input('Введите номер класса: '))
        class_letter = input('Введите букву класса: ').upper()
        target_class_subj_lesson = Lesson.objects.filter(
            year_of_study=class_number,
            group_letter=class_letter,
            subject__title=subject_name
        ).order_by('-date').first()
        if not target_class_subj_lesson:
            print('Урок не был найден. Введите верные данные.')
            continue
        else:
            return target_class_subj_lesson


def fix_marks():
    schoolkid = get_kid_by_name()
    Mark.objects.filter(
        schoolkid=schoolkid, points__in=[2, 3]
    ).update(points=5)
    print('Оценки исправлены.')


def remove_chastisements():
    schoolkid = get_kid_by_name()
    target_kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    target_kid_chastisements.delete()
    print('Замечания удалены.')


def create_commendation():
    schoolkid = get_kid_by_name()
    target_class_subj_lesson = get_subject_last_lesson()
    praise_lines = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    date = target_class_subj_lesson.date
    subject = target_class_subj_lesson.subject
    teacher = target_class_subj_lesson.teacher
    Commendation.objects.create(
        text=random.choice(praise_lines),
        created=date,
        schoolkid=schoolkid,
        subject=subject,
        teacher=teacher
    )
    print(f'Похвала к последнему уроку по предмету "{subject.title}" создана.')
