from app.lib import Singleton
from app.models import KaizenQuestion
from app.repository.sql_context import SqlContext


class KaizenQuestionRepo(metaclass=Singleton):

    @staticmethod
    def get_kaizen_questions_by_kaizen_type(kaizen_type):
        with SqlContext() as sql_context:
            query = sql_context.session.query(KaizenQuestion).filter(
                KaizenQuestion.question_type == kaizen_type
            ).order_by(KaizenQuestion.sort_order)
            return query.all()

    @staticmethod
    def get_kaizen_question_by_type_stage(kaizen_type, kaizen_stage):
        with SqlContext() as sql_context:
            query = sql_context.session.query(KaizenQuestion).filter(
                KaizenQuestion.question_type == kaizen_type,
                KaizenQuestion.question_stage == kaizen_stage
            ).order_by(KaizenQuestion.sort_order)
            return query.all()

    @staticmethod
    def get_kaizen_question_by_id(question_id):
        with SqlContext() as sql_context:
            query = sql_context.session.query(KaizenQuestion).filter(
                KaizenQuestion.id == question_id
            )
            return query.scalar()
