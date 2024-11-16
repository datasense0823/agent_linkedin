import requests
import os

api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
response = requests.get(
            api_endpoint,
            params={"url": "https://www.linkedin.com/in/shagunnagpal/"},
            headers=header_dic,
            timeout=10,
        )
print(response)
print(response._content)