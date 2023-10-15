/*
    Author: @DarkCells - Márcio Moda  
*/

#include <iostream>
#include "Q1.cpp"
#include "Q1_IF.cpp" 
#include "Q2_IF.cpp"


using namespace std;

void mostrar1(){
    cout << "\n1 - Lista IF\n";
    cout << "\n1 - Lista IF\n";
    cout << "\n1 - Lista IF\n";
    cout << "\n1 - Lista IF\n";

}

void mostrar_questaoIF(){

}



int main(){
    setlocale(LC_ALL, "Portuguese");
    
    int op;

    while (op !=0){
        mostrar1();

        switch (op){
        case 1:
            mostrar_questaoIF();
            break;
        
        default:
            break;
        }
    }
}