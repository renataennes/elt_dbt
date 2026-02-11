# 🚀 ELT Pipeline com Snowflake + dbt + Python

## 📌 Visão Geral do Projeto

Este projeto implementa um pipeline **ELT (Extract–Load–Transform)** completo para ingestão, armazenamento e transformação de dados de vagas de trabalho remoto.

Fluxo geral do pipeline (conforme arquitetura do projeto):

1. **Extração (E)** – Dados são coletados da API pública da **Jobicy** via scripts em Python.
2. **Load (L)** – Os dados brutos são carregados no **Snowflake** como tabela de origem (raw).
3. **Transformação (T)** – Modelagens analíticas são realizadas no **dbt Core**, gerando tabelas tratadas (camada silver) prontas para análise.

---

## 🏗️ Arquitetura

![Arquitetura ELT](docs/architecture.png)

🔹 **Componentes principais:**

* **Jobicy API** – Fonte de dados de vagas remotas
* **Python** – Responsável por extrair e carregar os dados no Snowflake
* **Snowflake** – Data warehouse onde os dados são armazenados
* **dbt Core** – Ferramenta de transformação e modelagem dos dados

---

## 📂 Estrutura do Repositório

```
elt_dbt/
├── extraction/           # Scripts de extração e carga (Python)
│   ├── script.py
│   ├── script_v2.py
│   └── script_v3.py
│
├── dbt_elt/              # Projeto dbt
│   ├── models/           # Modelos SQL (transformações)
│   │   └── example/
│   │       └── silver/
│   │           └── trabalho_remoto.sql
│   ├── seeds/
│   ├── snapshots/
│   ├── tests/
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── pyproject.toml        # Dependências do projeto (Poetry)
├── poetry.lock           # Lockfile de dependências
└── .gitignore
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Instalar dependências

Certifique-se de ter **Python 3.9+** e **Poetry** instalados.

```bash
poetry install
```

### 2️⃣ Executar a extração e carga no Snowflake

```bash
python extraction/script_v3.py
```

> ⚠️ Antes de rodar, configure suas credenciais do Snowflake no arquivo `profiles.yml`.

### 3️⃣ Rodar transformações no dbt

```bash
cd dbt_elt
dbt run
```

### 4️⃣ (Opcional) Rodar testes de qualidade de dados

```bash
dbt test
```

---

## 🧠 Modelo de Dados (Camada Silver)

O modelo principal gerado pelo dbt é:

* **trabalho_remoto** – tabela tratada contendo:

  * título da vaga
  * nome da empresa
  * salário mínimo e máximo anual
  * salário mensal calculado

Essa tabela está pronta para consumo por ferramentas de BI ou análises avançadas.

---

## 🎯 Próximos Passos (Roadmap)

Algumas melhorias planejadas para versões futuras:

* ✔️ Implementar testes de qualidade de dados no dbt (data tests)
* 🔄 Criar carregamento incremental no Snowflake
* 🤖 Automatizar o pipeline com GitHub Actions
* 📊 Criar dashboards no Power BI ou Tableau

---


📍 GitHub: [https://github.com/renataennes](https://github.com/renataennes)

