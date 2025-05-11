import requests

url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdBTDIyMTE1NSIsIm5hbWUiOiJZYXRoYXJ0aCBQYXRhbmthciIsImVtYWlsIjoieWF0aGFydGhwYXRhbmthcjIyMTA5N0BhY3JvcG9saXMuaW4iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjI2NjQsImV4cCI6MTc0Njk2MzU2NH0.G-leAoi2PMcSLe1lNOBLjgj1rQRujY-74Jn_qK3rRaA",
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
