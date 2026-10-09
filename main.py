# Digite o import


# --- Configurações do Jogo ---



# Posição horizontal onde os bots vencem (próximo ao lado esquerdo)
VOLTAS_PARA_VENCER = 3


# --- Funções do Jogo ---

    # Desenha a pista (linhas laterais)
  

    # Desenha a linha de chegada
  

# --- Classe para o Bot ---
class Bot:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.posicao = LARGURA_PISTA - 2  # Começa do lado direito
        self.voltas = 0

    def mover(self):
        # Diminui a posição do bot em um valor aleatório (1 a 3)
        self.posicao -= random.randint(1, 3)


# -- função para desenhar o jogo --



def verificar_vencedor(bots):
    for bot in bots:
        if bot.posicao <= LINHA_CHEGADA:
            bot.posicao = (
                LARGURA_PISTA - 2
            )  # Reseta a posição para a próxima volta (lado direito)
            bot.voltas += 1
            print(f"\n--- Bot {bot.nome} completou uma volta! ---")
            if bot.voltas >= VOLTAS_PARA_VENCER:
                print(f"\n🏆 Bot {bot.nome} venceu a corrida! 🏆")
                return True
    return False


# --- Lógica Principal do Jogo ---
def iniciar_corrida():
    bots = [Bot("🚗", "vermelho"), Bot("🚙", "azul")]
    pista = criar_pista()
    vencedor = False

    while not vencedor:
        desenharjogo(pista, bots)

        for bot in bots:
            bot.mover()

        time.sleep(0.5)  # Espera 0.5 segundos antes de atualizar a tela

        vencedor = verificar_vencedor(bots)


if __name__ == "__main__":
    iniciar_corrida()
