# galeria/utils/gerar_dados.py
from galeria.factories import FotografiaFactory
from galeria.models import Fotografia


def criar_fotografias_massa(quantidade=100, limpar_existente=False):
    """
    Cria fotografias em massa para testes

    Parâmetros:
    quantidade: int - número de registros a criar (padrão: 100)
    limpar_existente: bool - se True, apaga todos os registros existentes primeiro
    """
    if limpar_existente:
        Fotografia.objects.all().delete()
        print("⚠️ Todos os registros existentes foram removidos da tabela Fotografia.")

    FotografiaFactory.create_batch(quantidade)
    return f"{quantidade} fotografias criadas com sucesso!"


if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
    django.setup()

    # Configuração para executar via linha de comando
    quantidade = 200  # Altere este valor
    limpar = False    # Mude para True se quiser limpar os dados existentes

    resultado = criar_fotografias_massa(quantidade, limpar)
    print(resultado)
