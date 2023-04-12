from fastapi import APIRouter, status
from fastapi.logger import logger
from fastapi.responses import JSONResponse

from app.lib.custom_exception import DBFetchFailureException, DBRecordNotFound, InvalidDataException
from app.request_models import ApplyKaizenData
from app.serializers import KaizenSchema
from app.service import KaizenApplyService

apply_kaizen_api_router = APIRouter(prefix='/apply_kaizen_apis')

@apply_kaizen_api_router.post('/apply_kaizen')
def apply_kaizen(question_data: ApplyKaizenData, status_code=status.HTTP_200_OK):
    try:
        kaizen = KaizenApplyService.apply_kaizen(question_data)

        kaizen_schema = KaizenSchema()
        kaizen = kaizen_schema.dump(kaizen)

    except DBFetchFailureException as ex:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    except Exception as ex:
        import traceback
        traceback.print_exc()
        logger.error(f'Unexpected error occurred. Error - {ex}')
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(ex))

    return kaizen