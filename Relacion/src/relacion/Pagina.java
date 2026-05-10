package relacion;
public class Pagina {
    private int numeroPagina;
    private String contenidoPagina;

    public Pagina(int numeroPagina, String contenidoPagina) {
        this.numeroPagina = numeroPagina;
        this.contenidoPagina = contenidoPagina;
    }

    public void mostrarPagina() {
        System.out.println("Página " + numeroPagina + ": " + contenidoPagina);
    }
}
