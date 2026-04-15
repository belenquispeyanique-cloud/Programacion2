package lab3;
public class Juego {
    public int numeroDeVidas;
    public int record = 0;
    private int vidasIniciales;

    public Juego(int vidas) {
        this.numeroDeVidas = vidas;
        this.vidasIniciales = vidas;
    }

    public void reiniciaPartida() {
        this.numeroDeVidas = vidasIniciales;
    }

    public void actualizaRecord() {
        this.record++;
    }

    public boolean quitaVida() {
        this.numeroDeVidas--;
        if (this.numeroDeVidas > 0) {
            return true;
        } else {
            return false;
        }
    }
}
