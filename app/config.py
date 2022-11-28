from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

MAIL_SMTP_HOST = os.getenv('MAIL_SMTP_HOST')
MAIL_SMPT_USER = os.getenv('MAIL_SMPT_USER')
MAIL_SMPT_PASSWORD = os.getenv('MAIL_SMPT_PASSWORD')
MAIL_SMTP_PORT = os.getenv('MAIL_SMTP_PORT')

MAIL_DEFAULT_FROM = os.getenv('MAIL_DEFAULT_FROM')
