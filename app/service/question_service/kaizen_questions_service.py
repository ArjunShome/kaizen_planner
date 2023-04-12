from fastapi.logger import logger

from app.lib import Singleton
from app.lib.custom_exception import DBFetchFailureException, DBRecordNotFound, InvalidDataException
from app.repository import KaizenQuestionRepo


class KaizenQuestionsService(metaclass=Singleton):

    @staticmethod
    def get_kaizen_questions_by_kaizen_type(question_data):
        """
        Service to get all the kaizen question based upon kaizen type input.
        """
        kaizen_type = question_data.kaizen_type
        question_stage = question_data.question_stage
        try:
            if not kaizen_type:
                error_msg = f'kaizen_type is a required parameter to fetch the kaizen questions {kaizen_type}.'
                logger.error(error_msg)
                raise InvalidDataException(error_msg)

            elif kaizen_type and question_stage:
                questions = KaizenQuestionRepo.get_kaizen_question_by_type_stage(kaizen_type, question_stage)
                if not questions:
                    error_msg = f'No Questions found for kaizen type {kaizen_type} and stage - {question_stage}.'
                    logger.error(error_msg)
                    raise DBRecordNotFound(error_msg)

            else:
                questions = KaizenQuestionRepo.get_kaizen_questions_by_kaizen_type(kaizen_type)
                if not questions:
                    error_msg = f'No Questions found for kaizen type {kaizen_type}.'
                    logger.error(error_msg)
                    raise DBRecordNotFound(error_msg)
        except Exception as ex:
            error_msg = f'Error occurred while fetching kaizen questions of kaizen_type {kaizen_type}'
            logger.error(f'{ex} {error_msg}')
            raise DBFetchFailureException(error_msg)
        return questions

    @staticmethod
    def get_kaizen_question_by_id(question_data):
        """
        Service to get the kaizen question based upon kaizen question id as input.
        """
        question_id = question_data.kaizen_question_id
        try:
            if not question_id:
                error_msg = 'kaizen question id is a required parameter to fetch the kaizen question.'
                logger.error(error_msg)
                raise InvalidDataException(error_msg)

            else:
                question = KaizenQuestionRepo.get_kaizen_question_by_id(question_id)
                if not question:
                    error_msg = f'No Questions found for Question id {question_id}.'
                    logger.error(error_msg)
                    raise DBRecordNotFound(error_msg)
        except Exception as ex:
            error_msg = f'Error occurred while fetching kaizen question of question id {question_id}'
            logger.error(f'{ex} {error_msg}')
            raise DBFetchFailureException(error_msg)
        return question
