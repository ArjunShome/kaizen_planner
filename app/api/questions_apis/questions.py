from fastapi import APIRouter, status
from fastapi.logger import logger
from fastapi.responses import JSONResponse

from app.lib.custom_exception import DBFetchFailureException, DBRecordNotFound, InvalidDataException
from app.request_models import QuestionData, QuestionDataId
from app.serializers import KaizenQuestionSchema
from app.service import KaizenQuestionsService

questions_api_router = APIRouter(prefix='/api')


@questions_api_router.post('/get_questions')
def get_kaizen_questions(question_data: QuestionData, status_code=status.HTTP_200_OK):
    try:
        questions = KaizenQuestionsService.get_kaizen_questions_by_kaizen_type(question_data)

        question_schema = KaizenQuestionSchema(many=True)
        questions = question_schema.dump(questions)

    except DBFetchFailureException as ex:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    except DBRecordNotFound as ex:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    except InvalidDataException as ex:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(ex))

    except Exception as ex:
        import traceback
        traceback.print_exc()
        logger.error(f'Unexpected error occurred. Error - {ex}')
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    return questions


@questions_api_router.post('/get_question_by_id')
def get_kaizen_question_by_id(question_data: QuestionDataId, status_code=status.HTTP_200_OK):
    try:
        questions = KaizenQuestionsService.get_kaizen_question_by_id(question_data)

        question_schema = KaizenQuestionSchema(many=True)
        questions = question_schema.dump(questions)

    except DBFetchFailureException as ex:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    except DBRecordNotFound as ex:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    except InvalidDataException as ex:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(ex))

    except Exception as ex:
        import traceback
        traceback.print_exc()
        logger.error(f'Unexpected error occurred. Error - {ex}')
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    return questions
