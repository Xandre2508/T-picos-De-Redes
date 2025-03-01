class Switch:
    def __init__(self):
        # Tabela MAC para armazenar o mapeamento de endereços MAC para portas
        self.mac_table = {}

    def learn_mac(self, mac_address, port):
        """
        Aprender um endereço MAC na tabela, associando-o a uma porta.
        """
        self.mac_table[mac_address] = port
        print(f"Endereço MAC {mac_address} aprendido na porta {port}")

    def forward(self, src_mac, dst_mac, packet):
        """
        Encaminha o pacote com base no endereço MAC de destino.
        Se o destino não for encontrado na tabela, o pacote é transmitido para todas as portas.
        """
        print(f"\nPacote recebido de {src_mac} para {dst_mac}")

        # Verifica se o endereço MAC de destino está na tabela
        if dst_mac in self.mac_table:
            # Encaminha o pacote para a porta associada ao endereço MAC de destino
            dst_port = self.mac_table[dst_mac]
            print(f"Encaminhando pacote de {src_mac} para {dst_mac} na porta {dst_port}")
        else:
            # Se o destino não for encontrado, realiza a transmissão para todas as portas
            print(f"Destino {dst_mac} desconhecido! Transmitindo para todas as portas.")
            for mac, port in self.mac_table.items():
                if mac != src_mac:
                    print(f"Encaminhando pacote para {mac} na porta {port}")

# Testando o Switch

# Criando o objeto switch
my_switch = Switch()

# Aprendendo endereços MAC nas portas
my_switch.learn_mac("00:1A:2B:3C:4D:5E", 1)
my_switch.learn_mac("00:1A:2B:3C:4D:5F", 2)
my_switch.learn_mac("00:1A:2B:3C:4D:60", 3)

# Simulando o envio de pacotes
my_switch.forward("00:1A:2B:3C:4D:5E", "00:1A:2B:3C:4D:5F", "Pacote de dados 1")
my_switch.forward("00:1A:2B:3C:4D:5E", "00:1A:2B:3C:4D:61", "Pacote de dados 2")  # MAC não existe
my_switch.forward("00:1A:2B:3C:4D:60", "00:1A:2B:3C:4D:5F", "Pacote de dados 3")
