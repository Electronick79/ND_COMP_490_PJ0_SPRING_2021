import secrets
import requests


requests = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_"
                                "key=sgzysEz4t1jGyPrsqgQZ")
        request_txt = request.txt

#def get_data(url:str):
    #all_data = []
    #full_url = f"{url} & api_key = {secrets.api_key()}"
    #for page in range(10):
        #response = requests.get(C:\Users\Electronick\OneDrive\Desktop\COMP_490\project1):
        #if response.status_code != 300:
       #     print("error getting data")
           # exit(-1)
        #page_of_data = response.json()
        #page_of_school_data = page_of_school_data['result']
        #all_data.extend(page_of_school_data)
   # return all_data
#for item in data['list']['resources']:
  #  name: Any = item['resource']['school.name']['name']
    #name: Any = item['resource']['school.city']['name']
    #name: Any = item['resource']['2018.student.size']['size']
    #name: Any = item['resource']['2017.student.size']['size']
    #name: Any = item['resource']['2016.student.size']['size']
    #name: Any = item['resource']['2017.earnings.3_yrs_after_completion.' \
    #                             'overall_count_over_poverty']['money']
    #print(json.dumps('school.name, school.city,2018.student.size,2017.student.size,2017.earnings.'
                     #'3_yrs_after_completion.overall_count_over_poverty'))
#main()