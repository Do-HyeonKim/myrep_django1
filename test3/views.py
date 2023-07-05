from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.db import connections 

# Create your views here.
@api_view(['POST'])
def test(request):
    idx = 0
    setting_key = ""
    id = request.data.get('id')
    childs = request.data.get('child', None)
    filter = request.data.get('filter', None)
    first_model = QueryModel.objects.filter(id=id).values()[0]['query']    
    first_model +=  makeFilter(filter)
    first_query = f"({first_model}) as table{idx}"
    print("query0=",first_query)

    set_key = request.data.get('mapKey',None)
    from_key = set_key[0]['cols'][0]['from']
    to_key =  set_key[0]['cols'][0]['to']
    setting_key += f" where table{idx}.{from_key} = table{idx+1}.{to_key}"


    if len(childs) > 0 :
        idx += 1 
        ch_id = childs.get('id')
        filter = childs.get('filter')
        second_model = QueryModel.objects.filter(id=ch_id).values()[0]['query'] 
        second_model +  makeFilter(filter)
        second_query = f"({second_model}) as table{idx}"
        print("query1=",second_query)

        set_key = childs.get('mapKey',None)
        from_key = set_key[0]['cols'][0]['from']
        to_key =  set_key[0]['cols'][0]['to']
        setting_key += f" and table{idx}.{from_key} = table{idx+1}.{to_key}"

        if 'child' in childs : 
            idx += 1 
            next_childs = childs.get('child')
            ch_id = next_childs.get('id')
            filter = next_childs.get('filter')
            third_model = QueryModel.objects.filter(id=ch_id).values()[0]['query'] 
            third_model +  makeFilter(filter)
            third_query = f"({third_model}) as table{idx}"
            print("query2=",third_query)

            set_key = next_childs.get('mapKey',None)
            from_key = set_key[0]['cols'][0]['from']
            to_key =  set_key[0]['cols'][0]['to']
            setting_key += f" and table{idx}.{from_key} = table{idx+1}.{to_key}"
            if 'child' in next_childs :
                 idx += 1 
                 next_childs2 = next_childs.get('child')
                 ch_id = next_childs2.get('id')
                 filter = next_childs2.get('filter')
                 last_model = QueryModel.objects.filter(id=ch_id).values()[0]['query'] 
                 last_model +  makeFilter(filter)
                 last_query = f"({last_model}) as table{idx}"
                 print("query3=",last_query)
    
    prepared_query = f"select table{idx}.* from {first_query}, {second_query}, {third_query}, {last_query} {setting_key} "

    print(prepared_query)

    total_query = f" select * from ({prepared_query}) as table{idx+1}"
    return Response({"data":total_query})


def makeFilter(filter):
    query_model =""
    if filter and len(filter) > 0 :
        if filter[0]['colType'] == 'int' :
            str_nameEn = str(filter[1]['nameEn'])
            value = filter[2]['value']
            query_model = f" where {str_nameEn} like '%{value}%' "
    
    return query_model


@api_view(['POST'])
def test2(request):
    idx = 0
    setting_key = ""
    id = request.data.get('id')
    childs = request.data.get('child', None)
    filter = request.data.get('filter', None)
    first_model = QueryModel.objects.filter(id=id).values()[0]['query']
    first_model += makeFilter(filter)
    first_query = f"({first_model}) as table{idx}"
    print("query0=", first_query)

    set_key = request.data.get('mapKey', None)
    from_key = set_key[0]['cols'][0]['from']
    to_key = set_key[0]['cols'][0]['to']

    queries = [first_query]

    if childs:
        setting_key += f" where table{idx}.{from_key} = table{idx+1}.{to_key}"
        child_dict = childs  # 'child' 키 값을 원하는 경우 child_dict = childs.get('child', None) 대신에 이렇게 설정
        while child_dict:
            # child_dict를 사용하여 작업 수행
            idx += 1
            ch_id = child_dict.get('id')
            filter = child_dict.get('filter')
            model = QueryModel.objects.filter(id=ch_id).values()[0]['query']
            model += makeFilter(filter)
            child_query = f"({model}) as table{idx}"
            print(f"query{idx-1}=", child_query)

            set_key = child_dict.get('mapKey', None)
            from_key = set_key[0]['cols'][0]['from']
            to_key = set_key[0]['cols'][0]['to']
            if child_dict.get('child', None) : 
                setting_key += f" and table{idx}.{from_key} = table{idx+1}.{to_key}"
            child_dict = child_dict.get('child', None)  # 다음 child_dict를 설정하기 위해 재할당
            
            queries.append(child_query)
    prepared_query = f"select table{idx}.* from {', '.join(queries)} {setting_key}"
    # prepared_query = f"select {queries[-1]}.* from {', '.join(queries)} {setting_key}"

    print(prepared_query)

    total_query = f"select * from ({prepared_query}) as table{idx+1}"
    return Response({"data": total_query})
    # return Response({"data": "total_query"})

