#include <iostream>
#include <string>

using namespace std;

class Pessoa{
    private:
    string nome;
    string nacionalidade;
    string posicao;
    int dataNascimento;
    float peso;
    float altura; 
    
    
    public:
        Pessoa(string posicao, string nome, int dataNascimento, float peso, float alturam, string nacionalidade) : 
        nome(nome), dataNascimento(dataNascimento), peso(peso), altura(altura), nacionalidade(nacionalidade), posicao(posicao){}

        virtual void exibirInformacoes(){
            cout << "Nome: " << nome << "Data de Nascimento: " << dataNascimento << "peso: " << peso << "altura: " << altura << endl;
        }
        string getPosicao(){
            return posicao;
        }
        string getNacionalidade(){
            return nacionalidade;
        }
        string getNome(){
            return nome;
        }
        int getdataNascimento(){
            return dataNascimento;
        }
        float getPeso(){
            return peso;
        }
        float getAltura(){
            return altura;
        }

        void setNome(string newNome){
            nome = newNome;
        }
        void setdataNasciment(int newData){
            dataNascimento = newData;
        }
        void setPeso(float newPeso){
            peso = newPeso;
        }
        void setAltura(float newAltura){
            altura = newAltura;
        }     
        void setNacionalidade(string newNacao){
            nacionalidade = newNacao;
        }
        void setPosica(string newPosicao){
            posicao = newPosicao;
        }
};

class Jogador : public Pessoa{
    private:
        

    public:
     
        void calcularIdade(){

        } 
};