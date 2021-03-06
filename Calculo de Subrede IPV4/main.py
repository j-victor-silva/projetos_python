'''
Calculadora de subredes IPV4

Esse programa usa uma classe para que seja definido posteriormente por seu objeto
o endereço de IP da rede, retornando assim suas informações, como:
-IP;
-Máscara;
-IP da rede;
-Broadcast;
-CIDR (prefixo);
-Número de IP's disponíveis.
'''
class CalcIPV4:
    '''Esta é a classe para calcular a rede IPV4'''
    bits = [128, 64, 32, 16, 8, 4, 2, 1]
    masc = 24
    zeros = 0
    bits_vazios = []

    def __init__(self, ip, mascara=None, cidr=None) -> None:
        '''Nosso método construtor, onde está sendo definido
        os atributos que serão retornados na execução do programa'''
        self.ip = ip
        self.mascara = mascara
        self.cidr = cidr
        self.rede = None
        self.broadcast = None
        self.numero_ips = None

    def calc_mascara(self):
        '''Método que calcula a máscara de subrede caso
        não tenha sido atribuida no objeto'''
        if not self.mascara:
            self.mascara = '255.255.255.'
            self.zeros = self.cidr - self.masc
            num = 0
            for e, b in enumerate(self.bits):
                if e == self.zeros:
                    break
                num += b
            self.mascara += str(num)
            return
        
        return self.mascara

    def calc_cidr(self):
        '''Método que retorna o CIDR da rede caso não tenha sido
        atribuido, utilizando a máscara de subrede como base'''
        if not self.cidr:
            ultimo_digito = self.mascara.split('.')
            var = 0
            for i in self.bits:
                if i > int(ultimo_digito[-1]):
                    self.bits_vazios.append(0)
                    continue
                else:
                    if var == int(ultimo_digito[-1]):
                        while not len(self.bits_vazios) == 8:
                            self.bits_vazios.append(0)
                        break

                    if (var + i) > int(ultimo_digito[-1]):
                        self.bits_vazios.append(0)
                        continue
                    else:
                        var += i
                        self.bits_vazios.append(1)

            self.cidr = self.bits_vazios.count(1)
            self.zeros = self.bits_vazios.count(0)
            self.cidr += self.masc

        elif self.cidr:
            self.zeros = self.calculo_cidr(self.zeros, self.cidr)

    def calc_numero_ips(self):
        '''Método que calcula o número de hosts (IP's)'''
        self.numero_ips = (2 ** self.zeros)

    def calc_rede(self):
        '''Método que retorna o IP da rede'''
        self.rede = self.ip.split('.')
        self.rede[-1] = '0'
        self.rede = '.'.join(self.rede)
        self.broadcast = self.ip.split('.')
        self.broadcast[-1] = str(2 ** self.zeros)
        self.broadcast = '.'.join(self.broadcast)

    @staticmethod
    def calculo_cidr(zeros, valor: int):
        '''Método estático para calcular o número de IP's
        caso tenha sido atribuido o CIDR'''
        cidr = [x for x in range(32, 23, -1)]
        new_dict = dict({})
        for v1, v2 in enumerate(cidr):
            new_dict[v1] = v2
            if valor in new_dict.values():
                zeros += v1
                return zeros
            else:
                continue

    def executar_classe(self):
        '''Método para executar toda a classe'''
        self.calc_mascara()
        self.calc_cidr()
        self.calc_numero_ips()
        self.calc_rede()


if __name__ == '__main__':
    calc_ipv4 = CalcIPV4(ip='192.168.0.20', mascara='255.255.255.2')
    calc_ipv4.executar_classe()
    print(f'IP: {calc_ipv4.ip}')
    print(f'Máscara: {calc_ipv4.mascara}')
    print(f'Rede: {calc_ipv4.rede}')
    print(f'Broadcast: {calc_ipv4.broadcast}')
    print(f'Prefixo: {calc_ipv4.cidr}')
    print(f'Número de IPs da rede: {calc_ipv4.numero_ips}')
