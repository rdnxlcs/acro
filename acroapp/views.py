from django.shortcuts import render

import datetime

import re
import emoji

mss = [
{
    'name': 'Коялис Сергей',
    'year': '2000',
    'photo': 'static/mss/koyalis.jpg',
}, {
    'name': 'Cергеенко Ирина',
    'year': '2000',
    'photo': 'static/mss/Сергеенко.jpg',
}, {
    'name': 'Ширяева Наталья',
    'year': '2000',
    'photo': 'static/mss/ширяева.jpg',
}, {
    'name': 'Кондратьева Екатерина',
    'year': '2001',
    'photo': 'static/mss/Кондратьева.jpg',
}, {
    'name': 'Казак Ольга',
    'year': '2004',
    'photo': 'static/mss/Казак.jpg',
}, {
    'name': 'Ремнева Александра',
    'year': '2004',
    'photo': 'static/mss/Ремнева.jpg',
}, {
    'name': 'Семенов Михаил',
    'year': '2005',
    'photo': 'static/mss/Семенов.jpg',
}, {
    'name': 'Комаров Денис',
    'year': '2005',
    'photo': 'static/mss/комаров.jpg',
}, {
    'name': 'Поляков Илья',
    'year': '2006',
    'photo': 'static/mss/Поляков.jpg',
}, {
    'name': 'Сазанова Ольга',
    'year': '2006',
    'photo': 'static/mss/Сазанова.jpg',
}, {
    'name': 'Кожикова Ольга',
    'year': '2006',
    'photo': 'static/mss/Кожикова.jpg',
}, {
    'name': 'Швиндт Марина',
    'year': '2006',
    'photo': 'static/mss/швиндт.jpg',
}, {
    'name': 'Левошук Виктор',
    'year': '2006',
    'photo': 'static/mss/левошук.jpg',
}, {
    'name': 'Воронкова Анастасия',
    'year': '2006',
    'photo': 'static/mss/воронкова.jpg',
}, {
    'name': 'Дюкарев Георгий',
    'year': '2007',
    'photo': 'static/mss/дюкарев.jpg',
}, {
    'name': 'Маршев Дмитрий',
    'year': '2008',
    'photo': 'static/mss/маршев.jpg',
}, {
    'name': 'Тяжкороб Владимир',
    'year': '2011',
    'photo': 'static/mss/тяжкороб.jpg',
}, {
    'name': 'Маршева Ирина',
    'year': '2012',
    'photo': 'static/mss/маршева.jpg',
}, {
    'name': 'Кузнецов Владислав',
    'year': '2013',
    'photo': 'static/mss/кузнецов.jpg',
}, {
    'name': 'Гостищев Константин',
    'year': '2015',
    'photo': 'static/mss/гостищев.jpg',
}, {
    'name': 'Беспалов Стефан',
    'year': '2015',
    'photo': 'static/mss/беспалов.jpg',
}, {
    'name': 'Авакян Артур',
    'year': '2015',
    'photo': 'static/mss/авкян.jpg',
}, {
    'name': 'Герасименко Андрей',
    'year': '2015',
    'photo': 'static/mss/герасименко.jpg',
}, {
    'name': 'Мирошниченко Юлия',
    'year': '2015',
    'photo': 'static/mss/мирошниченко.jpg',
}, {
    'name': 'Гончаров Дмитрий',
    'year': '2015',
    'photo': 'static/mss/гончаров.jpg',
}, {
    'name': 'Петров Дмитрий',
    'year': '2015',
    'photo': 'static/mss/петров.jpg',
}, {
    'name': 'Вальзер Вадим',
    'year': '2015',
    'photo': 'static/mss/вальезр.jpg',
}, {
    'name': 'Оситковский Владислав',
    'year': '2016',
    'photo': 'static/mss/оситковский_01.jpg',
}, {
    'name': 'Оситковский Евгений',
    'year': '2017',
    'photo': 'static/mss/оситковский_02.jpg',
}, {
    'name': 'Атаманова Анастасия',
    'year': '2018',
    'photo': 'static/mss/атаманова.jpg',
}, {
    'name': 'Мирошниченко Ксения',
    'year': '2018',
    'photo': 'static/mss/мирошниченкоК.jpg',
}, {
    'name': 'Зима Дмитрий',
    'year': '2018',
    'photo': 'static/mss/зима.jpg',
}, {
    'name': 'Щербакова Мария',
    'year': '2018',
    'photo': 'static/mss/щербакова.jpg',
}, {
    'name': 'Овчинникова Ангелина',
    'year': '2018',
    'photo': 'static/mss/овчинникова.jpg',
}, {
    'name': 'Киреева Екатерина',
    'year': '2018',
    'photo': 'static/mss/киреева.jpg',
}, {
    'name': 'Кантонистова Екатерина',
    'year': '2018',
    'photo': 'static/mss/кантонистова.jpg',
}, {
    'name': 'Соловьев Михаил',
    'year': '2019',
    'photo': 'static/mss/соловьев-михаил.jpg',
}, {
    'name': 'Дробыш Александр',
    'year': '2019',
    'photo': 'static/mss/дробыш-алекс.jpg',
}, {
    'name': 'Картавых Никита',
    'year': '2019',
    'photo': 'static/mss/картавых.jpg',
}, {
    'name': 'Петрунин Владислав',
    'year': '2019',
    'photo': 'static/mss/петрунин.jpg',
}, {
    'name': 'Мартишонок Александр',
    'year': '2019',
    'photo': 'static/mss/мартишонок-александр.jpg',
}, {
    'name': 'Ильина Мария',
    'year': '2022',
    'photo': 'static/mss/ильина.jpeg',
}, {
    'name': 'Белосток Ксения',
    'year': '2022',
    'photo': 'static/mss/белосток.jpg',
}, {
    'name': 'Солютенко Ксения',
    'year': '2022',
    'photo': 'static/mss/солютенко.jpg',
}, {
    'name': 'Беляева Елизавета',
    'year': '2022',
    'photo': 'static/mss/беляева.jpg',
}, {
    'name': 'Русаков Егор',
    'year': '2022',
    'photo': 'static/mss/русаков.jpg',
}, {
    'name': 'Кулинич Никита',
    'year': '2022',
    'photo': 'static/mss/никита-кулинич.jpg',
}, {
    'name': 'Мартишонок Евгений',
    'year': '2022',
    'photo': 'static/mss/мартишонок-евгений.jpg',
}, {
    'name': 'Кузьмина Владислава',
    'year': '2022',
    'photo': 'static/mss/Кузьмина.jpg',
}, {
    'name': 'Гончарова София',
    'year': '2023',
    'photo': 'static/mss/Гончарова.jpg',
}, {
    'name': 'Фирсова Марина',
    'year': '2023',
    'photo': 'static/mss/фирсова.jpg',
}, {
    'name': 'Фомина Кристина',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Фролова Полина',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Фарзалиев Рустам',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Жарикова София',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Прялгаускайте Лиана',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Новикова Маргарита',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Зиневич Юлия',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Гарт Вера',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Тятлина Алиса',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Оразбаева Алена',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Ксенжик София',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Иванова Ксения',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Базылеева Ульяна',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Лузганов Александр',
    'year': '2023',
    'photo': '',
}, {
    'name': 'Заев Александр',
    'year': '2024',
    'photo': '',
}, {
    'name': 'Кузенкова Вероника',
    'year': '2024',
    'photo': '',
}, {
    'name': 'Полтинин Никита',
    'year': '2024',
    'photo': '',
}, {
    'name': 'Макаренко Марк',
    'year': '2024',
    'photo': '',
}, {
    'name': 'Сухомлинов Егор',
    'year': '2024',
    'photo': '',
}, {
    'name': 'Брусницын Василий',
    'year': '2024',
    'photo': '',
}, {
    'name': 'Лукиянчук Иван',
    'year': '2024',
    'photo': '',
}
]

coaches = [
{ # Ольга владимировна ирина константиновна оситковские цса
    'name': 'Кондратьева Елена Владимировна',
    'achievements': ['Основатель спортивной акробатики Калининградской области', 'Президент Федерации спортивной акробатики Калининградской области', 'Спортивный судья Всероссийской категории', 'Старший тренер сборной команды Калининградской области'],
    'term': '41 год',
    'tel': '+7 (963) 299-77-16',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'ev',
    'organization': 'Основатель спортивной акробатики Калининградской области',
}, {
    'name': 'Кондратьева Екатерина Петровна',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья Всероссийской категории', 'Тренер сборной команды Калининградской области', 'Директор ШСА «Пирамида»'],
    'term': '19 лет',
    'tel': '+7 (909) 777-90-51',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'ep',
    'organization': 'CДЮШОР №1 / ШСА «Пирамида»',
}, {
    'name': 'Гостищев Константин Викторович',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Кандидат в мастера спорта Республики Казахстан по спортивной акробатике', 'Спортивный судья Всероссийской категории'],
    'term': '8 лет',
    'tel': '+7 (962) 251-64-19',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'kv',
    'organization': 'CДЮШОР №1',
}, {
    'name': 'Кулинич Никита Владимирович',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья первой категории'],
    'term': '5 лет',
    'tel': '+7 (909) 795-11-52',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'nv',
    'organization': 'CДЮШОР №1 / ШСА «Пирамида»',
}, {
    'name': 'Константинова Анастасия Сергеевна',
    'achievements': ['Ведущий хореограф сборной команды Калининградской области'],
    'term': '12 лет',
    'tel': '',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'as',
    'organization': 'МАОУ ДТДиМ',
}, {
    'name': 'Овчинникова Ангелина Олеговна',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья второй категории'],
    'term': '6 лет',
    'tel': '+7 (952) 050-21-23',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'ao',
    'organization': 'МАОУ ДТДиМ',
}, {
    'name': 'Петрунин Владислав Сергеевич',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья третьей категории'],
    'term': '4 года',
    'tel': '+7 (952) 799-82-10',
    'addresses': ['ул. Сергеева, 10', 'ул. Аксакова, 112'],
    'code': 'vs',
    'organization': 'МАОУ ДТДиМ',
}, {
    'name': 'Поляков Илья Алексеевич',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья первой категории'],
    'term': '11 лет',
    'tel': '39-10-20',
    'addresses': ['ул. Гаражная, 2'],
    'code': 'ia',
    'organization': '«Kenig Jump»',
}, {
    'name': 'Беляева Наталья Викторовна',
    'achievements': ['Мастер спорта России по спортивной акробатике'],
    'term': '26 лет',
    'tel': '39-10-20',
    'addresses': ['ул. Гаражная, 2'],
    'code': 'nva',
    'organization': '«Kenig Jump»',
}, {
    'name': 'Мальшаков Антон Игоревич',
    'achievements': ['Мастер спорта России по спортивной акробатике'],
    'term': '5 лет',
    'tel': '39-10-20',
    'addresses': ['ул. Гаражная, 2'],
    'code': 'ai',
    'organization': '«Kenig Jump»',
}, {
    'name': 'Тимофеева Александра Павловна',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья первой категории'],
    'term': '18 лет',
    'tel': '+7 (906) 231-05-75',
    'addresses': ['ул. Гагарина д.99'],
    'code': 'ap',
    'organization': 'ГАУ ДО КО «Комплексная спортивная школа Олимпийского резерва»',
}, {
    'name': 'Гребнева Инна Сергеевна',
    'achievements': ['Мастер спорта Республики Казахстан по спортивной акробатике', 'Спортивный судья второй категории'],
    'term': '14 лет',
    'tel': '',
    'addresses': ['ул. Гагарина д.99'],
    'code': 'is',
    'organization': 'ГАУ ДО КО «Комплексная спортивная школа Олимпийского резерва»',
}, {
    'name': 'Верига Екатерина Александровна',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья второй категории'],
    'term': '9 лет',
    'tel': '+7 (909) 797-80-69',
    'addresses': ['ул. Карташева,111'],
    'code': 'ea',
    'organization': 'МАУ ДК «Машиностроитель»',
}, {
    'name': 'Прялгаускайте Лиана Сваюновна',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья второй категории'],
    'term': '3 года',
    'tel': '+7 (909) 797-80-69',
    'addresses': ['ул. Карташева,111'],
    'code': 'lianka',
    'organization': 'МАУ ДК «Машиностроитель»',
}, {
    'name': 'Капитонова Татьяна Николаевна',
    'achievements': ['Кандидат в мастера спорта России по спортивной акробатике', 'Спортивный судья третьей судейской категории'],
    'term': '15 лет',
    'tel': '+7(911) 477 - 08 - 90',
    'addresses': ['ул.Советская, 8(г.Светлый)', 'ул.Горького 3 а(г.Светлый)'],
    'code': 'tn',
    'organization': 'МАУ ДО МО «СГО» «ДШИ г. Светлого»',
}, {
    'name': 'Куликовская Анастасия Вадимовна',
    'achievements': ['Хореограф'],
    'term': '8 лет',
    'tel': '',
    'addresses': ['ул.Советская, 8(г.Светлый)'],
    'code': 'av',
    'organization': 'МАУ ДО МО «СГО» «ДШИ г. Светлого»',
}, {
    'name': 'Гончаров Дмитрий Александрович',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья второй категории'],
    'term': '8 лет',
    'tel': '+7(900) 347 - 12 - 13',
    'addresses': ['ул.Аксакова, 112', 'ул.Советская, 8(г.Светлый)', 'ул.Калининградская, 19(г.Гвардейск)'],
    'code': 'da',
    'organization': 'МАУ ДО МО «СГО» «ДШИ г. Светлого»',
}, {
    'name': 'Кантонистова Екатерина Витальевна',
    'achievements': ['Мастер спорта России по спортивной акробатике', 'Спортивный судья третьей категории'],
    'term': '3 года',
    'tel': '+7(906) 233 - 60 - 88',
    'addresses': ['ул.Аксакова, 112', 'ул.Калининградская, 19(г.Гвардейск)'],
    'code': 'evi',
    'organization': 'МБУ ДО ДЮСШ г. Гвардейска',
}, {
    'name': 'Тесленко Светлана Владимировна',
    'achievements': ['Спортивный судья третьей категории'],
    'term': '43 года',
    'tel': '+7(981) 455 - 39 - 91',
    'addresses': ['ул.Спортивная, 12(г.Славск)'],
    'code': 'sv',
    'organization': 'ДЮСШ г. Славска',
}, {
    'name': 'Перятинская Елена Юрьевна',
    'achievements': ['Мастер спорта России по спортивной акробатике'],
    'term': '25 лет',
    'tel':  '+7(921) 005-04-87',
    'addresses': ['ул.Спортивная, 12(г.Славск)'],
    'code': 'ey',
    'organization': 'ДЮСШ г. Славска',
}]

import vk_api

def get_wall(token, group_id, count=100):
  vk_session = vk_api.VkApi(token=token)
  vk = vk_session.get_api()

  try:
    response = vk.wall.get(owner_id=-int(group_id), count=count)
    return response['items']
  except vk_api.exceptions.ApiError as e:
    print(f"Ошибка API: {e}")
    return []
  
def get_video(access_token, owner_id, video_id, access_key):
  vk_session = vk_api.VkApi(token=access_token)
  vk = vk_session.get_api()

  try:
    videos = f"{owner_id}_{video_id}_{access_key}"
      
    response = vk.video.get(videos=videos)
    if response["count"] > 0:
      video_info = response["items"][0]
      return video_info.get("player")  # Прямая ссылка на проигрыватель
    else:
      print("Видео не найдено.")
  except vk_api.exceptions.ApiError as e:
    print(f"Ошибка API: {e}")
    return None

def get_enogh(posts):
  new_posts = []
  texts = []
  for post in [post for post in posts]:
    try:
      photos = [attachment['photo']['orig_photo']['url'] for attachment in post['attachments'] if attachment['type'] == 'photo']
    except:
      photos = []

    try:
      videos = [get_video(access_token, f'-{group_id}', attachment['video']['id'], attachment['video']['access_key']) for attachment in post['attachments'] if attachment['type'] == 'video']
    except:
      videos = []

    try:
      cover = [attachment for attachment in post['attachments'] if 'video' in attachment][0]['video']['photo_1280']
    except:
      cover = ''



    t = {
      'title': delete_emojis(post['text'].split('\n')[0]),
      'text': delete_emojis(re.sub(r'^(<br>)+', '', ''.join(re.split(r'(\n)', post['text'])[1:]).replace('\n', '<br>'))),
      'date': datetime.datetime.fromtimestamp(post['date']),
      'photos': photos,
      'videos': videos,
      'cover': cover
    }
    if post['text']:
      new_posts.append(t)
  return new_posts
    
def get_competitions(posts, dates):
  competitions = []
  for post in posts:
    if post['date'] in dates:
      competitions.append(post)
  return competitions

def delete_emojis(text):
  return emoji.replace_emoji(text, replace='')

access_token = 'vk1.a.YsOUyacskb6Q90oYztrKpxJzENSqM7UqFH30TjWXPuNMp03jZvyDwUbeY7ofghmHULiePuGQYqpnrPoCFFOtduo7vUQQ1H1a-qY-8MK6_LG_ccffBkUCskHwdewg1FT1dE4WS98pQe9LCgCP_yBRSLte-wYz9AMGdk8QxFxXbGraSaCmpBhuMryR9m12XkNuPOLA2z3m0iyVPJNJgD58pQ'  # Замените на свой токен
group_id = "19645656"

