from bs4 import BeautifulSoup
import requests
import time
import datetime 

listacorta={
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-acaramelada-vocacion-paq-150-grm/_/A-00126515-00126515-200", 
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-chocolat-lincoln-paq-153-grm/_/A-00182769-00182769-200"}

lista=[
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-acaramelada-vocacion-paq-150-grm/_/A-00126515-00126515-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galldulces-chocolat-lincoln-paq-153-grm/_/A-00182769-00182769-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-galletitas-dulces-lincoln-clasica-paq-153-grm/_/A-00256311-00256311-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gallcrackers-mini-sadwich-don-satur-bsa-250-grm/_/A-00473723-00473723-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cuadril--seleccion-x-kg/_/A-00042317-00042317-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesa-coto-cja-4-uni/_/A-00231388-00231388-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesa--swift-cja-4-uni/_/A-00290728-00290728-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-hamburguesa-clasica-paty-cja-320-grm/_/A-00288503-00288503-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha-paladini-paq-6-uni-225-grm/_/A-00014508-00014508-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha-escudo-de-oro-sin-piel-paq-6-uni-190-grm/_/A-00225560-00225560-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha-granja-iris-paq-6-uni-225-grm/_/A-00001034-00001034-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchicha--patyviena-x-6-225-grm/_/A-00255263-00255263-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jamon-cocido-feteado-primera-marc-xkg/_/A-00035168-00035168-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchichon-c-jamon-feteado-ebro-xkg/_/A-00034891-00034891-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchichon-primavera-feteado-ebro-xkg/_/A-00034890-00034890-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchichon-c-jam-feteado-la-octava-xkg-1-kgm/_/A-00047931-00047931-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salchichon-primav-fetead-la-octava-xkg-1-kgm/_/A-00047935-00047935-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-salame-crespon-feteado-ebro-x-kg/_/A-00045182-00045182-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-girasol--natura---botella-15-l/_/A-00014076-00014076-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-girasol--canuelas--botella-15-l/_/A-00099437-00099437-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-ultra-entera-extcal-vit-a--la-serenisi-sch-1-ltr/_/A-00251050-00251050-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-entera-ultrapas-coto-sch-1-ltr/_/A-00010226-00010226-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-en-polvo--nido---lata-800-gr/_/A-00297552-00297552-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-en-polvo-entera-coto--caja-800-gr/_/A-00128296-00128296-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-en-polvo-entera-sancor--caja-800-gr/_/A-00257385-00257385-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pategras-fraccionado-milkaut-xkg/_/A-00038207-00038207-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pategras-horma-la-serenisi--1-kgm/_/A-00044921-00044921-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-pategras-holandit-veronica-xkg/_/A-00084795-00084795-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sardo--xkg/_/A-00000149-00000149-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sardo-vit-a-d-fraccionado-la-serenisi--1-kgm/_/A-00047779-00047779-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sardo--veronica-xkg/_/A-00000145-00000145-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yogentfirmfort-frutilla-yogurisimo-pot-190-grm/_/A-00261282-00261282-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yogentfirm-multi-vainilla-sancor-yogs-pot-190-grm/_/A-00253130-00253130-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-clasico-sancor-pot-400-grm/_/A-00226340-00226340-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche--coto-pot-400-grm/_/A-00285028-00285028-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-fuente-d-calci-la-serenisi-pot-400-grm/_/A-00251874-00251874-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-leche-familiar-milkaut-pot-400-grm/_/A-00166221-00166221-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-blanco--coto-bli-12-uni/_/A-00234311-00234311-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-blanco-grand----cja-12-uni/_/A-00022865-00022865-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-huevo-color----cja-12-uni/_/A-00022878-00022878-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tomate-perita-arcor--lata-400-gr/_/A-00047153-00047153-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-tomate-perita-la-campagnola--lata-400-gr/_/A-00046126-00046126-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arveja--la-campagnola-remojadas-lata-300-gr/_/A-00070445-00070445-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arveja--arcor-secas-lata-300-gr/_/A-00085362-00085362-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sal-fina-nobleza-gaucha-----paquete-500-gr/_/A-00185448-00185448-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sal-fina-dos-anclas-----caja-500-gr/_/A-00014111-00014111-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-sal-fina-celusal-----caja-500-gr/_/A-00011701-00011701-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-flan-ciudad-del-lago-vainilla---caja-65-gr/_/A-00231080-00231080-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-flan-royal-vainilla---sobre-60-gr/_/A-00167111-00167111-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-flan-exquisita-vainilla---caja-60-gr/_/A-00281954-00281954-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-coca-cola-light---botella-15-l-/_/A-00008685-00008685-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-gaseosa-pepsi-light---botella-15-l-/_/A-00006302-00006302-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineral--eco-de-los-andes---botella-15-l/_/A-00010405-00010405-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineral--villavicencio----botella-15-l/_/A-00003478-00003478-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineral--glaciar---botella-15-l/_/A-00009924-00009924-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineral--nestle---botella-15-l/_/A-00082515-00082515-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--brahma---botella-1-l/_/A-00238215-00238215-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--quilmes---botella-1-l/_/A-00238214-00238214-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza-lager-schneider---botella-1-l/_/A-00245789-00245789-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--palermo--botella-1-l/_/A-00007306-00007306-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-zumuva---blanco-1-l/_/A-00200296-00200296-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-termidor-tradicion---tinto-1-l/_/A-00253715-00253715-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-toro---tinto-dulce-1-l/_/A-00105735-00105735-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-la-virginia---paquete-500-gr/_/A-00234301-00234301-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-los-5-hispanos---paquete-500-gr/_/A-00013274-00013274-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cafe-molido-cabrales---paquete-500-gr/_/A-00005915-00005915-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-en-polvo-ala--lavado-a-mano--paquete-800-gr/_/A-00256322-00256322-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-en-polvo-granby-----paquete-800-gr/_/A-00259716-00259716-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-en-polvo-zorro---paquete-800-gr/_/A-00266490-00266490-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-detergente-zorro--pepino--botella-750-ml/_/A-00461853-00461853-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-detergente-ala--limon---botella-750-ml/_/A-00254247-00254247-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-en-pan-ala--multiaccion-paquete-200-gr/_/A-00196972-00196972-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavandina-liquida-ayudin----maxima-pureza-botella-1-l/_/A-00260195-00260195-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavandina-liquida-aditivada-heroe-----botella-1-l/_/A-00295513-00295513-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-sedal---ceramidas-botella-650-ml/_/A-00295133-00295133-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-tresemme---hidratacion-profunda-botella-400-ml/_/A-00299213-00299213-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-johnson-s-baby-proteccion-uv-bot-400-ml/_/A-00245738-00245738-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-shampoo-sedal---ceramidas-botella-340-ml/_/A-00295200-00295200-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-oliva-y-aloe-v-palmolive-bol-375-grm/_/A-00296834-00296834-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-jabon-tocador-lux-delicadeza-floral-paq-125-grm/_/A-00266974-00266974-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desodorante-antitraspirante-nivea-dry-confort--aerosol-150-cc/_/A-00258583-00258583-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desodorante-antitraspirante-rexona--invisible--aerosol-/_/A-00299042-00299042-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-enjuague-para-ropa-vivere-clasico-doypack-900-ml/_/A-00258398-00258398-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-enjuague-para-ropa-comfort-clasico-doypack-900-ml/_/A-00256737-00256737-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-enjuague-para-ropa-suave-libre-enjuague-doypack-900-ml/_/A-00267252-00267252-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-cif-antigrasa-doy-900-ml/_/A-00263405-00263405-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-ayudin-antigrasa-doy-900-cc/_/A-00220762-00220762-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-limpiador-mr-musculo-total-cocina-doy-900-cc/_/A-00268222-00268222-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desodorante-de-ambiente-poett-lavanda---aerosol-360-cc/_/A-00288632-00288632-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-desodorante-de-ambiente-glade-campo-de-lavanda-aerosol-360-cc/_/A-00268784-00268784-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-insecticida-raid-mata-mos-y-mosquit-form-mejorada-aer-360c/_/A-00266604-00266604-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-insecticida-mata-mosquito-fuyi-efectividad-comproba-aer-360-g/_/A-00265969-00265969-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-rollo-de-cocina-sussex-180-panos-paquete-3-unidades/_/A-00261279-00261279-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-rollo-de-cocina-campanita-180-panos-paquete-3-unidades/_/A-00224749-00224749-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-rollo-de-cocina-elite-180-panos-paquete-3-unidades/_/A-00473206-00473206-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cocina-aurora-4h-inox-enc-lz-autolm-xle/_/A-00251462-00251462-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cocina-whirlpool-4-hornallas-blanco-wfb56db/_/A-00250060-00250060-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cocina-electrolux-4-hornallas-gris-exmr856/_/A-00285019-00285019-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-heladera-con-freezer--314-l-phct320x--inoxidable/_/A-00487416-00487416-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-heladera-con-freezer-top-house-314-l-d60350--inoxidable/_/A-00267612-00267612-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-termotanque-a-gas-rheem-120-l-tgnp120rh-natural/_/A-00457971-00457971-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-termotanque-a-gas-saiar-120-l-tpg120-multigas/_/A-00192961-00192961-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aire-acondicionado-split-top-house-3000-fg-3450-watts-frio-calor--/_/A-00485655-00485655-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aire-acondicionado-split-bgh-silent-air-3000-fg-3450-watts-frio-calor-bsh35wcp/_/A-00469610-00469610-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavarropas-automatico-top-house-carga-frontal-7-kg-xqg70-q712e-blanco/_/A-00472160-00472160-200",
"https://www.cotodigital3.com.ar/sitios/cdigi/producto/-lavarropas-automatico-samsung-carga-frontal-7-kg-ww70j4463gw-blanco/_/A-00484039-00484039-200"
]


file1 = open('Coto.txt', 'r') 
listaarchivo = file1.readlines()


a=""

for l in listaarchivo: 
	try:
		r = requests.get(l.replace("\n",""))
		soup = BeautifulSoup(r.content, 'html.parser')
		print(l.replace("\n",""))
		a = a + l.replace("\n","") + ";"
		a = a + soup.find_all('h1', {'class':'product_page'})[0].text.replace(" ","").replace("\n","").replace("\r","") + ";" 
		a = a + soup.find_all('span', {'class':'atg_store_newPrice'})[1].text.replace("$","").replace(" ","").replace("\n","").replace("\r","").replace("PRECIOCONTADO","") + "\n" 
	except:
		print("error")
		a = a +  "\n" 

now = datetime.datetime.now()
nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
#print(nw)
with open('Coto ' + nw + '.csv', 'w', newline="\n", encoding='ISO-8859-1') as f:
	f.write(a)
f.close

