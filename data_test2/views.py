from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import json
import os
import pandas as pd

@api_view(['POST'])
def microseconds_to_date(request):
    microseconds = 1683114594400000
    seconds, microseconds = divmod(microseconds, 1000000)
    dt = datetime.fromtimestamp(seconds)
    microseconds = microseconds 
    date_time = dt.strftime('%Y-%m-%d %H:%M:%S')
    print(date_time)
    return Response(date_time)


@api_view(['POST'])
def date_to_microseconds(request):
    date_time = '2023-05-03 20:49:54'
    dt = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    microseconds = int(dt.timestamp() * 1000000)
    print(microseconds)
    return Response(microseconds)

@api_view(['POST'])
def json_test(request):
    json_file_path = os.getcwd() + '/json_test.txt'
    csv_file_path = os.getcwd() + '/csv_test.csv'
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)

    return Response()