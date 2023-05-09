from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import * 
from django.db.models import Q

@api_view(['POST'])
def test_find_column(request):
    # 입력받은 쿼리
    query = request.data.get('query')
        
   # 쿼리에서 컬럼 추출
    select_index = query.upper().find('SELECT')
    from_index = query.upper().find('FROM')
    columns = query[select_index+6:from_index].split(',')
    columns = [c.strip().split()[-1].split('.')[-1] for c in columns]
    print(columns)

   # 등록된 컬럼 처리
    registered_columns = []
    for column in columns:
        # 해당 컬럼이 포함된 모든 테이블을 가져옴
        tables = ColumnTable.objects.filter(column_en=column)

        # 해당 컬럼이 포함된 테이블 중에서 pizza 혹은 cheese 테이블만 등록
        for table in tables:
            if table.table_name in ['pizza', 'cheese']:
                column_data = {
                    'column_en': "NEW_1_"+column,
                    'column_kr': table.column_kr,
                    'table_name': "1",
                }
                # 이미 등록된 컬럼인지 확인
                if not ColumnTable.objects.filter(column_en=column_data['column_en'], table_name=column_data['table_name']).exists():
                    column_ser = ColumnSerializer(data=column_data)
                    if column_ser.is_valid():
                        column_ser.save()
                    registered_columns.append(column_data)

    return Response(registered_columns)





@api_view(['POST'])
def test_find_column2(request):
    # 입력받은 쿼리
    query = request.data.get('query')
        
   # 쿼리에서 컬럼 추출
    select_index = query.upper().find('SELECT')
    from_index = query.upper().find('FROM')
    columns = query[select_index+6:from_index].split(',')
    columns = [c.strip().split()[-1].split('.')[-1] for c in columns]
    print(columns)
    
    # 등록된 컬럼 처리
    registered_columns = []
    for column in columns:
        column_qs = ColumnTable.objects.filter(column_en=column)
        if column_qs.exists():
            column_obj = column_qs.first()
            column_data = {
                'column_en': column,
                'column_kr': column_obj.column_kr,
                'table_name': 'new'
            }
            column_ser = ColumnSerializer(data=column_data)
            if column_ser.is_valid():
                column_ser.save()
            registered_columns.append(column_data)
    return Response(registered_columns)