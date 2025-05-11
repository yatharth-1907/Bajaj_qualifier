import requests

url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdBTDIyMTE1NSIsIm5hbWUiOiJZYXRoYXJ0aCBQYXRhbmthciIsImVtYWlsIjoieWF0aGFydGhwYXRhbmthcjIyMTA5N0BnbWFpbC5jb20iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjE5OTAsImV4cCI6MTc0Njk2Mjg5MH0.ywnbdi8ZQ2Y9RdPOv6AGErMFbtwv8MHokJhOVQovPdI",
    "Content-Type": "application/json"
}

data = {
    "finalQuery": '''
    SELECT p.AMOUNT AS SALARY,CONCAT(e.FIRST_NAME,' ',e.LAST_NAME) AS NAME,TIMESTAMPDIFF(YEAR,E.DOB,CURDATE()) AS AGE, d.DEPARTMENT_NAME FROM PAYMENTS p
    JOIN EMPLOYEE e on p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT d ON e.DEPARTMENT=d.DEPARTMENT_ID
    WHERE DAY(p.PAYMENT_TIME) !=1
    ORDER BY p.AMOUNT DESC
    LIMIT 1;
'''
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)
