import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Налаштування логування
logging.basicConfig(
level=logging.INFO
)

# Конфігурація бота
class Config:
    BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Структура даних для модулів та уроків
MODULES = {
    'python': {
        'name': 'Python для початківців',
        'lessons': {
            'intro': {
                'name': 'Вступ до Python',
                'video_url': 'https://example.com/python-intro-video',
                'text_notes': 'module_1_lesson_1_notes.pdf',
                'tasks': [
                    'Написати першу программу "Hello, World!"',
                    'Створити змінні та вивести їх значення'
                ]
            },
            'variables': {
                'name': 'Змінні та типи даних',
                'video_url': 'https://example.com/python-variables-video',
                'text_notes': 'module_1_lesson_2_notes.pdf',
                'tasks': [
                    'Створити змінні різних типів',
                    'Виконати операції з числами'
                ]
            }
        }
    },
    'web': {
        'name': 'Web-розробка',
        'lessons': {
            'html_basics': {
                'name': 'Основи HTML',
                'video_url': 'https://example.com/html-intro-video',
                'text_notes': 'web_module_lesson_1_notes.pdf',
                'tasks': [
                    'Створити першу HTML-сторінку',
                    'Додати базові теги на сторінку'
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
        # Реєстрація обробників подій
        self.dp.message.register(self.start_command, CommandStart())
        self.dp.message.register(self.help_command, Command('help'))
        self.dp.callback_query.register(self.process_module_selection, lambda c: c.data and c.data.startswith('module_'))
        self.dp.callback_query.register(self.process_lesson_selection, lambda c: c.data and c.data.startswith('lesson_'))

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
        keyboard = InlineKeyboardMarkup(row_width=1)
        for module_key, module_info in MODULES.items():
            keyboard.add(
                InlineKeyboardButton(
                    text=module_info['name'], 
                    callback_data=f'module_{module_key}'
                )
            )
        return keyboard

    async def process_module_selection(self, callback: types.CallbackQuery):
        """Обробка вибору модуля"""
        module_key = callback.data.split('_')[1]
        module = MODULES[module_key]
        
        keyboard = InlineKeyboardMarkup(row_width=1)
        for lesson_key, lesson_info in module['lessons'].items():
            keyboard.add(
                InlineKeyboardButton(
                    text=lesson_info['name'], 
                    callback_data=f'lesson_{module_key}_{lesson_key}'
                )
            )
        
        await callback.message.edit_text(
            f"Модуль: {module['name']}\nОберіть урок:", 
            reply_markup=keyboard
        )
        await callback.answer()

    async def process_lesson_selection(self, callback: types.CallbackQuery):
        """Обробка вибору уроку"""
        _, module_key, lesson_key = callback.data.split('_')
        lesson = MODULES[module_key]['lessons'][lesson_key]
        
        lesson_details = (
            f"Урок: {lesson['name']}\n\n"
            f"🎥 Відео: {lesson['video_url']}\n"
            f"📄 Конспект: {lesson['text_notes']}\n\n"
            "Завдання для практики:\n"
        )
        
        for i, task in enumerate(lesson['tasks'], 1):
            lesson_details += f"{i}. {task}\n"
        
        await callback.message.edit_text(lesson_details)
        await callback.answer()

    async def start(self):
        """Запуск бота"""
        try:
            await self.dp.start_polling(
self.bot
)
        except Exception as e:
            logging.error(f"Помилка при запуску бота: {e}")

async def main():
    """Головна функція запуску"""
    bot = ProgrammingSchoolBot(Config.BOT_TOKEN)
    await bot.start()

if __name__ == '__main__': 
    asyncio.run(main()) 
