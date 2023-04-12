from fastapi import APIRouter
from app.api.questions_apis import questions_api_router, analysis_questions_api_router
from app.api.apply_kaizen_apis import apply_kaizen_api_router

ping_router = APIRouter()


@ping_router.get('/ping')
def health_check():
    return 'pong ... !'


API_ROUTERS = [
    ping_router,
    questions_api_router,
    analysis_questions_api_router,
    apply_kaizen_api_router
]
