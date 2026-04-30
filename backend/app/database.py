import os
from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = (
    f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASS']}"
    f"@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
)
engine = create_engine(DATABASE_URL)

def create_db():
    SQLModel.metadata.create_all(engine)

# 依存の注入
def get_session():
    with Session(engine) as session:
        yield session