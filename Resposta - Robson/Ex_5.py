n = int(input("Informe um número: "))

if n == 0:
    print("O número zero não é par e nem ímpar")

elif n < 0:
    print("Número negativo")

elif n % 2 == 0:
    print("Número par")

else:
    print("Número ímpar")


# Exercício simples para demonstrar:
# - entrada de dados com input();
# - conversão de valores com int();
# - utilização de condicionais;
# - operador matemático de resto (%);
# - verificação de números positivos;
# - negativos;
# - pares;
# - ímpares;
# - e exibição de resultados com print().
#
# Observação:
# O operador % retorna o resto da divisão.
#
# Exemplo:
# 10 % 2 = 0
#
# Se o resto da divisão por 2 for igual a 0,
# o número é considerado par.
#
# Caso contrário,
# o número será ímpar.
#
# O número zero foi tratado separadamente
# apenas para fins didáticos neste exercício.