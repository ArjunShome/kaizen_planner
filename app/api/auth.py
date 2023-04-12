# from fastapi import Header, HTTPException, status
# from fastapi.logger import logger
#
# from app.service import KaizenQuestionsService
#
#
# def authorize_client(gs_api_key: str = Header(None)):
#     logger.info(f'Authorizing client with API key - {gs_api_key}')
#     if not gs_api_key:
#         error_msg = 'API key is not provided.'
#         logger.error(error_msg)
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_msg)
#
#     try:
#         # ClientService.get_client_data_by_key(gs_api_key)
#     except Exception as ex:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(ex))
#
#     logger.info(f'Authorization successful for API key - {gs_api_key}')
#     return True
