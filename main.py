import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами
import pandas as pd  # Для формирования датафрейма с результатами

import requests

url = "https://uslugi.mosreg.ru/zdrav/doctor_appointment/api/doctors?lpuCode=&departmentId=46&doctorId=&days=14"

payload = {}
headers = {
  'Cookie': 'da_sPol=; da_nPol=6456240891052977; da_birthday=08.03.1957; da_auth=true; polis_login_failed=0; _ym_uid=1683391171887871442; _ym_d=1683391171; SSESSa8582a3dc976377cc65d7fbc474627fe=zqwOWaN9eqBo1BKbWsM-rasDPlnYOre_eZ2pFPkhUKo; has_js=1; _ym_isad=2; _ym_visorc=w'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
