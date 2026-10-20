
# Laboratorio 8 - Respostas

## Exercicio 1 - Forca da senha

### a) GFC e complexidade

O GFC pode ser descrito pelos nos abaixo:

```text
Entrada -> len(senha) < 8
             | sim -> fraca -> saida
             | nao -> pontos = 0 -> teste do for

for: ainda ha caractere?
       | nao -> pontos >= 4?
       | sim -> c.isdigit()?
                  | sim -> pontos += 1 -> for
                  | nao -> not c.isalnum()?
                             | sim -> pontos += 2 -> for
                             | nao -> for

pontos >= 4?
   | sim -> forte -> saida
   | nao -> media -> saida
```

Ha cinco nos de decisao: o `if` do tamanho, o teste do `for`, o `if` de digito, o `elif` de simbolo e o `if` final. Portanto:

- Pela formula dos predicados: `V(G) = 5 + 1 = 6`.
- Pela formula estrutural, com `N = 13` (incluindo entrada e saida), `E = 17` e `P = 1`: `V(G) = E - N + 2P = 17 - 13 + 2 = 6`.

### b) Base de caminhos

Uma base de seis caminhos, usando `L` para letra, `D` para digito e `S` para simbolo, e:

1. `len < 8 -> fraca`; entrada `abc`, resultado `fraca`.
2. `len >= 8 -> for sem iteracao -> media`; caminho teorico, **inviavel**, pois `len >= 8` obriga pelo menos oito iteracoes.
3. `len >= 8 -> L -> for -> pontos < 4 -> media`; entrada `abcdefgh`, resultado `media`.
4. `len >= 8 -> D -> pontos += 1 -> for -> pontos >= 4 -> forte`; entrada `12345678`, resultado `forte`.
5. `len >= 8 -> S -> pontos += 2 -> for -> pontos >= 4 -> forte`; entrada `!!!!aaaa`, resultado `forte`.
6. `len >= 8 -> D e S -> pontos >= 4 -> forte`; entrada `a1!bcdef4`, resultado `forte`.

A independencia vem da introducao, em cada caminho, de uma aresta que nao aparece nos caminhos anteriores: retorno do laco, ramo de digito, ramo de simbolo, acumulacao e cada resultado final. O caminho sem iteracoes e inviavel pelo requisito de tamanho minimo.

### c) Testes e ramos

Os cinco casos parametrizados em `test_senha.py` cobrem os caminhos praticaveis: senha curta, apenas letras, digitos, simbolos e mistura. A suite atinge 100% dos ramos praticaveis. Ela usa cinco casos executaveis, enquanto `V(G) = 6`, porque um dos caminhos da base e inviavel.

Com o ambiente preparado pelo PDF, a medicao e:

```bash
coverage run --branch --source=senha -m pytest -q
coverage report -m
```

### d) Teste de lacos

As categorias teoricas sao 0, 1, 2 e muitas voltas. Para esta funcao, 0 e 1 volta sao inviaveis quando o laco e alcancado: chegar ao `for` exige uma senha com pelo menos 8 caracteres. O caso minimo executavel tem 8 voltas; `12345678` e `abcdefgh` cobrem esse caso, e `!!!!aaaa`/`a1b2c3d4` cobrem varias voltas com diferentes ramos do corpo.

## Exercicio 2 - Controle de embarque

### a) `mcdc.py`

A regra direta da especificacao e:

```python
cartao and documento and (grupo_chamado or prioridade)
```

`pares_independentes(decisao, n)` gera pares de linhas que diferem em exatamente uma condicao e mudam a decisao.

### b) Pares e conjuntos MC/DC

Considerando as condicoes na ordem `(cartao, documento, grupo_chamado, prioridade)`, a quantidade de pares independentes e:

| Condicao | Pares |
|---|---:|
| cartao | 3 |
| documento | 3 |
| grupo_chamado | 1 |
| prioridade | 1 |

