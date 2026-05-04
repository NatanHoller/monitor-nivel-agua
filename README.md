# :droplet: Monitor de Nível de Água

Sistema de monitoramento de nível de água em Python com alertas coloridos no terminal por bibliotecas colorama.

Interface simples com exibição de alertas coloridos e organizados.

:pushpin:Funcionalidades

- Monitoramento de 5 níveis de água
- Exibição de mensagens coloridas no terminal
- Simulação de um ambiente real de reservatório

:art:Níveis do sistema

| Nível | Situação | Cor |
|------|--------|-----|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

:gear:Tecnologias utilizadas

- Python
- Colorama

:arrow_forward:Como executar?

```bash
pip install -r requirements.txt
python main.py
