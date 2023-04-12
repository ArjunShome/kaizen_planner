from app.lib import Singleton
from app.models import Kaizen
from app.models.enum_model import KaizenStatus
from app.repository.sql_context import SqlContext


class KaizenApplyRepo(metaclass=Singleton):

    @staticmethod
    def apply_kaizen(user_id, kaizen_type, title):
        kaizen = Kaizen()
        kaizen.user_id = user_id
        kaizen.type = kaizen_type
        kaizen.created_by = user_id
        kaizen.title = title
        kaizen.status = KaizenStatus.IN_PROGRESS
        with SqlContext() as sql_context:
            sql_context.session.add(kaizen)
        return kaizen

    @staticmethod
    def get_kaizen_by_id(kaizen_id):
        with SqlContext() as sql_context:
            query = sql_context.session.query(Kaizen).filter(
                Kaizen.id == kaizen_id
            )
            return query.scalar()

    @staticmethod
    def get_kaizen_by_userid_title_type(user_id, title, kaizen_type):
        with SqlContext() as sql_context:
            query = sql_context.session.query(Kaizen).filter(
                Kaizen.user_id == user_id,
                Kaizen.title == title,
                Kaizen.type == kaizen_type
            )
            return query.scalar()

    @staticmethod
    def get_kaizen_by_kaizen_type_user_id(kaizen_type, user_id):
        with SqlContext() as sql_context:
            query = sql_context.session.query(Kaizen).filter(
                Kaizen.user_id == user_id,
                Kaizen.type == kaizen_type,
                Kaizen.status == KaizenStatus.IN_PROGRESS
            )
            return query.scalar()