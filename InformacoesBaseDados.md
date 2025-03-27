# 🗃️ Dicionário de Variáveis - Dataset de Crédito

Este arquivo documenta o significado dos códigos presentes nas colunas do dataset utilizado para avaliação de risco de crédito.

---

## `laufkont` → `status` (Status da Conta Corrente)

| Código | Significado                                  |
|--------|----------------------------------------------|
| 1      | Sem conta corrente                           |
| 2      | Saldo menor que 0 DM                         |
| 3      | Saldo entre 0 e 200 DM                       |
| 4      | Saldo maior ou igual a 200 DM / salário estável |

---

## `laufzeit` → `duration`  
**Duração do empréstimo** (em meses)

---

## `moral` → `credit_history` (Histórico de Crédito)

| Código | Significado                                         |
|--------|-----------------------------------------------------|
| 0      | Atraso anterior                                     |
| 1      | Conta crítica / outros créditos                     |
| 2      | Nenhum crédito / todos pagos                        |
| 3      | Créditos pagos corretamente até agora               |
| 4      | Todos os créditos neste banco pagos corretamente    |

---

## `verw` → `purpose` (Finalidade do Crédito)

| Código | Significado           |
|--------|-----------------------|
| 0      | Outros                |
| 1      | Carro novo            |
| 2      | Carro usado           |
| 3      | Móveis / Equipamentos |
| 4      | Rádio / TV            |
| 5      | Eletrodomésticos      |
| 6      | Reparos               |
| 7      | Educação              |
| 8      | Férias                |
| 9      | Reciclagem profissional |
| 10     | Negócios              |

---

## `sparkont` → `savings` (Conta Poupança)

| Código | Significado               |
|--------|---------------------------|
| 1      | Desconhecido / Nenhuma    |
| 2      | < 100 DM                  |
| 3      | 100–499 DM                |
| 4      | 500–999 DM                |
| 5      | >= 1000 DM                |

---

## `beszeit` → `employment_duration` (Tempo de Emprego)

| Código | Significado           |
|--------|-----------------------|
| 1      | Desempregado          |
| 2      | < 1 ano               |
| 3      | 1 a < 4 anos          |
| 4      | 4 a < 7 anos          |
| 5      | >= 7 anos             |

---

## `rate` → `installment_rate` (% da renda comprometida)

| Código | Significado      |
|--------|------------------|
| 1      | >= 35%           |
| 2      | 25% a < 35%      |
| 3      | 20% a < 25%      |
| 4      | < 20%            |

---

## `famges` → `personal_status_sex`

| Código | Significado                               |
|--------|-------------------------------------------|
| 1      | Homem divorciado / separado               |
| 2      | Mulher não solteira ou homem solteiro     |
| 3      | Homem casado / viúvo                      |
| 4      | Mulher solteira                           |

---

## `buerge` → `other_debtors`

| Código | Significado   |
|--------|---------------|
| 1      | Nenhum        |
| 2      | Co-requerente |
| 3      | Fiador        |

---

## `wohnzeit` → `present_residence` (Tempo de residência atual)

| Código | Significado        |
|--------|--------------------|
| 1      | < 1 ano            |
| 2      | 1 a < 4 anos       |
| 3      | 4 a < 7 anos       |
| 4      | >= 7 anos          |

---

## `verm` → `property` (Propriedade)

| Código | Significado                            |
|--------|----------------------------------------|
| 1      | Nenhuma / desconhecida                 |
| 2      | Carro ou outro bem                     |
| 3      | Poupança / seguro                      |
| 4      | Imóvel                                 |

---

## `alter` → `age`  
**Idade do cliente**

---

## `weitkred` → `other_installment_plans`

| Código | Significado |
|--------|-------------|
| 1      | Banco       |
| 2      | Lojas       |
| 3      | Nenhum      |

---

## `wohn` → `housing`

| Código | Significado |
|--------|-------------|
| 1      | Gratuito    |
| 2      | Alugado     |
| 3      | Próprio     |

---

## `bishkred` → `number_credits` (Número de créditos existentes)

| Código | Significado  |
|--------|--------------|
| 1      | 1 crédito    |
| 2      | 2–3 créditos |
| 3      | 4–5 créditos |
| 4      | >= 6 créditos|

---

## `beruf` → `job` (Profissão)

| Código | Significado                                 |
|--------|---------------------------------------------|
| 1      | Desempregado / não qualificado (estrangeiro)|
| 2      | Não qualificado - residente                 |
| 3      | Empregado qualificado / funcionário         |
| 4      | Gerente / autônomo / altamente qualificado  |

---

## `pers` → `people_liable` (Dependentes financeiros)

| Código | Significado     |
|--------|-----------------|
| 1      | 3 ou mais       |
| 2      | 0 a 2           |

---

## `telef` → `telephone`

| Código | Significado                        |
|--------|------------------------------------|
| 1      | Não possui                         |
| 2      | Sim (em nome do cliente)           |

---

## `gastarb` → `foreign_worker` (Trabalhador estrangeiro)

| Código | Significado |
|--------|-------------|
| 1      | Sim         |
| 2      | Não         |

---

## `kredit` → `credit_risk` (**variável alvo**)

| Código | Significado |
|--------|-------------|
| 0      | Risco ruim  |
| 1      | Risco bom   |
