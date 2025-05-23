
# 🏥 Sistema de Gerenciamento Hospitalar

Este é um sistema simples de gerenciamento hospitalar, desenvolvido em **Python**, como parte do **projeto final** da disciplina de **Algoritmos e Programação em Python** do curso de **Pós-Graduação em Ciência de Dados** da **Facens**.

O projeto foi realizado em **equipe**, aplicando conceitos de **manipulação de dados**, **orientação a objetos** e **persistência de dados** com arquivos CSV.

---

## ✅ Funcionalidades

- **Cadastro, listagem, edição e exclusão** de:
  - Pacientes
  - Consultas
  - Procedimentos
- **Validação de CPF** e **validação de datas**.
- **Geração automática de IDs**.
- **Armazenamento persistente** via arquivos CSV.
- **Interface interativa** via terminal.

---

## 🗂️ Estrutura do Projeto

```
/dados
    pacientes.csv
    consultas.csv
    procedimentos.csv
    ultimo_id_paciente.txt
    ultimo_id_consulta.txt
    ultimo_id_procedimento.txt
/logs
    log.txt
/models
    paciente.py
    consulta.py
    procedimento.py
/utils
    configs.py
initialize.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **pandas** — Manipulação de dados
- **tabulate** — Formatação de tabelas no terminal
- **datetime** — Validação de datas
- **os** — Manipulação de arquivos e diretórios

---

## 🚀 Como executar o projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências:

```bash
pip install pandas tabulate
```

### 3. Execute o sistema:

```bash
python initialize.py
```

---

## 📁 Armazenamento de Dados

- Os registros são armazenados em arquivos CSV localizados na pasta `dados`.
- Arquivos `.txt` são utilizados para controle dos IDs.
- A pasta `logs` está preparada para armazenamento de registros futuros.

---

## 📌 Melhorias Futuras

- Implementação de sistema de logs completo.
- Desenvolvimento de interface gráfica (GUI) ou Web.
- Integração com banco de dados relacional.
- Implementação de autenticação e controle de acesso.

---

## 👥 Integrantes do Grupo

- [José Dantas](https://github.com/dantasjose)
- [Waldir Pulzi Jr](https://github.com/waldirpulzijr)
- [Daniele Costa](https://github.com/danycosta40)
- [Denis Borg](https://github.com/denisborg)

---

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como requisito de avaliação para a disciplina de **Algoritmos e Programação em Python** no curso de **Pós-Graduação em Ciência de Dados** — **Facens**.

---

## 📄 Licença

Este projeto é de uso acadêmico e está sob a licença **MIT**.
