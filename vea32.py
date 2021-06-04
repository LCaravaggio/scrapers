import time
from urllib.request import urlretrieve
#from PIL import Image
import pytesseract
from selenium import webdriver
import re
import datetime


from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")

lista=[
"https://www.veadigital.com.ar/prod/412416/galletitas-terrabusi-lincoln-chocolate-153-gr",
"https://www.veadigital.com.ar/prod/440316/galletitas-terrabusi-lincoln-clasica-153-gr",
"https://www.veadigital.com.ar/prod/359098/galletitas-de-agua-criollitas-originales-100-gr",
"https://www.veadigital.com.ar/prod/359100/galletitas-de-agua-criollitas-originales-500-gr",
"https://www.veadigital.com.ar/prod/435093/galletitas-de-agua-media-tardes-cl%C3%A1sicas-110-gr",
"https://www.veadigital.com.ar/prod/198921/colita-de-cuadril-de-novillito-por-kg",
"https://www.veadigital.com.ar/prod/79020/cuadril-churrasco-de-novillito-por-kg",
"https://www.veadigital.com.ar/prod/470466/hamburguesas-good-mark-de-carne-354-gr",
"https://www.veadigital.com.ar/prod/467329/hamburguesas-paty-de-carne-320-gr",
"https://www.veadigital.com.ar/prod/8135/salchichas-paladini-tipo-viena-sin-piel-225-gr",
"https://www.veadigital.com.ar/prod/439711/salchichas-paty-de-viena-225-gr",
"https://www.veadigital.com.ar/prod/491909/salchichas-granja-iris-americana-x-5un-x-225gr",
"https://www.veadigital.com.ar/prod/120327/jam%C3%B3n-cocido-paladini-feteado-200-gr",
"https://www.veadigital.com.ar/prod/137082/jamon-cocido-campo-austral-tradicional-feteado-sobre-1-kg",
"https://www.veadigital.com.ar/prod/143105/salchichon-primavera-lario-feteado--kg",
"https://www.veadigital.com.ar/prod/504796/salame-fuet-lario-x-150g",
"https://www.veadigital.com.ar/prod/4002/aceite-de-girasol-natura-1,5-l",
"https://www.veadigital.com.ar/prod/159352/aceite-de-girasol-cocinero-900-ml",
"https://www.veadigital.com.ar/prod/203115/aceite-de-girasol-natura-900-ml",
"https://www.veadigital.com.ar/prod/253792/leche-entera-la-seren%C3%ADsima-con-vitamina-c-1-l",
"https://www.veadigital.com.ar/prod/85542/leche-entera-armon%C3%ADa-microfiltrada-1-l",
"https://www.veadigital.com.ar/prod/453073/leche-en-polvo-nido-prebio-800-gr",
"https://www.veadigital.com.ar/prod/446453/queso-pategras-la-serenisima-fraccionado-1-kg",
"https://www.veadigital.com.ar/prod/435128/queso-pategras-sancor-trad--ca-pintado-sob-kg-1",
"https://www.veadigital.com.ar/prod/449071/yogurt-entero-yogur%C3%ADsimo-firme-frutilla-190-gr",
"https://www.veadigital.com.ar/prod/436684/yogurt-entero-firme-yogs-multivitaminas-190-gr",
"https://www.veadigital.com.ar/prod/435108/dulce-de-leche-la-seren%C3%ADsima-cl%C3%A1sico-400-gr",
"https://www.veadigital.com.ar/prod/246514/dulce-de-leche-milkaut-400-gr",
"https://www.veadigital.com.ar/prod/430662/huevos-blancos-vea-12-un-bja-un-12",
"https://www.veadigital.com.ar/prod/430663/huevos-color-vea-bja-un-6",
"https://www.veadigital.com.ar/prod/430664/huevos-color-vea-bja-un-12",
"https://www.veadigital.com.ar/prod/81918/tomate-perita-entero-la-campagnola-240-gr",
"https://www.veadigital.com.ar/prod/413213/arvejas-arcor-300-gr",
"https://www.veadigital.com.ar/prod/445967/arvejas-secas-remojadas-molto-350-gr",
"https://www.veadigital.com.ar/prod/382133/sal-fina-dos-anclas-trilaminado-500-gr",
"https://www.veadigital.com.ar/prod/36225/sal-fina-celusal-500-gr",
"https://www.veadigital.com.ar/prod/416793/flan-royal-vainilla-60-gr",
"https://www.veadigital.com.ar/prod/462017/flan-exquisita-vainilla-60-gr",
"https://www.veadigital.com.ar/prod/494454/flan-godet-de-vainilla-30-gr",
"https://www.veadigital.com.ar/prod/198560/gaseosa-coca-cola-175-l",
"https://www.veadigital.com.ar/prod/50191/pepsi-15-l",
"https://www.veadigital.com.ar/prod/3655/agua-mineral-con-gas-eco-de-los-andes-15-l",
"https://www.veadigital.com.ar/prod/3782/agua-mineral-sin-gas-villavicencio-15-l",
"https://www.veadigital.com.ar/prod/3735/agua-mineral-sin-gas-glaciar--15-l",
"https://www.veadigital.com.ar/prod/416674/cerveza-quilmes-cl%C3%A1sica-rubia-1-l-botella-retornable",
"https://www.veadigital.com.ar/prod/427010/cerveza-schneider-1-l",
"https://www.veadigital.com.ar/prod/435639/vino-tinto-termidor-tradici%C3%B3n-1000-cc",
"https://www.veadigital.com.ar/prod/18038/vino-tinto-toro-1-l",
"https://www.veadigital.com.ar/prod/409867/caf%C3%A9-la-virginia-molido-equilibrado-cl%C3%A1sico-500-gr",
"https://www.veadigital.com.ar/prod/412/caf%C3%A9-la-planta-de-caf%C3%A9-molido-250-gr",
"https://www.veadigital.com.ar/prod/443928/jab%C3%B3n-en-polvo-granby-bolsa-800gr",
"https://www.veadigital.com.ar/prod/435731/detergente-en-polvo-zorro-baja-espuma-cl%C3%A1sico-800-gr",
"https://www.veadigital.com.ar/prod/159602/jab%C3%B3n-en-polvo-ala-lavado-a-mano-800g",
"https://www.veadigital.com.ar/prod/441854/detergente-lavavajillas-zorro-600-ml",
"https://www.veadigital.com.ar/prod/340432/jab%C3%B3n-en-pan-ala-multiacci%C3%B3n-200-gr",
"https://www.veadigital.com.ar/prod/3011/lavandina-ayud%C3%ADn-cl%C3%A1sica-1-l",
"https://www.veadigital.com.ar/prod/486909/lavandina-ayud%C3%ADn-maxima-pureza-1-l",
"https://www.veadigital.com.ar/prod/347606/shampoo-johnson-baby-cl%C3%A1sico-400-ml",
"https://www.veadigital.com.ar/prod/362080/shampoo-sedal-sos-ceramidas-340-ml",
"https://www.veadigital.com.ar/prod/450235/shampoo-tresemme-400-ml",
"https://www.veadigital.com.ar/prod/454771/jab%C3%B3n-en-barra-palmolive-naturals-oliva-y-aloe-125g-pack-3u",
"https://www.veadigital.com.ar/prod/484082/desodorante-femenino-antitranspirante-rexona-invisible-150-ml",
"https://www.veadigital.com.ar/prod/453893/desodorante-femenino-antitranspirante-nivea-pwder-150-ml",
"https://www.veadigital.com.ar/prod/445114/desodorante-femenino-antitranspirante-nivea-dry-150-ml",
"https://www.veadigital.com.ar/prod/441794/enjuague-para-ropa-suavizante-comfort-regular-clasico-900--ml",
"https://www.veadigital.com.ar/prod/280781/limpiador-antigrasa-procenex-repuesto-420-ml",
"https://www.veadigital.com.ar/prod/330317/gatillo-cif-limpiador-l%C3%ADquido-antigrasa-500-ml",
"https://www.veadigital.com.ar/prod/431618/repuesto-econ%C3%B3mico-limpiador-cif-antigrasa-450-ml",
"https://www.veadigital.com.ar/prod/242231/desodorante-de-ambiente-poett-primavera-360-ml",
"https://www.veadigital.com.ar/prod/270908/desodorante-de-ambiente-ayud%C3%ADn-original-332-ml",
"https://www.veadigital.com.ar/prod/319647/desodorante-de-ambiente-ayud%C3%ADn-frescura-natural-332-ml",
"https://www.veadigital.com.ar/prod/259966/insecticida-selton-mata-moscas-efecto-prolongado-color-azul-aerosol-360-cc",
"https://www.veadigital.com.ar/prod/519031/insecticida-raid-mmm-eficacia-segura-360-cc",
"https://www.veadigital.com.ar/prod/399711/rollo-de-cocina-campanita-classic-3-u",
"https://www.veadigital.com.ar/prod/410898/rollo-de-cocina-new-elegante-100-pa%C3%B1os",
"https://www.veadigital.com.ar/prod/417817/rollo-de-cocina-vea-3-u-x-60-pa%C3%B1os",
"https://www.veadigital.com.ar/prod/482148/cocina-volcan-blanco-a-gas",
"https://www.veadigital.com.ar/prod/521058/cocina-orbis-macrovision-858bc3m-blanca",
"https://www.veadigital.com.ar/prod/521136/heladera-c--freezer-ciclica-patrick-hpk136a00n",
"https://www.veadigital.com.ar/prod/522349/heladera-electrolux-dfn3000b-no-frost-269lts",
"https://www.veadigital.com.ar/prod/485200/termotanque-saiar-gas-s7-14l-gn-cja-un-1",
"https://www.veadigital.com.ar/prod/485196/termotanque-rheem-gas-r7-14l-gn-cja-un-1",
"https://www.veadigital.com.ar/prod/516366/aire-acondicionado-bgh-frio-calor",
"https://www.veadigital.com.ar/prod/522704/aire-acondicionado-alaska-als26wccr-2700w-fc",
"https://www.veadigital.com.ar/prod/506493/lavarropas-drean-7-kg-eea",
"https://www.veadigital.com.ar/prod/506496/lavarropas-aurora-7510-c-f-7k",
]

listacorta=[
"https://www.veadigital.com.ar/prod/412416/galletitas-terrabusi-lincoln-chocolate-153-gr"
]

file1 = open('VEA.txt', 'r') 
listaarchivo = file1.readlines()


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )+2
        end = s.index( last, start )-2
        return s[start:end]
    except ValueError:
        return ""

a=""


for l in listaarchivo: 
	try: 
		driver.get(l)
		time.sleep(2)
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		#print(soup)
		
		s = str(soup.find_all('input', {'id':'hfProductData'})[0])
		#print(s)
		#print(find_between(s, "DescripcionArticulo", "Grupo_Marca") + ": ")
		#print(find_between(s, "Precio", "unidadPedida"))
		l=l.replace("\n","") 
		print(l)
		a = a + l + ";"
		a = a + find_between(s, "DescripcionArticulo", "Grupo_Marca") + ";" 
		a = a + find_between(s, "Precio", "unidadPedida") + "\n" 
	except: 
		print("no se pudo acceder al url")
	


driver.close()


now = datetime.datetime.now()
nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
#print(nw)
with open('VEA ' + nw + '.csv', 'w', newline="\n", encoding='ISO-8859-1') as f:
	f.write(a)
f.close

