import requests
# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
res.raise_for_status()
# print("웹 스크래핑을 진행합니다.")
# print("응답코드 : ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("에러. [에러코드]", res.status_code, "]")


print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)