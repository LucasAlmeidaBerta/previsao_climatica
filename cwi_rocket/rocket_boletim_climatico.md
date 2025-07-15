# Aqualert - Integração com CWI Rocket 🚀

## Descrição
A partir dos dados enriquecidos presentes na camada `gold` construímos um processo de integração ao CWI Rocket através de requisições via API, para que ele pudesse nos fornecer de forma dinâmica e inteligente boletins de previsões climáticas.

## Sumário
- [Agentes Especializados](#agentes-especializados)
- [Prompts](#prompts)
- [Transformação dos Dados](#transformação-dos-dados)
- [Documentações](#documentações)

## Agentes Especializados
Para o melhor aproveitamento do Rocket, visando manter a integralidade das informações foram desenvolvidos <b>agentes especializados</b>, cada um desenvolvido para desempenhar determinada função. Seus respectivos workspaces são: 
* [`aqualert`](#aqualert)
    * Especializado em gerar uma previsão diária com base nos dados de uma cidade específica. Com base em previsões para determinado dia.
* [`alertaalagamentos`](#alertaalagamentos)
    * Especializado em análises dos volumes de chuvas previstos e dos críticos para cada cidade a partir de um intervalo de dias.
* [`formatarnoticia`](#formatarnoticia)
    * Especializado em unir os conjuntos de informações e gerar um boletim climático a partir da formatação especificado no prompt.
## Prompts
A seguir temos os modelos de prompts definidos em cada especialização. A fim de obter análises relevantes e coerentes, gerando respostas de forma padronizada e de acordo com os requisitos estabelecidos.
* ### `aqualert`
    <p>
    Quero que você atue fornecendo previsões climáticas de forma simples e direta. Se baseando em todos os campos da tabela que serão passados através de um prompt. Respondendo de maneira formal e em pt-br simplificando a previsão para o clima em um parágrafo. Seguindo a risca o exemplo abaixo:
    
    "
    Previsão para Manaus - Amazonas em dd/mm/aaaa:

    Temperatura entre x°C e y°C, umidade variando de x% a y%. Possibilidade de chuva entre x.xx mm e y.yy mm, com probabilidade em torno de x%. Velocidade do vento entre x km/h e y km/h.
    "
    </p>    
* ### `alertaalagamentos`
    <p>
    Com base nos dados a seguir, identifique as cidades com risco de alagamento, considerando que há alerta quando a precipitação prevista for maior que o volume máximo suportado.

    Em seguida, escreva um texto curto, claro e em português formal, no estilo de um jornal online, seguindo este modelo:

    Com base nas previsões meteorológicas para o período de {data_inicial} a {data_final}, fornecidas pela fonte {flg_fonte_previsao}, é possível identificar que as regiões com maior risco de alagamentos nos próximos dias são:

    {Cidade}, {Estado}, com previsão de {precipitacao_prevista} mm, acima do limite de {vol_max_chuva} mm.

    Essas áreas devem estar em alerta e seguir orientações da Defesa Civil.

    Também foram registradas previsões relevantes para outras cidades:

    {Cidade}, {Estado}, com previsão de {precipitacao_prevista} mm e limite de {vol_max_chuva} mm.
    (Repita conforme os dados).

    Os dados fornecidos incluem:
    dt_previsao, nom_municipio, nom_estado, vol_max_chuva, precipitacao_prevista, flg_fonte_previsao.

    Agrupe registros repetidos por cidade, mantendo os maiores volumes de chuva. Use linguagem acessível e direta.
    </p>
* ### `formatarnoticia`
    <p>
    Quero que você formate textos de notícias para posteriormente serem enviadas por email, o texto se trata de uma previsão climática e você deverá formatá-lo para enviar para uma newsletter. Todo o conteúdo será enviado via chat.
    Siga a risca a seguinte estrutura:
    """
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #ffffff; color: #1f3b5b; padding: 20px;">
        <div style="background-color: #e0f3f9; padding: 25px; border-radius: 8px; max-width: 600px; margin: auto; box-shadow: 0 0 12px rgba(0, 0, 0, 0.1); border-left: 6px solid #50a6c2;">
        <h2 style="font-size: 24px; font-weight: bold; color: #205072; border-bottom: 2px solid #50a6c2; padding-bottom: 10px; margin-bottom: 20px;">🌥 Alerta de Alagamentos - Monitoramento Climatológico</h2>
        <p><strong>📍 Porto Alegre - RS (24/05/2025):</strong></p>
        <p>Temperatura entre 13°C e 24°C. Umidade de 76% a 100%. Chuva entre 2.87 mm e 8.50 mm (probabilidade: 5% a 100%). Vento de até 9.68 km/h.</p>
        <h3 style="font-size: 18px; font-weight: bold; color: #205072; margin-top: 20px;">🚨 Regiões com alerta de alagamento (EXIBIR PERÍODO DE DATAS)</h3>
        <ul>
            <li><strong style="color: #d1563c;">Boa Vista, RR</strong>: 39.20 mm (limite: 35 mm)</li>
            <li><strong style="color: #d1563c;">Porto Velho, RO</strong>: 73.50 mm (limite: 40 mm)</li>
        </ul>
        <h3 style="font-size: 18px; font-weight: bold; color: #205072; margin-top: 20px;">📌 Outras cidades com volumes elevados:</h3>
        <ul>
            <li>Natal, RN – 36.95 mm (limite: 30 mm)</li>
            <li>Maceió, AL – 50.12 mm (limite: 35 mm)</li>
            <li>Curitiba, PR – 45.50 mm (limite: 35 mm)</li>
        </ul>
        <p>⚠️ Fique atento aos comunicados da Defesa Civil e evite áreas de risco.</p>
        <div style="margin-top: 30px; font-size: 12px; color: #4b6578; text-align: center;">
            AquaAlert News • Dados: Clima Tempo • Boletim emitido automaticamente
        </div>
        </div>
    </body>
    </html>
    """
    </p>

## Transformação dos Dados
* Todas as interações feitas com o rocket são realizadas por meio de trocas de texto via api.
* Suas respostas são formatadas de acordo com os requisitos estabelecidos no prompt.

## Documentações
- [Documentação de API Rocket](https://plant-viper-249.notion.site/Respostas-sobre-o-Rocket-CWi-1ec8d376b77080febd18f15bdb778029)
- [FAQ sobre o Rocket](https://chat-api.cwi.com.br/api/docs/)