package lab3;
public class JuegoAdivinaImpar extends JuegoAdivinaNumero{
    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
    }
    
    public boolean validarNumero(int x){
        if ( x % 2 != 0 && x>=0 && x<=10) {
            return true;
        } else {
            System.out.println("Error");
            return false;
        }
    }
}
