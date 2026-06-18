from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8624726972:AAHa89X4pWrLaD7c-GI3OUjmx7FuSL-5pQQ"

WELCOME_TEXT = """
📚 سامانه جامع مطالعات علوم سنتی

این سامانه بر پایه هزاران منبع خطی، سنگی و نسخه‌های قدیمی
طراحی شده است.

هدف از ایجاد این مجموعه، گردآوری و تحلیل اطلاعات پراکنده
در منابع مختلف و ارائه نتیجه‌ای منظم و یکپارچه است.

برای استفاده از سامانه ابتدا هزینه دسترسی را پرداخت نمایید.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "💳 پرداخت و شروع تحلیل",
                callback_data="payment"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=reply_markup
    )

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "💳 درگاه پرداخت در مرحله بعد متصل خواهد شد."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(payment, pattern="payment"))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
