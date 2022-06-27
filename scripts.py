from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import Schoolkid


def get_kid_by_name(kid_name: str) -> Schoolkid:
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('There is several students with this name.')
        print('Please, specify the name.')
        exit(1)
    except ObjectDoesNotExist:
        print('There is no student with such name.')
        exit(1)
    else:
        return kid


def fix_marks(kid_name: str):
    from datacenter.models import Mark
    schoolkid = get_kid_by_name(kid_name)
    target_kid_bad_marks = Mark.objects.filter(schoolkid=schoolkid,
                                               points__in=[2, 3])
    for bad_mark in target_kid_bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(kid_name: str):
    from datacenter.models import Chastisement
    schoolkid = get_kid_by_name(kid_name)
    target_kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    target_kid_chastisements.delete()


def create_commendation(kid_name: str, subject_name: str):
    import random
    from datacenter.models import Lesson, Commendation
    schoolkid = get_kid_by_name(kid_name)
    target_class_subj_lesson = Lesson.objects \
        .filter(year_of_study=6,
                group_letter='А',
                subject__title=subject_name) \
        .order_by('-date').first()
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
    Commendation.objects.create(text=random.choice(praise_lines),
                                created=date, schoolkid=schoolkid,
                                subject=subject,
                                teacher=teacher)
