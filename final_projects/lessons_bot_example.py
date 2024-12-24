import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Конфігурація бота
class Config:
    BOT_TOKEN = '7917109078:AAF46ksMo77T7oQTzW7VXWoSGTu7sy0tczA'

# Структура даних для модулів та уроків
MODULES = {
    'intro': {
        'name': 'Вступ до Пайтона',
        'lessons': {
            'intro': {
                'name': 'Вступ до Python',
                'video_url': 'https://youtu.be/aJm1nvJQv1o',
                'text_notes': 'module_1_lesson_1_notes',
                'tasks': [
                    'Написати першу программу "Hello, World!"',
                    'Створити змінні та вивести їх значення'
                ]
            },
            'variables': {
                'name': 'Змінні та типи даних',
                'video_url': 'https://youtu.be/Bc4qNzkOfd0',
                'text_notes': 'module_1_lesson_2_notes',
                'tasks': [
                    'Створити змінні різних типів',
                    'Виконати операції з числами'
                ]
            }
        }
    },
    'OOP': {
        'name': "Об'єктно-орієнтоване програмування",
        'lessons': {
            'classes': {
                'name': 'Класи в ООП',
                'video_url': 'https://youtu.be/AA0osQm1uAc',
                'text_notes': 'OOP_lesson_1_notes',
                'tasks': [
                    'Створити перший клас',
                    "Створити об'єкт класу"
                ]
            }
        }
    }
}

class ProgrammingSchoolBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher()
        self.setup_handlers()

    def setup_handlers(self):
        """Реєстрація обробників подій"""
        self.dp.message.register(self.start_command, CommandStart())
        self.dp.message.register(self.help_command, Command('help'))
        self.dp.callback_query.register(self.process_module_selection, lambda c: c.data and c.data.startswith('module_'))
        self.dp.callback_query.register(self.process_lesson_selection, lambda c: c.data and c.data.startswith('lesson_'))
        self.dp.callback_query.register(self.back_to_modules, lambda c: c.data and c.data == "back_to_modules")

    async def back_to_modules(self, callback: types.CallbackQuery):
        """Обробник кнопки повернення до списку модулів"""
        keyboard = self.get_modules_keyboard()
        await callback.message.edit_text(
            "Оберіть модуль, який хочете вивчати:",
            reply_markup=keyboard
        )
        await callback.answer()

    async def start_command(self, message: types.Message):
        """Обробник команди /start"""
        keyboard = self.get_modules_keyboard()
        await message.answer(
            "Вітаємо в школі програмування! 🚀\n"
            "Оберіть модуль, який хочете вивчати:",
            reply_markup=keyboard
        )

    async def help_command(self, message: types.Message):
        """Обробник команди /help"""
        help_text = (
            "Як користуватися ботом:\n"
            "1. Оберіть модуль\n"
            "2. Виберіть урок\n"
            "3. Отримайте навчальні матеріали\n\n"
            "Доступні команди:\n"
            "/start - почати спочатку\n"
            "/help - показати довідку"
        )
        await message.answer(help_text)

    def get_modules_keyboard(self):
        """Створення клавіатури для вибору модулів"""
        buttons = []
        for module_key, module_info in MODULES.items():
            buttons.append([
                InlineKeyboardButton(
                    text=module_info['name'], 
                    callback_data=f'module_{module_key}'
                )
            ])
        
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    async def process_module_selection(self, callback: types.CallbackQuery):
        """Обробка вибору модуля"""
        module_key = callback.data.split('_')[1]
        module = MODULES[module_key]
        
        # Створюємо список кнопок для уроків
        buttons = []
        for lesson_key, lesson_info in module['lessons'].items():
            buttons.append([
                InlineKeyboardButton(
                    text=lesson_info['name'], 
                    callback_data=f'lesson_{module_key}_{lesson_key}'
                )
            ])
        
        # Додаємо кнопку повернення до списку модулів
        buttons.append([
            InlineKeyboardButton(
                text="↩️ Назад до списку модулів", 
                callback_data="back_to_modules"
            )
        ])
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        
        await callback.message.edit_text(
            f"Модуль: {module['name']}\nОберіть урок:", 
            reply_markup=keyboard
        )
        await callback.answer()

    async def process_lesson_selection(self, callback: types.CallbackQuery):
        """Обробка вибору уроку"""
        _, module_key, lesson_key = callback.data.split('_')
        module = MODULES[module_key]
        lesson = module['lessons'][lesson_key]
        
        lesson_details = (
            f"Урок: {lesson['name']}\n\n"
            f"🎥 Відео: {lesson['video_url']}\n"
            f"📄 Конспект: {lesson['text_notes']}\n\n"
            "Завдання для практики:\n"
        )
        
        for i, task in enumerate(lesson['tasks'], 1):
            lesson_details += f"{i}. {task}\n"
        
        # Створюємо навігаційні кнопки
        buttons = []
        
        # Знаходимо поточний індекс уроку та загальну кількість уроків
        lesson_keys = list(module['lessons'].keys())
        current_index = lesson_keys.index(lesson_key)
        
        navigation_buttons = []
        
        # Додаємо кнопку "Попередній урок", якщо це не перший урок
        if current_index > 0:
            prev_lesson_key = lesson_keys[current_index - 1]
            navigation_buttons.append(
                InlineKeyboardButton(
                    text="⬅️ Попередній",
                    callback_data=f"lesson_{module_key}_{prev_lesson_key}"
                )
            )
        
        # Додаємо кнопку "Наступний урок", якщо це не останній урок
        if current_index < len(lesson_keys) - 1:
            next_lesson_key = lesson_keys[current_index + 1]
            navigation_buttons.append(
                InlineKeyboardButton(
                    text="Наступний ➡️",
                    callback_data=f"lesson_{module_key}_{next_lesson_key}"
                )
            )
        
        if navigation_buttons:
            buttons.append(navigation_buttons)
        
        # Додаємо кнопки навігації по модулях
        buttons.append([
            InlineKeyboardButton(
                text="↩️ До списку уроків",
                callback_data=f"module_{module_key}"
            )
        ])
        buttons.append([
            InlineKeyboardButton(
                text="🏠 До списку модулів",
                callback_data="back_to_modules"
            )
        ])
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(lesson_details, reply_markup=keyboard)
        await callback.answer()


    async def start(self):
        """Запуск бота"""
        try:
            await self.dp.start_polling(self.bot)
        except Exception as e:
            logging.error(f"Помилка при запуску бота: {e}")

async def main():
    """Головна функція запуску"""
    bot = ProgrammingSchoolBot(Config.BOT_TOKEN)
    await bot.start()

if __name__ == '__main__':
    asyncio.run(main())
