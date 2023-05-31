from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "newtonde97@gmail.com"
MY_PASSWORD = "blwrejwokdapjclz"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,en-GB;q=0.8,en-AU;q=0.7,en-IN;q=0.6,fr-FR;q=0.5,fr;q=0.4,en-NZ;q=0.3"
}
url = "https://www.amazon.in/dp/B07BZ5VC4H/?coliid=I193NLT2E5KGIZ&colid=2KVYKXNREIZ9C&psc=1&ref_=lv_ov_lig_dp_it"
response = requests.get(url=url, headers=headers)

amazon_html = response.text
soup = BeautifulSoup(amazon_html, 'html.parser')

item_name = soup.select_one("#productTitle").getText().strip()

price = float(soup.select_one("span .a-price-whole").getText().strip().replace(",", ""))
print(price)

if price < 1400:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="newtonnarzary28@gmail.com",
            msg=f"Amazon price alert! {item_name} is now only {price} \n{url}"
        )