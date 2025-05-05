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


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        f'Реєстрацію скасовано.'
    )

    return ConversationHandler.END