from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connections 
# Create your views here.


@api_view(['POST'])
def test(request):
    table_name = request.data.get('name',None)
    data_num = request.data.get('num',None)
    partition_value = request.data.get('partition',None)

    field_list =  get_field_list(table_name,data_num)
    where_condition = get_where_condition(partition_value)
    print(where_condition)

    query = ""
    if field_list is not None or where_condition is not None :
        query += field_list + "  "
        query += where_condition
   
    return Response({"select_query" : field_list,
                     "where_query" : where_condition,
                     "total_query" : query})


def get_field_list(table_name,data_num) : 
    conn = connections['default']
    
    if data_num == 1 : 
        query = f"SELECT value_info FROM test_table WHERE table_info = '{table_name}' and data_num = '1' "
    elif data_num ==2 :
        query = f"SELECT value_info FROM test_table WHERE table_info = '{table_name} ' "

    cur = conn.cursor()
    cur.execute(query)
    result= cur.fetchall()

    column_list = [row[0] for row in result]

    all_column_list  = ", ".join(column_list)

    prepared_select_query = f"SELECT {all_column_list} FROM {table_name}"

    return prepared_select_query


def get_where_condition(partition_value) :
    where_query = "WHERE "


    conditions = []
    for key, value in partition_value.items():
        condition = f"{key} = '{value}'"
        conditions.append(condition)

    where_query += " AND ".join(conditions)
    return where_query