Existem **4 conjuntos MC/DC minimos**, todos com **5 casos**. O limite de cinco decorre de quatro condicoes que precisam demonstrar efeito independente, mais um caso compartilhado.

### c) Todos V e todos F

Os testes `(V,V,V,V)` e `(F,F,F,F)` passam tanto na funcao defeituosa quanto na especificacao. Eles exercitam os resultados verdadeiro e falso do `if`, portanto podem aparentar cobertura de ramos completa, mas nao isolam a precedencia de `and` e `or`.

### d) Comparacao e correcao

A funcao fornecida interpreta a expressao como:

```python
(cartao and documento and grupo_chamado) or prioridade
```

Isso permite embarque apenas com prioridade, mesmo sem cartao ou documento. Dos quatro conjuntos MC/DC enumerados, **3 detectam** essa diferenca e **1 nao detecta**. Portanto MC/DC minimo depende do conjunto escolhido. MCC (Multiple Condition Coverage) sempre encontra o defeito porque exercita todas as 16 combinacoes das quatro condicoes, incluindo combinacoes com `prioridade=True` e cartao/documento falsos.

A funcao corrigida usa:

```python
cartao and documento and (grupo_chamado or prioridade)
```

## Exercicio 3 - Preco com desconto VIP

### a) Definicoes, usos e pares DU

Numeracao conforme o codigo do enunciado:

- `total`: definicao na linha 3 (`total = preco`); uso c-use na linha 6; uso p-use na linha 7; uso c-use na linha 9.
- `total`: nova definicao na linha 6 (`total = ...`); uso p-use na linha 7; uso c-use na linha 9.
- `total`: nova definicao na linha 8 (`total = 50`); uso c-use na linha 9.
- `desconto`: definicao na linha 5; uso c-use na linha 6.

Pares definição-uso viaveis:

- `total(3) -> total(6)` pelo ramo VIP.
- `total(3) -> total(7)` pelo ramo nao VIP.
- `total(3) -> total(9)` pelo ramo nao VIP quando o total nao e menor que 50.
- `total(6) -> total(7)` pelo ramo VIP.
- `total(6) -> total(9)` pelo ramo VIP quando o total nao e menor que 50.
- `total(8) -> total(9)` quando o piso de R$50 e aplicado.
- `desconto(5) -> desconto(6)`.

### b) Pares nao percorridos pela suite atual

A suite atual usa `(60, True)` e `(200, False)`. Ela nao percorre:

- `total(6) -> total(9)`, pois falta um caso VIP cujo total calculado fique acima de R$50.

Os demais pares sao percorridos: o caso 60 VIP cobre `total(3) -> total(6)`, `total(6) -> total(7)`, `total(8) -> total(9)` e `desconto(5) -> desconto(6)`; o caso 200 nao VIP cobre os usos de `total(3)`.

### c) All-Uses e defeito mascarado

A partir da especificacao, falta um caso VIP acima do piso para completar o par DU ausente. O caso adicional essencial e, por exemplo, `preco_final(100, True) == 80`: ele evita o piso e revela que a funcao defeituosa calcula `100 * 0.8 - 20 = 60` em vez de `80`.

A suite atual nao viu o defeito porque, para `60` VIP, o valor incorreto `28` ainda e transformado em `50` pelo piso. O segundo caso, `200` nao VIP, nao executa o calculo do desconto. Assim, 100% de ramos nao garante que cada valor definido alcance cada uso.

### d) Correcao

A linha defeituosa:

```python
total = total * 0.8 - desconto
```

foi substituida por:

```python
total = total - desconto
```

A suite corrigida inclui os dois casos originais e casos que cobrem desconto acima do piso e o piso sem desconto.

## Execucao

Na pasta `lab08`, com as dependencias do PDF instaladas:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
pytest -q --cov=senha --cov=embarque --cov=preco --cov-branch --cov-report=term-missing
```

A suite funcional criada nesta entrega passa com **19 testes**.
