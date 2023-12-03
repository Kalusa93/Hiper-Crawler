from requests_html import HTMLSession
from configparser import ConfigParser
import concurrent.futures
import csv

config = ConfigParser()
config.read("branch_config.ini")

branch = input("Ingrese el nro de sucursal: ")

categorias = {
    'tecnologia': ['tv-y-video', 'audio', 'informatica', 'celulares-y-tablets', 'videojuegos', 'smartwatch'],
    'electrodomesticos': ['climatizacion', 'pequenos-electrodomesticos', 'lavado', 'cocinas-y-hornos', 'heladeras-y-freezers', 
        'hogar-y-limpieza', 'cuidado-personal-y-salud', 'termotanques-y-calefones'],
    'hogar': ['muebles-de-interior', 'cocina-y-comedor', 'bano', 'organizacion', 'iluminacion', 'dormitorio',
        'herramientas-y-mantenimiento', 'deco'],
    'bebidas': ['aperitivos', 'cervezas', 'gaseosas', 'jugos', 'aguas', 'vinos-y-espumantes', 'isotonicas-y-energizantes', 
        'bebidas-blancas-y-licores'],
    'almacen': ['aceites-y-vinagres', 'aceitunas-y-encurtidos', 'aderezos', 'arroz-y-legumbres', 'caldos-sopas-y-pure',
        'conservas', 'desayuno-y-merienda', 'golosinas-y-chocolates', 'harinas', 'sin-tacc', 'panificados',
        'para-preparar', 'pastas-secas-y-salsas', 'sal-pimienta-y-especias', 'snacks'],
    'lacteos': ['dulce-de-leche', 'leches', 'cremas', 'yogures', 'mantecas-y-margarinas', 'postres-y-flanes'],
    'quesos-y-fiambres': ['quesos', 'fiambres', 'salchichas'],
    'carnes': ['carne-vacuna', 'carne-de-cerdo', 'carne-de-pollo', 'embutidos', 'pescados', 'mariscos'],
    'frutas-y-verduras': ['frutas', 'verduras', 'huevos', 'legumbres-y-semillas', 'hierbas-aromaticas', 'lena-y-carbon'],
    'congelados': ['frutas-congeladas', 'verduras-congeladas', 'papas-congeladas', 'comidas-preparadas', 
        'prefritos-congelados', 'helados-y-postres', 'carnes-y-pollo', 'hamburguesas-y-milanesas'],
    'pastas-frescas-y-tapas': ['levaduras-y-grasas', 'fideos-y-noquis', 'pastas-rellenas', 'tapas'],
    'taeq': ['almacen-taeq', 'frutas-y-verduras-taeq', 'congelados-taeq'],
    'limpieza': ['accesorios-de-limpieza', 'calzado', 'cuidado-de-la-ropa', 'desodorantes-de-ambiente', 'insecticidas',
        'lavandina', 'limpieza-de-bano', 'limpieza-de-cocina', 'limpieza-de-pisos-y-muebles', 'papeles'],
    'perfumeria': ['cuidado-capilar', 'cuidado-oral', 'cuidado-personal', 'cuidado-de-la-piel', 
        'proteccion-femenina', 'proteccion-para-adultos', 'farmacia'],
    'bebes-y-ninos': ['higiene-y-salud', 'lactancia-y-alimentacion', 'seguridad-del-bebe', 'paseo-del-bebe', 
        'vehiculos-infantiles', 'muebles-infantiles', 'jugueteria', 'accesorios', 'panales-y-toallitas-humedas'],
    'vehiculos': ['accesorios-para-automoviles', 'accesorios-para-motos', 'neumaticos'],
    'mascotas': ['alimentos', 'accesorios-para-mascotas'],
    'aire-libre-y-jardin': ['camping', 'piletas', 'cuidado-del-jardin', 'muebles-de-exterior', 'asador', 
        'iluminacion-exterior'],
    'libreria': ['libreria-y-papeleria'],
    'deportes': ['fitness', 'bicicletas', 'accesorios-deportivos', 'patinaje']
}

categorias_claves = list(categorias.keys())

print(f"Las categorías existentes son {categorias_claves}")
categoria_ingresada = input("Ingrese una categoría: ")

if categoria_ingresada in categorias:
    print(f"La categoría '{categoria_ingresada}' contiene las siguientes subcategorías: {categorias[categoria_ingresada]}")
    subcategoria_ingresada = input("Ingrese una subcategoría: ")
    if subcategoria_ingresada in categorias[categoria_ingresada]:
        url = f'https://www.hiperlibertad.com.ar/{categoria_ingresada}/{subcategoria_ingresada}?sc={branch}&page='
        print(url)
    else:
        print(f"Error: La subcategoría '{subcategoria_ingresada}' no existe en la lista.")
else:
    print(f"Error: La categoría '{categoria_ingresada}' no existe en la lista.")

pages = int(input("Ingrese la cantidad de páginas de la subcategoría: "))

s = HTMLSession()
def get_all_links(url, start_page, end_page):
    all_links = []
    for x in range(start_page, end_page + 1):
        r = s.get(url + str(x))
        r.html.render(sleep=2, timeout=100)
        products = r.html.xpath('//*[@id="gallery-layout-container"]', first=True)
        links = products.absolute_links
        url_list = list(links)
        all_links = all_links + url_list
    
    return all_links

