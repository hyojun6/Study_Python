# # #main.py 
# # from fastapi import FastAPI
# # from fastapi.responses import HTMLResponse
# # import pandas as pd
# # import random

# # app = FastAPI()

# # # 1. 가짜 날씨 데이터 생성
# # def generate_fake_weather_data():
# #     cities = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "수원"]
# #     weather_conditions = ["맑음", "구름 많음", "비", "눈", "흐림", "바람"]

# #     data = []
# #     for city in cities:
# #         temperature = round(random.uniform(-5, 35), 1)  # -5도에서 35도 사이
# #         humidity = random.randint(30, 90)  # 30%에서 90% 사이
# #         condition = random.choice(weather_conditions)

# #         # Python 3.10의 구조적 패턴 매칭을 사용하여 날씨 상태 분류
# #         match condition:
# #             case "맑음1":
# #                 icon = "☀️"
# #             case "구름 많음1":
# #                 icon = "☁️"
# #             case "비1":
# #                 icon = "🌧️"
# #             case "눈1":
# #                 icon = "❄️"
# #             case "흐림1":
# #                 icon = "🌥️"
# #             case "바람1":
# #                 icon = "💨"
# #             case _:
# #                 icon = "❓"

# #         data.append({
# #             "도시": city,
# #             "온도 (°C)": temperature,
# #             "습도 (%)": humidity,
# #             "날씨": f"{condition} {icon}"  # 날씨 상태와 아이콘 결합
# #         })

# #     return pd.DataFrame(data)

# # # 2. FastAPI 엔드포인트
# # @app.get("/", response_class=HTMLResponse)
# # async def show_weather():
# #     df = generate_fake_weather_data()
    
# #     # HTML 테이블로 변환
# #     table_html = df.to_html(index=False, escape=False, justify="center", border=1)

# #     # HTML 페이지 생성
# #     html_content = f"""
# #     <html>
# #         <head>
# #             <title>대한민국 주요 도시 날씨</title>
# #             <style>
# #                 body {{ font-family: Arial, sans-serif; text-align: center; }}
# #                 table {{ margin: 0 auto; border-collapse: collapse; width: 80%; }}
# #                 th, td {{ padding: 10px; border: 1px solid #ddd; text-align: center; }}
# #                 th {{ background-color: #f4f4f4; }}
# #             </style>
# #         </head>
# #         <body>
# #             <h1>대한민국 주요 도시 날씨 정보11</h1>
# #             //{table_html}
# #         </body>
# #     </html>
# #     """
# #     return HTMLResponse(content=html_content)

# import csv
# from bs4 import BeautifulSoup
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# # 파일 경로
# svg_path = '/Users/yanghyojun/Desktop/Python/Python_class/project/file/Busan_districts.svg'
# csv_path = '/Users/yanghyojun/Desktop/Python/Python_class/project/file/부산명소 국문 정보.csv'

# # SVG 파일 읽기
# with open(svg_path, 'r', encoding='utf-8') as svg_file:
#     svg_content = svg_file.read()

# # CSV 파일 읽기 및 데이터 처리
# district_count = {}

# with open(csv_path, 'r', encoding='utf-8') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         district = row['구군']
#         if district in district_count:
#             district_count[district] += 1
#         else:
#             district_count[district] = 1

# # BeautifulSoup을 사용하여 SVG 파싱
# soup = BeautifulSoup(svg_content, "lxml-xml")
# paths = soup.findAll('path')

# # 색상 코드 정의
# colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

# # 구군별 명소 수에 따라 색상 적용
# for p in paths:
#     if p.get('id') and p['id'] in district_count:
#         count = district_count[p['id']]
#         if count >= 10:
#             color_class = 5
#         elif count >= 7:
#             color_class = 4
#         elif count >= 5:
#             color_class = 3
#         elif count >= 3:
#             color_class = 2
#         elif count >= 1:
#             color_class = 1
#         else:
#             color_class = 0
        
#         # 색상 적용
#         color = colors[color_class]
#         style = f"fill:{color};stroke:#000000;stroke-width:0.5;"
#         p['style'] = style

# print(soup.prettify())
# # # 결과 출력
# # output_path = 'output_map.svg'
# # with open(output_path, 'w', encoding='utf-8') as output_file:
# #     output_file.write(soup.prettify())

# print(f"색상이 적용된 SVG 파일이 '{output_path}'로 저장되었습니다.")


# import csv
# from bs4 import BeautifulSoup

# svg = open('/Users/yanghyojun/Desktop/Python/Python_class/project/file/Busan_districts.svg', 'r').read()
# data = csv.reader(open('/Users/yanghyojun/Desktop/Python/Python_class/project/file/부산명소 국문 정보.csv', 'r'), delimiter=',')

