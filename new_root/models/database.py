from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgre@localhost:5432/root_models')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    try:
        import new_root.models.models  # Make sure this import is correct
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error during database initialization: {e}")