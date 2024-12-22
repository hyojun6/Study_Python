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
