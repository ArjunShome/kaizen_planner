from fastapi.logger import logger

from app.lib import Singleton
from app.lib.custom_exception import DBFetchFailureException, DBRecordNotFound, InvalidDataException
from app.repository import KaizenApplyRepo


class KaizenApplyService(metaclass=Singleton):

    @staticmethod
    def apply_kaizen(kaizen_data):
        """
        Service to create a new Kaizen
        """
        user_id = kaizen_data.user_id
        kaizen_type = kaizen_data.kaizen_type
        title = kaizen_data.title
        # if any in progress kaizen exists with this user id and kaizen type, return it, else create the record and return
        try:
            kaizen = KaizenApplyRepo.get_kaizen_by_kaizen_type_user_id(kaizen_type, user_id)
            if kaizen:
                return kaizen
            else:
                kaizen = KaizenApplyRepo.apply_kaizen(user_id, kaizen_type, title)
        except Exception as ex:
            error_msg = f'Error occurred while applying kaizen with kaizen type {kaizen_type}, user_id {user_id} and title {title}'
            logger.error(f'{ex} {error_msg}')
            raise DBFetchFailureException(error_msg)
        return kaizen