from datetime import datetime
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from models import Order  # Assuming Order model is defined in models.py
from integration.database import connect_to_remote_db  # Assuming connect_to_remote_db function is defined in database.py

