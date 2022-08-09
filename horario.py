# -*- coding: utf-8 -*-
#-----------------------------------------------------------------

def main():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')
    

class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
    def __init__(self, h=0, m=0, s=0):
        '''(Horario, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros h, m e s que representam
        a hora, os minutos e os segundos.

        Exemplos:

        >>> hora = Horario(14,30,5) # construtor chama __init__()
        >>> hora.dados
        [5,30,14]
        >>> hora.dados[0]
        5
        '''
        while s >= 60:
            s = abs(s - 60)
            m += 1
        while m >= 60:
            m = abs(m - 60)
            h += 1
        while h >= 24:
            h = abs(h - 24)
        self.dados = [s,m,h]
    
    #-------------------------------------------------------------------
    def __str__(self):
        '''(Horario) -> str

        Recebe uma referencia `self` a um objeto da classe Horario e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:

        >>> hora = Horario(2,5,7)
        >>> print(hora)
        02:05:07
        '''
        d = self.dados[:]
        i = 0
        while i < 3:
            if d[i] < 10:
                d[i] = f"0{d[i]}"
            i += 1
        return f"{d[2]}:{d[1]}:{d[0]}"
    #-------------------------------------------------------------------
    def __add__(self, other):
        """ (Horario, Horario) -> Horario

        Retorna a soma do Horario `self` e do Horario `other`.
        Usado pelo Python quando escrevemos Horario + Horario.

        """    
        hsoma = self.dados[2] + other.dados[2]
        msoma = self.dados[1] + other.dados[1]
        ssoma = self.dados[0] + other.dados[0]
        return Horario(hsoma,msoma,ssoma)
    #-------------------------------------------------------------------
    def __sub__(self, other):
        """ (Horario, Horario) -> Horario

        Retorna a subtração do Horario `self` e do Horario `other`.
        Usado pelo Python quando escrevemos Horario - Horario.
        """
        h1 = self.dados[:]
        h2 = other.dados[:]
        s_self = h1[0] + 60 * h1[1] + 3600 * h1[2]
        s_other = h2[0] + 60 * h2[1] + 3600 * h2[2]
        if s_other > s_self:
            return Horario()
        sub = s_self - s_other       
        return Horario(0,0,sub)        
        
    #-------------------------------------------------------------------
    def __eq__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario == Horario
        """
        return self.dados == other.dados
    #-------------------------------------------------------------------
    def __gt__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario > Horario
        """
        if self.dados[2] > other.dados[2]:
            return True
        if self.dados[2] < other.dados[2]:
            return False
        #então h são iguais
        if self.dados[1] > other.dados[1]:
            return True
        if self.dados[1] < other.dados[1]:
            return False
        #então h e m são iguais
        if self.dados[0] > other.dados[0]:
            return True
        else:
            return False
    #-------------------------------------------------------------------
    def __lt__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario < Horario
        """
        if self.dados[2] < other.dados[2]:
            return True
        if self.dados[2] > other.dados[2]:
            return False
        #então h são iguais
        if self.dados[1] < other.dados[1]:
            return True
        if self.dados[1] > other.dados[1]:
            return False
        #então h e m são iguais
        if self.dados[0] < other.dados[0]:
            return True
        else:
            return False
    #-------------------------------------------------------------------
    def __le__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario <= Horario
        """
        if self.dados == other.dados:
            return True 
        if self.dados[2] < other.dados[2]:
            return True
        if self.dados[2] > other.dados[2]:
            return False
        #então h são iguais
        if self.dados[1] < other.dados[1]:
            return True
        if self.dados[1] > other.dados[1]:
            return False
        #então h e m são iguais
        if self.dados[0] < other.dados[0]:
            return True
        else:
            return False
    #-------------------------------------------------------------------
    def __ge__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario >= Horario
        """
        if self.dados == other.dados:
            return True 
        if self.dados[2] > other.dados[2]:
            return True
        if self.dados[2] < other.dados[2]:
            return False
        #então h são iguais
        if self.dados[1] > other.dados[1]:
            return True
        if self.dados[1] < other.dados[1]:
            return False
        #então h e m são iguais
        if self.dados[0] > other.dados[0]:
            return True
        else:
            return False
#-------------------------------------------------------------------    
if __name__ == '__main__':
    main()
    