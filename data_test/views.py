from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import * 
import os
import datetime
import json
import pandas as pd

# Create your views here.

@api_view(['post'])
def read_time_value(request) :

    temp_folder = 'C:/tempdir/'
    # 현재 시간을 기준으로 폴더 경로 생성
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    uuid = "506caa780ec64039894e"
    current_date_uuid = current_date +'/'+ uuid
    folder_path = os.path.join(temp_folder, current_date_uuid)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 파일 이름 생성
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{current_time}.txt"
    file_name_csv = f"{current_time}.csv"
    file_path = os.path.join(folder_path, file_name)
    file_path_csv = os.path.join(folder_path, file_name_csv)
    save_list = []
    
    status_model = StatusModel.objects.filter(run_date = current_date).order_by('-reg_dtm').first()
    
    if status_model :
        get_last_timestamp = status_model.last_timestamp
        print(get_last_timestamp)
        
        file_list = ['test_2.txt', 'test_3.txt']
        print(file_list)

        for file in file_list : 
            print(file)
            test_file_path = os.getcwd() + '/' + file
            # print(test_file_path)
            with open(test_file_path,'r') as f :
                for line in f:
                    data = json.loads(line)
                    save_list.append(data)


            new_save_list = []
            for i in range(len(save_list)):
                timestamp = save_list[i]['timestamp']
                if int(timestamp) > int(get_last_timestamp):
                    print(int(timestamp))
                    new_save_list.append(save_list[i])

            print(new_save_list)
            # 파일 쓰기 1 
            # with open(file_path, "w") as f:
            #     f.write(json.dumps(new_save_list))
                # for data in save_list:
                #     f.write(json.dumps(data) + "\n")
            # 파일 쓰기 2 - csv
            df = pd.DataFrame(new_save_list)
            df.to_csv(file_path_csv, index=False)

            if new_save_list : 
                last_data = new_save_list[-1]
                last_timestamp = last_data['timestamp']
                print(last_timestamp)

                status = {}
                # status['uuid'] = uuid
                status['last_timestamp'] = last_timestamp
                status['last_file_name'] = file_name

                status_ser = StatusSerializer(data=status)
                print(status_ser.is_valid())
                print(status_ser.errors)

                if status_ser.is_valid() :
                    status_ser.save()

        return Response(new_save_list)

    else : 
        test_file_path = os.getcwd() + '/test.txt'
        # print(test_file_path)
        with open(test_file_path,'r') as f :
            for line in f:
                data = json.loads(line)
                save_list.append(data)
        print(save_list)

        last_data = save_list[-1]
        last_timestamp = last_data['timestamp']
        print(last_timestamp)

        # 파일 쓰기
        with open(file_path, "w") as f:
            f.write(json.dumps(save_list))

        status = {}
        # status['uuid'] = uuid
        status['last_timestamp'] = last_timestamp
        status['last_file_name'] = file_name

        status_ser = StatusSerializer(data=status)
        print(status_ser.is_valid())
        print(status_ser.errors)

        if status_ser.is_valid() :
             status_ser.save()



    return Response(save_list)



@api_view(['post'])
def read_time_value2(request) :

    temp_folder = 'C:/Temp_dir/'
    
    # 현재 시간을 기준으로 폴더 경로 생성
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    folder_path = os.path.join(temp_folder, current_date)
    # 폴더가 없는 경우 새로 만들기
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 새로 저장될 파일 이름 현재 시간으로 생성
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{current_time}.json"
    file_path = os.path.join(folder_path, file_name)
    # 읽은 데이터를 저장할 list 선언
    save_list = []

    # 등록일 내림차순으로 실행일자 = 오늘 날짜인 데이터의 첫번째 값을 status_model 변수의 값으로 지정
    status_model = StatusModel.objects.filter(run_date = current_date).order_by('-reg_dtm').first()

    #status_model이 있는 경우 실행되는 로직
    if status_model :
        get_last_timestamp = status_model.last_timestamp
        print(get_last_timestamp)

        
        #추가된 timestamp가 있는 경우 txt 파일 읽어오기
        test_file_path = os.getcwd() + '/test_2.txt'
        with open(test_file_path,'r') as f :
            for line in f:
                data = json.loads(line)
                save_list.append(data)

        #새로 추가된 값을 저장할 list 선언
        new_save_list = []
        for i in range(len(save_list)):
            timestamp = save_list[i]['timestamp']
            # status_model 에서 가져온 get_last_timestamp의 값보다 새로 읽어온 timestamp 가 더 큰 경우
            # new_save_list 리스트에 저장
            if int(timestamp) > int(get_last_timestamp):
                new_save_list.append(save_list[i])
        print(new_save_list)
        if new_save_list  : 
          # 새로 저장할 파일 쓰기
            with open(file_path, "w") as f:
                f.write(json.dumps(new_save_list))

            last_data = new_save_list[-1]
            last_timestamp = last_data['timestamp']
            last_value = last_data['value']

            status = {}
            status['last_timestamp'] = last_timestamp
            status['last_value'] = last_value
            status['last_file_name'] = file_name

            status_ser = StatusSerializer(data=status)
            print(status_ser.is_valid())
            print(status_ser.errors)

            if status_ser.is_valid() :
                status_ser.save()
            
            return Response(new_save_list)
        
        else : 
            return Response([])

            
    #status_model이 없는 경우 실행되는 로직
    else : 
        #txt 파일 읽어오기
        test_file_path = os.getcwd() + '/test.txt'
        with open(test_file_path,'r') as f :
            for line in f:
                data = json.loads(line)
                save_list.append(data)

        last_data = save_list[-1]
        last_timestamp = last_data['timestamp']
        last_value = last_data['value']

        # json 파일 쓰기
        with open(file_path, "w") as f:
            f.write(json.dumps(save_list))

        status = {}
        status['last_timestamp'] = last_timestamp
        status['last_value'] = float(last_value)
        status['last_file_name'] = file_name

        status_ser = StatusSerializer(data=status)
        print(status_ser.is_valid())
        print(status_ser.errors)

        if status_ser.is_valid() :
             status_ser.save()

    return Response(save_list)

# @api_view(['post'])
# def find_last_timestamp(request) : 