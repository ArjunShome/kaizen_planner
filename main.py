import json
import logging

import uvicorn
from starlette.requests import Request
from starlette.responses import Response

from app import create_app
from config import app_config

request_logger = logging.getLogger('RequestLogger')

fast_app = create_app(app_config)


@fast_app.middleware('http')
def logging_middleware(request: Request, call_next):
    request_logger.debug(json.dumps({
        'path': request.url.path,
        'method': request.method,
        'gs_api_key': request.headers.get('gs-api-key')
    }))
    response: Response = call_next(request)
    return response


if __name__ == '__main__':
    uvicorn.run('main:fast_app', host='0.0.0.0', port=8000, reload=True)