def get_product(link):
    r = s.get(link)
    r.html.render(sleep=2)
        
    try:
        list_price_thousands = r.html.find('body > div.render-container.render-route-store-product >'
            'div > div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > div > '
            'div:nth-child(2) > div > section > div > div > div > div > div > div > div.pr0.items-'
            'stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > div:nth-child(5) > div > '
            'div > div:nth-child(1) > span > span > span > span:nth-child(3)', first=True).text
        list_price_units = r.html.find('body > div.render-container.render-route-store-product > div >'
            'div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > div > '
            'div:nth-child(2) > div > section > div > div > div > div > div > div > div.pr0.items-'
            'stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > div:nth-child(5) > div > '
            'div > div:nth-child(1) > span > span > span > span:nth-child(5)', first=True).text
        list_price_decimals = r.html.find('body > div.render-container.render-route-store-product > '
            'div > div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > div > '
            'div:nth-child(2) > div > section > div > div > div > div > div > div > div.pr0.items-'
            'stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > div:nth-child(5) > div > '
            'div > div:nth-child(1) > span > span > span > span.vtex-product-price-1-x-currencyFraction.'
            'vtex-product-price-1-x-currencyFraction--pdp-list-price', first=True).text
    except:
        list_price_thousands = 'none'
        list_price_units = 'none'
        list_price_decimals = 'none'
        
    try:
        list_price_integer = int(f"{list_price_thousands}{list_price_units}")
        list_price = float(f"{list_price_integer}.{list_price_decimals}")
    except:
        list_price_integer = 'None'
        list_price = 'None'
    
    if r.html.find('div.vtex-button__label.flex.items-center.justify-center.h-100.ph6.w-100.border-box'):
        stock = 'In Stock'
    else:
        stock = 'Out of stock'
    
    try:
        title = r.html.find('body > div.render-container.render-route-store-product > '
            'div > div.vtex-store__template.bg-base > div > div > div > '
            'div:nth-child(3) > div > div:nth-child(2) > div > section > '
            'div > div > div > div > div > div > div.pr0.items-stretch.'
            'vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > '
            'div:nth-child(3) > h1 > span', first=True).text
    except:
        title = 'None'
        
    try:
        brand = r.html.find('body > div.render-container.render-route-store-product > div > '
            'div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > div > '
            'div:nth-child(2) > div > section > div > div > div > div > div > div > div.pr0.'
            'items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > '
            'div:nth-child(2) > div > div > div.pr6.items-stretch.vtex-flex-layout-0-x-'
            'stretchChildrenWidth.flex > div > span', first=True).text
    except:
        brand = 'None'
    
    try:
        price_thousands = r.html.find('body > div.render-container.render-route-store-product > '
            'div > div.vtex-store__template.bg-base > div > div > div > '
            'div:nth-child(3) > div > div:nth-child(2) > div > section > '
            'div > div > div > div > div > div > '
            'div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > '
            'div > div:nth-child(5) > div > div > div:nth-child(2) > span > '
            'span > span > span:nth-child(3)', first=True).text
        price_units = r.html.find('body > div.render-container.render-route-store-product > div > '
            'div.vtex-store__template.bg-base > div > div > div > '
            'div:nth-child(3) > div > div:nth-child(2) > div > section > '
            'div > div > div > div > div > div > '
            'div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > '
            'div > div:nth-child(5) > div > div > div:nth-child(2) > span > span > '
            'span > span:nth-child(5)', first=True).text
        price_decimal = r.html.find('body > div.render-container.render-route-store-product > div > '
            'div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > '
            'div > div:nth-child(2) > div > section > div > div > div > div > div > '
            'div > div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > '
            'div > div:nth-child(5) > div > div > div:nth-child(2) > span > span > span > '
            'span.vtex-product-price-1-x-currencyFraction.vtex-product-price-1-x-'
            'currencyFraction--pdp-selling-price', first=True).text
    except:
        price_thousands = 'None'
        price_units = 'None'
        price_decimal = 'None'
    
    try:
        price_integer = int(f"{price_thousands}{price_units}")
        price = float(f"{price_integer}.{price_decimal}")
    except:
        price_integer = 'None'
        price = 'None'
        
    try:
        descripcion = r.html.find('body > div.render-container.render-route-store-product > '
                                'div > div.vtex-store__template.bg-base > div > div > div > '
                                'div:nth-child(3) > div > div:nth-child(1) > div > section > '
                                'div > div > div > div:nth-child(3) > div > div.vtex-tab-'
                                'layout-0-x-contentContainer.vtex-tab-layout-0-x-contentContainer--'
                                'pdp-product-info-content.w-100 > div > div.vtex-store-components-3-'
                                'x-productDescriptionContainer > div > div > div.vtex-store-components-'
                                '3-x-content.h-auto', first=True).text
    except:
        descripcion = 'None'
    
    product = {
        'title': title,
        'brand': brand,
        'list_price': list_price,
        'price': price,
        'stock': stock,
        'url': link,
        'branch_id': branch,
        'category': categoria_ingresada,
        'subcategory': subcategoria_ingresada
    }
        
    print(product)
    return product

links = get_all_links(url, 1, pages)
results = []

for link in links:
    results.append(get_product(link))

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_product, links)

with open(f'{subcategoria_ingresada}.csv', 'w', encoding='utf-8', newline='') as file:
    wr = csv.DictWriter(file, fieldnames=results[0].keys(),)
    wr.writeheader()
    wr.writerows(results)
 
print('End.')
print(len(get_all_links(url, 1, pages)))