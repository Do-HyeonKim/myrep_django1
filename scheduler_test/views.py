from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
import os

@api_view(['POST'])
def run(request):

    # start_date_str로 받은 날짜
    start_date_str = request.data.get('start_date')
    save_dir = request.data.get('save_dir')

    # 오늘 날짜부터 7일 전 날짜 가져오기
    end_date = datetime.today()
    # 시작 날짜 변환
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    # 날짜 범위 계산
    date_range = end_date - start_date

    # 폴더 생성
    for i in range(date_range.days + 1):
        folder_date = start_date + timedelta(days=i)
        folder_name = folder_date.strftime("%Y-%m-%d")
        folder_path = os.path.join(save_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    return Response({   
        "start_date" :start_date.date() ,
        "end_date" : end_date.date()
        })



@api_view(['POST'])
def run2(request):

    # start_date_str로 받은 날짜
    start_date_str = request.data.get('start_date')
    save_dir = request.data.get('save_dir')

    start_date_str = str(start_date_str).replace("-","")
    # 오늘 날짜 가져오기
    end_date = datetime.today() 
    # 시작 날짜 변환
    start_date = datetime.strptime(start_date_str, "%Y%m%d")

    # 날짜 범위 계산
    date_range = end_date - start_date

    # 폴더 생성
    for i in range(date_range.days + 1):
        folder_date = start_date + timedelta(days=i)
        folder_name = folder_date.strftime("%Y%m%d")
        folder_path = os.path.join(save_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    return Response("ok")





