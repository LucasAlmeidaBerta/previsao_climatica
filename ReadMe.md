# 🌧️ Projeto de Engenharia de Dados: Previsão do Clima com Databricks

---

### 1. 📖 Descrição do Projeto

A tragédia causada pelas enchentes no Rio Grande do Sul em 2024 evidenciou a necessidade urgente de sistemas eficientes de alerta. Se a população tivesse sido avisada com antecedência sobre a alta quantidade de chuva prevista, muitos bens materiais poderiam ter sido protegidos e, principalmente, vidas poderiam ter sido salvas.

Trabalhos como o **AQUALERT** mostram o potencial da tecnologia e da engenharia de dados para transformar dados em ações preventivas, promovendo segurança e resiliência diante de desastres naturais.

Este projeto visa construir um pipeline robusto e escalável, que reúna e trate dados meteorológicos de diversas fontes para disponibilizá-los em formato acessível a analistas, cientistas de dados e modelos de IA, com foco em detecção de riscos como alagamentos.

#### 📡 Dados utilizados:

* Clima Tempo via WebScraping — [https://www.climatempo.com.br/](https://www.climatempo.com.br/)
* Weather via WebScraping — [https://weather.com/](https://weather.com/)
* OpenWeatherMap via API — [https://openweathermap.org/](https://openweathermap.org/)
* Weather API via API — [https://www.weatherapi.com/](https://www.weatherapi.com/)
* INPE via API — [https://www.cptec.inpe.br/](https://www.cptec.inpe.br/)

#### 🔍 Fontes de pesquisa:

* CNN Brasil
* Scielo Brasil
* BBC News Brasil
* ANA — Agência Nacional de Águas e Saneamento Básico
* OMM — Organização Meteorológica Mundial
* CEMADEN — Centro Nacional de Monitoramento e Alertas de Desastres Naturais
* INMET — Instituto Nacional de Meteorologia

---

### 2. 🧰 Tecnologias e Ferramentas Utilizadas

![Arquitetura do Projeto](./ARQUITETURA.PNG)

* Python
* Databricks (notebooks em PySpark)
* Azure Blob Storage
* Unity Catalog
* Delta Lake
* Great Expectations
* CWI Rocket
* Databricks Workflows
* PyTest
* `concurrent.futures` (para paralelismo)
* Azure Functions
---

### 3. 🏗️ Arquitetura do Projeto

* Ingestão de dados de múltiplas fontes (API/WebScraping)
* Armazenamento em Azure Blob Storage
* ETL em camadas (Bronze → Silver → Gold)
* Validação de dados com Great Expectations
* Governança e controle de acesso via Unity Catalog
* Notificações via Teams e e-mail
* Integração com IA (CWI Rocket) para geração de newsletters
* Cadastro de e-mails para recebimento de boletins climáticos
---

### 4. 🔄 Pipeline de Dados

1. **Ingestão**

   * Coleta via WebScraping e APIs com PySpark.
   * Cada fonte recebe tratamento e schema individual.
   * Persistência em Blob Storage nos formatos CSV e Parquet.

2. **Camada Bronze**

   * Dados carregados e salvos em tabelas com colunas padronizadas como `string`.

3. **Validação (Bronze)**

   * Uso de Great Expectations para verificar colunas críticas (`data_previsao`, `cidade`, `precipitacao`, etc.) contra valores nulos.

4. **Camada Silver**

   * Renomeação e conversão de tipos de dados.
   * Limpeza de valores ruidosos.
   * Persistência em Delta Lake.

5. **Validação (Silver)**

   * Aplicação de regras por fonte: valores esperados, faixas válidas e colunas obrigatórias.

6. **Camada Gold**

   * Consolidação dos dados em `clima_gold`.
   * Criação de tabelas:

     * `previsao_clima`: previsões para os próximos 15 dias.
     * `alerta_alagamentos`: alertas com base em volume crítico por cidade.
     * `clima_alagamento`: dados focados em precipitação e probabilidade.

7. **Consumo dos Dados**

   * Dashboards interativos no Databricks.
   * Notificações automáticas para usuários em áreas de risco.
   * Integração com CWI Rocket para geração de newsletters.

---

### 5. ✅ Validações com Great Expectations

* **Testes utilizados**:

  * `expect_column_values_to_not_be_null`
  * `expect_column_values_to_be_between`
  * `expect_column_values_to_match_regex`
  * `expect_column_values_to_be_in_set`

* **Armazenamento de resultados**:

  * Os relatórios são gerados em HTML no diretório `/uncommitted/data_docs/` e salvos em JSON em `/validations`.

* **Tratamento de falhas**:

  * Caso algum checkpoint falhe, o pipeline aborta antes da próxima camada e o erro é logado.
  * Logs e validações são utilizados para ajustes manuais ou notificações automatizadas via Databricks Workflows.

---

### 6. 📂 Estrutura de Diretórios

```bash
📦grupo-01
├── config/
├── great_expectations/
│   ├── gx/
│   ├── funcoes/
│   └── utils_gx/
├── workflow/
├── src/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── motores/
│   ├── cwi_rocket/
│   ├── testes/
│   └── utils/
└── README.md
```

---

### 7. 🚀 Como Executar o Projeto

1. **Pré-requisitos**:

   * Instalar as bibliotecas: `beautifulsoup4`, `requests`, `great-expectations`, `pytest`.

2. **Configuração**:

   * Defina suas chaves de acesso no arquivo `config/access_key.py`.
   * Adicione as chaves de APIs e do CWI Rocket em `config/enum_config.py`.

3. **Execução**:

   * Rodar o script `workflow/workflow.py` no Databricks para iniciar o pipeline completo.

---

### 8. 🧪 Testes

* Os testes foram implementados com `PyTest` no notebook:

  * `src/testes/testa_funcoes_utilizadas.py`
* Cobrem validações funcionais de coleta, transformação e consistência dos dados.

---

### 9. 📊 Resultados e Conclusões

* Os dados finais estão organizados e padronizados em Delta Tables.
* São utilizados em dashboards, notificações de risco e modelos de machine learning.
* A arquitetura foi desenhada para ser extensível: novas fontes podem ser integradas facilmente.
* Com dados confiáveis e atualizados, é possível antecipar eventos críticos e agir preventivamente.

---

### 10. 📎 Referências

#### 📌 Fontes de dados e pesquisa:

* [Clima Tempo](https://www.climatempo.com.br/)
* [Weather](https://weather.com/)
* [OpenWeatherMap](https://openweathermap.org/)
* [WeatherAPI](https://www.weatherapi.com/)
* [INPE](https://www.cptec.inpe.br/)
* [CEMADEN](https://www.cemaden.gov.br/)
* [INMET](https://portal.inmet.gov.br/)
* [ANA](https://www.gov.br/ana/pt-br)
* [CNN Brasil](https://www.cnnbrasil.com.br/)
* [BBC News Brasil](https://www.bbc.com/portuguese)
* [Scielo Brasil](https://scielo.org/)

#### 📘 Documentações técnicas:

* [Databricks](https://docs.databricks.com/)
* [PySpark](https://spark.apache.org/docs/latest/api/python/)
* [Azure Blob Storage](https://learn.microsoft.com/pt-br/azure/storage/blobs/)
* [Great Expectations](https://docs.greatexpectations.io/)
* [Delta Lake](https://docs.delta.io/latest/delta-intro.html)
* [CWI Rocket (IA)](https://www.cwi.com.br/)
* [Python concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
* [PyTest](https://docs.pytest.org/)
* [Azure Functions Python developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=get-started%2Casgi%2Capplication-level&pivots=python-mode-decorators)