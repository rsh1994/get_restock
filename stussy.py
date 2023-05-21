import requests
from bs4 import BeautifulSoup
import schedule
import time
from config import headers, url

session = requests.Session()

def get_html(url):
    response = requests.get(url)
    html = response.text
    return html

def choose_size(size):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    size_labels = soup.find_all('label', {'class': 'product-swatch__label'})
    
    for label in size_labels:
        if label.text.strip() == size:
            size_id = label['for']
            buy_button = soup.find('button', {'data-variant': size_id, 'class': 'btn btn--secondary product__bin max-w-none uppercase flex-1'})
            if buy_button:
                add_to_cart_url = '여기에_카트_URL_입력'
                session.post(add_to_cart_url, data={'variant': size_id})  # 사이즈 선택 (카트에 추가)
                buy_now_url = '여기에_구매_URL_입력'
                session.post(buy_now_url, data={'variant': size_id})  # 구매 버튼 누르기
                print("사이즈 {} 선택 및 구매 완료".format(size))
            else:
                print("해당 사이즈의 상품이 품절되었습니다.")
            break
    
def check_availability():
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    buy_button = soup.find('button', {'class': 'btn btn--secondary product__bin max-w-none uppercase flex-1'})
    
    if buy_button:
        print("상품 구매 가능")
        choose_size('M')  # 사이즈 선택 (여기서는 예로 L을 선택)
    else:
        print("상품 품절")


if __name__ == '__main__':
    schedule.every(1).second.do(check_availability)
    while True:
        schedule.run_pending()
        time.sleep(1)