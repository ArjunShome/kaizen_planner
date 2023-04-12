from fastapi import Header, HTTPException, status
from fastapi.logger import logger

from app.cache import app_cache
# from app.cache.client_cache import ClientCache


def throttle_apis(gs_api_key: str = Header(None)):
    logger.info(f'Verifying the API usage of client with API key - {gs_api_key}')
    if not gs_api_key:
        error_msg = 'API key is not provided.'
        logger.error(error_msg)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_msg)

    try:
        client_data = app_cache.get(gs_api_key)
        # if not client_data:
        #     client_data = ClientCache.hydrate_client_cache(gs_api_key)

        call_count = client_data.get('call_count')
        per_day_limit = client_data.get('client').get('per_day_limit')

    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(ex))

    if per_day_limit is not None and per_day_limit < call_count:
        msg = 'Your API call limit is over for today.'
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=msg)

    logger.info(f'Authorization successful for API key - {gs_api_key}')
    return True
