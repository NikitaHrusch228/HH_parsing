import json
import os
import random
from datetime import date, timedelta
from random import sample

import numpy as np
import pandas as pd
import requests
from dateutil.parser import parse
from sqlalchemy import engine as sql

########################################################################################################################
# Создаем списки для столбцов таблицы vacancies
IDs = []  # Список идентификаторов вакансий
names = []  # Список наименований вакансий
descriptions = []  # Список описаний вакансий
salary_from = []  # Заработная плата низ
salary_to = []  # Заработная плата верх
currency = []  # Валюта
open_time = []  # Дата открытия вакансии
sum_time = []  # Общее время, которое висит вакансия в днях
employment = []  # Занятость
status = []  # Статус вакансии
employer_name = []  # Компания name
employer_id = []  # Компания id
cities = []  # Город с вакансией
emp_login = []
emp_password = []
########################################################################################################################
# Создаем списки для столбцов таблицы skills
skills_vac = []  # Список идентификаторов вакансий
skills_name = []  # Список названий навыков
########################################################################################################################
# Создадим списки для распределения на секции
it_skills = ["Анализ данных", "SQL", "Python", "MS Visio", "MS SQL", "Power Query", "C++", "C", "C#", "Postgresql",
             "Java", "JavaScript"]
lang_skills = ["Английский язык", "Немецкий язык", "Французский язык", "Испанский язык", "Итальянский язык",
               "Китайский язык"]
