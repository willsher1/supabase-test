from dotenv import dotenv_values
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import User


def test_user():
    config = dotenv_values(".env")
    url = config["SUPABASE_DB_URL"]

    engine = create_engine(url)

    with Session(engine) as session:
        assert session.scalars(select(User)).all()

