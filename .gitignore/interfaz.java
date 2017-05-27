package more.tese;

/**
 *
 * @author  https://github.com/enriquemore587
 */
public interface ISockets {

//  funcion 1
//  publica puerto
    void escucho(int puerto);
    
//  funcion 2
//  conecta a un dispositivo
    boolean conectar(String ip, int puerto);

//  funcion 3
//  manda mensaje con el formato "dispositivoA,mensaje"  o     <dispositivo>dispositivoA</dispositivo><mensaje>hola o adios</mensaje>
    void outMsg(String msg);
    

//  funcion 4
//  recibe mensaje con el formato "dispositivoA,mensaje"  o     <dispositivo>dispositivoA</dispositivo><mensaje>hola o adios</mensaje>
    String inMsg();
    
    
    
    
/*
    funcion 5 NO SE SABE SI SEA NECESARIO
    crea XML  CON EL FORMATO
    <dispositivo>
        dispositivoA
    </dispositivo>
    <mensaje>
        hola o adios
    </mensaje>
*/
    boolean createXML(String cadena);//recibe el formato "dispositivoA,mensaje"
}
