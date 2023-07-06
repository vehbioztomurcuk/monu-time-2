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
        return '# !yardim / !help\n\n- **!monu** (Sonraki Monument)\n  Sonraki monument spawn zamanını belirler. Monument kesildikten hemen sonra kullanılmalıdır.\n- **!monu2** (Sonraki DV2 Monument)\n  `!monu` komutunun DV2 versiyonu.\n- **!log** (Kayıtlar)\n  Bot tarafından kaydedilen son zamanları gösterir.\n\nEk yardımcı komutlar:\n- `!rün` or `!rune` (Rünler): Rün sistemi\n- `!craft` or `!meslek` or `!meslekler` (Craft veya Meslekler): Craft sistemi ve meslekler\n- `!weaponcraft` or `!silahcraft` (Silah Craft): Silah üretim sistemi\n- `!jewelcraft` or `!takıcraft` (Takı Craft): Takı üretim sistemi\n- `!clan` or `!klan` (Klan): Klan binaları ve özellikleri\n- `!silah` or `!weapons` (Silahlar): Oyundaki silahlar\n- `!takı` or `!accessories` (Takılar): Oyundaki takılar\n- `!belt` or `!kemer` (Kemerler): Oyundaki kemerler\n- `!ring` or `!yüzük` (Yüzükler): Oyundaki yüzükler\n- `!küpe` or `!earring` (Küpeler): Oyundaki küpeler\n- `!neck` or `!kolye` or `!pendant` (Kolyeler): Oyundaki kolyeler\n- `!hata` or `!error` (Hatalar): Tüm hatalar ve çözümleri\n- `!upgrade` (Upgrade): Upgrade başarı oranları'

    if p_message == '!help':
        return '# !yardim / !help\n\n- **!monu** (Next Monument)\n  Determines the next monument spawn time. It should be used immediately after the monument is killed.\n- **!monu2** (Next DV2 Monument)\n  The DV2 version of the `!monu` command.\n- **!log** (Log)\n  Displays the recent times recorded by the bot.\n\nAdditional helper commands:\n- `!rün` or `!rune` (Runes): Rune system\n- `!craft` or `!meslek` or `!meslekler` (Craft or Professions): Craft system and professions\n- `!weaponcraft` or `!silahcraft` (Weapon Craft): Weapon crafting system\n- `!jewelcraft` or `!takıcraft` (Jewel Craft): Jewel crafting system\n- `!clan` or `!klan` (Clan): Clan buildings and their features\n- `!silah` or `!weapons` (Weapons): In-game weapons\n- `!takı` or `!accessories` (Accessories): In-game accessories\n- `!belt` or `!kemer` (Belts): In-game belts\n- `!ring` or `!yüzük` (Rings): In-game rings\n- `!küpe` or `!earring` (Earrings): In-game earrings\n- `!neck` or `!kolye` or `!pendant` (Necklaces): In-game necklaces\n- `!hata` or `!error` (Errors): All errors and their solutions\n- `!upgrade` (Upgrade): Upgrade success rates'

    if p_message == '!rün'or p_message == '!rune':
        return '>>> **Rise Online World (Erken Erişim) - Rünler**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-erken-erisim-runler.17973/'
    
    if p_message == '!craft'or p_message == '!meslek'or p_message == '!meslekler':
        return '>>> **1. Rise Online World (Erken Erişim) - Craft Sistemi ve Meslekler**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-erken-erisim-craft-sistemi-ve-meslekler.13888/\n**2. Rise Online World - Meslekler Rehberi (Erken Erişim)**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-meslekler-rehberi-erken-erisim.12903/'
    
    if p_message == '!weaponcraft'or p_message == '!silahcraft':
        return '>>> **Rise Online World (Erken Erişim) - Silah Üretimi (Weapon Smithing)**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-erken-erisim-silah-uretimi-weapon-smithing-guncellemesi.17984/'
    
    if p_message == '!jewelcraft'or p_message == '!takıcraft':
        return '>>> **Rise Online World (Erken Erişim) - Takı Üretimi (Jewel Crafting)**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-erken-erisim-taki-uretimi-jewel-crafting-guncellemesi.17986/'

    if p_message == '!clan'or p_message == '!klan':
        return '>>> **Rise Online World (Erken Erişim) - Klan Binalarının Özellikleri**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-erken-erisim-klan-binalarinin-ozellikleri.17331/#post-123382'

    if p_message == '!silah'or p_message == '!weapons':
        return '>>> **Rise Online World - Silahlar**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-silah-duzenlemeleri.15711/'
    
    if p_message == '!takı'or p_message == '!accessories':
        return '>>> **Takı Upgrade Sistemi ve Takılar:**\nhttps://forum.riseonlineworld.com/konular/taki-upgrade-sistemi-aktif-edildi.17972/'
    
    if p_message == '!belt'or p_message == '!kemer':
        return '>>> **Oyundaki beltler:**\nhttps://forum.riseonlineworld.com/attachments/belts-jpg.13555/'
    
    if p_message == '!ring' or p_message == '!yüzük':
        return '>>> **Oyundaki yüzükler:**\nhttps://forum.riseonlineworld.com/attachments/rings-jpg.13556/'
    
    if p_message == '!küpe'or p_message == '!earring':
        return '>>> **Oyundaki küpeler:**\nhttps://forum.riseonlineworld.com/attachments/earrings-jpg.13557/'
    
    if p_message == '!neck'or p_message == '!kolye'or p_message == '!pendant':
        return '>>> **Oyundaki kolyeler:**\nhttps://forum.riseonlineworld.com/attachments/necklaces-jpg.13558/'
    
    if p_message == '!hata'or p_message == '!error':
        return '>>> **Tüm Hatalar ve Çözümleri**\nhttps://forum.riseonlineworld.com/konular/tum-hatalar-ve-cozumleri.6163/'
    
    if p_message == '!upgrade':
        return '>>> **Upgrade oranları**\nhttps://forum.riseonlineworld.com/konular/rise-online-world-basarili-upgrade-oranlari.11847/'
    

    

    if p_message == '!log':
        if log:
            return 'Bot tarafından girilmiş olan son saatler aşağıdadır:\n\n' + '\n\n'.join([f'{i+1}. {log[i][1]}' for i in range(len(log)-1, -1, -1)])
        else:
            return 'Kayıt bulunamadı.'
