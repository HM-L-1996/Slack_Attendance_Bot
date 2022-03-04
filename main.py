import requests
from datetime import datetime

def main():
    # webhook url
    url = "https://hooks.slack.com/services/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"
    t =datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분")

    text = "출석체크"
    # text = t+"입니다 여러분들 출석체크 해주세요~~!!!"
    #
    payload = {
        "text": text,
        "emoji": True,
    }
    #     "attachments": [
    #         {
    #         "actions": [
    #             {
    #                 "name": "check",
    #                 "text": "출석체크",
    #                 "type": "button",
    #                 "value": "check",
    #                 "confirm": {
    #                     "title": "출석체크",
    #                     "text": datetime.today().strftime("%H시 %M분")+"에 출석체크하시겠습니까?",
    #                     "ok_text": "Yes",
    #                     "dismiss_text": "No"
    #                 }
    #             }
    #         ]
    #         }]
    # }

    requests.post(url, json=payload)

# 이 스크립트에서 실행할 함수는 main
if __name__ == "__main__":
    main()