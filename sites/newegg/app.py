from core import crawler, scraper

urls = [
    "https://www.newegg.ca/msi-geforce-rtx-3070-rtx-3070-suprim-x-8g/p/N82E16814137620?Item=N82E16814137620"
    # "https://www.newegg.ca/gigabyte-geforce-rtx-3060-ti-gv-n306taorus-m-8gd/p/N82E16814932375?Item=N82E16814932375",
    # "https://www.newegg.ca/asus-geforce-rtx-3060-tuf-rtx3060-o12g-gaming/p/N82E16814126491?Item=N82E16814126491",
    # "https://www.newegg.ca/gigabyte-geforce-rtx-3070-gv-n3070eagle-oc-8gd/p/N82E16814932343?Item=N82E16814932343",
    # "https://www.newegg.ca/asus-geforce-rtx-3060-rog-strix-rtx3060-o12g-gaming/p/N82E16814126492?Item=N82E16814126492",
    # "https://www.newegg.ca/msi-geforce-rtx-3070-rtx-3070-gaming-x-trio/p/N82E16814137603?Item=N82E16814137603",
    # "https://www.newegg.ca/gigabyte-geforce-rtx-3060-gv-n3060aorus-e-12gd/p/N82E16814932400?Item=N82E16814932400",
    # "https://www.newegg.ca/msi-rx6700xtmech-2x12goc/p/N82E16814137640?Item=N82E16814137640",
    # "https://www.newegg.ca/asus-radeon-rx-6700-xt-tuf-rx6700xt-o12g-gaming/p/N82E16814126499?Item=N82E16814126499",
    # "https://www.newegg.ca/evga-geforce-rtx-3070-08g-p5-3755-kr/p/N82E16814487530?Item=N82E16814487530",
    # "https://www.newegg.ca/asus-radeon-rx-6700-xt-dual-rx6700xt-12g/p/N82E16814126500?Item=N82E16814126500",
    # "https://www.newegg.ca/sapphire-radeon-rx-6700-xt-11306-01-20g/p/N82E16814202399?Item=N82E16814202399",
    # "https://www.newegg.ca/sapphire-radeon-rx-6700-xt-11306-02-20g/p/N82E16814202400?Item=N82E16814202400",
    # "https://www.newegg.ca/asus-geforce-rtx-3070-tuf-rtx3070-o8g-gaming/p/N82E16814126461?Item=N82E16814126461",
    # "https://www.newegg.ca/powercolor-radeon-rx-6700-xt-axrx-6700xt-12gbd6-3dhl/p/N82E16814131782?Item=N82E16814131782",
    # "https://www.newegg.ca/asus-geforce-rtx-3070-dual-rtx3070-o8g/p/N82E16814126459?Item=N82E16814126459",
    # "https://www.newegg.ca/asrock-radeon-rx-5700-xt-rx-5700-xt-challenger-d-8g-oc/p/N82E16814930020?Item=N82E16814930020",
    # "https://www.newegg.ca/asus-geforce-rtx-3070-ko-rtx3070-o8g-gamin/p/N82E16814126466?Item=N82E16814126466",
    # "https://www.newegg.ca/asus-geforce-rtx-3070-rog-strix-rtx3070-o8g-gaming/p/N82E16814126458?Item=N82E16814126458",
    # "https://www.newegg.ca/evga-geforce-rtx-3070-08g-p5-3767-kr/p/N82E16814487532?Item=N82E16814487532",
    # "https://www.newegg.ca/msi-radeon-rx-6700-xt-rx-6700-xt-gaming-x-12g/p/N82E16814137642?Item=N82E16814137642"
]


def lambda_handler(event, context):
    for url in urls:
        html_content = crawler.crawl_html(url)
        html_content_tree = scraper.get_html_tree(html_content)
        print(scraper.get_title(html_content_tree), scraper.get_prices(html_content_tree),
              scraper.get_stock(html_content_tree))

    return {
        "statusCode": 200,
        "body": {"message": "newegg scraper worked"}
    }
