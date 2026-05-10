package relacion;

import java.util.ArrayList;

public class Libro {
    private String titulo;
    private String isbn;

    // COMPOSICIÓN
    private ArrayList<Pagina> paginas;

    public Libro(String titulo, String isbn, String[] contenidos) {
        this.titulo = titulo;
        this.isbn = isbn;

        paginas = new ArrayList<>();

        for (int i = 0; i < contenidos.length; i++) {
            paginas.add(new Pagina(i + 1, contenidos[i]));
        }
    }

    public String getTitulo() {
        return titulo;
    }

    public void leer() {
        System.out.println("Leyendo libro: " + titulo);

        for (Pagina p : paginas) {
            p.mostrarPagina();
        }
    }

    public void mostrarInfo() {
        System.out.println("Título: " + titulo);
        System.out.println("ISBN: " + isbn);
    }
}