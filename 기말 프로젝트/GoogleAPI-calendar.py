from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime

def get_calendar_service():
    """Google Calendar API 서비스 객체를 생성합니다."""
    creds = None
    # 정확한 파일 경로를 지정
    creds_path = r"C:\Users\bk200\ByeongGwan Kang\python_nykwak\python_nykwak\기말 프로젝트\client_secret_362557770044-3rtn99c6g8kc0muf5bbh1n8epjn9vm5u.apps.googleusercontent.com.json"
    flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes=['https://www.googleapis.com/auth/calendar'])
    creds = flow.run_local_server(port=0)

    service = build('calendar', 'v3', credentials=creds)
    return service

# 예제: 구글 캘린더 서비스 객체 생성 및 사용
service = get_calendar_service()

# 예를 들어, 캘린더에서 이벤트 목록을 가져오는 기능을 테스트하려면:
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
