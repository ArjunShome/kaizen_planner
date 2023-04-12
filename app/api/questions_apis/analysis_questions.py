from fastapi import APIRouter, status
from fastapi.logger import logger
from fastapi.responses import JSONResponse

from app.lib.custom_exception import DBFetchFailureException, DBRecordNotFound, InvalidDataException
from app.request_models import AnalysisQuestionData, AnalysisQuestionDataId
from app.serializers import KaizenAnalysisQuestionSchema
from app.service import KaizenAnalysisQuestionsService

analysis_questions_api_router = APIRouter(prefix='/analysis_question_apis')


@analysis_questions_api_router.post('/get_analysis_questions')
def get_kaizen_analysis_questions(question_data: AnalysisQuestionData, status_code=status.HTTP_200_OK):
    try:
        analysis_questions = KaizenAnalysisQuestionsService.get_kaizen_analysis_questions_by_analysis_type(question_data)

        analysis_question_schema = KaizenAnalysisQuestionSchema(many=True)
        analysis_questions = analysis_question_schema.dump(analysis_questions)

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

    return analysis_questions

@analysis_questions_api_router.post('/get_analysis_question_by_id')
def get_kaizen_analysis_question_by_id(analysis_question_data: AnalysisQuestionDataId, status_code=status.HTTP_200_OK):
    analysis_question_id = analysis_question_data.kaizen_analysis_question_id
    try:
        analysis_question = KaizenAnalysisQuestionsService.get_kaizen_analysis_question_by_question_id(analysis_question_id)

        analysis_question_schema = KaizenAnalysisQuestionSchema()
        analysis_question = analysis_question_schema.dump(analysis_question)

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

    return analysis_question
