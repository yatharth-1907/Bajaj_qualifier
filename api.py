import requests

name = "Yatharth Patankar"
reg_no = "0827AL221155"
email = "yatharthpatankar221097@acropolis.in"

url1 = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
body = {
    "name": name,
    "regNo": reg_no,
    "email": email
}

response1 = requests.post(url1, json=body)

if response1.status_code == 200:
    data = response1.json()
    webhook_url = data['webhook']
    access_token = data['accessToken']

    print("Webhook generated!")

    url2 = webhook_url
    headers = {
        "Authorization": access_token,
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

    response2 = requests.post(url2, json=data, headers=headers)
    print(response2.status_code)
    print(response2.text)