posts = [{
    'title': 'ВНИМАНИЕ ',
    'text': 'Набор на вакантные места в составах ',
    'date': datetime.datetime(2024, 7, 9, 13, 49, 59),
    'photos': ['https://sun9-3.userapi.com/s/v1/ig2/fwncxj1p1F1nXbavTQUfCs03tVTUANCc0SfAPf4vVMfbf8JsLIaGGlU_fa5FBWu-j3h81Wn97Vf2bK05sElUP95h.jpg?quality=95&as=32x45,48x68,72x102,108x153,160x227,240x340,360x510,480x680,540x765,640x906,720x1020,1080x1530,1280x1813,1440x2039,1446x2048&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Акробаты отправились на выездные соревнования в г.Великий Новогород ',
    'text': 'Первенство Новгородской области по спортивной акробатике пройдет с 4 по 8 декабря <br><br>Желаем ребятам удачи и успешных выступлений',
    'date': datetime.datetime(2024, 12, 5, 8, 12, 8),
    'photos': ['https://sun9-57.userapi.com/s/v1/ig2/JHJI8HrpqGplGuwXTNdY5bHZLZ5ZvLuGXQSOYJSIb2hhL5JlDZgl3nkmG8hfbnwqmnqj26MU-zkwhMVTcTfSs2S7.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Невероятные моменты с соревнований по спортивной акробатике, которые прошли 1 декабря в спортивном зале «Созвездие»',
    'text': 'Яркие выступления, мастерство и дух соревнования – вдохновляйтесь вместе с нами! ',
    'date': datetime.datetime(2024, 12, 3, 13, 43, 25),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456243047&hash=f701dccb7d8d5ce7&__ref=vk.api&api_hash=173339265011213f3d23444d80b9_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7520229919350&idx=15&type=39&tkn=y_SDjO2wSBHTYDF9E-ltgMhmaHs&fn=vid_w'
}, {
    'title': 'Итоги Всероссийских соревнований «Кубок Волкова» прошедших с 9 по 16 ноября в г.Великий Новгород ',
    'text': '<p class="lead mb-2">Категория 11-16 КМС:</p><strong>Среди мужских пар</strong><ul class="ms-3 mt-3 mb-3"><li>2 место: Малай Федор, Анёв Дмитрий</li></ul><p class="lead mb-2">Среди смешанных пар</p><strong>3 место:</strong><ul class="ms-3 mt-3 mb-3"><li>СМП Барановская Виктория, Баженов Андрей</li></ul><p class="m-0 mt-3 mb-3"><strong>Поздравляем спортсменов и их тренеров — Кондратьеву Елену Владимировну и Гостищева Константина Викторовича с успешным завершением соревнований! Ваши достижения — это результат настоящего мастерства, упорного труда и командного духа.</strong></p><p class="m-0 mt-3 mb-3">Пусть впереди будет еще больше побед и новых высот!</p>',
    'date': datetime.datetime(2024, 11, 21, 10, 5, 42),
    'photos': ['https://sun9-8.userapi.com/s/v1/ig2/Fg2QSXcoPhWWol3WmcqH0JSqopJa8mTxZe3JM-UkQwgoFefS_EgcuqFUC0JCy3G2A6KR6Ul9mrULihBujFvhcDl-.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1350x1800&from=bu', 'https://sun9-16.userapi.com/s/v1/ig2/LwQsEcbdtinCzq7wpKJyYHQwyaxh8y7FgGb_FgvHYAcrWBZeuV0t0As-_yzfrwol9v6bl_i5HEO2qqnf5w61xI9e.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1800x1350&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Мы представляем открытое занятие в Центре спортивной акробатики! Аксакова 112 ',
    'text': 'Наши талантливые спортсмены продемонстрировали невероятные навыки и потрясающие трюки. <br><br>Посмотрите, как увлекательно и динамично проходит тренировка в нашей команде! <br><br>Присоединяйтесь к нам, чтобы испытать радость акробатики и развивать свои способности!',
    'date': datetime.datetime(2024, 11, 19, 9, 48, 38),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242966&hash=b2c852f54236be37&__ref=vk.api&api_hash=173339265195cb2b63d28b987daa_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7295343528476&idx=11&type=39&tkn=T17JxLsTpYVXEbQySmnFS0paxNo&fn=vid_w'
}, {
    'title': 'Открытое занятие в Центре спортивной акробатики Аксакова 112 ',
    'text': 'В этом видео вы увидите самые яркие моменты тренировки, а также увлекательные трюки и упражнения наших спортсменов. ',
    'date': datetime.datetime(2024, 11, 17, 11, 37, 29),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242961&hash=5792d5babcaada1f&__ref=vk.api&api_hash=17333926519c9c51b143857e912a_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7287161686556&idx=8&type=39&tkn=seNBo9AOoPkKr6oqKiZfs_CgOrw&fn=vid_w'
}, {
    'title': 'Подведение итогов соревнований в Казани',
    'text': '<p class="lead mb-2">2 юношеский разряд:</p><strong>Смешанные пары</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Кулагина Екатерина - Федосеев Семён</li></ul><p class="lead mb-2">1 юношеский разряд</p><strong>Мужские пары</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Слесаревич Демид - Дворецкий Дмитрий</li></ul><strong>Тройки</strong><ul class="ms-3 mt-3 mb-3"><li>2 место: Рыжова София - Ковальчук Мария - Тарасова Ксения</li></ul><p class="lead mb-2">3 спортивный разряд</p><strong>Женские пары</strong><ul class="ms-3 mt-3 mb-3"><li>3 место: Крига София - Сергеева Алина</li></ul><strong>Смешанные пары</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Антоненко Марика - Кондратьев Артем</li></ul><strong>Тройки</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Лебедева Мария - Литвинчук Варвара - Коваленко Кира-Виктория</li><li>2 место: Подколзина Елисавета - Гаврильчик Дарья - Стародубцева Вероника</li></ul><p class="lead mb-2">2 Спортивный разряд</p><strong>Тройки</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Боброва Ангелина - Казимирова Анастасия - Князева Алена</li><li>2 место: Распутина Варвара - Романенко Таисия - Бумбуль Варвара</li></ul><p class="lead mb-2">1 спортивный разряд</p><strong>Женские пары</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Ершова Алиса - Скрипниченко Елизавета</li></ul><strong>Смешанные пары</strong><ul class="ms-3 mt-3 mb-3"><li>3 место: Танник Ярослава - Батманов Тимофей</li></ul><p class="lead mb-2">11-16 лет</p><strong>Женские пары</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Дейнега Анжелика - Львова Ксения</li></ul><strong>Тройки</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Куратова София - Проказина Вероника - Науменко Ульяна</li></ul><p class="lead mb-2">КМС</p><strong>Тройки</strong><ul class="ms-3 mt-3 mb-3"><li>1 место: Пилюгина Екатерина - Иванова Ксения - Светлакова Полина</li></ul><p class="m-0 mt-3 mb-3"><strong>Поздравляем всех участников соревнований в Казани! Вы продемонстрировали высочайший уровень подготовки, стремление к победе и командный дух.</strong></p><p class="m-0 mt-3 mb-3"><strong>Особая благодарность тренерам:</strong></p><ul class="ms-3 mt-3 mb-3"><li><a class="text-blue text-decoration-none" href="https://vk.com/id17399913">Екатерина Кондратьева</a></li><li><a class="text-blue text-decoration-none" href="https://vk.com/id282420900">Никита Кулинич</a></li><li><a class="text-blue text-decoration-none" href="https://vk.com/id96996577">Екатерина Верига</a></li><li><a class="text-blue text-decoration-none" href="https://vk.com/id745637984">Лиана Прялгаускайте</a></li></ul><p class="m-0 mt-3 mb-3">Вы вложили максимум усилий в подготовку спортсменов. Ваш труд и преданность не остаются незамеченными!</p>',
    'date': datetime.datetime(2024, 11, 10, 9, 51, 3),
    'photos': ['https://sun9-41.userapi.com/s/v1/ig2/vtfcoMpQ3A2Jssg6yataJCCMzk-57Svc_anDQC_cE2sGHPoU9ScPWCrHYn4LcVE5YL6uxGH3gCXiP8-sJGglI8D9.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu', 'https://sun9-68.userapi.com/s/v1/ig2/2G30CGXiCV0_mBPRSalBDpe-K3tEuFcKFNdK7Txy1JGi-1yYAfmlnQrCD_XT214TKjH8id1GqJyNRrhxp5-bVyJh.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1350x1800&from=bu', 'https://sun9-7.userapi.com/s/v1/ig2/Ffyoha5dwLdtkRIZae7HfCSYZO8EKGjeywN_46eRHGCM9porWF6z8EFXRxYAXk6ozUXnKjlv2ccWrdJhl6R7nUUC.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1800x1350&from=bu', 'https://sun9-35.userapi.com/s/v1/ig2/Ag_12O8qtmNF9J7XASundOlW9Ho3oezzz1tLQ2xuarNY2t30grczTUB96SsH_RZFQR95pQLjkDQ90IVYWO-2Ssfz.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Акробаты отправились в г.Великий Новгород на Всероссийские соревнования ',
    'text': '«Кубок Волкова» <br><br>Желаем ребятам удачных выступлений ',
    'date': datetime.datetime(2024, 11, 9, 15, 42, 1),
    'photos': ['https://sun9-59.userapi.com/s/v1/ig2/yY7HxV2eTki5Vg-QW3i9kRgtYx3WQEO51d7LcWALP153FuAEOUODDcT2kZfmF10jdLZqzpc0OfI8e8TXylxtwqd-.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Желаем акробатам удачи на соревнованиях в Казани! ',
    'text': 'Пусть ваше выступление будет ярким и впечатляющим',
    'date': datetime.datetime(2024, 11, 3, 18, 8, 6),
    'photos': ['https://sun9-76.userapi.com/s/v1/ig2/n3-Uk0StHBr7ics_uXxXJuscq6verkgNOfhxvZuF5N95fNj95rkipIauas2vjhHoP7S1PUTl78d7GC8LDUSDXCDf.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Результаты соревнований по спортивной акробатике в городе Брест!',
    'text': '<p class="lead mb-2">Четверки 14+лет</p><strong>1 место:</strong><ul class="ms-3 mt-3 mb-3"><li>Пименов Лев - Макаренко Марк - Петрунин Владислав - Сухомлинов Егор</li></ul><p class="lead mb-2">Тройки 12-18 лет</p><strong>2 место:</strong><ul class="ms-3 mt-3 mb-3"><li>Осадчук Василиса - Федерякина Мария - Бабич Ангелина</li></ul><p class="lead mb-2">Смешанные пары 12-18 лет</p><strong>2 место:</strong><ul class="ms-3 mt-3 mb-3"><li>Народовская Кира - Анев Роман</li></ul><p class="lead mb-2">Мужские пары 12-18 лет</p><strong>2 место:</strong><ul class="ms-3 mt-3 mb-3"><li>Малай Федор - Анев Дмитрий</li></ul><p class="m-0 mt-3 mb-3"><strong>Поздравляем всех участников с блестящими выступлениями!</strong></p><p class="m-0 mt-3 mb-3"><strong>Особая благодарность тренерам, которые вложили свою душу и знания в подготовку спортсменов!</strong></p><p class="m-0 mt-3 mb-3">Желаем всем дальнейших успехов и новых побед!</p>',
    'date': datetime.datetime(2024, 11, 1, 11, 36),
    'photos': ['https://sun9-69.userapi.com/s/v1/ig2/2E1Dmx2dKrL-ZsdQfnBIwmZiaWmyLDIAzlQnSV8SMfenq7NHslxqRjqg-WGpIzB-1Ly-ArkWijwPi2mrvTNSW26s.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-71.userapi.com/s/v1/ig2/9AS6WSL9nP0HM0NIgrjyAHOjBOWoo5uRCvDf4hRZwVSjxSO8AU2B8Gcz3UAyAuS4fqVzeva7s8wEGqhMLfJviGWj.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-18.userapi.com/s/v1/ig2/Buy7UTAFsM5FbRti17vj4wvNmCagGT9CmHKchDQ689D0L7kVtJloEFyfAAhgUAxj04quDFxlmaxoLJH_9UWEbKqU.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-20.userapi.com/s/v1/ig2/70inD1YFnqcxbEt6UY546WjQL_D1Q0d1JczMBw7Xe4-mpZWB_FM8lqQj8ouOaZPx5dgwdnw-TUS_KOnppgfoHYam.jpg?quality=95&as=32x31,48x46,72x69,108x104,160x154,240x231,360x347,480x463,540x520,640x617,720x694,1080x1041,1280x1234,1440x1388,1600x1542&from=bu', 'https://sun9-56.userapi.com/s/v1/ig2/YKE6nLxIukamlCPB_NAngJFlXG35XxMuT3KVML6eY9VmklUYNhMj4lBGSA3tLc1YEn4cBlU87MuB8H_uYK0W8RA3.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Показательное выступление ',
    'text': 'Во Дворце Спорта Юность ',
    'date': datetime.datetime(2024, 10, 31, 14, 0, 10),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242892&hash=3f908717671f7543&__ref=vk.api&api_hash=17333926514fc9fdaa9f1edaf7d7_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7301940120201&idx=3&type=39&tkn=FINVnH5GKECOWtOr-vd-ZIAxVr8&fn=vid_w'
}, {
    'title': 'Все видео выступлений акробатов в г. Брест ',
    'text': 'По ссылке : <br><br>https://youtube.com/playlist?list=PLUGUElwOl8IYP0QmFuLHQnNapOkXXqD7w&si=HOKMWRb4C5iWoY3F',
    'date': datetime.datetime(2024, 10, 30, 10, 26, 37),
    'photos': ['https://sun9-19.userapi.com/s/v1/ig2/WYgKgFaW8WPJJnHoNFGhE24BLXOq4IjJctTNL5soRF8eIeifn7SNwBrG-f56oPFJQMvPiaHCsrQiZZ2NOC-vtmqx.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Поздравляем с Днем тренера! Этот день — особенный, поскольку мы отмечаем ваш вклад в развитие спортивной акробатики и формирование новых поколений чемпионов. ',
    'text': 'Вы — настоящие наставники, источники вдохновения и примеры безграничного терпения. Ваши усилия и самоотверженность помогают спортсменам достигать новых высот, преодолевать трудности и верить в себя. Вы обучаете не только зрелищным элементам и техникам, но и ценным жизненным урокам, которые останутся с вашими подопечными на всю жизнь.<br><br>В этот знаменательный день мы выражаем вам искреннюю благодарность за ваш труд, вашу веру и вашу уверенность. Желаем вам здоровья, энергии, новых побед и вдохновения на пути к будущим свершениям. <br><br>#СпасибоТренер2024',
    'date': datetime.datetime(2024, 10, 30, 9, 55, 51),
    'photos': ['https://sun9-28.userapi.com/s/v1/ig2/GXCidDadATMd210ECUc_E0apMcnKm4VCcvbtw2N63JkT4GVhSDEI_qRgSJeSMwX5p4oVIImo3gbGo6o_56AAytFk.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1800x1350&from=bu', 'https://sun9-59.userapi.com/s/v1/ig2/isdcXRux3vEmQ8XmzDK6QsrVOsDNBc0PXfyd2ggCQDFojKePpTuGNlMCz_cQFZCQkjgU8abSlqXAsTVuTZzc2rji.jpg?quality=95&as=32x21,48x32,72x48,108x72,160x107,240x160,360x240,480x320,540x360,640x427,720x480,1080x720,1280x853,1440x960,2500x1667&from=bu', 'https://sun9-29.userapi.com/s/v1/ig2/3qo808Q1JtTfarHBXvZf4usj1VllcWGfEygNSZ6rmRgRf7ngWpPV12rofjbBC6cCvp1E4LvtdX2fFLtyXES44tQe.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu', 'https://sun9-77.userapi.com/s/v1/ig2/35r5HfGX-DdMnc_xBXRNmS_c7w9W0i3PWtBQH4lovRO0lG9Moi9jmwUjyn_Lko9__I9KnQNGyPmKF6DxZztDFM3f.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1350x1800&from=bu', 'https://sun9-3.userapi.com/s/v1/ig2/U6qKIILScL7mySVnwUTUIOxUX9ev_w6b8bCdoNd51y2Iim9DMftgQCTrm3h9OOHGwpWfnRDQbEt1ucLZ6BjD2ger.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Акробаты отправились в г.Брест ',
    'text': 'Желаем ребятам удачи и ярких выступлений ',
    'date': datetime.datetime(2024, 10, 28, 11, 51, 10),
    'photos': ['https://sun9-58.userapi.com/s/v1/ig2/vokRaLqxuHmMomN8WM9pDyqcSEOJlYNB_4NlWmoJTJ_uPlFhaCYF7wUTxwMmT7UKi8cbxw9wH2wVFPcls1zU3kNh.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Показательное выступление акробатов на Всероссийских соревнованиях по борьбе ',
    'text': 'ФОК «АВТОТОР-Арена»',
    'date': datetime.datetime(2024, 10, 21, 12, 40, 42),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242863&hash=9a3fc7e0c5a557ab&__ref=vk.api&api_hash=1733392651c0b7b700babbb04a1d_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7138625063526&idx=12&type=39&tkn=GjXM01i0jcnYl84xZDHpCvVAUz8&fn=vid_w'
}, {
    'title': ' Уникальные моменты и захватывающие выступления на Кубке города Калининграда по спортивной акробатике!  Смотрите, как наши талантливые спортсмены демонстрируют силу, грацию и командный дух!  #Калининград #СпортивнаяАкробатика #КубокГорода',
    'text': '',
    'date': datetime.datetime(2024, 10, 16, 9, 58, 54),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242838&hash=975945889c8eab7a&__ref=vk.api&api_hash=1733392651f7eb152f38b97a0ace_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7127666920102&idx=15&type=39&tkn=ccU673TsqvnH1uK188ryd7ji1EU&fn=vid_w'
}, {
    'title': 'Открытый Кубок Великого Новгорода по спортивной акробатике подошел к концу и мы спешим сообщить вам результаты наших спортсменов: ',
    'text': 'Тройки 2 взрослый разряд <br>2 место: Васенкова Анна - Фефелова Ульяна - Негреева Мария<br><br>СмП 3 взрослый разряд<br>1 место: Золотухина Вера - Черных Андрей<br><br>Женские пары 1 юношеский разряд <br>2 место: Самсонова Ева - Самсонова Есения<br><br>Тройки 2 юношеский разряд <br>1 место: Кухарская Анастасия - Чмелюк Элиза - Ливанская Екатерина<br>2 место: Кухарская София  - Бюйюкстузджу Эрика - Белоусова Алиса<br>3 место: Барановская Алла - Позднышева София - Трайгель Ева<br><br>Четверки 2 юношеский разряд <br>2 место: Башанкаев Константин - Коваленко Кирилл - Новиков Иван  - Ивашков Сергей<br><br>Поздравляем спортсменов с успешным завершением соревнований! Вы проделали огромную работу, демонстрируя силу воли, упорство и дух команды. Каждое ваше выступление — это результат тренировки, стараний и стремления к победе.<br><br>Также , поздравляем тренеров: <br>Кондратьева Елена Владимировна <br>Гостищев Константин Викторович <br>Овчинникова Ангелина Олеговна <br>Петрунин Владислав Сергеевич <br><br>Желаем вам новых достижений и энергии для дальнейших свершений. Пусть впереди будут яркие победы и незабываемые моменты!',
    'date': datetime.datetime(2024, 10, 11, 11, 39, 57),
    'photos': ['https://sun9-54.userapi.com/s/v1/ig2/W_-GTbP3OTk0VDO49Fyq63yajknW-kiExDKv6gaQFLRIC4By7M0QFxwR20bGGRf7Q48AdptNihQlCo1RCBgXSJd6.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-76.userapi.com/s/v1/ig2/01YWXzaaq0AGx9SbPDYw3liolxfi9fsAMd__4jPVivDw89h_msy2XR37QDhsSOwdrFD8uaL_PTti22s6Z2hv0OeY.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1350x1800&from=bu', 'https://sun9-69.userapi.com/s/v1/ig2/q2eP0RdELBem9Tt1r_WlOKBh2YdnB1qm6DVHGdnOYNT2uH5RcjyJ8cTS6qk_CH3bGixY9E_zhJ_47pwOMtJdYtuP.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1800x1350&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'КУБОК ГОРОДА',
    'text': '\xa0<br>\xa0Подведены итоги соревнований «Кубок города» <br>С 3 по 6 октября свое мастерство демонстрировали спортсмены от юношеских разрядов до Мастеров спорта <br>По итогам соревнований места распределились следующим образом:<br>\xa0<br>МУЖСКИЕ ПАРЫ <br>3-1 юношеский разряд:<br>1 место: Слесаревич Демид - Дворецкий Дмитрий (1 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>2 место: Божинский Даниил - Пустовит Ян (1 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., \xa0Овчинникова А.О.<br>3 место: Власов Николай - Бибрих Евгений (2 юн. р-д.) КРСДМОО, тренеры: Беляева Н.В., Поляков И.А.<br>\xa0<br>3-2 спортивный разряд6<br>1 место: Денщиков Ратибор - Слесаренко Артем (2 сп. р-д.) МАУ ДК «Маш-ль», тренеры: Верига Е.А., ПрялгаускайтеЛ.С.<br>2 место: Джанунц Эрик - Жемчужников Сергей (2 сп. р-д.) КСШОР тренеры: Тимофеева А.П., \xa0Гребнева И.С., РафаевичА.П.<br>3 место: Микелайтис Егор - Лысиков Георгий (2 сп. р-д.) ШСА «ОСЬ», тренеры: Оситковский В.О., Оситковский Е.О.<br>\xa0<br>1 спортивный разряд – МС 14+ лет:<br>1 место: Малай Федор - Анев Дмитрий (КМС) МАУДО ДТДиМ, тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С.<br>2 место: Дьячков Кирилл - Сергиенко Роман (2 сп. р-д.) КСШОР тренеры: Тимофеева А.П., Гребнева И.С., РафаевичА.П.<br>3 место: Егоров Федор - Казаков Сергей (КМС) КСШОРтренеры: Тимофеева А.П., Гребнева И.С., Рафаевич А.П.<br>\xa0<br>ЖЕНСКИЕ ПАРЫ<br>3-1 юношеский разряд:<br>1 место: Самсонова Ева - Самсонова Есения (1 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>2 место: Копарева Анна - Щипко Виктория (1 юн. р-д.) КРОО ФСА, тренеры: Ерохина Т.Н., Гончаров Д.А., Куликовская А.В.<br>3 место: Маркова Кира - Садыкова Анна (3 юн. р-д.) ШСА «ОСЬ», тренеры: Оситковский Е.О., Щербакова М.Р.<br>\xa0<br>3-2 спортивный разряд:<br>1 место: Крига София - Сергеева Алина (3 сп. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>2 место: Ноак Оливия - Косых Елизавета (2 сп. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>3 место: Журавлёва Милана - Ткаченко Марина (2 сп. р-д.)ШСА «ОСЬ», тренеры: Оситковский В.О., Оситковский Е.О.<br>\xa0<br>1 спортивный разряд – МС 14+ лет: <br>1 место: Ильюхина Маргарита - Ильина Мария (12-18 лет) МАУДО СШ№1, тренеры: Кондратьева Е.П., Кулинич Н.В<br>2 место: Ли Милана - Куличева Валерия (КМС) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>3 место: Ташлыкова Диана - Фоменко Ярослава (13-19 лет) МАУДО СШ№1, тренеры: Кондратьева Е.В., Гостищев К.В.<br>\xa0<br>СМЕШАННЫЕ ПАРЫ <br>3 – 1 юношеский разряд:<br>1 место: Константинова София - Плюснин Кирилл (3 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>2 место: Хачатурова Алеся - Фомин Арсений (1 юн. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>3 место: Дюкова Даниэла - Макаров Никита (1 юн. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>\xa0<br>3 – 2 спортивный разряд: <br>1 место: Золотухина Вера - Черных Андрей (3 сп. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>2 место: Ковалева Анна - Киселев Егор (3 сп. р-д.) МАУ ДК «Маш-ль», тренеры: Верига Е.А., Прялгаускайте Л.С.<br>3 место: Антоненко Марика - Кондратьев Артем (3 сп. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., ОвчинниковаА.О.<br>\xa0<br>1 спортивный разряд – МС 14+ лет: <br>1 место: Симороз Виктория - Куликов Максим (13-19 лет) МАУДО СШ№1, тренеры: Кондратьева Е.П., Кулинич Н.В<br>2 место: Бугаева Ульяна - Богатенко Константин (КМС)СШ№1, тренеры: Кондратьева Е.П., Кулинич Н.В<br>3 место: Барановская Виктория - Баженов Андрей (КМС) СШ№1, тренеры: Кондратьева Е.В., Гостищев К.В.<br>\xa0<br>ТРОЙКИ <br>3 – 1 юношеский разряд:<br>1 место: Рыжова София - Тарасова Ксения - Ковальчук Мария(1 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>2 место: Юрчак Виктория - Финк Ксения - Верешкина Таисия(2 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>3 место: Рыбальченко Юлианна - Костерина Мария - ДзотоваКаталея (2 юн. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>\xa0<br>3 – 2 спортивный разряд: <br>1 место: Петрова Ольга - Борисюк Александра - Наумова Анна(2 сп. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>2 место: Распутина Варвара - Романенко Таисия - БумбульВарвара (2 сп. р-д.) МАУДО ДТДиМ, тренеры: Кондратьева Е.П., Кулинич Н.В<br>3 место: Жукова Николь - Нагаева Иоланта - Лущиц Оксана (2 сп. р-д.) МАУДО ДТДиМ тренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>\xa0<br>1 спортивный разряд – МС 14+ лет: <br>1 место: Божок Алина - Иващук Мария - Атаманова Александра (13-19 лет) МАУДО СШ№1, тренеры: Кондратьева Е.В., Гостищев К.В.<br>2 место: Алексеева Вероника - Рудакова Вероника - КузенковаВероника (12-18 лет) МАУДО ДТДиМ СШ№1, тренеры: Кондратьева Е.П., Кулинич Н.В<br>3 место: Пилюгина Екатерина - Иванова Ксения - СветлаковаПолина (КМС) МАУДО ДТДиМ СШ№1, тренеры: Кондратьева Е.П., Кулинич Н.В<br>\xa0<br>ЧЕТВЕРКИ<br>3 – 1 юношеский разряд:<br>1 место: Молчанов Федор - Пирог Евгений - Ильюхин Роман - Хромов Артем (1 юн. р-д.) МАУДО ДТДиМ тренеры:Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>2 место: Гильзендегер Михаил - Марков Матвей - Марков Андрей - Болотов Артемий (3 юн. р-д.) ШСА «ОСЬ», тренеры: Оситковский Е.О., Щербакова М.Р.<br>3 место: Гришаев Степан - Евстигнеев Антон - Ермолаев Юрий - Лебедев Вячеслав (3 юн. р-д.) КСШОР тренеры: Тимофеева А.П., Гребнева И.С., Рафаевич А.П.<br>\xa0<br>1 спортивный разряд – МС 14+ лет: <br>1 место: Пименов Лев - Макаренко Марк - Петрунин Владислав - Сухомлинов Егор (14+ лет) МАУДО СШ№1, тренеры: Кондратьева Е.В., Гостищев К.В.<br>2 место: Стальмаков Илья - Юрченко Владислав - Двуреченский Леон - Андреев Матвей (КМС) МАУДО ДТДиМтренеры: Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>3 место: Незговоров Андрей - Нагаев Артем - Амельков Артем- Плоцкий Тимофей (КМС) МАУДО ДТДиМ тренеры:Кондратьева Е.В., Гостищев К.В., Петрунин В.С., Овчинникова А.О.<br>\xa0<br>\xa0<br>Поздравляем победителей и участников соревнований, которые показали выдающуюся технику и силу духа. Ваши достижения являются примером для подражания и источником вдохновения для всех, кто любит спорт и акробатику. Ваши усилия и труд не остались незамеченными, и мы надеемся, что вы будете продолжать развивать свои навыки и достигать новых высот.<br>Поздравляем наших талантливых тренеров, которые помогли нашим спортсменам достичь таких высоких результатов!<br>Ваши усилия, знания и опыт помогли спортсменам развивать свои навыки и достичь успеха в соревнованиях.',
    'date': datetime.datetime(2024, 10, 9, 13, 13, 18),
    'photos': ['https://sun9-71.userapi.com/s/v1/ig2/lMPJjVZfeAtOj-Dzd03OGFcmPJDmyvZ-4lxOWAfaDd4UFDrfwcKWkcCnqtG-05fbky_xoQ6yPstvJWtzpdhCEMBA.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1800x1350&from=bu', 'https://sun9-39.userapi.com/s/v1/ig2/5Z438KQtD2reSCFeMOXoSUBKm0LtU7HzPeGmwQTSnP-VdXVv3Ur31URUCJbwRWuUN-QLEzweaBOA0IgUDf6goSiW.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1800x1350&from=bu', 'https://sun9-38.userapi.com/s/v1/ig2/WQe5GadtKVoM2mbEfvLt-j-NjHjYN48C2pvyHRPlUvC6ldNEjpfmiZdUDJtYuTmXwMFNsCTJAsu6cjf6u9cthu2Y.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': '1 Мастер спорта ',
    'text': 'Поздравляем Макаренко Марка с присвоением звания Мастер спорта России по спортивный акробатике <br><br>Отдельно поздравляем тренеров:<br>Кондратьева Елена Владимировна <br>Гостищев Константин Викторович <br><br>Это великое достижение, которое является результатом вашего труда и упорства.<br><br>Также , хотим поделиться с вами Акро-эволюцией спортсмена <br>https://youtu.be/p-HaYyhXY1A<br><br>Хотите увидеть какой путь прошли спортсмены?<br>Скорее переходите на наш Youtube канал, ведь там уже размещены акроэволюции. Это небольшие видео, подготовленные спортсменами.<br>В данное видео обычно включают фото и видео со своих тренировок и соревнований в хронологическом порядке.',
    'date': datetime.datetime(2024, 10, 9, 9, 33, 11),
    'photos': ['https://sun9-15.userapi.com/s/v1/ig2/OtsRfTradvm7GswnXPx6tqjUbdbCbE_J3pZPgS_qDYwRPrQ9fbkmJV0RNt7mcziyCwKpRqer07VzCOcqe6K6asL8.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x284,240x427,360x640,480x853,540x960,640x1138,720x1280,900x1600&from=bu', 'https://sun9-54.userapi.com/s/v1/ig2/GkKoU0S9s3QtYKDozkrKmG48siMwX5Lz4qI0AwkV8ed6PZMnIq7deIxlRVsKcsoffBAKJGdqV_7Pgg9sRzNMgP0u.jpg?quality=95&as=32x49,48x74,72x111,108x167,160x247,240x371,360x557,480x742,540x835,640x990,720x1114,783x1211&from=bu', 'https://sun9-56.userapi.com/s/v1/ig2/f3sNDjI9kjmnlz45qFZCfzsTashxzlKbfH1ogds0mY435AnhmR0W0MMmpPNGBf3Ttvi2gkQc-tdyvoK-SH-n4k62.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu'],
    'videos': ['https://www.youtube.com/embed/p-HaYyhXY1A?__ref=vk.api'],
    'cover': ''
}, {
    'title': 'Наши спортсмены отправились на соревнования в г.Великий Новгород ',
    'text': 'Открытый Кубок Великого Новгорода по спортивной акробатике пройдет с 9 по 11 октября <br><br>Желаем ребятам удачи и побед ',
    'date': datetime.datetime(2024, 10, 9, 8, 54, 51),
    'photos': ['https://sun9-38.userapi.com/s/v1/ig2/b6xXeIZqEqCxTf88eqwEib1TthOnqjYEeIUeLUV15EWLOgVPEBYDjFO-NFu8noFbedyAAxLA7G8irGkBWQn6YnoP.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1600x1200&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Показательное выступление акробатов в ФОК «АВТОТОР-Арена»',
    'text': 'В честь открытия Чемпионата России по скалолазанию ',
    'date': datetime.datetime(2024, 10, 3, 11, 4, 14),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242757&hash=9da566d42e770c06&__ref=vk.api&api_hash=1733392652b13b5da0d8870702c0_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=6883033942532&idx=1&type=39&tkn=9rNxNxRt0qC0QWTuul2kPMSsEjo&fn=vid_w'
}, {
    'title': 'Сегодня мы поздравляем С днем рождения Президента Федерации спортивной акробатики Калининградской области ',
    'text': 'Дорогая Елена Владимировна!<br><br>С днем рождения! <br>Ваше лидерство и преданность делу развития спортивной акробатики в Калининградской области вдохновляют нас всех.<br><br>Вы вкладываете душу и силы в поддержку спортсменов, способствуете их роста и достижениям. Благодаря вашему труду и целеустремленности, наша область уверенно занимает достойные места на всероссийских и международных соревнованиях.<br><br>Желаем здоровья, счастья и неиссякаемой энергии! Пусть впереди будет много побед, интересных проектов и единомышленников.',
    'date': datetime.datetime(2024, 10, 2, 9, 57, 11),
    'photos': ['https://sun9-62.userapi.com/s/v1/ig2/fPYNhylQmZT7oTZjZ-9_MKRtMUkO3a2PBlZ33TJtPKUKIWU1typLyX9BS44ifzP1Jnkq6LrbC27qYL3YzLECO2p2.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x361,360x541,480x721,540x811,640x961,720x1082,852x1280&from=bu', 'https://sun9-29.userapi.com/s/v1/ig2/FREzcN97WMhfpYXrK8mVl9rleC1jNnX_5rT7NkbfeBQlBhrw7lrg8F70L-dfKnktFz9vjuKBcaw5apX4PHR94IU3.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Внимание, Знаменск! ',
    'text': 'С радостью сообщаем о долгожданном открытии новой точки по спортивной акробатике ! <br><br> Место проведения: п. Знаменск , ФОК ул.Ленина, 31 <br><br>Приглашаем всех желающих присоединиться<br><br>Не упустите возможность окунуться в мир акробатики, развить свои навыки и найти новых друзей! <br><br> Для получения дополнительной информации и записи на тренировки звоните по телефону: +7 900 347 12 13<br><br>Ждем вас на открытии! Давайте вместе сделаем спорт частью нашей жизни! <br><br>#СпортивнаяАкробатика #Знаменск #Открытие #СпортДляВсех#спортивнаяакробатика #калининград #спорт #дети #спортивнаяакробатикакалининград#sport#acrobatic',
    'date': datetime.datetime(2024, 9, 24, 12, 1, 40),
    'photos': ['https://sun9-51.userapi.com/s/v1/ig2/a0kgHghBrYGs8vlNs9FjK71ovZThrGGRyW3yHJmI4jlZHDpWz9hEyqDwm-vX9XCskH7QNU0z8INtwriY61Sgtyq-.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x284,240x426,360x639,480x852,540x958,640x1136,720x1278,1080x1917,1244x2208&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Сегодня мы хотим поздравить с днем рождения тренера , а также действующего спортсмена [id184475059|Влад Петрунин]  ',
    'text': 'Пусть каждый новый день приносит удовлетворение от результатов вашей работы, здоровья и сил для новых свершений. А впереди пусть будет много побед, как на спортивной арене, так и в жизни!  <br><br>Желаем вдохновения, счастья, благополучия и, конечно же, интересных и увлекательных тренировок! ',
    'date': datetime.datetime(2024, 9, 23, 14, 8, 48),
    'photos': ['https://sun9-79.userapi.com/s/v1/ig2/DBFPiXMfs6MJ27OFeStdqxLL3b0As_LK4Yge1EHqQV8bF9YyhwssIQDl8JdrDcVVzOEqYadZ-BF9JCFX8-I03qDh.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x241,240x361,360x541,480x722,540x812,640x962,720x1082,1080x1624,1280x1924,1440x2165&from=bu', 'https://sun9-77.userapi.com/s/v1/ig2/mnPzyafxG_YLxWlDsx-4aXNIMNHb-vfd7vCksImluHYdtkKG91pR6U2j9owrvfRWHvT6AcVfATjzlK5K7Nexw-z0.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu', 'https://sun9-6.userapi.com/s/v1/ig2/DotfNsePi3g6IAhX9dtkmhEKrIheG9pORCMtH6ZWuhE7x8izb5WC4sMK7w99e9iI4CzApiApWMXq1a11DEYmsvmq.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x284,240x427,360x640,480x853,540x960,640x1138,720x1280,900x1600&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Спешим поделиться с Вами Акро-эволюцией наших новоиспеченных Мастеров Спорта ',
    'text': 'Заев Александр <br> https://youtu.be/4vPrFx62jNs<br><br>Кузенкова Вероника <br> https://youtu.be/_2skxBLHiBs<br><br>Полтинин Никита  <br> https://youtu.be/x-2E4EESfjk<br><br>Хотите увидеть какой путь прошли спортсмены?<br>Скорее переходите на наш Youtube канал, ведь там уже размещены акроэволюции. Это небольшие видео, подготовленные спортсменами. <br>В данное видео обычно включают фото и видео со своих тренировок и соревнований в хронологическом порядке.',
    'date': datetime.datetime(2024, 9, 19, 12, 45, 15),
    'photos': [],
    'videos': ['https://www.youtube.com/embed/4vPrFx62jNs?__ref=vk.api'],
    'cover': ''
}, {
    'title': ' Дорогие друзья! ',
    'text': 'С огромной радостью и гордостью поздравляем наших талантливых спортсменов:<br>- Заев Александр <br>- Кузенкова Вероника <br>- Полтинин Никита <br>с присвоением званий Мастеров спорта по спортивной акробатике! <br><br>Этот великий успех стал возможен благодаря вашему усердному труду, страсти и стремлению к совершенству.<br><br>Особую благодарность мы хотим выразить вашим замечательным тренерам.  <br>Кондратьева Елена Владимировна <br>Кондратьева Екатерина Петровна <br>Гостищев Константин Викторович <br>Кулинич Никита Владимирович <br><br>Ваше терпение, профессионализм и поддержка были неоценимыми на этом пути. Вы вложили в своих подопечных свои знания и силу , и теперь вместе с ними радуетесь их достижению. <br><br>Мы желаем вам новых высот, успехов и свершений в будущем. Пусть каждый новый день приносит радость от тренировок и вдохновение для покорения новых вершин!',
    'date': datetime.datetime(2024, 9, 13, 10, 26, 3),
    'photos': ['https://sun9-68.userapi.com/s/v1/ig2/vBhHPPo6me5G1gn0hzcp3_UBmVwsa_CqE-i6TsYE9n3XVAPhFSiScCOh3tWER5200_CPsF7MCZ2gKNAOTkpeamR-.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x239,240x359,360x539,480x718,540x808,640x958,720x1077,822x1230&from=bu', 'https://sun9-79.userapi.com/s/v1/ig2/1DSB3PsBy1hPXh4F8sJbw2JFBvM6_kkvd_E8STHvQF0u0IuktBNmzaM9yg0kXGQjZhu_lUivfOP1B1I1of3IbmpV.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-79.userapi.com/s/v1/ig2/JEeGu20xU0BrzrgO0JLlqOaD1CClwO10PSQpsoxnVy5BoK_Jr34_BXqFE_3BNDy197J4LPM3i5lmfClpau_wLvZO.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,853x1280&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': ' ВНИМАНИЕ ',
    'text': '',
    'date': datetime.datetime(2024, 9, 5, 11, 22, 59),
    'photos': ['https://sun9-51.userapi.com/s/v1/ig2/kwdWxJtkPSWy38cjBD5gMIfZK61x-3iQzjzoB0WLENkdcxC7f93DpbglH3VT-uYB5Ena0Vl5gbfyaATlnH6qNB7m.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x284,240x426,360x639,480x852,540x958,640x1136,720x1278,1080x1917,1242x2204&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': ' Дорогие тренеры, спортсмены и любители спортивной акробатики! ',
    'text': 'С огромной радостью поздравляем вас с началом нового сезона!  Пускай этот год будет наполнен яркими достижениями, незабываемыми моментами и, конечно, новыми вершинами!',
    'date': datetime.datetime(2024, 9, 1, 12, 29, 7),
    'photos': ['https://sun9-68.userapi.com/s/v1/ig2/wwZfC53KUzKqaTtbkehvwF89QYKL5tpAaJUuSlWGDWEjQ05Yldqt2jxkwK5RKGXSaZMajf8xI0fSSfV0hVT8Fy8P.jpg?quality=95&as=32x33,48x50,72x75,108x113,160x167,240x251,360x377,480x502,540x565,610x638&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Прошел ежегодный финал соревнований  по О и СФП',
    'text': 'Это событие стало настоящим тестом на силу, выносливость и командный дух. Все участники продемонстрировали выдающиеся результаты и невероятную мотивацию!<br><br>Подведем итоги<br><br>НИЖНИЕ <br><br>МАЛЬЧИКИ <br>1 место - Анёв Роман <br>2 место - Богатенко Константин <br>3 место - Сухомлинов Егор <br>4 место - Макаренко Марк <br>5 место - Анёв Дмитрий <br><br>ДЕВОЧКИ <br>1 место - Ильина Мария <br>2 место - Атаманова Александра <br>3 место - Рудакова Вероника <br>4 место - Куличева Валерия <br>5 место - Литвинчук Варвара <br><br>ВЕРХНИЕ <br>МАЛЬЧИКИ И ДЕВОЧКИ <br>1 место - Пименов Лев <br>2 место - Симороз Виктория <br>3 место - Ильюхина Маргарита <br>4 место - Ташлыкова Диана <br>5 место - Божок Алина <br><br>Поздравляем спортсменов и тренеров с достигнутым результатом и надеемся на дальнейшие успехи)  ',
    'date': datetime.datetime(2024, 9, 1, 12, 4, 33),
    'photos': ['https://sun9-80.userapi.com/s/v1/ig2/6YStxtU2ig29fAY2P3sUiwrsbzGWFv5ONirN9L7L3uBLcIX4DEPEcJKdpzTlOD6sTVLyXqX9glpbRsdiQi_zfiLw.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-10.userapi.com/s/v1/ig2/sCKKo1AR7QflakLjIIa0gWg_H16KgywdERM-yEJvIPHdCHin1w53s_rwInz-rd9_rhHI-fCaKCx7wv53uunoHkH8.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu', 'https://sun9-45.userapi.com/s/v1/ig2/nBkw5tpGWg9q5Wn5D8lck4vZvK9DYM8UuDGmB6IM9UTYn49ljnlgiDbJrnfgwpP8Do-kpL5Vc_qzanL-j9B6PgjF.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu', 'https://sun9-26.userapi.com/s/v1/ig2/zbh6vwN7ZAMqgRXXC5KH7A8d7NIwd1J-0nvLE1YRodxQVX7n7Xby_g9AvR7KVYnc8D7GfdA6aceN5W1_n-BsxsCI.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242654&hash=ed3e6d6da690a8ee&__ref=vk.api&api_hash=17333926539ac84fe2e2eb1ed7c0_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7005562866217&idx=13&type=39&tkn=FB7dg9X1eLQYmoK8Leccr8JuGQA&fn=vid_w'
}, {
    'title': ' августа прошли судейские курсы для судей, спортсменов и тренеров ',
    'text': 'Данные курсы не только помогают нам понять и усовершенствовать наши знания о правилах и процедуре, но и формируют профессионалов, способных принимать справедливые и взвешенные решения.<br><br>По итогам, участникам будут присвоены спортивные судейские категории:<br>- Юный спортивный судья <br>- Спортивный судья третьей категории <br>- Спортивный судья второй категории <br>- Спортивный судья первой категории',
    'date': datetime.datetime(2024, 8, 29, 12, 12, 29),
    'photos': ['https://sun9-79.userapi.com/s/v1/ig2/Q-UeKRW2loNOSaatEpJidml1L4wvzzrO0NFF2URXHxmfjKzQCG45bTjm0I5UOJl6xGmRHnIqlUMHjkXtRCPtcH0W.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu', 'https://sun9-44.userapi.com/s/v1/ig2/QvAw7qkqqblFY64s92DmL9b0SX8LEn9unjmgbHLYj4_IHGSxmkvxh56n1oFYLIsLJO824C5rYNC23E1rVy9Ro3m9.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242648&hash=213f4ce10d939ddd&__ref=vk.api&api_hash=1733392654938956b78b6b4f717e_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=6924657429096&idx=7&type=39&tkn=TBEzINBh0gkG_hfS9Tg9XcgHD_Y&fn=vid_w'
}, {
    'title': 'Показательное выступление акробатов в ЖК «Восток» ',
    'text': '',
    'date': datetime.datetime(2024, 8, 27, 16, 31, 43),
    'photos': ['https://sun9-8.userapi.com/s/v1/ig2/5g4UmrGrHBB086TmbzCex-fYAByh3BQTziUsSy6NZDXsqOeUQzOMrMoqWe8_AAk7D7UNR3nKKRD7XJGTzcazFH23.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1600x1200&from=bu', 'https://sun9-32.userapi.com/s/v1/ig2/K4ujmNjlOW9TPPd-x_orWVmIRHemdz2wjY8rmQq7VMLJt0v_Jaf5DDiARxGbVxYlczIFjggFGt_mykV9j8DVuhrr.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242639&hash=14807cf536a21e1d&__ref=vk.api&api_hash=173339265492d68ff99d5cf949a9_GMYDSOJQGMZTGOI', 'https://vk.com/video_ext.php?oid=-19645656&id=456242640&hash=bb0ad6c2d9b19171&__ref=vk.api&api_hash=1733392654ba89b23b6d1558c66a_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7142060264076&idx=5&type=39&tkn=8EawqpTTNgdFsylRPzZ15M8dKMI&fn=vid_w'
}, {
    'title': 'Показательное выступление акробатов на финальном этапе Всероссийского марафона «Земля спорта» ',
    'text': '',
    'date': datetime.datetime(2024, 8, 25, 14, 53, 58),
    'photos': ['https://sun9-1.userapi.com/s/v1/ig2/wnVbiYHJAZBbjdcJ1G9lIC06pvk-sT7dAJyVAssI-ypOhsABoqa0gmCPxaV26qcv9aip4VJbvPHgqxrK4MQ7JF6a.jpg?quality=95&as=32x24,48x36,72x54,108x81,160x120,240x180,360x270,480x360,540x405,640x480,720x540,1080x810,1280x960,1440x1080,1600x1200&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242631&hash=315b931a2455023b&__ref=vk.api&api_hash=17333926550d9c3c04d642f572cc_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7043983936234&idx=0&type=39&tkn=kgyH2s5lGF0XnNKVk87z789VBlQ&fn=vid_w'
}, {
    'title': 'Показательное выступление на территории Музея Мирового океана',
    'text': '',
    'date': datetime.datetime(2024, 8, 25, 10, 1, 18),
    'photos': ['https://sun9-24.userapi.com/s/v1/ig2/LWuFLN1buxDEjA6uFtvhDm1uQ0_0R6kUti0Ap3AM4YQVUL-F5U5oDp1va5SaNNb3UcFdIrewAoKInjcq4K8Jv5lN.jpg?quality=95&as=32x21,48x32,72x48,108x71,160x106,240x159,360x238,480x318,540x357,640x424,720x476,1080x715,1280x847,1440x953,1632x1080&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242630&hash=f40cebcfed29621d&__ref=vk.api&api_hash=1733392655084ba6869b26e6876d_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=6762098920005&idx=14&type=39&tkn=dJ4A3LF35NCgsZDev2x_O6ZrYe8&fn=vid_w'
}, {
    'title': 'Спеши',
    'text': '',
    'date': datetime.datetime(2024, 8, 21, 13, 15, 6),
    'photos': ['https://sun9-57.userapi.com/s/v1/ig2/aBsJ4_9lZRryk1Q7v10ZBtUISJdPjNbXlF39dQJbNcWRVtQWIPYbaeOOKqq4gcoEzqwPQqCObPuklDnye0TwGO0d.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x284,240x427,360x640,480x853,540x960,640x1138,720x1280,1080x1920,1242x2208&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Сегодня свой день рождения празднует один из ведущих тренеров Калининградской области по спортивной акробатике ',
    'text': '[id27465184|Константин Гостищев]!<br><br>В этот знаменательный день мы хотим выразить вам благодарность за ваш профессионализм, преданность делу и тщательную работу.<br><br>Желаем вам крепкого здоровья, вдохновения и новых достижений как в  спорте, так и в жизни!',
    'date': datetime.datetime(2024, 8, 17, 9, 58, 22),
    'photos': ['https://sun9-46.userapi.com/s/v1/ig2/mf247k2P4FH1FIAnsH9BlWRMiiPK5nYA3thzxyLKQZxh5k_CVwN2t_2h7NNTtoFotIXIIdJzMIeftuKovzDgJa6y.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x241,240x361,360x541,480x722,540x812,640x963,720x1083,851x1280&from=bu', 'https://sun9-31.userapi.com/s/v1/ig2/7qGz4Wmv_9tHMRnxjHpIDR2848TBRCiCmi-th2GqT2LdGJ3ZmVaxk00idvylZj2qeElYcgLyEpj6F2eLr__0Su9f.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Федерация спортивной акробатики проводит просмотр:',
    'text': 'Требуются мальчики<br>- \ufeff\ufeff2009 - 2013 г.р.<br>- \ufeff\ufeffкрепкое телосложение<br>- \ufeff\ufeffподготовка в смежных видах спорта приветствуется<br>Для тренировок и выступлений в составе сборной комады<br>Калининградской области<br>Запись по телефону<br>+7 963-299-77-16',
    'date': datetime.datetime(2024, 8, 12, 14, 12, 5),
    'photos': ['https://sun9-67.userapi.com/s/v1/ig2/9ZR9-acnOGcWMRkj5_aRdhcYSVdeEWNVtRBwf9IBGTHI96WaOQFS2nIIKvaFdLHOuF0x5MJMDmhC9HOfZAAA8tvp.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x284,240x427,360x640,480x853,540x960,640x1138,720x1280,1080x1920,1280x2276,1350x2400&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Мы открываем новую группу «ПРЕМИУМ»',
    'text': '- \ufeff\ufeffподготовка к отбору<br>- \ufeff\ufeffгарантируемый результат в течение 1 года<br>- \ufeff\ufeffиндивидуальный подход к каждому спортсмену<br>- \ufeff\ufeffразвитие физических и технических навыков, способствующих достижению спортивных результатов<br>Вся информация в видео , поспеши) <br><br>Адрес: Аксакова 112 <br>Тренер: Кулинич Никита Владимирович',
    'date': datetime.datetime(2024, 8, 12, 12, 14, 14),
    'photos': ['https://sun9-1.userapi.com/s/v1/ig2/Kb_36tM1_IFiDyMi9n2me-XpsnUzJh2hXXcwktRxXnytP13wj9LIqT2Xpl5NRs938Tf3ap3LVc1Cw01hVzWipc8O.jpg?quality=95&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440,2048x2048&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242592&hash=6b3a7be644f96b46&__ref=vk.api&api_hash=17333926555fcff347ae3c6a58d9_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=6869081131752&idx=11&type=39&tkn=_owrR9XFvcX3IQ9JCiExOvbBbDA&fn=vid_w'
}, {
    'title': 'Показательное выступление в честь ДНЯ ФИЗКУЛЬТУРНИКА в ДЮСШ г. Гвардейск ',
    'text': '',
    'date': datetime.datetime(2024, 8, 10, 9, 14, 44),
    'photos': [],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242586&hash=2c2ab6f82c4031a4&__ref=vk.api&api_hash=1733392655de4de8a4f6cb5526c9_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7023125137935&idx=14&type=39&tkn=J1aDE9gdsnLBtZvZVr0rxVpoklY&fn=vid_w'
}, {
    'title': 'Показательное выступление акробатов в честь Всероссийского дня физкультурника 2024 в Центральной музыкальной школе - академии исполнительского искусства П.И. Чайковского',
    'text': '',
    'date': datetime.datetime(2024, 8, 9, 20, 16, 34),
    'photos': ['https://sun9-34.userapi.com/s/v1/ig2/desFnZMUdE7dtT2y-qj7G245KsWckINi3ukOBfPK80HHtUmx0BhPs0WpBVGwAj8p9IXJUIlxlvOPzwbQwKdJ5A33.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1350x1800&from=bu'],
    'videos': ['https://vk.com/video_ext.php?oid=-19645656&id=456242582&hash=d1efeb3a17b898b1&__ref=vk.api&api_hash=1733392655c9040789cbefe912a8_GMYDSOJQGMZTGOI'],
    'cover': 'https://i.mycdn.me/getVideoPreview?id=7155849169425&idx=13&type=39&tkn=aCllYJXQswbPqNY5Pj6__pqYens&fn=vid_w'
}, {
    'title': 'Набор в группы в г. Гвардейск ',
    'text': 'Приводя ребенка к нам вы получаете:<br> • \ufeff\ufeffВсестороннее физическое развитие<br> • \ufeff\ufeffРазвитие координации, через изучение различных акроэлемнтов<br> • \ufeff\ufeffРегулярное участие в соревнованиях<br> • \ufeff\ufeffРазвитие силы и выносливости<br>Парно-групповой вид спорта помогает ребенку социально адаптироваться<br>Самые усердные и трудолюбивые получат разряды и звания.<br>Запись и справки по телефону:<br> 8 （906） 233-60-88',
    'date': datetime.datetime(2024, 8, 8, 10, 10, 18),
    'photos': ['https://sun9-29.userapi.com/s/v1/ig2/aCoJ_rEkYS3YVw0eTG4rdGJi9bW0QhdXLfTOMGke9UMy63RDAYvtJSsKNPGFCuX6Ln9CnT7avYckCQaa-Hb8gzt-.jpg?quality=95&as=32x45,48x68,72x102,108x153,160x227,240x340,360x510,480x680,540x765,640x906,720x1020,1080x1530,1280x1813,1440x2039,1446x2048&from=bu'],
    'videos': [],
    'cover': ''
}, {
    'title': 'Внимание ',
    'text': '24 августа - 18:00<br>И<br>26 августа - 18:00<br>Во Дворце творчества Детей и Молодежи (ул. Сергеева,10 - каб. 27) состоится просмотр детей от  до  лет для зачисления в группы Начальной и Спортивной подготовки <br><br>С собой: <br>- Форма ( шорты , футболка, белые носки)<br>- Документы:<br> копия свидетельства о рождении <br> номер ПФДО<br> копия СНИЛСа<br><br>Важно - для зачисления будет необходима справка от педиатра  о допуске ребенка к занятиям Спортивной Акробатикой',
    'date': datetime.datetime(2024, 8, 5, 10, 2, 42),
    'photos': ['https://sun9-3.userapi.com/s/v1/ig2/DOlK2gCrQQVarCgPC0qBMlxSX9s19fUqFEUbRfbujiMJEnfkxc7jAviL_kzHJd56BpRMmIjmN-5yGYW9WXA9SkyI.jpg?quality=95&as=32x45,48x68,72x102,108x153,160x227,240x340,360x510,480x680,540x765,640x906,720x1020,1080x1530,1280x1813,1440x2039,1446x2048&from=bu'],
    'videos': [],
    'cover': ''
}]

articles = [
  {
    'art': 'isrc',
    'title': 'Интервью с родителем чемпиона: Фомина Кристина и Ивкова Оксана',
    'text': '<p>В данной рубрике мы будем брать небольшое интервью у родителей наших спортсменов и выкладывать его для вас.</p> <p>Сегодня мы взяли интервью у мамы Фоминой Кристины, которая является мастером спорта России по спортивной акробатике!</p> <p><strong>Добрый день, меня зовут Ивкова Оксана Александровна, я мама Фоминой Кристины.</strong></p> <p><strong>Здравствуйте, расскажите как ваш ребёнок пришёл в спорт?</strong></p> <p><strong>Оксана:</strong> Когда Кристине было 10 лет, она захотела заниматься танцами, и мы записали её в ДК «Янтарь». Там она целый год занималась хореографией, выучила танец и даже пару раз выступала перед родителями. На следующий год мы снова пришли туда заниматься, но, узнав, что будет тот же танец, решили искать другие варианты.</p> <p><strong>Почему же выбрали именно спортивную акробатику?</strong></p> <p><strong>Оксана:</strong> В разговоре с владельцем моего выпускника, я узнала об акробатике. После пробного занятия тренер сразу сказала, что Кристина будет верхней в группе. Так 1 сентября 2017 года мы начали заниматься.</p> <p><strong>Удавалось ли Кристине совмещать учёбу и спорт?</strong></p> <p><strong>Оксана:</strong> Конечно же, некоторые моменты по учёбе приходилось двигать на второй план. Но в основном она справлялась. Были хвосты в школе, но у кого их не было… В 21 час заканчивалась тренировка, в 21:30 мы были дома, и Кристина садилась за уроки.</p> <p><strong>Расскажите, как вы находили силы совмещать бытовые проблемы, работу и воспитание ребёнка с заинтересованностью в больших успехах дочери в спорте?</strong></p> <p><strong>Оксана:</strong> У нас на первом плане всегда была дочь. Мы живём на окраине города, куда ходит всего один автобус, и мне была отведена роль личного водителя Кристины: утром отвезти в школу, потом забрать домой, через два часа — снова везти на тренировку, а через 3-4 часа забрать. Так за день накатывала 200 км. Между поездками успевала сделать дела по хозяйству, принять гостей, которые приехали выбирать котёнка. Даже кошачьи выставки проводить успевала, где акробаты выступали для зрителей!</p> <p><strong>Разглядел ли тренер задатки чемпиона в ребёнке в самом начале пути? И какова была ваша реакция на это?</strong></p> <p><strong>Оксана:</strong> Мы люди с амбициями! Нам меньше, чем чемпион, не надо. Не скрою, несколько раз подходила к тренеру и спрашивала о результатах. Она честно говорила и о недостатках, и о достоинствах Кристины. Кристина как реактивный самолёт: в сентябре 2017 начала заниматься, а в феврале 2021 выполнила норматив мастера спорта.</p> <p><strong>Спортсмены, как правило, работают на пределе возможностей. Сказывались ли физические и эмоциональные нагрузки ребёнка на ваши взаимоотношения?</strong></p> <p><strong>Оксана:</strong> Нет, взаимоотношения у нас всегда были ровные. Я понимала, что после 4 часов тренировок ей хотелось тишины. Поэтому домой ехали молча или под музыку. А через час после приезда она снова тренировалась дома, отрабатывая движения до идеала.</p> <p><strong>Влиял ли спорт на жизнь всей семьи?</strong></p> <p><strong>Оксана:</strong> Конечно. Все приходящие к нам гости становились подопытными. Кристина использовала всех для своих занятий. Кому на плечи забраться, кого заставить держать её на руках. Но больше всего доставалось папе — он был её постоянным партнёром.</p> <p><strong>Замечали ли вы, как спорт воспитывал личность вашего ребёнка?</strong></p> <p><strong>Оксана:</strong> Кристина по характеру трудяга. Акробатика помогла ей преодолеть проблемы с вестибулярным аппаратом и научила преодолевать боль. Упал, ушибся — встал, улыбнулся и продолжил.</p> <p><strong>Как вы помогали с режимом питания?</strong></p> <p><strong>Оксана:</strong> С питанием проблем не было. Если тренер что-то запрещал, она этого не ела. Шоколад любит, но мы её не ограничиваем. Хочет быть в прыщах — её выбор.</p> <p><strong>Были ли моменты, когда ребёнку хотелось сдаться?</strong></p> <p><strong>Оксана:</strong> Нет, Кристина не из тех, кто сдаётся. Ласковое слово мамы и похвала тренера всегда её поддерживали.</p> <p><strong>Ваши советы родителям детей, которые занимаются спортом?</strong></p> <p><strong>Оксана:</strong> Не вмешивайтесь в работу тренера, не жалейте ребёнка и не пропускайте тренировки. Если растите спортсмена, приоритеты должны быть чёткими. Удачи и побед!</p> </body>',
    'date': '22.03.2023',
    'photos': ['https://sun9-32.userapi.com/impg/xblAf0KWRTUdgFgwd_gOSqd_CpaXXrHj42HCqw/V7KuIRAbTIk.jpg?size=1050x750&quality=96&sign=1e75a9cbec750a4d5a9071834b2d2109&type=album', 'https://sun9-17.userapi.com/impg/hscmTxD3_q3E0Q3Z7l2vepKFmuR2PaHty6Q7DA/6k9OGfC7kI8.jpg?size=720x729&quality=96&sign=383d098b530f958f03deb3886d6f7c07&type=album', 'https://sun9-54.userapi.com/impg/gKdqSJy9yr_c-kUNISGEZbe4v1ph6BUdKf_g0A/ukWwGehjE9k.jpg?size=1048x1280&quality=96&sign=21715c5d59eb1e17114830e9b7ea1a96&type=album', 'https://sun9-39.userapi.com/impg/mj0vGIBlJd6H7enE8Fm0wWqXqSBrGDm3rOlp5g/9uw-5hu5bDs.jpg?size=720x1280&quality=96&sign=204c8b871db05dab8317d4e8b25142d2&type=album']
  },
  {
    'art': 'zskvfpgs',
    'title': 'Знакомство с составом: Кривцун Вероника, Фролова Полина и Гончарова София',
    'text': '<p><strong>Давно не было нашей рубрики «Знакомство с составом».</strong> Мы просто никак не могли выбрать героев нашего интервью. Сегодня мы расскажем вам про женскую группу, трех девушек, которые влюблены в спортивную акробатику и вместе добиваются успехов в выбранном ими виде спорта: Кривцун Веронику (13 лет), Фролову Полину (18 лет) и Гончарову Софию (18 лет).</p> <p><strong>Привет! Расскажите пожалуйста, как давно вы занимаетесь акробатикой? И почему выбрали именно этот спорт?</strong></p> <p><strong>Полина:</strong> Акробатикой занимаюсь с 7 лет, начала еще в Казахстане. Летом 2019 года переехала в Калининград и продолжила заниматься. У меня особо не было выбора, так как, когда мы пришли, набор в группу уже закончился, и по счастливым обстоятельствам директором спорткомплекса был знакомый моей мамы (взяли «по блату» получается), поэтому пришлось ходить.</p> <p><strong>София:</strong> Я занимаюсь акробатикой 6 лет. С детства наблюдала за данным видом спорта, со временем интерес и желание тренироваться самой только росли.</p> <p><strong>Вероника:</strong> Акробатикой я занимаюсь не так давно, как могло показаться. Всего 4 года назад я впервые переступила порог спортзала. Он был очень маленький, в посёлке им. А. Космодемьянского. Некоторое время меня тренировали именно там, но во мне явно удалось разглядеть что-то, что сформировало мой переход в более старшую группу, следовательно, и в более оборудованный зал. Там начались более серьезные тренировки. Но с нагрузкой я справилась, меня поставили в первый состав, и история началась. Этот вид я выбрала совсем не погружаясь в здоровый образ жизни. Моя одноклассница занималась акробатикой. Важная часть — она занималась не профессионально. Я же совершенно не знала, что в акробатике существуют составы и работа в команде. Я считала, что в этом виде спорта лишь обучают разным элементам и трюкам, но мнение было ошибочно. Мой успех пришел, скорее всего, из-за зависти в сторону одноклассницы. Я хотела быть совершенней её, даже в учебе.</p> <p><strong>В составе вас трое. Сложно ли было найти общий язык с напарницами? Или вы сразу сдружились?</strong></p> <p><strong>Вероника:</strong> Наверное, сложно было довериться девочкам в плане отношений. Я боялась сказать что-то лишнее, думая, что надо мной будут смеяться, обсуждать и т. п., поэтому вечно молчала, и цитировала наперед каждое сказанное мной слово. Однако, девочки оказались не монстрами, которых я могла представлять, а абсолютно спокойными и добрыми напарницами.</p> <p><strong>Полина:</strong> Не легко уж точно.</p> <p><strong>София:</strong> Поначалу было непросто, но со временем привыкли друг к другу.</p> <p><strong>В дальнейшем планируешь связать профессию с акробатикой?</strong></p> <p><strong>Полина:</strong> Скорее да, чем нет. Акробатика на данный момент в приоритете, но не исключаю тот факт, что всё может перевернуться на 360 градусов.</p> <p><strong>София:</strong> Определённо хотелось бы связать свою жизнь с акробатикой, как в сфере профессионального спорта, так и в рабочем плане.</p> <p><strong>Вероника:</strong> Думаю, скорее нет, чем да. На данный момент мне не нравится работа тренера, так как общаться с детьми, объяснять и доносить до них необходимый для выполнения элементов материал я бы навряд ли смогла. Были мысли насчёт профессии хореографа, но на данный момент понимаю, что танцевать расслаблено и от души не получается. Мне кажется, что расслабиться на ковре во время танца — сойти с ритма настроенного на работу спортсмена. Когда я расслабляюсь в определённом движении, следующее должно быть достаточно собранным, а перестроиться сразу не получается, поэтому надо нарабатывать.</p> <p><strong>Расскажи о своём самом лучшем моменте в спортивной карьере?</strong></p> <p><strong>Полина:</strong> Затрудняюсь ответить, казалось бы на такой легкий вопрос, наверное он просто еще не наступил.</p> <p><strong>София:</strong> Было достаточно много ярких моментов. Мне запомнилось множество выездных соревнований, пьедесталов и выступлений, однако выделить что-то конкретно не могу. Думаю, всё самое запоминающееся ещё впереди.</p> <p><strong>Вероника:</strong> Лучший момент — сборы 2019. Их проводили в Витебске, они же стали первыми и последними сборами на выезде, за пределы Калининграда...</p>',
    'date': '26.10.2022',
    'photos': ['https://sun9-44.userapi.com/impg/LYK9PnH_Le0ioXRexM3PRCgYYsT9_D8kaRw_HA/h6jnEuHmSRw.jpg?size=2560x1707&quality=95&sign=8dd5396492dfad350b7ad873f44b9106&type=album', 'https://sun9-16.userapi.com/impg/FQkCjngBpgkxjZjVdKF7bOA2SiAeoBsWUj227w/S_AtzrPtfPs.jpg?size=2560x1707&quality=95&sign=1f24eeb1669dee9c3d8574f3df15c81b&type=album', 'https://sun9-52.userapi.com/impg/hqOJxuqfxnggZ7Ni_6BkOyMI5hAJluQ0dUp64Q/zccvF5h6u2A.jpg?size=1728x2160&quality=95&sign=bdea6dfba3cbf95b7f065783843e3f75&type=album', 'https://sun9-23.userapi.com/impg/Y-MzuhnxvvBQ_gLOVb_nwMhi31-fIGpRB6JV0w/vTfudlQOdzs.jpg?size=774x1032&quality=95&sign=395c948814e79cb7875f71c7e1777c1d&type=album', 'https://sun9-59.userapi.com/impg/iSQRYiuNh7L6N3uV1XE7tBJ-HsHj6G4NbJwXRA/hbVU5H29S_w.jpg?size=853x1280&quality=95&sign=6249481eebed08fc805a32441d604d3f&type=album'],
  },
  {
    'art': 'zsksoata',
    'title': 'Знакомство с составом: Ксенжик София, Оразбаева Алёна и Тятлина Алиса',
    'text': '<p><strong>Знакомство с составом: Ксенжик София, Оразбаева Алёна и Тятлина Алиса</strong></p> <p>Пришло время для нашей рубрики «Знакомство с составом». Три наших сегодняшних героини пока что имеют звания «Кандидат в мастера спорта» по спортивной акробатике, но на этом они точно не планируют останавливаться. Мы будем рассказывать вам про женскую группу, трех девушек, таких разных, во многом непохожих, но одинаково влюбленных в спортивную акробатику: Ксенжик Софию (16 лет), Оразбаеву Алёну (16 лет) и Тятлину Алису (12 лет).</p> <p><strong>Привет! Расскажите пожалуйста как давно вы занимаетесь акробатикой? И почему выбрали именно этот спорт?</strong></p> <p><strong>Алёна:</strong> Акробатикой я занимаюсь уже ровно 11 лет. Этот спорт я не выбирала, родители отдали.</p> <p><strong>София:</strong> Честно, уже не помню, потеряла счёт времени начиная со второй недели) Примерно лет 5? На рандом пошла, даже не зная куда. Подруга за компанию позвала.</p> <p><strong>Алиса:</strong> Акробатикой занимаюсь 4 года с 9 лет. Я выбрала акробатику совершенно случайно. В первый день я пришла на отбор к Елене Владимировне Кондратьевой, но так как я была не сильно гибкая и была немного слабая меня направили к Ольге Владимировне Незговоровой.</p> <p><strong>В составе вас трое. Сложно ли было найти общий язык с напарницами? Или вы сразу сдружились?</strong></p> <p><strong>Алёна:</strong> С девочками легко было найти общий язык.</p> <p><strong>София:</strong> По началу было сложно). Характеры имеют свойство не сходится. Часто закрываем глаза на многие ситуации, но на данный момент все тихо-мирно, в общем, как и должно, наверное, быть. Работа идёт, не ссоримся, и все отлично!</p> <p><strong>Алиса:</strong> Общий язык нашли довольно быстро.</p> <p><strong>Общаетесь ли вы вне тренировок?</strong></p> <p><strong>Алёна:</strong> Вне тренировок мы не общаемся.</p> <p><strong>София:</strong> Скорее нет, чем да. Обычно общаемся только по делу, иногда новости и мемы скидываем друг другу, но это так, для справочки.</p> <p><strong>Алиса:</strong> Общаемся, но не часто(</p> <p><strong>В дальнейшем планируешь связать профессию с акробатикой?</strong></p> <p><strong>Алёна:</strong> Пока не знаю, хотелось бы.</p> <p><strong>София:</strong> Посмотрим, я не ручаюсь за себя через год, но на данный момент жизни - не думаю. Вряд ли смогу связать свою жизнь со спортом впринципе.</p> <p><strong>Алиса:</strong> Насчёт профессии пока что точно не знаю, но иногда думала об этом.</p> <p><strong>Расскажи о своём самом лучшем моменте в спортивной карьере?</strong></p> <p><strong>Алёна:</strong> Хороших моментов было много, но самый лучший был, когда меня перевели из верхних в нижние и поставили к Соне в тройку.</p> <p><strong>София:</strong> Лучший момент? Достаточно банальный ответ: когда очень долго у кого-то из состава что-то не получается, но путем попыток в один момент желаемое выполняется. А случайность это или наглость - уже не шибко важно. Самоудовлетворение, что сделал то, что долго не мог - одно из лучших ощущений впринципе.</p> <p><strong>Алиса:</strong> Наверное самым лучшим моментом в акробатике было, когда меня перевели из младшей группы в старшую🤸🏼‍♂️ И когда выполнили КМС).</p> <p><strong>Какие сборы вам запомнились больше всего?</strong></p> <p><strong>София:</strong> Я была только на двух: один раз в Минске, другой в Витебске. Пожалуй в Витебске запомнилось больше. Было много славных моментов, да и достаточно атмосферно.</p> <p><strong>Алиса:</strong> У меня были всего лишь одни сборы в Витебске, поэтому запомнились именно они).</p> <p><strong>Алёна:</strong> В этом составе на сборы я не ездила, но больше всего мне понравились мои самые первые сборы, они проходили в Литве.</p> <p><strong>А что больше всего запомнилось на сборах в Литве и сколько лет тебе было?</strong></p> <p><strong>Алёна:</strong> 8 лет. То что я тогда впервые была так далеко от родителей и долго по времени, то что мы жили на матах и однажды даже бегали кросс 50 кругов по стадиону, утренние тренировки под солнцем, хореография и квест по всему спортивному центру.</p> <p><strong>Что для тебя акробатика?</strong></p> <p><strong>Алёна:</strong> Акробатика для меня - это моё самое любимое занятие, которым я бы хотела заниматься и после выполнения.</p> <p><strong>София:</strong> Долго думала над этим вопросом изначально. Скорее возможность отвлечься от всего остального. Все же тренировки отличаются от моего стиля и ритма жизни почти кардинально, в том числе и люди, с которыми я занимаюсь, диаметрально противоположны. Да и Мастера Спорта хочется).</p> <p><strong>Алиса:</strong> Для меня акробатика как второй дом и вторая семья.</p> <p>Благодарим девочек за ответы и желаем им осуществления всех задуманных планов😉</p>',
    'date': '26.09.2022',
    'photos': ['https://sun9-72.userapi.com/impg/qpWlpIS5j1a5pri-gMRwAAvhVyHgQ2w5r7T11A/NjL2IIynNEU.jpg?size=960x1280&quality=95&sign=830723c87a31612f999791c544caacd2&type=album', 'https://sun9-44.userapi.com/impg/j7mbu0_VLYlprFQKUo8P1_q8ZH9XLHkJdBo9qA/KBxUwTAMUZs.jpg?size=852x1280&quality=95&sign=2f508f00d47461e668c3f5b4546b4f72&type=album', 'https://sun9-13.userapi.com/impg/Nac1oogPrAqezvcutSpGq9xk-SkWOzQJrYufPA/joqZKaALELQ.jpg?size=1280x852&quality=95&sign=db3a4c8e1c4a4b437a912f3de3f32509&type=album', 'https://sun9-79.userapi.com/impg/m8VAlX6lRJ7wPYFItFj9YIZUZFa3OiWDGWSAZQ/Yib-90owq10.jpg?size=852x1280&quality=95&sign=35b381be1317ac5a4c741ec443a4792e&type=album'],
  },
  {
    'art': 'zsbnbe',
    'title': 'Знакомство с составом: Беляева Наталья и Беляева Елизавета',
    'text': '<p><strong>Встречайте нашу ежемесячную рубрику «Знакомство с составом».</strong> Две наших сегодняшних героини влюблены в акробатику и имеют звания «Мастер спорта России» по спортивной акробатике. Нет, мы будем рассказывать вам не про пару, а про семью акробатов - маму и дочку: Беляеву Наталью Викторовну и Беляеву Елизавету.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №1</strong></p> <p><strong>Расскажите, сколько по времени вы тренировались?</strong></p> <p><strong>Наталья:</strong> Я тренировалась с 10 до 20 лет. На данный момент не тренируюсь, а тренирую.</p> <p><strong>Елизавета:</strong> Акробатикой я занимаюсь очень давно, примерно с 5 лет. Многие воспоминания связаны именно с ней. Единственное, что я помню с детства, это были именно тренировки и моменты из зала.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №2</strong></p> <p><strong>Почему выбрали именно акробатику?</strong></p> <p><strong>Наталья:</strong> Акробатика - это любовь с первого взгляда! Заглянула однажды в спортзал, а там шла тренировка у Елены Владимировны Кондратьевой, и поняла, что это именно тот вид спорта, которым бы я хотела заниматься. Три раза я проходила отбор, и, естественно, меня не взяли — была слишком слабая. Но у меня характер — если я что-то решила, то дойду до намеченной цели. Мама просила Елену Владимировну взять меня заниматься. Слава Богу, она сжалилась и взяла меня. Так и начался мой путь.</p> <p><strong>Елизавета:</strong> Ещё когда я была ребёнком, часто ходила с мамой в зал. Мне очень нравилась атмосфера и эстетика этого спорта. Акробатика совмещает в себе лёгкость хореографии и трудность элементов, и в совокупности это выглядит как произведение искусства. Эти детские воспоминания засели глубоко в моей душе. И когда представилась возможность, я без раздумий выбрала именно этот спорт.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №3</strong></p> <p><strong>Наталья, расскажите, как поменялись условия тренировок для спортсменов, если сравнивать нынешние условия с условиями, в которых начинали тренироваться вы?</strong></p> <p><strong>Наталья:</strong> Условия изменились колоссально. Сейчас у акробатов есть хороший помост, дорожка, батут, лонжи, зал отдельный. А когда-то не было ничего. Занимались в школьном спортзале, потихоньку смогли зацепиться во дворце творчества детей и молодёжи на ул. Сергеева. Помост был собран своими руками, но радовались и такому.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №4</strong></p> <p><strong>Наталья, когда вы начинали заниматься, сразу знали, что выполните мастера спорта или были другие цели?</strong></p> <p><strong>Наталья:</strong> Вообще не думала про мастера сначала. Просто приходила и получала удовольствие от тренировок, просто нравилось тренироваться. А со временем, конечно, появилась цель — звание «Мастер спорта».</p> <p><strong>Лиза, недавно пришёл приказ о долгожданном присвоении звания Мастера Спорта. Расскажи, пожалуйста, тяжело ли было достичь этой цели?</strong></p> <p><strong>Елизавета:</strong> В жизни мы ставим себе много целей, и всегда для их достижения приходится прикладывать уйму усилий. Так и для достижения моей одной из самых главных целей в жизни мне потребовалось приложить кучу усилий. Конечно, бывали трудности и недопонимания, но благодаря прекрасному тренерскому составу тренировки становились в радость. Хотя и приходилось преодолевать боль и слёзы, но радость побед затмевала их. Также благодаря поддержке тренеров на соревнованиях чувствовала себя уверенной.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №5</strong></p> <p><strong>Планируешь дальше связывать своё будущее с акробатикой?</strong></p> <p><strong>Елизавета:</strong> На данный момент у меня нет чёткого ответа на этот вопрос, но думаю, даже если моя профессия не будет связана с акробатикой, она навсегда останется в моем сердце.</p> <p><strong>Что тебе больше всего запоминалось за годы тренировок?</strong></p> <p><strong>Елизавета:</strong> Больше всего запомнились мне именно сборы. Это было время, когда наш коллектив превращался в одну сплочённую семью. Все были готовы прийти тебе на помощь и поддержать тебя.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №6</strong></p> <p><strong>Наталья, расскажите, пожалуйста, почему вы решили стать тренером?</strong></p> <p><strong>Наталья:</strong> Акробатика — это стиль жизни, философия, смысл жизни. Ну как с этим можно завязать? Никак. А понимание было, что век спортсмена недолгий, вот и пришла логичная мысль, что всё это будет продолжаться, если стать тренером.</p> <p><strong>Знакомство с составом: Беляева Наталья и Беляева Елизавета, изображение №7</strong></p> <p><strong>Наталья, расскажите, пожалуйста, почему вы не стали тренировать дочку самостоятельно?</strong></p> <p><strong>Наталья:</strong> Я тренировала Лизу до 7 лет, но потом отдала её другому тренеру. Потому что своих тренировать очень тяжело. Внутри борется тренер и мать. Для матери каждое выступление, каждая тренировка — всё является идеально исполненным, оттренированным, и все ошибки — ну подумаешь, со всеми случается. Для тренера: на тренировке никаких поблажек, всё должно быть чётко, по плану, без нытья, правильно и отточено. Любое выступление должно быть идеальным и т. д. Доходило до того, что я не разрешала на тренировках называть меня мама, а только по имени-отчеству. Дети не знали, что Лиза — моя дочь. Однажды на чешках у неё бант оторвался во время тренировки. Она подошла ко мне и говорит: "Наталья Викторовна, передайте моей маме, что у меня бант оторвался и его надо пришить!" Я с серьёзным видом пообещала, а дома хохотала. Не тренирую, чтоб не дать слабину, чтоб не переносить всё это в дом.</p> <p><strong>Благодарим Наталью и Елизавету за ответы и желаем им осуществления всех задуманных планов😉</strong></p>',
    'date': '31.07.2022',
    'photos': ['https://sun9-16.userapi.com/impg/h2aukCQf48G48K_FyY_A6Mh2NjTTECwMGhqR1Q/vBMbNA4u494.jpg?size=1023x1280&quality=95&sign=e54b4561f43e1807afb21b1af619b340&type=album', 'https://sun9-65.userapi.com/impg/KsfHL7UppmPyeJgfvdIeXMHA7KoltJ2NdrbotA/gsmdYY_dVZw.jpg?size=852x1280&quality=95&sign=e29f533b6ef3afeb07628aed45415f23&type=album', 'https://sun9-50.userapi.com/impg/R7br5bqt3loWTPMQsEg7xLmyRHMq06X_6c2Hjg/Jp6yplA-MSo.jpg?size=1080x727&quality=95&sign=e4e6651e0e4ac91364f503e380c96138&type=album', 'https://sun9-16.userapi.com/impg/tNZuF0kU9efoEE912wyco0ARYXXiO8ssbjTxNQ/vZ8w5zKYFpA.jpg?size=1280x913&quality=95&sign=379804d086aad31d38261c749b86e3be&type=album', 'https://sun9-49.userapi.com/impg/XVUCWcu_gPzK8qmIUjJkJVQIhhe7EAT-Gt24Ew/8__Uymh9oBA.jpg?size=940x1280&quality=95&sign=9dad762bd4a0230eb593d435822f6ce7&type=album'],
  },
  {
    'art': 'zslabu',
    'title': 'Знакомство с составом: Лузганов Александр и Базылеева Ульяна',
    'text': '<p><strong>Долгожданное возвращение рубрики «Знакомство с составом».</strong> Сегодня на наши вопросы дадут свои ответы Лузганов Александр и Базылеева Ульяна.</p> <p><strong>Знакомство с составом: Лузганов Александр и Базылеева Ульяна, изображение №1</strong></p> <p><strong>И для начала классический вопрос: как давно вы тренируетесь? Почему выбрали именно акробатику?</strong></p> <p><strong>Александр:</strong> Я пришёл на акробатику в 4 года в 2010 году, и занимаюсь уже 12 лет. Когда меня решили отвести на спорт, то дали выбрать вид спорта, и как то я выбрал акробатику. Уже и не помню почему.</p> <p><strong>Ульяна:</strong> Начала тренироваться в 2012 году, когда мне было 3 года в Казахстане (город Павлодар), а летом 2021 переехала в Калининград. В общей сложности занимаюсь уже 10 лет. Меня отвели на акробатику родители. Также параллельно до 7 лет занималась фигурным катанием.</p> <p><strong>Знакомство с составом: Лузганов Александр и Базылеева Ульяна, изображение №2</strong></p> <p><strong>Давайте немного поговорим о вашем составе. Расскажите немного про друг друга. Как вы встретились?</strong></p> <p><strong>Александр:</strong> В июне прошлого года, я спокойно себе отдыхал в Крыму и буквально за 3-4 дня ушла моя прошлая напарница и мне нашли новую. И когда я приехал обратно, нас познакомили тренера на тренировке.</p> <p><strong>Ульяна:</strong> Пришла я на тренировку, а мне дали какого-то негра (комментарий Александра: «ну я тогда весь загорелый приехал»).</p> <p><strong>Какое было первое впечатление друг о друге? Что больше всего испугало? А что понравилось?</strong></p> <p><strong>Александр:</strong> Я говорил о своём новом составе с другими спортсменами ещё в Крыму, и мне говорили, что она вообще замечательная, спокойная, все хорошо делает. Испугало, что она была более опытной и много чего делала того, что не умел я. Но это же и понравилось.</p> <p><strong>Знакомство с составом: Лузганов Александр и Базылеева Ульяна, изображение №3</strong></p> <p><strong>В этом году вы не встали на пьедестал на первенстве 11-16? Почему?</strong></p> <p><strong>Александр:</strong> В первый день первенства я выступил очень уверенно, но потом атмосфера соревнований нагнетала меня, и остальные дни были менее уверенными.</p> <p><strong>Ульяна:</strong> Считаю, что мы были недостаточно хороши и нужно было больше тренироваться.</p> <p><strong>А вот на первенстве 12-18 вы вышли в финал. Вы это ожидали или нет? Какие эмоции испытали?</strong></p> <p><strong>Александр и Ульяна:</strong> Вообще не ожидали, после первенства 11-16 мы уже эмоционально устали и хотели просто выступить и уехать. Поэтому не рассчитывали вообще на что-то. Очень обрадовались.</p> <p><strong>Знакомство с составом: Лузганов Александр и Базылеева Ульяна, изображение №4</strong></p> <p><strong>Довольны ли вы результатами в этом году?</strong></p> <p><strong>Александр:</strong> Результатами доволен, буду улучшать.</p> <p><strong>Ульяна:</strong> Нормально.</p> <p><strong>Какие планы на будущий спортивный год?</strong></p> <p><strong>Александр и Ульяна:</strong> Планов много: сильно улучшить результаты, встать на пьедестал на первенстве России. Планы и цели немножко разные вещи, поэтому планы есть, а цели ещё не поставили.</p> <p><strong>Какой старт за всё время больше всего понравился и чем именно запомнился?</strong></p> <p><strong>Александр:</strong> Запомнилось первенство России 11-16 лет и 12-18 лет. Близко подошли к пьедесталу на 11-16, прошли в финал по 12-18, а по некоторым упражнениям поставили рекорды по оценкам.</p> <p><strong>Ульяна:</strong> Запомнились первые соревнования в году в Новомихайловке, было тепло, пляж, море и вообще весело было.</p> <p><strong>Знакомство с составом: Лузганов Александр и Базылеева Ульяна, изображение №5</strong></p> <p>Благодарим ребят за ответы и желаем им осуществления всех задуманных планов😉</p>',
    'date': '27.06.2022',
    'photos': ['https://sun9-48.userapi.com/impg/jh6git0pwvoo5piLuRC3BygpWlblprfy5Zdm6Q/pub07Iny2QE.jpg?size=1170x780&quality=95&sign=f47c8ad45bf27a6f8c15f10a07f9c374&type=album', 'https://sun9-48.userapi.com/impg/Tc7oK1vMrISttScVgTUtCAjE3M_6mxqshtkkTA/BsyiBPVboO4.jpg?size=1024x1280&quality=95&sign=76d0c3948852f9aa194768ace97ed240&type=album', 'https://sun9-59.userapi.com/impg/1YlFVkpKFqLJv2sK8ouX7IdzzRL6R8rBY8smvw/KOXKT7EDwAw.jpg?size=1024x1280&quality=95&sign=fc1229a03ca65352f0e9c426d9566d18&type=album', 'https://sun9-40.userapi.com/impg/_-YX6RikbyYhOQhHVVM0EFJihZjmpMwkLQ47pg/w0vBsNmBkfA.jpg?size=1024x1280&quality=95&sign=da9669c01f28c945a1fd71e88e597051&type=album', 'https://sun9-66.userapi.com/impg/svxrSyTFk62rJc9_76_yoAarpdYlFJWmceg5Rw/0ZdTRlzMAXM.jpg?size=1170x780&quality=95&sign=562b75fc2c3957baa0f0d567e03c1752&type=album'],
  },
  {
    'art': 'zsbkim',
    'title': 'Знакомство с составом: Белосток Ксения и Ильина Мария',
    'text': '<p><strong>Сегодня мы познакомимся поближе с прекрасной Женской парой: Белосток Ксения и Ильина Мария.</strong></p> <p><strong>Мастера Спорта, стипендиаты Мэра и Губернатора, члены основной Сборной Калининградской обл…</strong> Девочки, вы поразили меня, еще не поговорив с вами! Начнем с малого, расскажите немного о себе: где учитесь? Сколько вам лет? И как вообще вас занесло в такой красивый и зрелищный спорт?</p> <p><strong>Ксения:</strong> Да мы такие, крутышки) хахаха) Мне 17 лет. Я учусь в Училище Олимпийского Резерва на 3 курсе. Учусь без долгов, все успеваю закрывать, не всегда вовремя конечно, но… мне делают «поблажки» за красивые глаза)) Очень часто приходится нагонять учебу во время выездов, это единственная сложность. Заниматься акробатикой я начала дома, лет в 9… Стояла разные стойки, кувыркалась постоянно, висела на всех ветках двора хах, и мама, дабы я не убилась во дворе, отвела меня в зал. Привела меня она сюда в 12 лет и по сей день я здесь и уходить не собираюсь).</p> <p><strong>Мария:</strong> Мне 13. Я отличница-восьмиклассница))) Успеваю во всем! Что в спорте, вечно стремлюсь к золотым медалям, что в школе, тоже стремлюсь к золотой)) В акробатике я с 5 лет, потому что что? Правильно! Я надоела родителям вечно стоять на голове на диване. С каждым годом, совмещать учебу и спорт становится труднее, из-за усложнения программы и там и там и многих других факторов… Ну и как обычно, в сумке на соревнования у тебя: выступательный костюм, разминочный, умывашка и учебники с тетрадками…</p> <p>Ну… Беря интервью у акробатов, я уже понял, что вы «можете уехать за тысячи километров от школы, но школа от вас не уедет никуда»… Но вы молодцы, что справляетесь! Дай бог будете успевать по жизни всегда и во всем!</p> <p><strong>А как насчет вашего старта в акробатике? С каких составов вы начинали? И с кем стоите сейчас?</strong></p> <p><strong>Ксения:</strong> С самого начала, как я пришла, буквально на 1-3 день меня сразу поставили в Женскую Группу. Мы недолго простояли, немного посоревновались. Позже меня поставили в Женскую Пару с Ульяной Магиной. С ней мы успели покататься по очень многим городам и странам. Выполнили КМС и нас расставили. И я получила в руки маленькую Машу, с которой мы за 1,5 года вместе успели сделать МС РФ)))</p> <p><strong>Мария:</strong> Мой первый состав был Смешанной Парой. Это был лишь начальный опыт и некий старт в акробатику. Стояли без особой инициативы, то 3 место, то 2, то никакое. Позже меня поставили к большому нижнему Никите Кулиничу и вот с ним мы уже работали серьезно. Усложняли программу, ездили и брали места на СЗФО, Международных сор-ях и Первенствах РФ. И вот, около 1,5 лет назад, меня поставили к Ксюше, с которой мы по сей день грызем ковер и разрываем судей своими харизматичными танцами)</p> <p>Охх… Аж жарко стало от таких слов… Фух.. Так девчонки, может расскажете немного о своих планах на будущее? Какие цели в спорте?</p> <p><strong>Ксения:</strong> МС РФ у меня в кармане, к МСМК не особо стремлюсь, но если будет – лишним не будет))) хах) А так, в целом хочется отработать уже поставленную программу и композиции на 101%, чтобы выступать достойно и изумлять судей. А там и МСМК уже не за горами))</p> <p><strong>Мария:</strong> Я очень хочу и дальше ездить на соревнования, увидеть новые города и страны, завести новые акробатические знакомства и выступать так шикарно, как не выступала никогда! Ну и конечно МСМК)) куда без него</p> <p><strong>Уверен, что именно ВЫ будете ПЕРВЫМИ МСМК в Калининградской Акробатике! Верю в вас!!!</strong></p>',
    'date': '15.09.2021',
    'photos': ['https://sun9-32.userapi.com/impg/6B-xyte0cqt9weBC4Sa_YVhGFqL6tjwBsBlbQw/pdhTGBZw7U8.jpg?size=828x1090&quality=96&sign=7a0b08d852db2347ab2f88f7bf3c4e1a&type=album', 'https://sun9-72.userapi.com/impg/qSSX-ZfZpxznM1BdKzpRhEWdz1buxPBjD5j9uQ/-VFZaQLvcy0.jpg?size=1440x1920&quality=96&sign=c2b297d8f6abac1eb0f2c2fee8ea7c19&type=album', 'https://sun9-34.userapi.com/impg/nsSbIkLSKJe7Vso0BDiVZnXWHiTfqHomGhHv4Q/YZE6g4VW68k.jpg?size=453x604&quality=96&sign=ef882348fed2ba31d22a23c2625afd47&type=album', 'https://sun9-54.userapi.com/impg/yDz2QyFe8w6cK214PwxI7UdlHU6SVkyYJ0eFig/NLvdEUfVXng.jpg?size=828x590&quality=96&sign=a238c45bf80e56b6fa5c42656ea539f9&type=album'],
  },
  {
    'art': 'zsdapvknfr',
    'title': 'Знакомство с составом. Дробыш Александр, Петрунин Владислав, Картавых Никита и Фарзалиев Рустам',
    'text': '<p>Здоровые, высокие, веселые парни, шикарные друзья, сплоченная команда, кратко говоря: 4 богатыря-Мастера Спорта РФ. Знакомьтесь, мужская группа, члены Сборной Калининградской области и РФ: Дробыш Александр, Петрунин Владислав, Картавых Никита и Фарзалиев Рустам</p> <p>Парни! Мы уже знаем, что вы все Мастера Спорта РФ и очень приятно с вами познакомиться и в целом узнать, кто вы и что из себя представляете.</p> <p><strong>Парни:</strong> Спасибо! И нам очень приятно рассказать о нас, как о личностях, о наших достижениях и целях на будущее!</p> <p>И так начнем с простых вопросов. Расскажите немного о себе, а именно: Сколько вам лет? И со скольки лет вы в спорте?</p> <p><strong>Дробыш Александр:</strong> Мне 17 лет. Занимаюсь спортом вроде… Всю свою сознательную жизнь, хах) А в Спортивную акробатику пришел в 2008г. Мама привела, чтобы дома не стоял на голове. Привела чтобы просто занимался, а не бегал по дворам, ну чтоб был чем-то да занят. Никто не ожидал, что это станет моим кредо и результаты будут… ухх…</p> <p><strong>Петрунин Владислав:</strong> Мне 19 лет. Акробатикой я занимаюсь уже 8 лет, с 2013г. Ой, где я себя только не пробовал. И в футбол играл, и на карате приемы учил, и вроде еще что-то было, но не значительное. В акробатику привели родители, ну а что? Там не хочу, там не нравится, и тд. А в акробатику затянуло так затянуло хах) Уже сейчас понимаю, что нравится этот вид спорта не только из-за его неописуемой красоты и зрелищности, а еще и потому, что равномерно развивается общая физическая форма и не маленькая такая дисциплина.</p> <p><strong>Картавых Никита:</strong> Мне 17 лет. В спорте я 13 лет, и кроме акробатики не пробовал ничего другого) Аналогично с парнями, оказался на акробатическом ковре благодаря родителям. По началу я не придавал особого значения моему «увлечению». Для меня это была «просто секция» чтоб чем-то да занимался. Было сложно выполнять физические упражнения, качать мышцы, вечная растяжка… уфф…. Для меня это был просто АД. Но теперь на этом построено мое будущее, и… Спасибо Маме и Папе, что привели меня в правильное место!</p> <p><strong>Фарзалиев Рустам:</strong> Мне 13 лет. На акробатику привела бабушка в 5 лет, чтобы подтянуть физическую форму. В другом ничем себя никогда не пробовал, да и не собираюсь) Тут классно) С ребятами нагоняем сложную программу, чтобы начать покорять МИР!!!!</p> <p>Ну судя по вашим рассказам, я думаю, что вы не очень то и жалеете, что не могли поиграть дома в компьютер или побегать по двору с палками. Ребята, пару слов про учебу. Где учитесь? Как успехи? Мешает ли учеба спорту или наоборот?</p> <p><strong>Дробыш Александр:</strong> Я в 11 классе, учусь без единой тройки и собираюсь поступать в Санкт-Петербург. Учеба мешает спорту хахаха</p> <p><strong>Петрунин Владислав:</strong> Я перешел на 2 курс БФУ по направлению «Пространственное планирование и управление приморских территориями и морских акваторий». Сложно, но что поделать. Ноутбук под руку и поехал на соревнования) Выступать, гулять по городу и не пропускать учебу.</p> <p><strong>Картавых Никита:</strong> Я учусь на 2 курсе в КМРК. Учеба никак не мешает заниматься. Конспекты и учебные пособия всегда со мной)</p> <p><strong>Фарзалиев Рустам:</strong> Я учусь в Кадетском корпусе им. А. Невского в 7 классе. Учусь спокойно, если какие-то хвосты или долги всплывают из-за выездов, то по приезду, преподаватели меня абсолютно понимают и даже помогают сдать мне тот или иной предмет.</p> <p>Расскажите нам немного о вашем составе и о том, в каких составах вы стояли</p> <p><strong>Дробыш Александр:</strong> Я всю жизнь стою в четверке и менять вид не вижу смысла.</p> <p><strong>Петрунин Владислав:</strong> Я как и Саня, всегда стоял в мужской группе. Для меня это самый зрелищный вид в акробатике. 4 парня залазят друг на друга и создают 6-ти метровую пирамиду и еще умудряются в ней менять позы и стойки! Подкидывают верхнего под потолок, ловят и сразу кидают еще… Что может быть круче?</p> <p><strong>Картавых Никита:</strong> Никогда не стоял нигде, кроме четверки. Пацаны менялись, но сейчас это мой лучший и самый успешный состав. С парнями у нас особая команда, мы столько всего уже пережили вместе. И удачи, и поражения и столько городов и стран увидели, и что только не происходило.</p> <p><strong>Фарзалиев Рустам:</strong> Я стоял очень много раз в Мужской паре, в четверках, потом опять в МП. Менял менял составы, пока не нашел ту самую «команду мечты!». Как раз таки меня и кидают под потолок и ловят. Это незабываемые и неповторимые ощущения и чувства!</p> <p>Парни, ну вы меня удивляете! А как у вас с соревнованиями? Расскажите про свои выезды:</p> <p><strong>Парни:</strong> Ну на наших счетах неисчисляемое кол-во соревнований, как в РФ так и за границей. Удачные практически все. Самые самые, это конечно 2 место на Первенстве РФ 12-18 по балансовому упражнению в 2018г. Вот тогда мы ощутили настоящий вкус успеха! Затем в следующем году мы повторили успех, и еще раз дважды взяли пьедестал на том же Первенстве РФ и отобрались в Сборную РФ!</p> <p>Как приятно слышать, что такие молодые и перспективные парни, уже дорожат своими достижениями и рвутся только вперед к еще большим победам и успехам! Молодцы! А какие планы на будущее? В плане спорта:</p> <p><strong>Дробыш Александр:</strong> Конечно заканчивать заниматься не хочется, но учеба для меня не менее важна. Поэтому величайших высот уже вряд ли успею добиться, но а так выполнить МСМК. Чем черт не шутит, правильно?</p> <p><strong>Петрунин Владислав:</strong> Из планов на спорт, это продвижение в Сборную РФ в категории 14+ и выполнение МСМК. А там как уже пойдет. Не люблю загадывать)</p> <p><strong>Картавых Никита:</strong> Ну со спортом я уже закончил, поэтому могу лишь рассказать о планах на жизнь. В первую очередь это продвижение себя по Морскому делу. Хочу ходить в море.</p> <p><strong>Фарзалиев Рустам:</strong> Для меня главное сделать МС РФ, и остаться в живых хах) А в дальнейшем конечно МСМК и даже больше)</p> <p>Ребята! Вы очень классные. Желаю вам достичь всего, что вы задумали. Чтобы все ваши планы и цели непременно осуществились! Здоровья и никаких травм! Ждем вас с удостоверениями МСМК и как можно скорее) хах)</p> <p><strong>Парни:</strong> Спасибо!</p>',
    'date': '28.06.2021',
    'photos': ['https://sun9-16.userapi.com/impg/VQCNKSUvrKbdYaWU-YhB-VrhGMN2rIYyLWIIvw/ZbkBi-BMjdg.jpg?size=1066x1600&quality=96&sign=dee0a0da8a7c7a62ea6b934c72bd2bab&type=album', 'https://sun9-14.userapi.com/impg/nBG7fvZZaVvDdzckrGOetKLUnvxst04lb3NYYw/qXOdYEkEu0k.jpg?size=2560x1709&quality=96&sign=76b690782c89ad314675135bfb9eab4c&type=album', 'https://sun9-28.userapi.com/impg/ytX2lf6xvEHwX-cuoxHjNqzmmUvf75EOpw25dw/fRh7wH3CGMI.jpg?size=1648x2013&quality=96&sign=4dd10e8403b974ca163ab716cf132990&type=album', 'https://sun9-35.userapi.com/impg/-GQYEkP85d9xBmNV12Q0vQHuaYod3XMJ1cVHOQ/aZ_uJehScWE.jpg?size=2560x1709&quality=96&sign=13536ca782bd09d7f7254dc5cffb51f4&type=album', 'https://sun9-35.userapi.com/impg/rj8hsJIfac0JJLIHRKTSqUOhrEe6OXg9x_y6ow/1dAafr-g5H4.jpg?size=1066x1600&quality=96&sign=ba6bdda59f0e08f430eb7d00459a3437&type=album'],
  },
  {
    'art': 'zsck',
    'title': 'Знакомство с составом. Четверка красавчиков!',
    'text': '<p>4 красавчиков! Именно так себя называют эти 4 подрастающих богатыря Пименов Лев, Лукиянчук Иван, Брусницын Василий и Сухомлинов Егор. В (сегодняшнем) интервью мы узнаем у парней: Кто они и что из себя представляют, как по отдельности, так и в составе? Чем они занимаются в свободное от Акробатики время? И какие у них планы на будущее в спорте?</p> <p>И так, богатыри, расскажите немного о себе. Сколько вам лет? С какого возраста вы в спортивной акробатике? Пробовали ли вы что-то до акробатики?</p> <p><strong>Иван:</strong> Привет, я Ваня, мне 13 лет. В акробатику меня отдала мама в 4 года, чтобы по дворам не носился, а занимался спортом. Был красивым и сильным. До акробатики занимался футболом</p> <p><strong>Василий:</strong> Привет, я Вася, но парни меня называют Васёк. В акробатику я пришел за своим братом в 9 лет и сейчас мне, как и Ваньку, 13 лет. Брату очень нравилось ходить и он постоянно звал меня и вот я здесь) Пробовал танцы, я и сейчас ими занимаюсь, каратэ, играл на аккордеоне в музыкальной школе</p> <p><strong>Лев:</strong> Я Лев, и хожу с 4 лет, а сейчас мне 9. Мама привела, чтоб был высоким, сильным и красивым спортсменом. Пока что получается всё, кроме быть высоким))) Ну мне и не надо, потому что я верхний. Пробовал футбол, плавание.</p> <p><strong>Егор:</strong> Меня зовут Егор Сухомлинов. Сейчас мне 12, а заниматься акробатикой я начал в 6 лет в г. Нижневартовск. Начал свой путь акробата я с роли Верхнего в Мужской паре. Летом 2020 я приехал в Калининград и встал к парням</p> <p>КРУТО! А у вас есть хобби? Чем вы занимаетесь в свободное от Акробатики время?</p> <p><strong>Иван:</strong> Я люблю поиграть в компьютер и с пацанами кататься на самокатах. Прыгать и крутить разные трюки на них</p> <p><strong>Василий:</strong> Я тоже катаюсь на самокате с парнями</p> <p><strong>Лев:</strong> Да не, особо ничего нет такого</p> <p><strong>Егор:</strong> Самокат</p> <p>Расскажите-ка нам, в скольких соревнованиях вы уже участвовали? И какие были самые запоминающиеся?</p> <p><strong>Иван:</strong> Я участвовал примерно в 50 соревнованиях, и в основном на пьедестале так как наш вид, мужские группы, один из самых редких. Самые интересные соревнования были в Воронеже в феврале 2020. Было очень много, порядка 15-ти достойных и весьма сильных соперников. Было интересно с ними побороться</p> <p><strong>Василий:</strong> Примерно в 30. Интересно было когда в Литве соревновались со смешанной парой</p> <p><strong>Лев:</strong> я не знаю, мало ещё. Интересные были самые первые соревнования в четверке с парнями в Воронеже</p> <p><strong>Егор:</strong> Да я много уже прошел) И по 12-18, и по 13-19 выступал. Интересно было когда ездили в Омск. Было невероятно холодно, и просто огромное кол-во соперников, около 20, и мы встали на 2 место</p> <p>Как родители относятся к тому что вы так часто выезжаете на соревы, пропуская учёбу:</p> <p><strong>Иван:</strong> Я в 7 классе. Учусь на 5, на выездах уроки делаю постоянно</p> <p><strong>Василий:</strong> «Лишь бы успевал школу»-моя мама. Я отличник, учусь в 7классе</p> <p><strong>Лев:</strong> Я хорошист в 3 классе. Родители говорят: Да приедешь догонишь программу)</p> <p><strong>Егор:</strong> Хорошист в 6кл. На выезды беру уроки</p> <p>Планы личные и составом:</p> <p><strong>Иван:</strong> В планах личных это МС РФ. В составе, это чтобы Вася бросил танцы и мы тренировались чаще</p> <p><strong>Василий:</strong> Личные это МС РФ, и остаться в 4 навсегда</p> <p><strong>Лев:</strong> Сделать МС РФ, прыгнуть 3 винта и Победить на Кубке мира!!!</p> <p><strong>Егор:</strong> Сделать МС РФ. Попасть в сборную России</p> <p>Следующий выезд?</p> <p><strong>Все:</strong> СЗФО. План: ПОБЕДА!</p> <p>Желаю вам придерживаться вашего плана и осуществить его) Удачи!</p>',
    'date': '17.12.2020',
    'photos': ['https://sun9-4.userapi.com/impg/l6kQaOC8HLYPij4zdeVBKISYNUgQZfMEJ1tvKw/Y2DnTci3pzc.jpg?size=1280x853&quality=96&sign=91caf79babc62c4a7f97afed94c0bf91&type=album', 'https://sun9-48.userapi.com/impg/4SY6XjyRmarah7f4g___swMJAAaT8BjeNZvwUQ/1bELaltZd-s.jpg?size=1200x1600&quality=96&sign=2355d0bca76386fc8eb5399d55dddf7e&type=album', 'https://sun9-35.userapi.com/impg/sRM-8Pf2sA3mt77cDXf_81ar0alo5n7yRmT7sg/byssHOPPFnI.jpg?size=1067x1600&quality=96&sign=26796aea89f525d0230b5d6e53444516&type=album', 'https://sun9-78.userapi.com/impg/lHpgxwnCEO0pP9ZOuf7XmT7zNg9qsle6WxKagw/B2n2tU0aLJQ.jpg?size=1067x1600&quality=96&sign=f553b8c46878870f36844fa269d0cc60&type=album'],
  },
  {
    'art': 'zsplik',
    'title': 'Знакомство с составом. Прялгаускайте Лиана и Иванова Ксения',
    'text': '<p><strong>Сегодня мы познакомимся с очень дружной и интересной Женской парой, а именно с:</strong></p> <p><strong>Лиана:</strong> Привет! Я Лиана Прялгаускайте</p> <p><strong>Ксюша:</strong> Хэй! Я Ксюша Иванова или Ксюха</p> <p><strong>Ребята, расскажите немного о себе. Буквально пару слов, сколько вам лет, где учитесь и как успехи на учебе?</strong></p> <p><strong>Лиана:</strong> Мне 15 лет. В этом году я перешла в 10 класс и не смотря на огромное кол-во тренировок, учусь я очень даже хорошо)</p> <p><strong>Ксюша:</strong> Мне 10 лет и я учусь в 5 классе на Хорошо, Отлично и Супер!</p> <p><strong>Прекрасно! По вашим словам сразу понятно, что вы очень позитивные девчонки, молодцы! А как давно вы занимаетесь Спортивной Акробатикой? И как вам удается совмещать учёбу и спорт?</strong></p> <p><strong>Лиана:</strong> Я в акробатике уже 8 лет, и 6 из них стою с Ксюхой в Женской Паре. Как мне удается совмещать учебу со спортом? Ну это скорее можно назвать не совмещаю, а замещаю хах) Ну да, конечно иногда приходится пропускать последние уроки из-за тренировок, а то и вовсе целые недели из-за поездок на соревнования, но учителя это понимают и принимают, так что пока проблем с учебой нету)</p> <p><strong>Ксюша:</strong> Я занимаюсь уже 7 лет. Совмещать учебу с тренировками конечно тяжко… Практически каждый день я прихожу со школы в зал, тренируюсь до изнеможения и потом еле-еле шагаю домой. Небольшой ужин, пару «вздохов» и сажусь до полуночи делать Д/З…</p> <p><strong>Охх… Быть спортсменом не так уж и легко… А что для вас самое сложное в этом прекрасном спорте? Есть ли что-то, что вы бы хотели поменять в своих тренировках или допустим в зале?</strong></p> <p><strong>Лиана:</strong> Меня все устраивает. Хоть наш тренер и тренирует нас до «ватных ног» каждую тренировку, я спокойно тяну всю программу. Даже не знаю, привыкла видимо) Зал нравится, всего хватает, вполне. Хотя стенки всё же немного давят)</p> <p><strong>Ксюша:</strong> Да меня тоже все устраивает. Все нравится, тренируемся, улыбаемся) Самое сложное наверно это найти общий язык со своим партнёром. И не просто для общения, а чтобы вы вдвоем делали одно общее дело максимально слаженно. А иначе как побеждать, когда в составе «бардак»? Никак!</p> <p><strong>Удивляете. Девочки вы просто меня удивляете. А расскажите-ка, каких успехов вы уже достигли в спорте? И может раскроете нам небольшой секрет, насколько грандиозные у вас планы на спорт?</strong></p> <p><strong>Лиана:</strong> Сейчас у нас с Ксюхой разряд КМС (Кандидат в Мастера Спорта). Из планов… Ну во-первых сделать МС (Мастер Спорта), а там уже и не останавливаться и идти напролом к МСМК (Мастер Спорта Международного Класса)</p> <p><strong>Ксюша:</strong> Да, КМС мы выполнили совсем недавно и уже вовсю готовимся с Лианкой к выполнению звания Мастер Спорта РФ и дальше, дальше, дальше!!!</p> <p><strong>Класс! Девочки молодцы! Я желаю вам достичь всего, что вы надумали в ближайшее время! И на последок попрошу вас сказать пару слов для ваших тренеров и для вашей команды. Ну может какие-то напутствия или просто теплые слова)</strong></p> <p><strong>Лиана:</strong> Спасибо большое тренерам за их нелегкий труд. Хочу им пожелать, терпения, здоровья и больше перспективных спортсменов, которые будут радовать их победами! А также спасибо всей нашей команде, которая всегда поддержит и не оставит в стороне!</p> <p><strong>Ксюша:</strong> Спасибо тренерам! Верьте в нас и мы победим! УРА!</p>',
    'date': '01.10.2020',
    'photos': ['https://sun9-77.userapi.com/impg/6jUE8bjGxkfLcV0UppBxpmjfRc_ECkyb_EYIGg/83WVCeqiQec.jpg?size=1617x1920&quality=96&sign=cc40bc3ea9cd8474572c42ef8d3e261b&type=album', 'https://sun9-72.userapi.com/impg/mYNa5KdbA_kdadtJRy4nefahxElahvH5a-99lw/V0-kFBlvr9I.jpg?size=1440x2160&quality=96&sign=8dbb6a0c3d9c678e83d2a71aba1b7347&type=album', 'https://sun9-16.userapi.com/impg/wyDkXIctoYB9_jWkEewyPKk0LTWn1TyJ5LG-kg/bGZqQTTfipU.jpg?size=853x1280&quality=96&sign=9036d8b15d9b77e26f588ad488afc4c0&type=album'],
  },
  {
    'art': 'zsmekv',
    'title': 'Знакомство с составом. Евгений Мартишонок и Кузьмина Владислава',
    'text': '<p><strong>Привет ребята! Представьтесь пожалуйста как вас зовут</strong></p> <p><strong>Женя:</strong> Привет, меня зовут Мартишонок Евгений, или просто Женя</p> <p><strong>Влада:</strong> Привет, меня зовут Кузьмина Владислава, ну можно Влада)</p> <p><strong>Отлично! Расскажите немного о себе. Где вы учитесь, в каком классе? Или может даже на каком курсе?</strong></p> <p><strong>Женя:</strong> Я учусь в 10 "Б" классе в школе №7, учусь на отлично и хорошо</p> <p><strong>Влада:</strong> Я учусь в 5 "Е" классе в 32 Гимназии, Учусь лучше всех</p> <p><strong>Молодцы! Учёбу не бросайте, образование какое-никакое нужно) Ладно ребята, расскажите немного о себе. Какие у вас есть хобби? Чем-нибудь увлекаетесь помимо спорта и учёбы?</strong></p> <p><strong>Женя:</strong> Я увлекаюсь баскетболом. В свободное время иногда отрабатываю броски, хах. Также нравится читать. Как бы странно не звучало, но мне нравятся детективы</p> <p><strong>Влада:</strong> Я учу английский и немецкий язык и еще я обожаю рисовать! Рисовать много и красиво!</p> <p><strong>Ох как здорово, какие вы разносторонние и интересные! Так держать! Давайте поговорим теперь о спорте. Собственно-то, зачем мы с вами здесь собрались. Расскажите, как называется ваш спорт, почему именно он и насколько сложный это спорт?</strong></p> <p><strong>Женя:</strong> Мы занимаемся Спортивной акробатикой. Я пришел сюда в 6 лет и занимаюсь до сих пор. Думаю заниматься пока не буду держать корочку МСМК (Мастер Спорта Международного Класса) в руках</p> <p><strong>Влада:</strong> И я тоже в 6. И тоже не собираюсь уходить пока не получу МСМК, а то и вовсе ЗМС (Заслуженный Мастер Спорта)</p> <p><strong>Ого! Какие амбиции! Вы наверное многое прошли вместе. Какие успехи? Какой был ваш самый запоминающийся выезд? Какой был самый для вас "ужасный", неприятный?</strong></p> <p><strong>Женя:</strong> Вместе стоим в составе уже чуть больше 5 лет и расходиться не собираемся! За все время что мы работаем с Владой, мы получили КМС (Кандидат в Мастера Спорта) и успели побывать на стольких соревнованиях, что считать придется целый день, хах)</p> <p><strong>Влада:</strong> Да, мы очень много ездим как в другие регионы РФ, так и за границу. Мы с Женей были в Литве, Польше, Германии, Чехии и… Где мы только не были</p> <p><strong>Женя:</strong> Самые запоминающиеся соревнования были в 2020 в В.Новгороде. Там мы смогли взять золото на Чемпионате и Первенстве СЗФО. А интересны эти соревнования были тем, что было много соперников и огромная мотивация всех победить. И вот пожалуйста, золото)<br> Ну а самые ужасные соревнования назвать трудно, так как благодаря нашим тренерам и хореографам мы готовимся к каждым соревнованиям на 101%, а благодаря нашей дружной команде и ее самой мощной поддержке, каждый выход на ковер ощущается как обычный тренировочный танец дома. Не переживаешь, не боишься, дышишь ровно и поддержка команды придает неимоверное кол-во сил!</p> <p><strong>Ухх как здорово! Удачи! Сил и терпения! А есть планы на будущее? Именно в составе. Расскажете? Или секрет?</strong></p> <p><strong>Женя:</strong> На сегодня у нас в планах выйдя с карантина начать выполнение Звания Мастера Спорта РФ в нашем составе.</p> <p><strong>Влада:</strong> И начать уже выполнять МСМК)</p> <p><strong>Понял вас. Тогда могу лишь пожелать вам побольше сил на выполнение МС РФ и удачи! Спасибо большое ребята! Было очень интересно с вами пообщаться! Желаю вам огромных успехов и много новых достижений! Побед и здоровья само собой! УРА!</strong></p> </body> </html>',
    'date': '16.09.2020',
    'photos': ['https://sun9-7.userapi.com/impg/q0N4cXBZWJkWCdh3dzNl912d-RAPI9A58s_JkQ/m53uh3MNUgc.jpg?size=1600x1066&quality=96&sign=9b999a769ae5335e178137e100526b6b&type=album', 'https://sun9-37.userapi.com/impg/QhrbnMKBIB-bs_5bGfcjlklrCCdCL1J-xJES8g/pEj7Ub5b3c8.jpg?size=720x960&quality=96&sign=739a5306f991d86de8c167fffe95cc16&type=album', 'https://sun9-79.userapi.com/impg/6PQjHq3gBFNZ7K0I3DVJZIyHWVhQPpAlW3RW3Q/GBepJ8soLsY.jpg?size=1437x2160&quality=96&sign=5e5be90a8e5f696344759127854baa31&type=album', 'https://sun9-66.userapi.com/impg/y6KTVgQmkVZ8VuU0UJBRZhGGNOCynDr1GFUUgA/JX82dLjdy-E.jpg?size=979x1600&quality=96&sign=b3b20d6fc7ef3c5c0353903185d824c2&type=album']
  }
]

news_context = {
  'posts': get_competitions(posts, [datetime.datetime(2024, 11, 21, 10, 5, 42), datetime.datetime(2024, 11, 10, 9, 51, 3), datetime.datetime(2024, 11, 1, 11, 36)]),
  'rec': get_competitions(posts, [datetime.datetime(2024, 10, 31, 14, 0, 10)]),
  'rec_photo': get_competitions(posts, [datetime.datetime(2024, 10, 31, 14, 0, 10)])[0]['cover'],
  'last': posts[1:4],
  'articles': articles,
}

competitions = [{
    "name": "Всероссийские соревнования «Юность Евразии»",
    "date": "19.01 - 24.01",
    "text": "8 - 15 | 3 юн. - 1 сп.",
    "city": "г. Оренбург"
}, {
    "name": "Межрегиональные спортивные соревнования посвящённые Дню космонавтики",
    "date": "10.04 - 14.04",
    "text": "8 - 15 | 11 - 16 | 12 - 18",
    "city": "г. Киров"
}, {
    "name": "СЗФО",
    "date": "04.02 – 09.02",
    "text": "11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Архангельск"
}, {
    "name": "Всероссийские соревнования «Сердца четырёх»",
    "date": "13.02 – 16.02",
    "text": "11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Саратов"
}, {
    "name": "Всероссийские соревнования «Памяти Александра Дергунова»",
    "date": "19.02 – 24.02",
    "text": "8 - 15 (КМС) | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Октябрьский"
}, {
    "name": "Всероссийские соревнования «На призы ЗТ СССР В.Д. Литвинова»",
    "date": "23.02 – 28.02",
    "text": "8 - 15 (1 сп.) | 11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Воронеж"
}, {
    "name": "Первенство России (11-16)",
    "date": "03.03 - 09.03",
    "text": "11 - 16",
    "city": "г. Орёл"
}, {
    "name": "Всероссийские соревнования «Черное золото Приобья»",
    "date": "10.03 – 15.03",
    "text": "8 - 15 (КМС) | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Нижневартовск"
}, {
    "name": "Всероссийские соревнования «Две звезды»",
    "date": "16.03 - 21.03",
    "text": "8 - 15 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Краснодар"
}, {
    "name": "Первенство России (12-18)",
    "date": "24.03 - 30.03",
    "text": "12-18",
    "city": "г. Ярославль"
}, {
    "name": "Всероссийские соревнования «Кубок МСМК М.Г. Круглякова»",
    "date": "05.04 - 10.04",
    "text": "8 - 15 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Волгоград"
}, {
    "name": "Первенство России (13-19)",
    "date": "14.04 – 20.04",
    "text": "13 - 19",
    "city": "г. Воронеж"
}, {
    "name": "Всероссийские соревнования «Кубок Нечерноземья»",
    "date": "23.04 – 27.04",
    "text": "8 - 15 (1 сп.) | 11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Тверь"
}, {
    "name": "Международные соревнования «Кубок ЗТ СССР Владимира Гургенидзе»",
    "date": "28.04 – 03.05",
    "text": "11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Одинцово"
}, {
    "name": "Чемпионат России (многоборье)",
    "date": "12.05 – 18.05",
    "text": "14+",
    "city": "г. Великий Новгород"
}, {
    "name": "Международные соревнования «Иртышские зори»",
    "date": "23.06 – 28.06",
    "text": "11 - 16 | 12 -18 | 13 - 19 | 12+",
    "city": "г. Павлодар, Республика Казахстан"
}, {
    "name": "Международные соревнования «Кубок Золотова»",
    "date": "05.09 - 10.09",
    "text": "11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Великий Новгород"
}, {
    "name": "Всероссийские соревнования «Памяти Заслуженного тренера СССР Г.К. Казаджиева»",
    "date": "15.09 - 20.09",
    "text": "11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Краснодар"
}, {
    "name": "Всероссийские соревнования «Жемчужины Алтая»",
    "date": "25.09 – 30.09",
    "text": "8 - 15 (1 сп.) | 11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Горно-Алтайск"
}, {
    "name": "Всероссийские соревнования «Кубок Петра I»",
    "date": "07.10 – 12.10",
    "text": "8 - 15 (1 сп.) | 11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Санкт-Петербург"
}, {
    "name": "Открытый Республиканский турнир «памяти ЗТ СССР В.П. Коркина»",
    "date": "По назначению",
    "text": "12 -18 | 13 - 19 | 14+",
    "city": "г. Брест, Республика Беларусь"
}, {
    "name": "Международные соревнования «Звёзды Азии» памяти Н.И. Лакиза",
    "date": "По назначению",
    "text": "12 - 18 | 17 и моложе | 12+",
    "city": "г. Ташкент, Республика Узбекистан"
}, {
    "name": "Кубок России",
    "date": "21.10 – 26.10",
    "text": "14+",
    "city": "г. Оренбург"
}, {
    "name": "Всероссийские соревнования «Кубок Памяти Р. Хафизова»",
    "date": "30.10 - 03.11",
    "text": "11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Тольятти"
}, {
    "name": "Всероссийские соревнования «Кубок ЗТР С.Г. Плешкова»",
    "date": "04.11 – 09.11",
    "text": "8 - 15 (1 сп.) | 11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Красноярск"
}, {
    "name": "Всероссийские соревнования «Кубок Волкова»",
    "date": "10.11 – 15.11",
    "text": "8 - 15 | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Великий Новгород"
}, {
    "name": "Всероссийские соревнования «Кубок Урала»",
    "date": "16.11 – 19.11",
    "text": "8 - 15 (1 сп.) | 11 - 16 (КМС) | 12 -18 | 13 - 19 | 14+",
    "city": "г. Екатеринбург"
}, {
    "name": "Международные соревнования «Памяти ЗТР Беларусь Л.И. Лившица»",
    "date": "По назначению",
    "text": "12 - 18 | 13 - 19 | 14+",
    "city": "г. Минск, Республика Беларусь"
}, {
    "name": "Чемпионат России (командный и упражнения)",
    "date": "19.11 – 24.11",
    "text": "14+",
    "city": "г. Киров"
}, {
    "name": "Всероссийские соревнования «Памяти И.С. Конева»",
    "date": "19.11 - 24.11",
    "text": "11 - 16 | 12 - 18 | 13 - 19",
    "city": "г. Киров"
}, {
    "name": "Всероссийские соревнования «Кубок имени ЗТ СССР В.Д. Павловского»",
    "date": "25.11 – 30.11",
    "text": "8 - 15 | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Москва"
}, {
    "name": "Всероссийские соревнования «На призы ЗМС Ю. Зикунова»",
    "date": "01.12 – 05.12",
    "text": "11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Омск"
}, {
    "name": "Всероссийские соревнования «Никольские пируэты»",
    "date": "09.12 – 12.12",
    "text": "8 - 15 | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Великий Новгород"
}, {
    "name": "Всероссийские соревнования «Звезды Кремля»",
    "date": "13.12 – 18.12",
    "text": "8 - 15 | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Москва"
}, {
    "name": "Всероссийские соревнования на «Кубок ЗТР К.М. Наумовой»",
    "date": "19.12 – 24.12",
    "text": "8 - 15 (КМС) | 11 - 16 | 12 -18 | 13 - 19 | 14+",
    "city": "г. Орёл"
}, {
    "name": "Международные соревнования «Игры Вызова легенд»",
    "date": "По назначению",
    "text": "14+",
    "city": "г. Екатеринбург"
}]

region_competitions = [{
    "name": "Чемпионат и Первенство г. Калининграда",
    "date": "19.01 - 24.01",
    "text": "8 - 15 | 3 юн. - 1 сп.",
    "city": "г. Калининград"
}, {
    "name": "Чемпионат и Первенство Калининградской области",
    "date": "19.01 - 24.01",
    "text": "8 - 15 | 3 юн. - 1 сп.",
    "city": "г. Калининград"
},
]

def index(request):
  context = {
    'posts': get_competitions(posts, [datetime.datetime(2024, 11, 21, 10, 5, 42), datetime.datetime(2024, 11, 10, 9, 51, 3), datetime.datetime(2024, 11, 1, 11, 36)]),
    'last': posts[1:4],
    'main_coaches': coaches[:4],
    'coaches': coaches[4:]
  }
  return render(request, 'index.html', context)

def news(request):
  return render(request, 'news.html', news_context)

def ms(request):
  return render(request, 'ms.html', {'mss': mss})

def calendar(request):
  return render(request, 'calendar.html',  {'competitions': competitions, 'region_competitions': region_competitions})

def groups(request):
  return render(request, 'groups.html')

def coach(request):
  for i in range(len(coaches)):
    coaches[i]['theme'] = i % 2

  return render(request, 'coach.html', {'coaches': coaches})

def contacts(request):
  return render(request, 'contacts.html')

def article(request, art):
  if art == "coach":
    return render(request, 'article-coach.html')
  else:
    try:
      news_context['current_article'] = [a for a in articles if a['art'] == art][0]
    except IndexError:
      return render(request, 'article-not-found.html')
    return render(request, 'article.html', news_context)

def wall(request):
  #print(get_enogh(get_wall(access_token, group_id)))
  news_context['posts'] = posts
  return render(request, 'wall.html', news_context)