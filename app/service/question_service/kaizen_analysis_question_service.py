from fastapi.logger import logger

from app.lib import Singleton
from app.lib.custom_exception import DBFetchFailureException, DBRecordNotFound, InvalidDataException
from app.repository import KaizenAnalysisQuestionRepo


class KaizenAnalysisQuestionsService(metaclass=Singleton):

    @staticmethod
    def get_kaizen_analysis_questions_by_analysis_type(question_data):
        """
        Service to get all the kaizen analysis questions based upon kaizen type input.
        """
        analysis_type = question_data.analysis_type
        try:
            if not analysis_type:
                error_msg = f'kaizen_type is a required parameter to fetch the kaizen questions {kaizen_type}.'
                logger.error(error_msg)
                raise InvalidDataException(error_msg)

            else :
                analysis_questions = KaizenAnalysisQuestionRepo.get_kaizen_analysis_questions_by_analysis_type(analysis_type)
                if not analysis_questions:
                    error_msg = f'No Questions found for kaizen type {analysis_type}.'
                    logger.error(error_msg)
                    raise DBRecordNotFound(error_msg)
        except Exception as ex:
            error_msg = f'Error occurred while fetching kaizen analysis questions of analysis_type {analysis_type}'
            logger.error(f'{ex} {error_msg}')
            raise DBFetchFailureException(error_msg)
        return analysis_questions

    @staticmethod
    def get_kaizen_analysis_question_by_question_id(question_id):
        """
        Get a specific analysis question detail based upon a analysis question id.
        """
        try:
            analysis_question = KaizenAnalysisQuestionRepo.get_kaizen_analysis_question_by_id(question_id)
            if not analysis_question:
                error_msg = f'No Questions found for kaizen analysis type with analysis question id as {question_id}.'
                logger.error(error_msg)
                raise DBRecordNotFound(error_msg)
        except Exception as ex:
            error_msg = f'Error occurred while fetching kaizen analysis question of question id {question_id}'
            logger.error(f'{ex} {error_msg}')
            raise DBFetchFailureException(error_msg)
        return analysis_question
