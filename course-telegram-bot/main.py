import os
import time
import logging
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes,
    CallbackContext
)

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Константи для станів бота
NAME, CITY, CONTACT, TARIFF = range(4)

# Тестові дані для тарифів
TARIFFS = ['Базовий', 'Стандарт', 'Преміум']

# Тестові дані для повідомлень курсу
COURSE_MESSAGES = [
    "Вітаємо вас на нашому курсі! Ми раді, що ви з нами.",
    "Урок 1: Основи роботи з Python. Сьогодні ви дізнаєтесь про базові конструкції мови.",
    "Урок 2: Робота з Telegram API. Навчимося створювати власних ботів для Telegram.",
    "Урок 3: Інтеграція з Google Sheets. Зберігання та обробка даних через Google таблиці."
]

# Налаштування Google Sheets
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Функція для підключення до Google Sheets
def connect_to_sheets():
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
    client = gspread.authorize(creds)
    # Відкриваємо таблицю за її назвою
    sheet = client.open('Telegram Bot Users').sheet1
    return sheet

# Функція для запису даних в Google Sheets
def write_to_sheet(sheet, data):
    sheet.append_row(data)
    logger.info(f"Дані {data} записані в таблицю")

# Функція старту бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    user_id = user.id
    username = user.username if user.username else "No username"
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Записуємо базову інформацію в таблицю
    try:
        sheet = connect_to_sheets()
        write_to_sheet(sheet, [user_id, username, start_time])
    except Exception as e:
        logger.error(f"Помилка запису в таблицю: {e}")
    
    # Зберігаємо ID користувача в контексті
    context.user_data['user_id'] = user_id
    context.user_data['username'] = username
    context.user_data['start_time'] = start_time
    
    await update.message.reply_text(
        f"Привіт, {user.first_name}! Для реєстрації на курс, будь ласка, вкажіть ваше повне ім'я:"
    )
    
    return NAME

# Функція для отримання імені
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_name = update.message.text
    context.user_data['name'] = user_name
    
    await update.message.reply_text(
        f"Дякую, {user_name}! Тепер вкажіть ваше місто:"
    )
    
    return CITY

# Функція для отримання міста
async def get_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    city = update.message.text
    context.user_data['city'] = city
    
    await update.message.reply_text(
        "Вкажіть ваші контактні дані (телефон або email):"
    )
    
    return CONTACT