# district_mapping = {
#     '부산진구': 'Busanjin-gu',
#     '해운대구': 'Haeundae-gu',
#     '남구': 'Nam-gu',
#     '동래구': 'Dongnae-gu',
#     '서구': 'Seo-gu',
#     '중구': 'Jung-gu',
#     '영도구': 'Yeongdo-gu',
#     '기장군': 'Gijang-gun',
#     '사하구': 'Saha-gu',
#     '금정구': 'Geumjeong-gu',
#     '강서구': 'Gangseo-gu',
#     '연제구': 'Yeonje-gu',
#     '수영구': 'Suyeong-gu',
#     '사상구': 'Sasang-gu',
#     '북구': 'Buk-gu',
#     '동구': 'Dong-gu'
# }

# place = {
#     'Busanjin-gu': 0,
#     'Haeundae-gu': 0,
#     'Nam-gu': 0,
#     'Dongnae-gu': 0,
#     'Seo-gu': 0,
#     'Jung-gu': 0,
#     'Yeongdo-gu': 0,
#     'Gijang-gun': 0,
#     'Saha-gu': 0,
#     'Geumjeong-gu': 0,
#     'Gangseo-gu': 0,
#     'Yeonje-gu': 0,
#     'Suyeong-gu': 0,
#     'Sasang-gu': 0,
#     'Buk-gu': 0,
#     'Dong-gu': 0
# }

# result = []

# for row in data:
#     idx = row[2]
#     district = district_mapping[idx]
#     place[district] += 1
#     result.append(place)
    
# soup = BeautifulSoup(svg)
# paths = soup.findAll('path')
# colors = ["#F1EEf6", "#D4B9BA", "#C994C7", "#DF65B0", "#D1C77", "#980043"]
# path_style = 'fill:'

# for p in paths:
#     if p['id']:
#         count = place[p['id']]
#         if count >= 20:
#             color_class = 5
#         elif count >= 15:
#             color_class = 4
#         elif count >= 10:
#             color_class = 3
#         elif count >= 8:
#             color_class = 2
#         elif count >= 5:
#             color_class = 1
#         else:
#             color_class = 0
#         color = colors[color_class]
#         p['style'] = path_style + color
# print(soup.prettify())

# import sys
# sys.stdout = open('bs.html', 'w')
# print(soup.prettify)


from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import csv
from bs4 import BeautifulSoup

app = FastAPI()

district_mapping = { #살려주세요
    '부산진구': 'Busanjin-gu',
    '해운대구': 'Haeundae-gu',
    '남구': 'Nam-gu',
    '동래구': 'Dongnae-gu',
    '서구': 'Seo-gu',
    '중구': 'Jung-gu',
    '영도구': 'Yeongdo-gu',
    '기장군': 'Gijang-gun',
    '사하구': 'Saha-gu',
    '금정구': 'Geumjeong-gu',
    '강서구': 'Gangseo-gu',
    '연제구': 'Yeonje-gu',
    '수영구': 'Suyeong-gu',
    '사상구': 'Sasang-gu',
    '북구': 'Buk-gu',
    '동구': 'Dong-gu'
}

place = {
    'Busanjin-gu': 0,
    'Haeundae-gu': 0,
    'Nam-gu': 0,
    'Dongnae-gu': 0,
    'Seo-gu': 0,
    'Jung-gu': 0,
    'Yeongdo-gu': 0,
    'Gijang-gun': 0,
    'Saha-gu': 0,
    'Geumjeong-gu': 0,
    'Gangseo-gu': 0,
    'Yeonje-gu': 0,
    'Suyeong-gu': 0,
    'Sasang-gu': 0,
    'Buk-gu': 0,
    'Dong-gu': 0
}

def load_csv_data(): #관광명소 지역별 카운트
    data = csv.reader(open('/Users/yanghyojun/Desktop/Python/Python_class/project/file/부산명소 국문 정보.csv', 'r'), delimiter=',')
    for row in data:
        idx = row[2]
        district = district_mapping[idx]
        place[district] += 1

def generate_svg(): #관광지가 많을수록 찐한색깔
    svg = open('/Users/yanghyojun/Desktop/Python/Python_class/project/file/Busan_districts.svg', 'r').read()
    soup = BeautifulSoup(svg, 'html.parser')
    paths = soup.findAll('path')

    colors = ["#F1EEf6", "#D4B9BA", "#C994C7", "#DF65B0", "#D1C77", "#980043"]
    path_style = 'fill:'

    for p in paths:
        if p['id']:
            count = place[p['id']]
            if count >= 20:
                color_class = 5
            elif count >= 15:
                color_class = 4
            elif count >= 10:
                color_class = 3
            elif count >= 8:
                color_class = 2
            elif count >= 5:
                color_class = 1
            else:
                color_class = 0
            color = colors[color_class]
            p['style'] = path_style + color

    return soup.prettify()

@app.get("/", response_class=HTMLResponse)
async def show_svg():
    load_csv_data()
    svg_html = generate_svg()

    html_content = f"""
    <html>
        <head>
            <title>부산 구별 명소 색상 표시</title>
        </head>
        <body>
            <h1>부산 구별 명소 색상 표시</h1>
            {svg_html}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
