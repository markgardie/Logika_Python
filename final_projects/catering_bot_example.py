import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import sqlite3
import os

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Меню страв (можна розширити)
MENU = {
    'meal1': 'Борщ',
    'meal2': 'Салат Цезар',
    'meal3': 'Котлета з пюре',
    'meal4': 'Паста Карбонара',
}

TOKEN = "7758745066:AAEZ3AFQwgbptrDcxXC_vKyl5haAD66XJjY"

# ID адміністратора (потрібно замінити на реальний)
ADMIN_ID = 45811064

# Визначаємо шлях до бази даних
DB_PATH = 'final_projects/lunch_orders.db'

# Створення бази даних
def init_db():
    # Створюємо директорію, якщо вона не існує
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders
        (user_id INTEGER, username TEXT, meal TEXT, order_date TEXT, order_time TEXT)
    ''')
    conn.commit()
    conn.close()

# Створення меню для вибору страв
def get_menu_keyboard():
    keyboard = []
    row = []
    for meal_id, meal_name in MENU.items():
        row.append(InlineKeyboardButton(meal_name, callback_data=meal_id))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == ADMIN_ID:
        await update.message.reply_text(
            "Вітаю, адміністраторе! Використовуйте /orders для перегляду замовлень на сьогодні."
        )
    else:
        await update.message.reply_text(
            "Вітаю! Оберіть страву на обід:",
            reply_markup=get_menu_keyboard()
        )

# Обробка вибору страви
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    username = query.from_user.username or "Unknown"
    
    # Отримуємо обрану страву
    meal = MENU[query.data]
    
    # Зберігаємо замовлення в базу даних
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    current_date = datetime.now().date().isoformat()
    current_time = datetime.now().strftime('%H:%M:%S')
    
    c.execute('''
        INSERT INTO orders (user_id, username, meal, order_date, order_time)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, username, meal, current_date, current_time))
    
    conn.commit()
    conn.close()

    await query.answer()
    await query.edit_message_text(
        f"Ви замовили: {meal}\nДякуємо за замовлення!"
    )

# Команда /orders для адміністратора
async def get_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("У вас немає доступу до цієї команди.")
        return

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    current_date = datetime.now().date().isoformat()
    
    c.execute('''
        SELECT username, meal, order_time 
        FROM orders 
        WHERE order_date = ?
        ORDER BY order_time
    ''', (current_date,))
    
    orders = c.fetchall()
    conn.close()

    if not orders:
        await update.message.reply_text("На сьогодні замовлень немає.")
        return

    message = "Замовлення на сьогодні:\n\n"
    for username, meal, order_time in orders:
        message += f"👤 {username}\n🍽 {meal}\n⏰ {order_time[:5]}\n\n"

    await update.message.reply_text(message)

def main():
    # Ініціалізація бази даних
    init_db()
    
    # Створення і налаштування бота
    application = Application.builder().token(TOKEN).build()

    # Додавання обробників команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("orders", get_orders))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()