########################################################################################################################
# Создаем списки для столбцов таблицы applicants
applicant_id = []  # id искателя
login = []  # Генерируемый логин
password = []  # Генерируемый пароль
email = []  # Email
phone_number = []  # Номер телефона
SNP = []  # Фамилия Имя Отчество
resume_id = []  # id резюме
work_exp = []  #
sex = []  # Пол
########################################################################################################################
# Создаём списки для подписки subscription
sub_appl = []
sub_empl = []
price = []
########################################################################################################################
# Создаём списки для подписки marks
marks_appl = []
marks_empl = []
size = []
comment = []
########################################################################################################################
# Создаём списки для опыта работы
work_exp_app_id = []
work_exp_interval_st = []
work_exp_interval_end = []
work_exp_company = []
work_exp_posit = []
########################################################################################################################
# Создаём списки для таблицы соответствия резюме и навыков
resume_id_cv = []
skill_id_cv = []
cv_skills_id = []
########################################################################################################################
# Создаём списки для столбцов работадателей
com_id = []
com_name = []
com_description = []
com_alternate_url = []
com_area_name = []
########################################################################################################################
#  Списки для резюме и навыков
res_skill_id = []
res_skill = []
########################################################################################################################
# Списки резюме
resume_id_app = []
resume_cr_data = []
########################################################################################################################
# Списки для откликов
response_app_id = []
response_vac_id = []
response_cr_time = []
########################################################################################################################
# Списки фамилий имён отчеств:
# Мужчины
men = [
    'Алексеев Глеб Миронович',
    'Бирюков Алексей Сергеевич',
    'Бобров Демид Иванович',
    'Борисов Дмитрий Алексеевич',
    'Васильев Илья Ильич',
    'Вишневский Владислав Денисович',
    'Галкин Александр Михайлович',
    'Головин Макар Александрович',
    'Головин Артём Арсеньевич',
    'Давыдов Даниил Маркович',
    'Егоров Савелий Дмитриевич',
    'Егоров Андрей Маркович',
    'Ерофеев Дмитрий Николаевич',
    'Журавлев Герман Фёдорович',
    'Зверев Артём Алексеевич',
    'Зуев Владислав Евгеньевич',
    'Ильин Никита Александрович',
    'Казаков Игорь Родионович',
    'Касаткин Артём Дмитриевич',
    'Ковалев Ярослав Иванович',
    'Костин Григорий Ильич',
    'Котов Александр Егорович',
    'Круглов Фёдор Владимирович',
    'Кузьмин Дмитрий Александрович',
    'Лебедев Тимур Александрович',
    'Лукьянов Михаил Михайлович',
    'Медведев Константин Михайлович',
    'Мешков Александр Маркович',
    'Михайлов Максим Михайлович',
    'Панкратов Савелий Глебович',
    'Пахомов Антон Даниилович',
    'Поляков Савелий Иванович',
    'Пономарев Андрей Иванович',
    'Попов Семён Дмитриевич',
    'Сальников Лев Денисович',
    'Сафонов Константин Михайлович',
    'Сергеев Алексей Лукич',
    'Смирнов Александр Артёмович',
    'Сорокин Фёдор Александрович',
    'Терехов Демид Даниилович',
    'Титов Георгий Глебович',
    'Ткачев Гордей Алексеевич',
    'Ульянов Даниил Даниилович',
    'Филимонов Матвей Ильич',
    'Филиппов Михаил Николаевич',
    'Фомин Иван Егорович',
    'Чернов Арсений Александрович',
    'Черняев Максим Павлович',
    'Швецов Антон Евгеньевич',
    'Шульгин Артём Максимович'
]
# Женщины
women = [
    'Анисимова Александра Евгеньевна',
    'Антонова Алина Артуровна',
    'Антонова Милана Тимофеевна',
    'Афанасьева Мария Львовна',
    'Белова Варвара Артёмовна',
    'Беляева Виктория Фёдоровна',
    'Борисова Алёна Ивановна',
    'Власова Кира Максимовна',
    'Волошина Юлия Максимовна',
    'Горшкова Диана Владимировна',
    'Дроздова Анастасия Михайловна',
    'Ермолова Вероника Фёдоровна',
    'Золотарева Дарья Михайловна',
    'Иванова Кира Дмитриевна',
    'Иванова Арина Глебовна',
    'Ильина Елизавета Данииловна',
    'Карпова Екатерина Никитична',
    'Ковалева Маргарита Глебовна',
    'Кольцова Анна Максимовна',
    'Королева Василиса Степановна',
    'Кулагина Арина Ивановна',
    'Кулешова София Дмитриевна',
    'Кулешова Светлана Данииловна',
    'Ларионова Варвара Елисеевна',
    'Латышева Дарина Владимировна',
    'Лебедева Дарья Кирилловна',
    'Лебедева Кристина Гордеевна',
    'Мешкова Дарья Владимировна',
    'Михайлова Антонина Тимофеевна',
    'Михайлова Яна Сергеевна',
    'Моисеева Александра Андреевна',
    'Осипова Полина Максимовна',
    'Осипова Милана Александровна',
    'Панова Виктория Андреевна',
    'Панова Алина Павловна',
    'Попова Елизавета Алексеевна',
    'Попова Анна Егоровна',
    'Скворцова Полина Леонидовна',
    'Смирнова София Егоровна',
    'Суворова Юлия Дмитриевна',
    'Тарасова Милана Максимовна',
    'Третьякова Варвара Александровна',
    'Федосеева Виктория Демьяновна',
    'Федотова София Кирилловна',
    'Филатова Мария Георгиевна',
    'Харитонова Мирослава Ильинична',
    'Хохлова Алиса Алексеевна',
    'Шевелева Василиса Павловна',
    'Шестакова Анна Фёдоровна',
    'Щербакова Алиса Всеволодовна']
# Списки для генерации паролей / Длина пароля будет 8 символов
alphabet = 'abcdefghijklmnopqrstuvwxyz'
########################################################################################################################
# Данные массивы созданы для сортировки данных перед загрузкой их в бд - сортируются и убираются дупликаты

numeric_arr = []
arr_for_ind = []

