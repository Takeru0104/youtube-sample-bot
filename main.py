import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        main();
    )
    

def main():
  USER_ID = info['USER_ID']
  messages=TextSendMessage(text="おはよう")
  line_bot_api.push_message(USER_ID , messages=messages)
if __name__ == "__main__":
  main()
