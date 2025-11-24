# 1. O programa deve começar solicitando ao usuário que insira seu nome.
nome = input('Digite seu nome: ')

# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input('Digite o valor do seu salário: '))

# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
multiplo_bonus = float(input('Digite o valor, em decimal, do bonus recebido. Ex.: Se o percentual for 5%, digite 0.05: '))

# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
CONSTANTE_BONUS = 1000
bonus = (CONSTANTE_BONUS + salario * multiplo_bonus)

# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f'Olá, {nome}, o seu valor bônus foi de {bonus:.2f}')

