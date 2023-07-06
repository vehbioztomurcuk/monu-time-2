import random
import datetime
from datetime import timedelta
import pytz


log = [] 
last_monu_time = None
last_monu2_time = None

def get_response(message: str) -> str:
    p_message = message.lower()

    global last_monu_time, last_monu2_time

    # Setting Turkey time zone
    turkey_tz = pytz.timezone('Turkey')

    if p_message == '!monu':
        now = datetime.datetime.now(turkey_tz)
        current_time = datetime.datetime.now(turkey_tz)
        monu_time = current_time + timedelta(minutes=60)
        monu_time2 = current_time + timedelta(minutes=90)
        formatted_time = monu_time.strftime('%H:%M')
        formatted_time2 = monu_time2.strftime('%H:%M')
        formatted_time_range = f'{formatted_time} ve {formatted_time2}'
        formatted_time2 = current_time.strftime('%H:%M')
        result = f'>>> **Monu çıkış saati ➡️__ {formatted_time_range}__ arasındadır.** \n`{formatted_time2} saatinde kesilen monu itibariyle geçerlidir.` @here'
        log.append((message, result))
        last_monu_time = now
        return result

    if p_message == '!monu2':
        now = datetime.datetime.now(turkey_tz)
        current_time = datetime.datetime.now(turkey_tz)
        monu2_time = current_time + timedelta(minutes=60)
        monu2_time2 = current_time + timedelta(minutes=90)
        formatted_time = monu2_time.strftime('%H:%M')
        formatted_time2 = monu2_time2.strftime('%H:%M')
        formatted_time_range = f'{formatted_time} ve {formatted_time2}'
        formatted_time2 = current_time.strftime('%H:%M')
        result = f'>>> **DV 2 monu çıkış saati ➡️__ {formatted_time_range}__ arasındadır.** \n`{formatted_time2} saatinde kesilen dv2 monu itibariyle geçerlidir.` @here'
        log.append((message, result))
        last_monu2_time = now
        return result

    if p_message == '!yardim' or p_message == '!yardım':
        return '- Monument kesildikten hemen sonra **!monu** yazınız. Bot bir sonraki monu çıkış saatlerini 60 ve 90 dakika sonrası olarak bildirecektir.\n- Dv 2 monument kesildikten hemen sonra **!monu2** yazınız. Bot bir sonraki dv2 monu çıkış saatlerini 60 ve 90 dakika sonrası olarak bildirecektir.\n- Bot tarafından girilmiş olan son saatleri görmek için **!log** yazabilirsiniz.'

    if p_message == '!log':
        if log:
            return 'Bot tarafından girilmiş olan son saatler aşağıdadır:\n\n' + '\n\n'.join([f'{i+1}. {log[i][1]}' for i in range(len(log)-1, -1, -1)])
        else:
            return 'Kayıt bulunamadı.'