# Функція для отримання контактних даних
async def get_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    contact = update.message.text
    context.user_data['contact'] = contact
    
    reply_keyboard = [[tariff] for tariff in TARIFFS]
    
    await update.message.reply_text(
        "Оберіть тариф:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    
    return TARIFF

# Функція для отримання обраного тарифу
async def get_tariff(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    tariff = update.message.text
    context.user_data['tariff'] = tariff
    
    # Записуємо всі дані користувача в таблицю
    try:
        sheet = connect_to_sheets()
        # Отримуємо збережені дані
        user_id = context.user_data.get('user_id')
        username = context.user_data.get('username')
        start_time = context.user_data.get('start_time')
        name = context.user_data.get('name')
        city = context.user_data.get('city')
        contact = context.user_data.get('contact')
        
        # Додаємо дані до таблиці
        write_to_sheet(sheet, [user_id, username, start_time, name, city, contact, tariff, "Не підтверджено"])
        
    except Exception as e:
        logger.error(f"Помилка запису в таблицю: {e}")
    
    await update.message.reply_text(
        f"Дякую! Ваші дані успішно зареєстровані. Тариф: {tariff}.\n"
        f"Очікуйте підтвердження початку курсу від адміністратора.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

# Функція для скасування реєстрації
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Реєстрація скасована. Для початку знову використайте команду /start",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

# Функція для перевірки та надсилання повідомлень курсу
async def check_course_starts(context: CallbackContext) -> None:
    try:
        sheet = connect_to_sheets()
        # Отримуємо всі дані з таблиці
        all_data = sheet.get_all_records()
        
        for idx, row in enumerate(all_data):
            # Перевіряємо чи підтверджено курс для користувача
            if row.get('Статус') == 'Підтверджено' and row.get('Повідомлення відправлені') != 'Так':
                # Отримуємо дані користувача
                user_id = row.get('user_id')
                
                # Відправляємо повідомлення користувачу
                await send_course_messages(context, user_id, idx + 2)  # +2 оскільки idx починається з 0 і є заголовок
    
    except Exception as e:
        logger.error(f"Помилка при перевірці початку курсу: {e}")

# Функція для відправки повідомлень курсу
async def send_course_messages(context: CallbackContext, user_id, row_idx) -> None:
    try:
        sheet = connect_to_sheets()
        
        # Відправляємо перше повідомлення про початок курсу
        await context.bot.send_message(
            chat_id=user_id,
            text=COURSE_MESSAGES[0]
        )
        
        # Оновлюємо статус відправки у таблиці
        sheet.update_cell(row_idx, 9, "Перше повідомлення відправлено")
        
        # Відправляємо решту повідомлень з інтервалом 10 секунд
        for i, message in enumerate(COURSE_MESSAGES[1:], 1):
            # Запускаємо відкладене надсилання повідомлень
            context.job_queue.run_once(
                send_delayed_message,
                i * 10,  # Інтервал у секундах
                data={
                    'user_id': user_id,
                    'message': message,
                    'row_idx': row_idx,
                    'message_idx': i
                }
            )
    
    except Exception as e:
        logger.error(f"Помилка при відправці повідомлень курсу: {e}")

# Функція для відправки відкладених повідомлень
async def send_delayed_message(context: CallbackContext) -> None:
    job_data = context.job.data
    user_id = job_data.get('user_id')
    message = job_data.get('message')
    row_idx = job_data.get('row_idx')
    message_idx = job_data.get('message_idx')
    
    try:
        # Відправляємо повідомлення
        await context.bot.send_message(
            chat_id=user_id,
            text=message
        )
        
        # Оновлюємо статус відправки у таблиці
        sheet = connect_to_sheets()
        
        # Якщо це останнє повідомлення, позначаємо як "Так"
        if message_idx == len(COURSE_MESSAGES) - 1:
            sheet.update_cell(row_idx, 9, "Так")
        else:
            sheet.update_cell(row_idx, 9, f"Повідомлення {message_idx+1} відправлено")
            
    except Exception as e:
        logger.error(f"Помилка при відправці відкладеного повідомлення: {e}")

# Команда для адміністратора для підтвердження початку курсу
async def admin_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Перевіряємо чи повідомлення містить команду та ID користувача
    if not context.args or len(context.args) != 1:
        await update.message.reply_text("Використовуйте команду у форматі: /confirm USER_ID")
        return
    
    user_id = context.args[0]
    
    try:
        sheet = connect_to_sheets()
        all_data = sheet.get_all_records()
        
        for idx, row in enumerate(all_data):
            if str(row.get('user_id')) == user_id:
                # Оновлюємо статус в таблиці
                sheet.update_cell(idx + 2, 8, "Підтверджено")
                await update.message.reply_text(f"Курс для користувача {user_id} підтверджено.")
                
                # Запускаємо відправку повідомлень курсу
                await send_course_messages(context, int(user_id), idx + 2)
                return
        
        await update.message.reply_text(f"Користувача з ID {user_id} не знайдено.")
    
    except Exception as e:
        logger.error(f"Помилка при підтвердженні курсу: {e}")
        await update.message.reply_text(f"Помилка при підтвердженні курсу: {e}")

def main() -> None:
    # Створюємо екземпляр програми
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    # Додаємо обробник розмови для реєстрації
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
            CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_contact)],
            TARIFF: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_tariff)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    # Додаємо обробники
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('confirm', admin_confirm))
    
    # Запускаємо перевірку початку курсів кожні 60 секунд
    job_queue = application.job_queue
    job_queue.run_repeating(check_course_starts, interval=60, first=10)
    
    # Запускаємо бота
    application.run_polling()

if __name__ == '__main__':
    main()