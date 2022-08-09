# Classe Horário

> Este programa foi realizado como exercício de programação para a disciplina de Princípios de Desenvolvimentos de Algoritmos (MAC0122) oferecida pela Universidade de São Paulo em 2021, ministrada pelos professores Jose Coelho de Pina Junior e Carlos Hitoshi Morimoto.

## Descrição do projeto

O objetivo deste exercício é continuar a prática de programação conhecida como Orientação a Objetos ao implementar a classe Horario.

A classe Horário construída possui um atributo de nome "dados". Esse atributo dados deve ser uma lista contendo três números inteiros maiores ou iguais zero. Assim, um horário é representado na lista dados da seguinte forma:

- dados[0]: um número inteiro entre 0 e 59 que indica segundos
- dados[1]: um número inteiro entre 0 e 59 que indica minutos
- dados[2]: um número inteiro entre 0 e 23 que indica horas

Os comportamentos correspondem aos métodos que a classe deve oferecer para que possamos manipular objetos do tipo Horario. Escolha nomes apropriados para cada comportamento e utilize os métodos especiais que desejar para implementar esses comportamentos.

Ao ser chamada pela função print(), um objeto Horario com dados = [7,5,2] deve imprimir a string ‘02:05:07’ que e podemos ler como 2 horas, 5 minutos e 7 segundos.

Para criar o horário ‘14:30:05’ devemos usar a chamada Horario(14,30,5). Observe que o atribtuto dados deve corresponder à lista [5,30,14].

Para criar o horário ‘11:45:00’ (onze e quarenta e cinco) devemos usar a chamada Horario(11,45).
Para criar o horário ‘12:00:00’ (doze horas) devemos usar a chamada Horario(12).