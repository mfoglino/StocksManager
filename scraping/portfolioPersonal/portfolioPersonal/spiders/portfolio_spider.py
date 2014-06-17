from scrapy.http import FormRequest
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log
from portfolioPersonal.items import PortfoliopersonalItem
import re

class PortfolioSpider(BaseSpider):
    name = "portfolioPersonal"
    allowed_domains = ["portfoliopersonal.com"]
    start_urls = ["https://trading.portfoliopersonal.com/web/Login.aspx"]
    ppUser=''
    ppPassword=''  

    #def parse(self, response):
    #    filename = response.url.split("/")[-2]
    #    open(filename, 'wb').write(response.body

    def __init__(self, ppUser, ppPassword):
        self.ppUser = ppUser
        self.ppPassword = ppPassword

    def parse(self, response):    
        #scrapy.log.start()

        self.log("Entre por aca", level=log.INFO)
        return [FormRequest.from_response(response,
                    formdata={'ctl00$ContentPlaceHolder1$TxtUserName': self.ppUser,
                              'ctl00$ContentPlaceHolder1$TxtPassword': self.ppPassword,
                              'ctl00$ContentPlaceHolder1$HdnRes': '1280x800px',
                              '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$LnkLogin'},
                    dont_click = True,
                    callback=self.after_login)]

    def after_login(self, response):
        # check login succeed before going on
        
        if "authentication failed" in response.body:
            self.log("Login Failed", level=log.ERROR)
            return
        else:
            self.log('Login OK', level=log.INFO)
                              
            #accionesPage = 'https://trading.portfoliopersonal.com/web/Cotizaciones/panelesacciones.aspx'
            merval25 = 'https://trading.portfoliopersonal.com/web/Cotizaciones/tca.aspx?p=1&_c=55'
            return Request(merval25, callback=self.parse_Acciones)
                      
                      
    def parse_Acciones(self, response):
        self.log("Parsing Acciones...", level=log.INFO)
         
        #selector = Selector(response)
       
        stocks = response.body.split("-\\")
        
        #open('merval25.txt', 'wb').write(stocks__)
                        
        #01\:54145|Petrobras|APBR|13/12/2013 01:47:50 p.m.|58,60|1,03|58,00|58,50|58,70|59,00|58,20|960.887,00|92,00|48,95|58,50|58,70
        for s in stocks:
            if s != '':
                 
                columns = s.split('|')
                # parseo el codigo
                m = re.match( "\d+\\\:(\d+)"  , columns[0])
                codigo= m.group(1)

                yield PortfoliopersonalItem(
                Codigo = codigo,
                Especie=columns[2], 
                Fecha=columns[3], 
                Precio=columns[4], 
                Variacion=columns[5], 
                Cierre=columns[6]
                ) 
       
        

            
