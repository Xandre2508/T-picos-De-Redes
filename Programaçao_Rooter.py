class Router:
    def __init__(self, name):
        # Inicializando as interfaces do roteador
        self.name = name
        self.interfaces = {}
        self.routing_table = {}

    def add_interface(self, interface_name, ip_address, subnet_mask):
        """
        Adiciona uma interface ao roteador com um IP e máscara de sub-rede.
        """
        self.interfaces[interface_name] = {
            "ip_address": ip_address,
            "subnet_mask": subnet_mask
        }
        print(f"Interface {interface_name} adicionada com IP {ip_address}/{subnet_mask}")

    def add_route(self, destination, gateway):
        """
        Adiciona uma rota estática à tabela de roteamento.
        """
        self.routing_table[destination] = gateway
        print(f"Rota adicionada para {destination} via gateway {gateway}")

    def forward_packet(self, src_ip, dst_ip, packet):
        """
        Encaminha pacotes de acordo com a tabela de roteamento.
        """
        print(f"\nRoteador {self.name} recebendo pacote de {src_ip} para {dst_ip}")

        # Verifica se a rede de destino está na tabela de roteamento
        for network, gateway in self.routing_table.items():
            if dst_ip.startswith(network):  # Verifica se o IP de destino está na rede
                print(f"Encaminhando pacote para {dst_ip} via gateway {gateway}")
                return

        print("Destino desconhecido! Pacote não pode ser encaminhado.")

# Criando o roteador
router = Router("Roteador1")

# Adicionando interfaces com IPs e máscaras de sub-rede
router.add_interface("eth0", "192.168.1.1", "255.255.255.0")  # Conectado à rede interna
router.add_interface("eth1", "10.0.0.1", "255.255.255.0")  # Conectado ao Switch

# Adicionando rotas estáticas para redes conectadas
router.add_route("192.168.1.0", "192.168.1.1")  # Rede interna
router.add_route("10.0.0.0", "10.0.0.1")  # Rede do Switch

# Simulando o envio de pacotes para redes conectadas ao switch
router.forward_packet("192.168.1.100", "10.0.0.10", "Pacote de dados 1")
router.forward_packet("192.168.1.100", "192.168.1.200", "Pacote de dados 2")  # Rede interna
router.forward_packet("192.168.1.100", "172.16.0.10", "Pacote de dados 3")  # Destino desconhecido
