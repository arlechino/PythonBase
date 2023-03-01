from datetime import datetime
class BaseData:
    baseLogin = "guest"
    basePassword = "welcome2qauto"
    host = "qauto.forstudy.space"
    base_url = f'https://{host}'
    car_url = f'https://{host}/panel/garage'

    @staticmethod
    def get_millage() -> int:
        # today = date.today()
        # today.strftime('%y%j%H%I')
        return int(datetime.now().strftime('%y%H%M'))