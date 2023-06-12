from apscheduler.schedulers.background import BackgroundScheduler
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import * 
from .serializer import *
import requests
from pathlib import Path
from datetime import datetime, timedelta

scheduler = BackgroundScheduler()

@api_view(['POST'])
def scheduler_start(request) : 
    app_info_list = get_app_info() 
    print("app_info_list = " , app_info_list)

    for app_info in app_info_list : 
        print("app_info  = " , app_info)
        app_name = app_info['app_name']
        url = app_info['url']
        save_dir = app_info['save_dir']
        status = app_info['status']

        job = scheduler.get_job(app_name)
        print(job)
        if job is None : 
            scheduler.add_job(
                run_download,
                args=(app_name,url,save_dir,status),
                trigger= "interval",
                seconds = 30,
                id = app_name
            )
        else : 
            scheduler.resume_job(app_name)
    scheduler.start()

    return Response({"msg" : "scheduler started"})

                                   
def run_download(app_name, url, save_dir, status) :

    print("run_download")
    app_model = AppInfoModel.objects.filter(app_name = app_name).values()[0]
    start_date = app_model['start_date']
    print(start_date)

    today = datetime.today().date()

    if "-" in start_date:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    else:
        start_date_obj = datetime.strptime(start_date, "%Y%m%d").date()

    if start_date_obj > today:
        print("Start date is in the future. Skipping the task.")
        return

    if status == "waiting" :
        try : 
            AppInfoModel.objects.filter(app_name = app_name).update(status="running")
            args = {
                "start_date" : start_date,
                "save_dir" : save_dir
            }
            response = requests.post(url,data=args)

            if response.status_code ==200 : 
                # log rdbms save 
                log = {}
                log['app_name'] = app_name
                log['status'] = "complete"
                log['start_date'] = start_date
                log['end_date'] = get_latest_folder(save_dir)

                log_serializer = AppDownloadLogSerializer(data=log)

                if log_serializer.is_valid():
                    log_serializer.save()
                    print("save")

                AppInfoModel.objects.filter(app_name = app_name).update(status="waiting" 
                                 ,start_date=get_next_day(get_latest_folder(save_dir)) )
            else :
                print("errored : ", response.status_code ) 
                AppInfoModel.objects.filter(app_name = app_name).update(status="errored")
        except Exception as e  :
            print (e)
            AppInfoModel.objects.filter(app_name = app_name).update(status="errored")

    elif status == "pause" :
        scheduler.pause_job(app_name)
        print("pause job")

    else : 
        print(app_name , "status ==" , status)
        return
        

def get_app_info() : 
    app_info_list = AppInfoModel.objects.values()
    return app_info_list


def get_latest_folder(directory):
    directory_path = Path(directory)

    # 디렉토리 내의 모든 폴더 리스트 가져오기
    folders = [f for f in directory_path.iterdir() if f.is_dir()]

    # 폴더가 없는 경우 None 반환
    if not folders:
        return None

    # 폴더 리스트에서 가장 큰 폴더 반환
    latest_folder = max(folders, key=lambda f: f.name)

    return latest_folder.name


def get_next_day(folder_name):
    is_formatted = "-" in folder_name

    if is_formatted:
        # 날짜 형식을 포함하는 경우
        # 폴더 이름을 날짜로 해석
        date = datetime.strptime(folder_name, "%Y-%m-%d")
        next_date = date + timedelta(days=1)
        next_folder_name = next_date.strftime("%Y-%m-%d")
    else:
        # 날짜 형식을 포함하지 않는 경우
        # 폴더 이름을 날짜로 추론
        date = datetime.strptime(folder_name, "%Y%m%d")
        next_date = date + timedelta(days=1)
        next_folder_name = next_date.strftime("%Y%m%d")

    return next_folder_name


