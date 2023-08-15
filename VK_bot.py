import vk_api
from vk_api.longpoll import *
import requests
import VK_bot_settings as settings

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# API-ключ созданный ранее
#token = "6a9c267cd469388709a9e9acaddbe0aa81a0abbf12239b3e597a31729ffbddb9c88e80a443554c918b8f7"

# Авторизуемся как сообщество
#vk_community = vk_api.VkApi(token=settings.token)
vk_community = vk_api.VkApi(token="bb34ceea0988537295feed62fc9af90141401c200a235cd943a22738f32c4bc8d2a0995da558e734369fd")

# Работа с сообщениями
messages_tech = VkLongPoll(vk_community)

# Основной цикл
for event in messages_tech.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")

            elif request == "пока":
                write_msg(event.user_id, "Пока((")

            else:
                write_msg(event.user_id, "Не понял вашего ответа...")
