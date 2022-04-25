import json
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    #X-Line-Signatureヘッダー値を取得します
    signature = request.headers['X-Line-Signature']

    #リクエスト本文をテキストとして取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #Webhook本体を処理する
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.reply_token == "00000000000000000000000000000000":
        return

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run(host="localhost", port=8000)
 
def main():
  USER_ID = info['USER_ID']
  messages=TextSendMessage(text="おはよう")
  line_bot_api.push_message(USER_ID , messages=messages)
if __name__ == "__main__":
    main()
