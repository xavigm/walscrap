import requests
from bs4 import BeautifulSoup

def scrape_products():
    url = "https://es.wallapop.com/user/xxxxx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    products = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        product_list = soup.find("ul", class_="public-profile-published-items_PublicProfileItems__list__qhrKb")
        
        if product_list:
            items = product_list.find_all("li", class_="public-profile-published-items_PublicProfileItems__card__E2D5a")
            for item in items:
                link_tag = item.find("a", href=True)
                link = f"https://es.wallapop.com{link_tag['href']}" if link_tag else "#"
                title = link_tag["title"] if link_tag and "title" in link_tag.attrs else "Sin título"
                img_tag = item.find("img", class_="item-card-images-slider_ItemCardImagesSlider__image__OqhLJ")
                image = img_tag["src"] if img_tag and "src" in img_tag.attrs else "https://via.placeholder.com/300x200"
                price_tag = item.find("strong", class_="item-card_ItemCard__price__D3QWU")
                price = price_tag.text.strip() if price_tag else "Sin precio"

                products.append({
                    "titulo": title,
                    "descripcion": title,
                    "precio": price,
                    "imagen": image,
                    "link": link
                })
    return products

