# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PortfoliopersonalItem(Item):
    # define the fields for your item here like:
    # name = Field()
    Codigo = Field()
    Especie = Field()
    Fecha  = Field()
    Precio = Field()
    Cierre  = Field()
    Variacion = Field()
    Compra  = Field()
    Venta  = Field()    
    
