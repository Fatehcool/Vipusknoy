import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("Токен")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['aLotOfTrash'])
def send_hello(message):
    bot.reply_to(message,'''🗑️ Куда правильно выбрасывать мусор и зачем ♻️

Мусор — это не просто отходы 🧃🍌📦. Это отражение нашего отношения к планете 🌍. Каждый день мы что-то выбрасываем, но важно знать — куда именно 🚮.

Правильная утилизация начинается с сортировки 🧺:
🔵 Пластик — в синий контейнер
🟢 Стекло — в зелёный
🟡 Бумага — в жёлтый
🍂 Органика — в компост
⚠️ Опасные отходы (батарейки, лампочки) — в специальные пункты

Зачем это нужно? 🤔

🌳 Сохраняем природу — переработка спасает деревья, воду и воздух
⚡ Экономим ресурсы — переработка требует меньше энергии
🧼 Снижаем загрязнение — меньше мусора, чище мир
👶 Заботимся о будущем — дети заслуживают жить в чистом мире

Каждый наш правильный шаг 🪜 — это вклад в общее дело 🌟. Выбрасывай мусор осознанно — и Земля скажет тебе спасибо! 🙏💚''')


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, 'Вы забыли загрузить картинку :(')

@bot.message_handler(commands=['mem'])
def send_mybirthday(message):
    bot.reply_to
    with open('images/mem.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['animals'])
def send_mybirthday(message):
    bot.reply_to
    with open('images/mem1.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['animal'])
def send_mybirthday(message):
    bot.reply_to
    with open('images/mem2.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['secretmem'])
def send_mybirthday(message):
    bot.reply_to
    with open('images/mem3.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['secretpokemon'])
def send_mybirthday(message):
    bot.reply_to
    with open('images/mem4.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['mybirthday'])
def send_mybirthday(message):
    bot.reply_to(message, "Поздравляю! С ДНЕМ РОЖДЕНИЕ!!!!")

@bot.message_handler(commands=['trash1'])
def send_mybirthday(message):
    bot.reply_to(message, "Привет Ребята если вы кидаете trash на пол то это кринж фулловый.Если вы trashite природу то это тоже кринж.Итог КИДАЙТЕ МУСОР КУДА НАДО ЙОУ.")

@bot.message_handler(commands=['trash2'])
def send_mybirthday(message):
    bot.reply_to(message, "Чтобы поизить разделение отходов, контейнеры для разных типов отходов окрашены в разные цвета: в зеленый кладется стекло, в синий – бумажный самолетик, в желтый – картон, в оранжевый – пластик безполезный, в коричневый –  dangerous отходы, а в черный – как говориться organic.")
    with open('images/picture.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)


    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    
    dowlonoad_file = bot.download_file(file_info.file_path)
    with open(f'images/{file_name}', 'wb') as new_file:
        new_file.write(dowlonoad_file)
    bot.reply_to(message, f'Картинка успешно загружена :)')

# Запускаем бота
bot.polling()
