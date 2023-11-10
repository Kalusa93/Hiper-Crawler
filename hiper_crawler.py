from requests_html import HTMLSession

url = 'https://www.hiperlibertad.com.ar/tecnologia/tv-y-video'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

item = r.html.find('.vtex-search-result-3-x-galleryItem')

products = r.html.xpath('//*[@id="gallery-layout-container"]', first=True)

for item in products.absolute_links:
    r = s.get(item)
    name_selector = ('body > div.render-container.render-route-store-product > div > '
                     'div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > '
                     'div > div:nth-child(1) > div > section > div > div > div > '
                     'div:nth-child(2) > div > div > ' 
                     'div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > '
                     'div > div:nth-child(3) > h1 > span')
    name = r.html.find(name_selector, first=True).text
    
    if r.html.find('body > div.render-container.render-route-store-product > div > '
                   'div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > '
                   'div > div:nth-child(1) > div > section > div > div > div > div:nth-child(2) > '
                   'div > div > div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > '
                   'div > div:nth-child(7) > div > div > '
                   'div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > '
                   'div > div > button > div > div > span'):
        stock = 'In Stock'
    else:
        stock = 'Out of stock'
    
    try:
        price = r.html.find('span.vtex-product-price-1-x-currencyInteger'
                            'vtex-product-price-1-x-currencyInteger--pdp-selling-price', first=True).text
    except:
        price = 'None'
    
    try:
        descripcion = r.html.find('body > div.render-container.render-route-store-product > '
                                  'div > div.vtex-store__template.bg-base > div > div > div > '
                                  'div:nth-child(3) > div > div:nth-child(1) > div > section > '
                                  'div > div > div > div:nth-child(3) > div > '
                                  'div.vtex-tab-layout-0-x-contentContainer.vtex-tab-layout-0-x-contentContainer--pdp-product-info-content.w-100 > '
                                  'div > div.vtex-store-components-3-x-productDescriptionContainer > '
                                  'div > div > div.vtex-store-components-3-x-content.h-auto', first=True).text
    except:
        descripcion = 'None'
    
    print(item, name, stock, price)

    