# В выводе будем отображать прогресс
# Для этого узнаем общее количество файлов, которые надо обработать
# Счетчик обработанных файлов установим в ноль
cnt_docs = len(os.listdir('C:/pythonProject1/pythonProject/vacancies'))
arr_url = []
i = 0
# Проходимся по всем файлам в папке vacancies
for fl in os.listdir('C:/pythonProject1/pythonProject/vacancies/'):

    # Открываем, читаем и закрываем файл
    f = open('C:/pythonProject1/pythonProject/vacancies/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()

    # Текст файла переводим в справочник
    jsonObj = json.loads(jsonText)

    if 'errors' not in jsonObj.keys():
        arr_url.append(jsonObj['employer']['url'])

    # Заполняем списки для таблиц
    if 'errors' not in jsonObj.keys():

        IDs.append(int(jsonObj['id']))
        names.append(jsonObj['name'])
        descriptions.append(jsonObj['description'])

        cities.append(jsonObj['area']['name'])

        employer_name.append(jsonObj['employer']['name'])
        employer_id.append(int(jsonObj['employer']['id']))

        date_time_obj = parse(jsonObj['published_at'])
        open_time.append(parse(jsonObj['published_at']).date())
        sum_time.append((date.today() - parse(jsonObj['published_at']).date()).days)

        status.append(jsonObj['type']['id'])
        employment.append(jsonObj['employment']['name'])

        if jsonObj['salary'] is not None:
            salary_from.append(jsonObj['salary']['from'])
            salary_to.append(jsonObj['salary']['to'])
            currency.append((jsonObj['salary']['currency']))
        else:
            currency.append(None)
            salary_from.append(None)
            salary_to.append(None)
    # Т.к. навыки хранятся в виде массива, то проходимся по нему циклом
    if 'errors' not in jsonObj.keys():

        for skl in jsonObj['key_skills']:
            skills_vac.append(int(jsonObj['id']))
            skills_name.append(skl['name'])

    i += 1

page = 0
params = {'page': page}

for urk in arr_url:
    req = requests.get(urk, params)
    data = req.content.decode()
    req.close()

    jsObj = json.loads(data)

    nextFileName = 'C:/pythonProject1/pythonProject/cur_emp/{}.json'.format(
        len(os.listdir('C:/pythonProject1/pythonProject/cur_emp')))

    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    for fl in os.listdir('C:/pythonProject1/pythonProject/cur_emp'):
        f = open('C:/pythonProject1/pythonProject/cur_emp/{}'.format(fl), encoding='utf8')
        jsonText = f.read()
        f.close()

        jsonObj = json.loads(jsonText)

        if 'errors' not in jsonObj.keys():
            com_id.append(int(jsonObj['id']))
            com_name.append(jsonObj['name'])
            com_description.append(jsonObj['description'])
            com_alternate_url.append(jsonObj['alternate_url'])
            com_area_name.append(jsonObj['area']['name'])

# Обработка дупликатов
unique_numbers = set(com_id)
for number in unique_numbers:
    numeric_arr.append(number)

for x in numeric_arr:
    s = com_id.index(x)
    arr_for_ind.append(s)

l = len(com_id)

for j in range(l - 1, -1, -1):
    if j not in arr_for_ind:
        com_id.pop(j)
        com_name.pop(j)
        com_alternate_url.pop(j)
        com_description.pop(j)
        com_area_name.pop(j)

total_subscribers = []

for i in range(len(com_area_name)):
    total_subscribers.append(random.randint(1, 100000))

########################################################################################################################
# Соискатели
amount = random.randint(1, 100)

second_part = []
name_part = []

for i in range(amount):
    y = random.randint(1000000, 9999999)
    while y in applicant_id:
        y = random.randint(1000000, 9999999)
    applicant_id.append(int(y))
    work_exp.append(int(y))

    # Добавление ФИО и пола
    s = random.randint(1, 3)

    if s == 1:
        g = random.choice(men)
        SNP.append(g)
        sex.append(s)

    if s == 2:
        g = random.choice(women)
        SNP.append(g)
        sex.append(s)

    if s == 3:
        r = random.choice([1, 2])

        if r == 1:
            g = random.choice(men)
            SNP.append(g)

        if r == 2:
            g = random.choice(women)
            SNP.append(g)

        sex.append(s)

    # Обработка логина
    k = random.randint(0, 1000)
    while k in name_part:
        k = random.randint(0, 1000)

    lines = g.split()
    login.append(lines[0][0] + lines[1][0] + lines[2][0] + str(k))

    # Создание пароля

    pass_piece = random.sample(range(0, 9), 6)

    word_amount = random.randint(0, len(pass_piece))

    for m in range(word_amount):
        d = random.randint(0, len(pass_piece) - 1)

        pass_piece[d] = random.choice(alphabet)
    cur_str = ''
    for j in range(len(pass_piece)):
        cur_str = cur_str + str(pass_piece[j])
    password.append(cur_str)

    # Создание логина
    email.append(cur_str + '@mail.com')

    # Создание номера телефона
    ph = random.randint(0, 999999999) + 89000000000
    while ph in phone_number:
        ph = random.randint(0, 999999999) + 89000000000
    phone_number.append(ph)

    # Создание id для резюме
    p = random.randint(1000000, 9999999)
    while p in resume_id:
        p = random.randint(1000000, 9999999)
    resume_id.append(int(p))

    #  Подумать как соединить список подписок
    # follow_list.append([])

########################################################################################################################
# Подписка
price_array = [100, 1500, 30000]

for i in range(len(com_id)):
    sub_empl.append(com_id[i])
    sub_appl.append(random.choice(applicant_id))
    price.append(random.choice(price_array))
########################################################################################################################
# Резюме
resume_id_app = resume_id

# Создание даты
d1 = date(1990, 1, 1)
d2 = date(2023, 1, 1)

date_d = d2 - d1
total_days = date_d.days
random.seed(a=None)
for j in range(len(resume_id)):
    randay = random.randrange(total_days)
    resume_cr_data.append(d1 + timedelta(days=randay))
########################################################################################################################
# Опыт работы
ssk = random.randint(1, len(applicant_id))

for j in range(ssk):
    d1_s = date(1990, 1, 1)
    d1_e = date(2010, 1, 1)

    d2_s = date(2010, 1, 1)
    d2_e = date(2023, 1, 1)

    dates_bet_1 = d1_e - d1_s
    dates_bet_2 = d2_e - d2_s

    total_days_1 = dates_bet_1.days
    total_days_2 = dates_bet_2.days

    random.seed(a=None)

    randay_1 = random.randrange(total_days_1)
    randay_2 = random.randrange(total_days_2)

    work_exp_app_id.append(random.choice(applicant_id))
    work_exp_company.append(random.choice(employer_name))
    work_exp_posit.append(random.choice(names))

    work_exp_interval_st.append(d1_s + timedelta(days=randay_1))
    work_exp_interval_end.append(d2_s + timedelta(days=randay_2))

########################################################################################################################
#  Навыки
timer = np.unique(skills_name)
skills_name_for_id = []
skills_section = []

for i in range(len(timer)):

    skills_name_for_id.append(timer[i])

    if timer[i] in it_skills:
        skills_section.append('IT')

    if timer[i] in lang_skills:
        skills_section.append('Language')

    if timer[i] not in it_skills and timer[i] not in lang_skills:
        skills_section.append('Another')
########################################################################################################################
#  Оценка
h = random.randint(1, 1000)

for i in range(h):
    marks_appl.append(random.choice(applicant_id))
    marks_empl.append(random.choice(com_id))
    size.append(round(random.uniform(0, 5), 1))
    comment.append('Пока пустая строка')
########################################################################################################################
#  Склейка резюме скиллов и резюме id
#  Генерируем случайное число - количество навыков для данного резюме
for t in range(len(resume_id_app)):
    num = random.randint(1, 10)

    buffer = []

    for _ in range(num):

        hu = random.choice(skills_name_for_id)
        while hu in buffer:
            hu = random.choice(skills_name_for_id)
        buffer.append(hu)
        res_skill.append(hu)
        res_skill_id.append(resume_id_app[t])
########################################################################################################################
# Отклики
# Будем придерживаться правила, что для соответствующего соискателя отклик не может возникнуть чем время создания резюме
# ,так как наличие резюме является необходимым условием для отклика

o = random.randint(1, 3)
response_app_id_test = sample(applicant_id, o)  # Возвращает без дупликатов
response_vac_id_test = sample(IDs, o)

response_resume = []
response_time = 0
current_date = date.today()

for j in range(o):
    # x = random.randint(1, 3)
    x = 1
    buffer = []
    for i in range(x):
        v = random.choice(response_vac_id_test)

        while v in buffer:
            v = random.choice(response_vac_id_test)

        buffer.append(v)
        response_app_id.append(response_app_id_test[j])
        response_vac_id.append(v)

        response_resume.append(resume_id[applicant_id.index(response_app_id_test[j])])
        # Время после которого можно создать даты отклика
        response_time = resume_cr_data[resume_id_app.index(resume_id[applicant_id.index(response_app_id_test[j])])]

        date_diff = current_date - response_time
        amount_of_days = date_diff.days
        random.seed(a=None)

        ran = random.randrange(amount_of_days)
        response_cr_time.append(response_time + timedelta(days=ran))
########################################################################################################################
#  Добиваем список откликов и скиллов в таблицу вакансий
response_sum = [0] * len(IDs)
for j in range(len(response_vac_id)):
    response_sum[IDs.index(response_vac_id[j])] += 1

skills_for_vac = IDs
########################################################################################################################
for p in range(len(com_id)):
    emp_password.append(str(random.randint(100, 99999)) + random.choice(alphabet) + str(
        random.randint(100, 99999)) + random.choice(alphabet))
    emp_login.append(random.choice(alphabet) + str(random.randint(100000, 9999999999)))
########################################################################################################################
# Дозаполнение follow_list
follow_list = [' '] * len(applicant_id)

for k in range(len(sub_appl)):
    follow_list[applicant_id.index(sub_appl[k])] += str(names[employer_id.index(sub_empl[k])]) + ', '
########################################################################################################################
# Создадим соединение с БД
eng = sql.create_engine('postgresql://postgres:12345678@localhost/postgres')
conn = eng.connect()
########################################################################################################################
df = pd.DataFrame({'applicant_id': response_app_id, 'vacancy_id': response_vac_id,
                   'creation_time': response_cr_time})
df.to_sql('response', conn, schema='public', if_exists='append', index=True)
########################################################################################################################
df = pd.DataFrame(
    {'cv_id': res_skill_id, 'skill_name': res_skill}
)
df.to_sql('cv_skills', conn, schema='public', if_exists='append', index=True)
########################################################################################################################
df = pd.DataFrame(
    {'applicant_id': marks_appl, 'employer_id': marks_empl, 'value': size, 'comment': comment}
)
df.to_sql('marks', conn, schema='public', if_exists='append', index=True)
########################################################################################################################
df = pd.DataFrame(
    {'applicant_id': applicant_id, 'snp': SNP, 'sex': sex, 'login': login, 'password': password, 'email': email,
     'phone_number': phone_number,
     'cv_id': resume_id}
)
df.to_sql('applicants', conn, schema='public', if_exists='append', index=False)
########################################################################################################################
# Вакансии\vacancies
df = pd.DataFrame(
    {'vacancy_id': IDs, 'name': names, 'city': cities,
     'employer_id': employer_id, 'skills': IDs, 'open_time': open_time, 'existment_time': sum_time,
     'commitment_type': employment, 'salary_from': salary_from, 'salary_to': salary_to, 'currency': currency,
     'description': descriptions})
df.to_sql('vacancies', conn, schema='public', if_exists='append', index=False)

########################################################################################################################
# Навыки от вакансий\vac_skills
df = pd.DataFrame({'vacancy_id': skills_vac, 'skill_name': skills_name})  # + просто Id какой-то
df.to_sql('vac_skills', conn, schema='public', if_exists='append', index=True)
########################################################################################################################
# Работодатели\employers
df = pd.DataFrame(
    {'employer_id': com_id, 'company': com_name, 'login': emp_login, 'password': emp_password,
     'area_name': com_area_name, 'subscriptions_amount': total_subscribers})
df.to_sql('employers', conn, schema='public', if_exists='append', index=False)
########################################################################################################################
# Опыт работы\ work_exp
df = pd.DataFrame(
    {'applicant_id': work_exp_app_id, 'start_date': work_exp_interval_st, 'end_date': work_exp_interval_end,
     'company': work_exp_company})
df.to_sql('work_exp', conn, schema='public', if_exists='append', index=True)
########################################################################################################################
# Подписка\subscription
df = pd.DataFrame({'employer_id': sub_empl, 'applicant_id': sub_appl})
df.to_sql('subscription', conn, schema='public', if_exists='append', index=True)
########################################################################################################################
# Навыки \ skills
df = pd.DataFrame({'skill_name': skills_name_for_id, 'section': skills_section})
df.to_sql('skills', conn, schema='public', if_exists='append', index=False)
########################################################################################################################
# Резюме \ резюме
df = pd.DataFrame({'cv_id': resume_id_app, 'creation_date': resume_cr_data})
df.to_sql('cv', conn, schema='public', if_exists='append', index=False)
########################################################################################################################
# Закрываем соединение с БД
conn.close()
