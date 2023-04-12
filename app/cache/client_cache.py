# from datetime import datetime
#
# from app.cache import app_cache
# from app.lib import Singleton
# # from app.repository import ClientRepo, ApiCallLogRepo
# # from app.serializers import ClientSchema
#
#
# class ClientCache(metaclass=Singleton):
#     @staticmethod
#     def hydrate_client_cache(api_key):
#         # client = ClientRepo.get_client_by_api_key(api_key)
#         # call_count = ApiCallLogRepo.get_call_count_by_api_key(api_key)
#         data_schema = ClientSchema()
#         # client = data_schema.dump(client)
#
#         curr_time = datetime.utcnow()
#         end_time = curr_time.replace(hour=11, minute=59, second=59)
#         # client_data = {'client': client, 'call_count': call_count}
#         # app_cache.set(api_key, client_data, expiration=(end_time-curr_time).seconds)
#         #
#         # return client_data
#
#     @staticmethod
#     def get_client_by_api_key(api_key):
#         client_data = app_cache.get(api_key)
#         # if not client_data:
#         #     client_data = ClientCache.hydrate_client_cache(api_key)
#
#         client = client_data.get('client')
#         data_schema = ClientSchema()
#         client = data_schema.load(client)
#
#         return client
#
#     @staticmethod
#     def update_call_count(api_key):
#         client_data = app_cache.get(api_key)
#         # if not client_data:
#         #     client_data = ClientCache.hydrate_client_cache(api_key)
#
#         curr_time = datetime.utcnow()
#         end_time = curr_time.replace(hour=11, minute=59, second=59)
#         call_count = client_data.get('call_count', 0) + 1
#         client_data['call_count'] = call_count
#
#         app_cache.set(api_key, client_data, expiration=(end_time-curr_time).seconds)
