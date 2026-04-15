package lab3;
public class main {
    public static void main(String[] args) {
        JuegoAdivinaNumero j = new JuegoAdivinaNumero(3);
        j.juega();
        System.out.println("juego par");
        JuegoAdivinaPar j1 = new JuegoAdivinaPar(3);
        j1.juega();
        System.out.println("juego impar");
        JuegoAdivinaImpar j2 = new JuegoAdivinaImpar(3);
        j2.juega();
    }
}
