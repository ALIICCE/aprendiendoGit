from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler
from inicio_bot import busca_arreglo
from dotenv import load_dotenv
import os


load_dotenv()
token_telegram = os.environ['token_telegram']
updater = Application.builder().token(token_telegram).build()

# Función para responder al comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy un bot que repite lo que dices. ¡Escríbeme algo!")

# Función de Echo: Responde con el mismo mensaje que recibe
async def echo(update: Update, context: CallbackContext):
    user_text = update.message.text
    value_return = busca_arreglo(user_text)
    await update.message.reply_text(value_return)
    # value_return = libreriaGroserias.busca_archivo_groseria() or {user_text}
    await update.message.reply_text(f"You say: {user_text}")

# Configuración del bot
app = Application.builder().token(token_telegram).build()

# Agregar manejadores (Handlers)
app.add_handler(CommandHandler("start", start))  # Maneja el comando /start
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Maneja cualquier mensaje de texto

# Iniciar el bot en modo polling (escucha mensajes constantemente)
print("🤖 Bot de Echo iniciado...")
app.run_polling()
