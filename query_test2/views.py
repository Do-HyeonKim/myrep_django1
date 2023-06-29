from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.db import connections 

@api_view(['POST'])
def test(request):
    mapping_datas = request.data

    if mapping_datas.get('data'):
        data_list = mapping_datas['data']

        for data in data_list:
            id = data['id']
            where_filters = data['where_condition']
            
            query_model = TotalQuery.objects.get(id=id)
            select_query = query_model.query

            if where_filters:
                where_query = " WHERE 1=1 "
                for filter in where_filters:
                    where_condition = get_where_condition(filter)
                    where_query += where_condition

        total_query = f"SELECT * FROM ({select_query}) AS {query_model._meta.db_table} {where_query}"
        print(total_query)
        return Response({"query": total_query})

def get_where_condition(where):
    where_query = " AND "
    for key, value in where.items():
        condition = f"{key} = '{value}'"
        where_query += condition
    return where_query