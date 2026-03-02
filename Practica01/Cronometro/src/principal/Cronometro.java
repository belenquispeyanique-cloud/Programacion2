package principal;

public class Cronometro {
	private long inicia;
	private long finaliza;
	
	public long getInicia() {
		return inicia;
	}
	
	public long getFinaliza() {
		return finaliza;
	}
	public Cronometro() {
		this.inicia= System.currentTimeMillis();
	}
	public void inicia() {
		this.inicia=System.currentTimeMillis();
	}
	public void detener() {
		this.finaliza = System.currentTimeMillis();
	}
	public long lapsoDeTiempo() {
		return (this.finaliza - this.inicia);
	}

}
