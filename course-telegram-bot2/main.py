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

def connect_to_sheets():
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
    client = gspread.authorize(creds)

    sheet = client.open('Telegram Bot Users').sheet1
    return sheet

def write_to_sheets(sheet, data):
    sheet.append_row(data)
    logger.info("Дані записані в таблицю")

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_name = update.message.text
    context.user_data['name'] = user_name

    await update.message.reply_text(
        f'Дякую, {user_name}! Вкажіть місто:'
    )

    return CITY

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

async def get_tariff(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    tariff = update.message.text
    context.user_data['tariff'] = tariff

    try:
        sheet = connect_to_sheets()

        user_id = context.user_data.get('user_id')
        username = context.user_data.get('username')
        start_time = context.user_data.get('start_time')
        name = context.user_data.get('name')
        city = context.user_data.get('city')
        contact = context.user_data.get('contact')

        write_to_sheets(sheet,
                        [user_id, username, start_time, name, city, contact]
                        )

    except Exception as e:
        logger.error(f'Помилка при записі в таблицю: {e}')

    await update.message.reply_text(
        f'Дякую, {user_name}! Ваші дані зареєстровані. Чекайте підтверження адміністратора.'
    )

    return ConversationHandler.END

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    user_id = user.id
    username = user.name if user.name else "No username"
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        sheet = connect_to_sheets()
        write_to_sheets(sheet, [user_id, username, start_time])
    except Exception as e:
        logger.error(f"Помилка запису в таблицю: {e}")

    context.user_data["user_id"] = user_id
    context.user_data["username"] = username    
    context.user_data["start_time"] = start_time 

    await update.message.reply_text(
        f"Доброго дня, {username}. Введіть ваше повне ім'я"
    )

    return NAME          


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    await update.message.reply_text(
        f'Реєстрацію скасовано.'
    )

    return ConversationHandler.END


async def check_course_starts(context: CallbackContext) -> None:
    try:
        sheet = connect_to_sheets()
        all_data = sheet.get_all_records()

        for idx, row in enumerate(all_data):
            if (row.get("Статус") == "Підтверджено" and 
                row.get("Повідомлення відправлені") != "Так"):
                user_id = row.get("user_id")

                await send_course_messages(context, user_id, idx + 2)
    except Exception as e:
        logger.error(f"Помилка при перевірці початку курсу: {e}")

async def send_course_messages(context: CallbackContext, user_id, idx) -> None:
    try:
        sheet = connect_to_sheets()

        await context.bot.send_message(
            chat_id = user_id,
            text = COURSE_MESSAGES[0]
        )

        sheet.update_cell(idx, 9, "Перше повідомлення відправлене")

        for i, message in enumerate(COURSE_MESSAGES[1:], 1):
            context.job_queue.run_once(
                send_delayed_message,
                i * 10,
                data= {
                    "user_id": user_id,
                    "message": message,
                    "row_idx": idx,
                    "message_idx": i
                }
            )

    except Exception as e:
        logger.error(f"Помилка при відправці повідомлення курсу: {e}")

async def send_delayed_message(context: CallbackContext) -> None:
    job_data = context.job.data

    user_id = job_data.get("user_id")
    message  = job_data.get("message")
    row_idx  = job_data.get("row_idx")
    message_idx = job_data.get("message_idx")


    try:
        await context.bot.send_message(
            chat_id = user_id,
            text = message
        )

        sheet = connect_to_sheets()

        if message_idx == len(COURSE_MESSAGES) - 1:
           sheet.update_cell(row_idx, 9, "Так")
        else: 
            sheet.update_cell(row_idx, 9, f"Повідомлення {message_idx + 1} відправлено")
    
    except Exception as e:
        logger.error(f"Помилка при відправці повідомлення курсу: {e}")
