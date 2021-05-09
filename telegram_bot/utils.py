from telegram_bot.management.commands.bot import send_message


def send_msg(serializer):
    text = f"Фамилия: {serializer.validated_data['surname']}\n" \
           f"Имя: {serializer.validated_data['name']} \n" \
           f"Отчество: {serializer.validated_data['patronymic']}\n" \
           f"Номер телефона: {serializer.validated_data['number']}\n"
    send_message(text)
