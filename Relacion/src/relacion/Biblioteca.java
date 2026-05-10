package relacion;

import java.util.ArrayList;

public class Biblioteca {
    private String nombreBiblioteca;

    // AGREGACIÓN
    private ArrayList<Libro> libros;
    private ArrayList<Autor> autores;

    // COMPOSICIÓN
    private Horario horario;

    private ArrayList<Prestamo> prestamos;

    public Biblioteca(String nombreBiblioteca) {
        this.nombreBiblioteca = nombreBiblioteca;

        libros = new ArrayList<>();
        autores = new ArrayList<>();
        prestamos = new ArrayList<>();

        // composición
        horario = new Horario(
                "Lunes a Viernes",
                "08:00",
                "20:00"
        );
    }

    public void agregarLibro(Libro libro) {
        libros.add(libro);
    }

    public void agregarAutor(Autor autor) {
        autores.add(autor);
    }

    public void prestarLibro(Estudiante estudiante, Libro libro) {
        if( libros.contains(libro)){
            Prestamo p = new Prestamo(estudiante, libro);
            prestamos.add(p);

            System.out.println("Préstamo realizado correctamente.");
            
        }
        else { System.out.println("El libro no existe");
    }}

    public void mostrarEstado() {
        System.out.println("\n===== BIBLIOTECA =====");
        System.out.println("Nombre: " + nombreBiblioteca);

        System.out.println("\n--- HORARIO ---");
        horario.mostrarHorario();

        System.out.println("\n--- LIBROS ---");
        for (Libro l : libros) {
            l.mostrarInfo();
            System.out.println();
        }

        System.out.println("\n--- AUTORES ---");
        for (Autor a : autores) {
            a.mostrarInfo();
            System.out.println();
        }

        System.out.println("\n--- PRÉSTAMOS ---");
        for (Prestamo p : prestamos) {
            p.mostrarInfo();
            System.out.println();
        }
    }

    public void cerrarBiblioteca() {
        System.out.println("La biblioteca está cerrando...");

        prestamos.clear();

        System.out.println("Todos los préstamos dejaron de existir.");
    }
}