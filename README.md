# test_task_restapi
This is the test task for creating of RESTapi for login and custom user's model and comunication with etherscan.io

for install:
   - virtualenv -p python3 /path
   - source ./path/bin/active
   - python manage.py runserver 0.0.0.0:8080

      list of api: 127.0.0.1:8080/api

          user(s): 127.0.0.1:8080/api/user

    documentation: 127.0.0.1:8080/docs

addition fields for etherscan.io access (address and api key): 127.0.0.1:8080/api/user/[user id]/etherapi

get information from etherscan.io GET method: 127.0.0.1:8080/api/user/[id]/etherinfo

   
