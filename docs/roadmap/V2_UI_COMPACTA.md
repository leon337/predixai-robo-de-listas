# Roadmap — PredixAI Robô de Listas V2

## Condição de início

A V2 só começa depois da validação local do atalho desktop da V1.

## Objetivo

Modernizar a interface sem remover as funções validadas da V1.

## Escopo aprovado

- janela inicial compacta, aproximadamente `560x520`;
- modo de execução compacto, aproximadamente `420x280`;
- seletores separados para hora, minuto e segundo;
- campos numéricos que não aceitam letras;
- cartões de sinais mais compactos;
- rolagem interna;
- botões com aparência mais clara e consistente;
- melhor recorte e aplicação da logomarca;
- manutenção da agenda com até cinco sinais;
- preservação da calibração, movimento e clique.

## Fluxo Git planejado

```txt
main
→ V1 estável

feature/v2-ui-compacta
→ desenvolvimento isolado da V2

Pull Request
→ revisão e validação

main
→ futura V2 estável
```

## Critérios de validação

- V1 continua executável;
- nenhum sinal é perdido ao reorganizar a interface;
- horários são ordenados corretamente;
- letras são rejeitadas nos campos de horário;
- até cinco sinais continuam disponíveis;
- calibração e clique continuam funcionando;
- interface cabe na resolução `1366x768`;
- modo compacto permanece utilizável.

## Estado

```txt
V1_DESKTOP=EM_VALIDACAO
V2_IMPLEMENTACAO=NAO_INICIADA
```
