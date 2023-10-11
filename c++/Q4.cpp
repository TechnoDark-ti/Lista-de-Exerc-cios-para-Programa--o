#include <iostream>
#include <string>


using namespace std;

class Elevador{
    private: 
        int andarAtual;
        int andarLimite;
        int totalCapacidade;
        int totalAndar;
        bool ligado = false;
        
    public:
        Elevador(int andarAtual, int andarLimite, int totalCapacidade, int totalAndar, bool ligado) : 
            andarAtual(andarAtual), andarLimite(andarLimite), totalAndar(totalAndar), totalCapacidade(totalCapacidade), ligado(ligado){}
        int getandarAtual(){
            return andarAtual;
        }
        int getandarLimite(){
            return andarLimite;
        }
        int gettotalCapaciade(){
            return totalCapacidade;
        }
        int gettotalAndar(){
            return totalAndar;
        }
        bool getLigado(){
            return ligado;
        }
        void setLigado(bool newLigado){
            newLigado = ligado;
        }
        void setandarAtual(int newandarAtual){
            newandarAtual = andarAtual;
        }
        void settotalCapacidade(int newCapacidade){
            newCapacidade = totalCapacidade;
        }
        
        void inicializar(){
            if (ligado == false){
                cout << "Ligando...";
                int andarAtual = 0;
                int andarLimite = 4;
                int totalCapacidade = 20;
                int totalAndar = 0;
                ligado = true;
            }else{
                cout << "O elevador já está ligado!";
            }
        }
        void entrar(){
            if (ligado && totalCapacidade <= 20){
                settotalCapacidade(totalCapacidade++);
            }
            else if (ligado && totalCapacidade >= 20){
                cout << "Capacaide máxima atiginda";
            }else{
                cout << "O elevador está desligado ou com problemas técnicos";
            }
        }
        void subir(){
            if(ligado && totalAndar <= 4){
                setandarAtual(totalAndar++);
            }
            
        }
        void descer(){

        }
        void sair(){
            if (ligado && totalCapacidade <= 20){
                settotalCapacidade(totalCapacidade = -1);
            }
            else if(ligado && totalCapacidade == 0){
                cout << "O elevador está vazio!";
            }
            else{
                cout << "O elevador está desligado ou com problemas técnicos";
            }
        }

        void exibir(){
            
        }
};