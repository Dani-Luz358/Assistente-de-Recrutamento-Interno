# -*- coding: utf-8 -*-
"""
Assistente de Recrutamento Interno
Desenvolvido por Danielle Luz
"""

import streamlit as st

def responder_pergunta(pergunta):
    regras = {
        "regras gerais": """
- O currículo deve estar atualizado, caso contrário, a inscrição será desclassificada.
- A inscrição precisa ser feita enquanto a vaga estiver publicada.
- O gestor atual do colaborador deve estar ciente da candidatura.
- Participar de um recrutamento por vez.
- Em caso de reprova, o colaborador poderá se candidatar normalmente a outro processo.
""",
        "elegibilidade": """
**Colaboradores**: 
- Mínimo **12 meses** no cargo atual e desde a última promoção.
- Ter atingido na avaliação de final de ano a nota de **“Atendeu ou Superou”**.
- Poderá participar apenas de vagas com salário igual ou superior ao atual.

**Estagiários**: 
- Mínimo **12 meses** de contrato e desempenho satisfatório (feedback formal do gestor).

**Aprendizes**: 
- Mínimo **11 meses** de contrato e desempenho satisfatório (feedback formal do gestor).
""",
        "política": "Política de Recrutamento e Seleção pode ser acessada através desse link: (https://www.ache.com.br/).",
        "divulgação": "Todas as publicações de vagas estarão disponíveis no Viva Engage e na Página de LinkedIn do Aché: (https://www.linkedin.com/jobs/search/?currentJobId=4368187837&f_C=50866&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION)."
    }

    for chave, resposta in regras.items():
        if chave in pergunta.lower():
            return resposta
    return "Desculpe, não encontrei uma regra específica. Tente usar palavras como 'divulgação', 'elegibilidade', 'regras gerais' ou 'política'."

# Interface Streamlit
st.title("Assistente de Recrutamento Interno - Atração de Talentos 🧠")
st.markdown("""
Bem-vindo ao **Assistente de Recrutamento Interno**!
Aqui você pode tirar dúvidas sobre a política de recrutamento e seleção, regras gerais, elegibilidade e divulgação de vagas.
""")

st.subheader("Faça sua pergunta")
pergunta = st.text_area("Digite sua pergunta:", height=120)

if st.button("Enviar"):
    if pergunta:
        resposta = responder_pergunta(pergunta)
        st.markdown(resposta)

st.markdown("---")

st.caption("Desenvolvido por Danielle Luz • Assistente de IA para Recrutamento Interno")
