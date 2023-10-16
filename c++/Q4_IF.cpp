#include <iostream>
#include <string>

using namespace std;

void Q4_If(string nome, string endereco, int telefone){
	cout << "Qual o seu nome? ";
	cin >> nome;
	cout << "Qual é o seu endereço?";
	cin >> endereco;
	cout << "Telefone para contato: ";
	cin >> telefone;

	cout << "Nome: " << nome << "\nendereço: " << endereco << "\ntelefone: " << telefone;
}
