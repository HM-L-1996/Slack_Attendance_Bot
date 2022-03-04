# ~/slackbot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import requests
import json
import pandas as pd
import os.path
import calendar



def post_message(token, channel, text,attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text,"emoji":True,"attachments":attachments})
    print(response)


# 봇 토큰 추가
bot_token = 'xoxb-3170797371863-3185447932163-FWIq77kVX5pgX1NFFJmqc1f2'

# Create your views here.
class Attend(APIView):
    def post(self, request):
        """
        슬랙에서 채팅 이벤트가 있을 때 호출하는 API
        :param request:
        :return:
        """

        # body에서 challenge 필드만 빼오기
        challenge = request.data.get('challenge')

        user = request.data.get('event').get('user')
        text = request.data.get('event').get('text')
        if text == '출석체크':
        # print("사용자 :", user, "| 메시지 :", text)

            t = datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분")
            text = t + "입니다 여러분들 출석체크 해주세요~~!!!"
            attachments =  {
                "fallback": "출석체크!",
                "callback_id": "Check_button",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "check",
                        "text": "출석체크",
                        "type": "button",
                        "value": "check"
                    },
                ]
            }
            attachments_list = [attachments]
            if user == 'U035FD5TE4T':
                print("봇 메시지")
            else:
                # 요기가 메시지 보내는 부분
                post_message(bot_token, "#출석체크",text,attachments_list)

        # 응답 데이터로 { challenge : challenge } 주기
        return Response(status=200, data=dict(challenge=challenge))
class Check(APIView):
    def post(self, request):
        data = json.loads(request.data.get('payload'))
        datetimeobj = datetime.fromtimestamp(float(data["action_ts"])).strftime("%Y년 %m월 %d일 %H시 %M분")
        datetime_col = datetime.fromtimestamp(float(data["action_ts"])).strftime("%Y-%m-%d")

        years = datetime.today().year
        months = datetime.today().month
        days = datetime.today().day
        day_cnt = calendar.monthrange(years, months)
        # if os.path.isfile('./Data/Attendance_{}_{}.csv'.format(years,months)):
        #     dataset = pd.read_csv('./Data/Attendance_{}_{}.csv'.format(years,months))
        # else:
        #     dataset = pd.DataFrame()
        # if not dataset['{}'.format(days)]:
        #     dataset.insert(int(days) - 1, days, '')
        print(data["user"]["name"])
        print(datetimeobj)
        return Response(status=200)