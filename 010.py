#  Crie um dicionário “notificacao” que representa uma mensagem de notificação com as seguintes chaves:
#
# Remetente
# Destinatário
# Mensagem
# Status (“NAO_LIDA”, “LIDA”)
#
# Implemente uma função marcar_como_lida(notificacao: dict) que altera o status para "LIDA".

notificacao = {
    "remetente": "sistema",
    "destinatario": "usuário",
    "mensagem": "nova mensagem",
    "status": "não lida"}

def marcar_como_lida(notificacao):
    notificacao["status"] = "lida"

marcar_como_lida(notificacao)
print(notificacao)