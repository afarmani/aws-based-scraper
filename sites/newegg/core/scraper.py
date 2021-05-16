from lxml import html


def get_html_tree(html_content):
    # print(html_content)
    return html.fromstring(html_content)


def get_title(tree):
    title_selector = "//h1[@class='product-title']"
    return get_text(tree, title_selector)


def get_text(tree, xpath_selector):
    elements = tree.xpath(xpath_selector)
    return list(map(lambda element: element.text_content(), elements))


def get_prices(tree):
    product_price_selector = "//div[contains(@class, 'product-price')]//li[contains(@class, 'price-current')]"
    return get_text(tree, product_price_selector)


def get_stock(tree):
    stock_selector = "//div[contains(@class, 'product-inventory')]"
    return get_text(tree, stock_selector)
