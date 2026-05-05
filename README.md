# Auto

Projeto de automação de testes para a disciplina de **Teste e Qualidade de Software**.

Cobre, em um único repositório, duas frentes de automação:

- **API** — Swagger Petstore (`https://petstore.swagger.io/v2`)
- **Web** — SauceDemo (`https://www.saucedemo.com/`)

Ambas são executadas automaticamente em pipeline (GitHub Actions).

## Tecnologias

| Camada | Ferramenta |
|---|---|
| Linguagem | Python 3.12 |
| Test runner | pytest |
| Cliente HTTP (API) | requests |
| Automação Web | Selenium |
| Driver | webdriver-manager (Chrome / Firefox) |
| Variáveis de ambiente | python-dotenv |
| CI | GitHub Actions |

## Estrutura do repositório

```
Auto/
├── api_tests/
│   ├── conftest.py
│   ├── tests/
│   │   ├── test_pet.py
│   │   ├── test_store.py
│   │   └── test_user.py
│   └── utils/
│       └── client.py
├── web_tests/
│   ├── conftest.py
│   ├── pages/
│   │   ├── base.py
│   │   ├── login.py
│   │   ├── inventory.py
│   │   ├── cart.py
│   │   └── checkout.py
│   ├── tests/
│   │   ├── test_login.py
│   │   └── test_checkout.py
│   └── utils/
│       └── driver.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Pré-requisitos

- Python 3.12
- Git
- Chrome **ou** Firefox instalado (apenas para a automação Web local)

## Instalação

```bash
git clone <url-do-repo>
cd Auto

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Executando os testes

### API (Petstore)

```bash
pytest api_tests/
```

Cobertura:

- **Pet** — criar, buscar por id, atualizar, buscar por status, deletar
- **Store** — criar pedido, consultar pedido, deletar pedido, inventário
- **User** — criar, buscar, atualizar, login, logout, deletar

### Web (SauceDemo)

```bash
pytest web_tests/
```

Cobertura:

- Login válido
- Login bloqueado (validação de mensagem de erro)
- Fluxo E2E: login → adicionar produtos → carrinho → checkout → confirmação

#### Variáveis de ambiente (Web)

| Variável | Valores | Default |
|---|---|---|
| `BROWSER` | `chrome`, `firefox` | `chrome` |
| `HEADLESS` | `true`, `false` | `true` |

Exemplo rodando com Firefox em modo visível:

```bash
BROWSER=firefox HEADLESS=false pytest web_tests/
```

### Rodar tudo

```bash
pytest
```

## Padrões e organização

- **API** — cliente HTTP encapsulado em `api_tests/utils/client.py`, fixture `api` compartilhada via `conftest.py`. Cada recurso (Pet, Store, User) em um arquivo de teste próprio, com fixtures de criação/limpeza para evitar dependência entre testes.
- **Web** — Page Object Model. Cada tela é uma classe em `web_tests/pages/` com seus locators e ações. Testes apenas orquestram páginas e fazem asserts. `BasePage` centraliza esperas e interações.

## Pipeline CI

`.github/workflows/ci.yml` roda em todo push e pull request para `main` (e pode ser disparada manualmente). São dois jobs em paralelo:

- `api-tests` — instala dependências e roda `pytest api_tests/`
- `web-tests` — instala dependências e roda `pytest web_tests/` com Chrome headless

## Autor

Leo Augusto — Teste e Qualidade de Software.
