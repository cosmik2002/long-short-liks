import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

db = os.environ.get('DATABASE_URL')

engine = create_engine(db)
while True:
    try:
        print('try to connect')
        engine.connect()
        break
    except:
        continue
