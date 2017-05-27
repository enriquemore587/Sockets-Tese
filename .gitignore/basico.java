
package more.tese;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;

/**
 *
 * @author https://github.com/enriquemore587
 */
public class socket {

    public static void main(String[] args) {
        try {
            Socket soc = new Socket("localhost", 5552);
            DataOutputStream out = new DataOutputStream(soc.getOutputStream());

            out.writeUTF("Hello Server");

            out.flush();

            DataInputStream in = new DataInputStream(soc.getInputStream());
            String rec = in.readLine();
            System.out.println("Respuesta del servidor:  \n \n " + rec);

            out.close();
            in.close();

            soc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
