package relacion;
public class Relacion {
    public static void main(String[] args) {

        Biblioteca biblioteca =
                new Biblioteca("Biblioteca Central UMSA");

        Autor autor1 = new Autor(
                "Gabriel García Márquez",
                "Colombiano"
        );

        Autor autor2 = new Autor(
                "Mario Vargas Llosa",
                "Peruano"
        );

        biblioteca.agregarAutor(autor1);
        biblioteca.agregarAutor(autor2);

        String[] paginas1 = {
                "Contenido página 1",
                "Contenido página 2",
                "Contenido página 3"
        };

        Libro libro1 = new Libro(
                "Cien años de soledad",
                "123456",
                paginas1
        );

        biblioteca.agregarLibro(libro1);

        Estudiante estudiante1 =
                new Estudiante("2024001", "Juan Pérez");

        biblioteca.prestarLibro(estudiante1, libro1);

        biblioteca.mostrarEstado();

        libro1.leer();

        biblioteca.cerrarBiblioteca();
    }
}