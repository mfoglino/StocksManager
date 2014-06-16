package hello;

public class StockInfo {
	
	private String Id;
	
	private String Name;
	
	private Float Compra;
	
	private Float Venta;

	public String getId() {
		return Id;
	}

	public void setId(String id) {
		Id = id;
	}

	public String getName() {
		return Name;
	}

	public void setName(String name) {
		Name = name;
	}

	public Float getCompra() {
		return Compra;
	}

	public void setCompra(Float compra) {
		Compra = compra;
	}

	public Float getVenta() {
		return Venta;
	}

	public void setVenta(Float venta) {
		Venta = venta;
	}

	//{"Especie": "YPFD", "Variacion": "-1,00", "Cierre": "346,50", "Fecha": "13/06/2014 05:00:20 p.m.", "Precio": "346,50", "Codigo": "10145"}

}
