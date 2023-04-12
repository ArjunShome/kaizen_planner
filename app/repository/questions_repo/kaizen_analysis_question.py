from app.lib import Singleton
from app.models import KaizenAnalysisQuestion
from app.repository.sql_context import SqlContext


class KaizenAnalysisQuestionRepo(metaclass=Singleton):

    @staticmethod
    def get_kaizen_analysis_questions_by_analysis_type(analysis_type):
        with SqlContext() as sql_context:
            query = sql_context.session.query(KaizenAnalysisQuestion).filter(
                KaizenAnalysisQuestion.analysis_type == analysis_type
            )
            return query.all()


    @staticmethod
    def get_kaizen_analysis_question_by_id(question_id):
        with SqlContext() as sql_context:
            query = sql_context.session.query(KaizenAnalysisQuestion).filter(
                KaizenAnalysisQuestion.id == question_id
            )
            return query.scalar()
