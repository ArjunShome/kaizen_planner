from app.models.base_model import SessionLocal


class SqlContext(object):
    def __init__(self):
        self.session = SessionLocal()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.session:
            try:
                self.session.commit()
            except Exception as ex:
                self.session.rollback()
                raise ex