@api_view(['POST'])
def test3(request):
    idx = 0
    setting_key = ""
    id = request.data.get('id')
    childs = request.data.get('child', None)
    filter = request.data.get('filter', None)
    first_model = QueryModel.objects.filter(id=id).values()[0]['query']
    first_model += makeFilter(filter)
    first_query = f"({first_model}) as table{idx}"
    print("query0=", first_query)

    set_key = request.data.get('mapKey', None)
    from_key = set_key[0]['cols'][0]['from']
    to_key = set_key[0]['cols'][0]['to']
    

    queries = [first_query]
    if childs : 
        setting_key += f" where table{idx}.{from_key} = table{idx+1}.{to_key}"
        child_dict = childs
        while child_dict:
            idx += 1
            ch_id = child_dict.get('id')
            filter = child_dict.get('filter')
            model = QueryModel.objects.filter(id=ch_id).values()[0]['query']
            model += makeFilter(filter)
            child_query = f"({model}) as table{idx}"
            print(f"query{idx-1}=", child_query)

            set_key = child_dict.get('mapKey', None)
            from_key = set_key[0]['cols'][0]['from']
            to_key = set_key[0]['cols'][0]['to']
            if child_dict.get('child'):
                setting_key += f" and table{idx}.{from_key} = table{idx+1}.{to_key}"
            queries.append(child_query)
            child_dict = child_dict.get('child', None)

    prepared_query = f"select table{idx}.* from {', '.join(queries)} {setting_key}"
    total_query = f"select * from ({prepared_query}) as table{idx+1}"
        
    print(total_query)

    return Response({"data": total_query})




# @api_view(['POST'])
# def test3(request):
#     idx = 0
#     setting_key = ""
#     id = request.data.get('id')
#     childs = request.data.get('child', None)
#     filter = request.data.get('filter', None)
#     first_model = QueryModel.objects.filter(id=id).values()[0]['query']
#     first_model += makeFilter(filter)
#     first_query = f"({first_model}) as table{idx}"
#     print("query0=", first_query)

#     set_key = request.data.get('mapKey', None)
#     from_key = set_key[0]['cols'][0]['from']
#     to_key = set_key[0]['cols'][0]['to']
#     setting_key += f" where table{idx}.{from_key} = table{idx+1}.{to_key}"

#     queries = [first_query]

#     if childs:
#         child_dict = childs.get('child', None)
#         while child_dict:
#             print(child_dict)
#             idx += 1
#             ch_id = child_dict.get('id')
#             filter = child_dict.get('filter')
#             model = QueryModel.objects.filter(id=ch_id).values()[0]['query']
#             model += makeFilter(filter)
#             child_query = f"({model}) as table{idx}"
#             print(f"query{idx-1}=", child_query)

#             set_key = child_dict.get('mapKey', None)
#             from_key = set_key[0]['cols'][0]['from']
#             to_key = set_key[0]['cols'][0]['to']
#             setting_key += f" and table{idx}.{from_key} = table{idx+1}.{to_key}"

#             queries.append(child_query)

#             child_dict = child_dict.get('child', None)

#     prepared_query = f"select table{idx}.* from {', '.join(queries)} {setting_key}"

#     print(prepared_query)

#     total_query = f"select * from ({prepared_query}) as table{idx+1}"
#     return Response({"data": total_query})





def makeFilter(filter):
    query_model = ""
    if filter and len(filter) > 0:
        if filter[0]['colType'] == 'int':
            str_nameEn = str(filter[1]['nameEn'])
            value = filter[2]['value']
            query_model = f" where {str_nameEn} like '%{value}%' "

    return query_model
