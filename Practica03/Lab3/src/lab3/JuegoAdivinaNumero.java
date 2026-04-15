package lab3;
import java.util.Scanner;
import java.util.Random;
public class JuegoAdivinaNumero extends Juego {
    public int numeroAAdivinar;
    public JuegoAdivinaNumero(int vidas) {
        super(vidas);
    }
    public void juega() {
        reiniciaPartida();
        Random generador = new Random();
        numeroAAdivinar = generador.nextInt(10) + 1;
        Scanner teclado = new Scanner(System.in);
        boolean elJuegoTermino = false;
        while (elJuegoTermino == false) {
            System.out.println("Adivina un número entre 0 y 10:");
            int intento = teclado.nextInt();
            while (!validarNumero(intento)) {
                System.out.println("Número no válido. Introduce un número entre 0 y 10:");
                intento = teclado.nextInt();
            }
            if (intento == numeroAAdivinar) {
                System.out.println("Acertaste!!");
                actualizaRecord();
                elJuegoTermino = true;
            } else {
                boolean leQuedanVidas = quitaVida();
                if (leQuedanVidas == true) {
                    if (numeroAAdivinar > intento) {
                        System.out.println("El número a adivinar es MAYOR. Inténtalo de nuevo.");
                    } else {
                        System.out.println("El número a adivinar es MENOR. Inténtalo de nuevo.");
                    }
                } else {
                    System.out.println("Te quedaste sin vidas. El número era: " + numeroAAdivinar);
                    elJuegoTermino = true;
                }
            }
        }
    }
    public boolean validarNumero(int x) {
        if (x >= 0 && x <= 10) {
            return true;
        }
        return false;
    }
}
