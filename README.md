# Auto

Projeto de automação de testes para a disciplina de **Teste e Qualidade de Software**.

Cobre duas frentes em um único repositório:

- **API** — Swagger Petstore (`https://petstore.swagger.io/v2`)
- **Web** — SauceDemo (`https://www.saucedemo.com/`)

Execução automática via **GitHub Actions** a cada push/PR para `main`.

## Tecnologias

| Camada | Ferramenta |
|---|---|
| Linguagem | Python 3.12 |
| Test runner | pytest |
| API | requests |
| Web | Selenium + Page Object Model |
| Driver | webdriver-manager (Chrome/Firefox) |
| CI | GitHub Actions |

## Pré-requisitos

- Python 3.12
- Chrome **ou** Firefox (apenas para os testes Web locais)

## Instalação


git clone https://github.com/LEEL-exe/Auto.git
cd Auto

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

## Execução

Rodar tudo (API + Web):


pytest

Apenas API:

pytest api_tests/

Apenas Web (Chrome headless por padrão):


pytest web_tests/


Trocar para Firefox ou desligar o headless via variáveis de ambiente:

BROWSER=firefox HEADLESS=false pytest web_tests/


## Estrutura

Auto/
├── api_tests/
│   ├── conftest.py            # fixture do ApiClient
│   ├── tests/                 # test_pet, test_store, test_user
│   └── utils/client.py        # wrapper de requests
├── web_tests/
│   ├── conftest.py            # fixture do WebDriver
│   ├── pages/                 # Page Objects (base, login, inventory, cart, checkout)
│   ├── tests/                 # test_login, test_checkout
│   └── utils/driver.py        # factory Chrome/Firefox + headless
├── .github/workflows/ci.yml   # pipeline de CI
├── pytest.ini
└── requirements.txt

## Cobertura de testes

**API — 15 testes** cobrindo os recursos `pet`, `store` e `user`:

- `pet`: create, get, update, delete, find by status
- `store`: create order, get order, delete order, inventory
- `user`: create, get, update, login, logout, delete

**Web — 3 testes**:

- Login com credenciais válidas
- Login com usuário bloqueado (mensagem de erro)
- Fluxo E2E completo: login → adicionar 2 produtos ao carrinho → checkout → confirmação

Total: **18 testes**.

## CI

Workflow em `.github/workflows/ci.yml`:

- Roda em `push` e `pull_request` na branch `main`, ou manualmente (`workflow_dispatch`)
- Dois jobs paralelos: `api-tests` e `web-tests`
- Web roda em Chrome headless no Ubuntu runner
