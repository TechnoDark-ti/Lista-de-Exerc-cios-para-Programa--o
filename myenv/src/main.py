def questao1():
	import Q1
	j = Q1.Jogador(
		nome = '',
		data_nascimento = '2000-01-01',
		altura = 0,
		peso = 0,
		nacionalidade = '',
		posicao = '')

	while True:
		import os, time

		os.system('clear') or None

		print('''
		================================================
		OPÇÕES: 
		================================================
		1 - inserir nome
		2 - inserir posicao(atacante, meio-campo,defesa)
		3 - inserir altura
		4 - inserir peso
		5 - inserir nacionalidade
		6 - inserir data_nascimento (ano, mês e dia)
		================================================
		FUNCÕES:
		================================================
		7 - mostrar informações
		8 - calcular a idade
		0 - sair
		================================================

		QUAL VOCÊ ESCOLHEU? _
				''')

		op = input('Escolha: ')
		os.system('clear') or None
		
		if op == '1':
			entrada = input('qual é nome? ')
			j.setNome(entrada)
		elif op == '2':
			entrada = input('Qual é a posição? ')
			j.setPosicao(entrada)
		elif op == '3':
			entrada = input ('Qual é altura? ')
			j.setAltura(entrada)
		elif op == '4':
			entrada = input('Qual é o peso? ')
			j.setPeso(entrada)
		elif op == '5':
			entrada = input('Qual é a nacionalidade?')
			j.setNacionalidade(entrada)
		elif op == '6':
			entrada = input('Qual é a data de nascimento?')
			j.setDatanascimento(entrada)
		elif op == '7':
			os.system('clear') or None

			j.getNome()
			j.getAltura()
			j.getNacionalidade()
			j.getPeso()
			j.getDatanascimento()
			j.getPosicao()
			j.toString()

			time.sleep(6)

		elif op == '8':
			os.system('clear') or None
			j.calcularIdade()
			time.sleep(3)
		
		elif op == '0':
			print('saindo...')
			time.sleep(3)
			os.system('clear') or None
			break
		else:
			print('Comando Inválido! Reiniciando...')	

def questao2():
	import ingresso

def questao3():
	import elevador


	elevador = elevador.Elevador(
		Ligado = False, 
		andarAtual = 0, 
		totalAndares = 0, 
		capacidadeElevador = 0, 
		capacidadeAtual = 0)
	

	from tqdm import tqdm
	import time, os

	for i in tqdm(range(4)):
		time.sleep(0.5)

	while True:
		print('''
		================================================
		OPÇÕES: 
		================================================
		1 - Ligar
		________________________________________________
		2 - Desligar
		________________________________________________
		3 - Inserir Pessoa
		________________________________________________
		4 - Retirar Pessoa
		________________________________________________
		5 - inserir nacionalidade
		________________________________________________
		6 - inserir data_nascimento (ano, mês e dia)
		________________________________________________
		================================================
		FUNCÕES:
		================================================
		[7] - Status
		[8] - Subir
		[9] - Descer

		[0] - sair
		================================================

		QUAL VOCÊ ESCOLHEU? _
				''')


		op = input('')

		if op == '1':
			pass
		elif op == '2':
			pass
		elif op == '3':
			pass
		elif op == '4':
			pass
		elif op == '5':
			pass
		elif op == '6':
			pass
		elif op == '7':
			elevador.toString()
		elif op == '0':
			for i in tqdm(range(5)):
				time.sleep(0.5)
				os.system('clear') or None
				main()
		else:
			print('Error 101!')


def main():
	while True:
		def opcao(op_principal):
			import os, time
			import Q1, Q2, Q3

			match op_principal:
				case '1':
					os.system('clear') or None
					Q1()
				case '2':
					print('Esta opcao está indisponível no momento...')
					time.sleep(2)
					os.system('clear') or None
					Q2()
				case '3':
					print('Esta opcao está indisponível no momento...')
					time.sleep(2)
					os.system('clear') or None
					Q3()
				case '0':
					os.system('clear') or None
					exit()
					
				case _:
					print('Comando Inválido! Tente Novamente!')	
					time.sleep(2)
					os.system('clear') or None

		print('''
			Escolha:
			[1]  - Questao1
			[2]  - Questao2
			[3]  - Questao3

			[0] - Sair...
			''')

		op_principal = input('Escolha: ')
		opcao(op_principal)

		
		
if __name__ == '__main__':
	main()