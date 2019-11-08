import json

with open('ITT_Student.json',encoding='UTF8') as json_file:
 json_object = json.load(json_file)
 json_string = json.dumps(json_object)
 g_json_big_data = json.loads(json_string)

i=0
while i<3:
 print("*학생 ID :%s" % g_json_big_data[i]['student_ID'])
 i +=1