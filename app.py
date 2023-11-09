import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Gera os dados

def simulate_controls_data_resume(unit_selection):
    np.random.seed(42)
    if unit_selection == 'Unidade de Varejo':
        # Controles de Crédito
        credit_controls_data = {
            'Utilização do Limite de Crédito': np.random.uniform(50, 100, 12),  # Simula uma taxa de utilização em porcentagem
            'efficacy': np.random.uniform(0.1, 0.2, 12)  # Simula eficácia dos controles de crédito
        }

        # Controles Operacionais
        operational_controls_data = {
            'Fraud_Detection_Rate': np.random.uniform(70, 100, 12),  # Simula taxa de detecção de fraude em porcentagem
            'efficacy': np.random.uniform(0.8, 1.0, 12)  # Simula eficácia dos controles operacionais
        }

        # Controles de Reputação
        reputation_controls_data = {
            'Índice de Satisfação do Cliente (%)_Score': np.random.uniform(3, 5, 12),  # Simula pontuação de satisfação do cliente de 1 a 5
            'efficacy': np.random.uniform(0.5, .7, 12)  # Simula eficácia dos controles de reputação
        }

        # Agrupa todos os dados de controle em um dicionário
        controls_data = {
            'Crédito': credit_controls_data,
            'Operacional': operational_controls_data,
            'Reputação': reputation_controls_data
        }

    elif unit_selection == 'Unidade Investimentos':
        # Políticas e Limites de Investimento
        investment_policy_controls_data = {
            'Policy_Compliance_Rate': np.random.uniform(80, 100, 12),  # Simula taxa de conformidade com políticas em porcentagem
            'efficacy': np.random.uniform(0.1, .5, 12) # Simula eficácia das políticas e limites de investimento
        }

        # Análise de Crédito
        credit_analysis_controls_data = {
            'Credit_Risk_Score': np.random.uniform(70, 100, 12),  # Simula pontuação de risco de crédito
            'efficacy': np.random.uniform(0.1, 1.0, 12) # Simula eficácia da análise de crédito
        }

        # Planos de Contingência de Liquidez
        liquidity_plan_controls_data = {
            'Liquidity_Coverage_Ratio': np.random.uniform(100, 150, 12),  # Simula razão de cobertura de liquidez
            'efficacy': np.random.uniform(0.1, 1.0, 12)  # Simula eficácia dos planos de contingência de liquidez
        }

        # Agrupa todos os dados de controle em um dicionário
        controls_data = {
            'Política de Investimento': investment_policy_controls_data,
            'Análise de Crédito': credit_analysis_controls_data,
            'Plano de Liquidação': liquidity_plan_controls_data
        }


    return controls_data

# Simular dados para os controles
def simulate_controls_data(unit_selection):
    if unit_selection == 'Unidade de Varejo':
        # Dados para controles de crédito
        credit_controls_data = pd.DataFrame({
            'Mês': pd.date_range(start='2022-01-01', periods=12, freq='M'),
            'Utilização do Limite de Crédito': np.random.rand(12) * 100,
            'Empreśtimos Acimo do Limite': np.random.randint(0, 10, size=12)
        })

        # Dados para controles operacionais
        operational_controls_data = pd.DataFrame({
            'Mês': pd.date_range(start='2022-01-01', periods=12, freq='M'),
            'Taxa de Detecção de Fraudes (%)': np.random.randint(0, 100, size=12),
            'Taxa de Prevenção de Fraudes (%)': np.random.randint(0, 100, size=12)
        })

        # Dados para controles de reputação
        reputation_controls_data = pd.DataFrame({
            'Mês': pd.date_range(start='2022-01-01', periods=12, freq='M'),
            'Avaliação do Cliente': np.random.rand(12) * 5,  # Avaliação de 1 a 5
            'Tempo de Resposta': np.random.randint(1, 48, size=12)  # Tempo de resposta em horas
        })

        return credit_controls_data, operational_controls_data, reputation_controls_data

    elif unit_selection == 'Unidade Investimentos':
        Mêss = pd.date_range(start='2021-01-01', periods=12, freq='M')
        # Simulação de dados para Políticas e Limites de Investimento
        investment_policy_data = pd.DataFrame({
            'Mês': Mêss,
            'Conformidade com a Política de Investimento': np.random.uniform(0.8, 1.0, size=12)  # Conformidade com a política como percentual
        })

        # Simulação de dados para Análise de Crédito
        credit_analysis_data = pd.DataFrame({
            'Mês': Mêss,
            'Score de risco de crédito': np.random.uniform(0.6, 1.0, size=12)  # Pontuação de avaliação de risco de crédito
        })

        # Simulação de dados para Planos de Contingência de Liquidez
        liquidity_plan_data = pd.DataFrame({
            'Mês': Mêss,
            'Força do Plano de Contingência de Liquidez': np.random.uniform(0.5, 1.0, size=12)  # Força do plano de contingência de liquidez
        })

        return investment_policy_data, credit_analysis_data, liquidity_plan_data

def simulate_summary_data(controls_data, unit_selection):
    
    if unit_selection == 'Unidade de Varejo':
        # Agrega dados para criar um resumo executivo
        summary_data = {
            'Total_Defaults': int(np.random.uniform(100, 500)),  # Total de inadimplências
            'Total_Frauds': int(np.random.uniform(50, 150)),  # Total de Taxa de Detecção de Fraudes (%)
            'Average_Índice de Satisfação do Cliente (%)': np.mean(controls_data['Reputation']['Índice de Satisfação do Cliente (%)_Score'])  # Média de satisfação do cliente
        }
    elif unit_selection == 'Unidade Investimentos':
        # Agrega dados para criar um resumo executivo para a Unidade de Investimentos
        summary_data = {
            'Total_Policy_Violations': int(np.random.uniform(0, 50)),  # Total de violações de políticas de investimento
            'Total_Credit_Risk_Events': int(np.random.uniform(0, 20)),  # Total de eventos de risco de crédito identificados
            'Average_Liquidity_Coverage': np.mean(controls_data['LiquidityPlan']['Liquidity_Coverage_Ratio'])  # Média da razão de cobertura de liquidez
        }


    # Avalia o estado geral dos controles com base nos KPIs de eficácia
    average_efficacy = np.mean([np.mean(controls_data[control]['efficacy']) for control in controls_data])
    controls_status = 'Verde' if average_efficacy > 0.75 else 'Amarelo' if average_efficacy > 0.5 else 'Vermelho'

    return summary_data, controls_status

def simulate_risk_data(unit_selection):
    if unit_selection == 'Unidade de Varejo':
        # Gerar dados de inadimplência para os últimos 12 meses
        credit_risk_data = pd.DataFrame({
            'Mês': pd.date_range(start='2022-01-01', periods=12, freq='M'),
            'Taxa de Inadimplência (%)': np.random.rand(12) * 100 - np.arange(0, 12) * 10 # Taxa de inadimplência como percentual
        })

        # Gerar dados de fraudes e falhas de segurança
        operational_risk_data = pd.DataFrame({
            'Mês': pd.date_range(start='2022-01-01', periods=12, freq='M'),
            'Fraudes': np.random.randint(0, 100, size=12),
            'Incidentes Cibernéticos': np.random.randint(0, 100, size=12)
        })

        # Gerar dados de satisfação do cliente
        reputation_risk_data = pd.DataFrame({
            'Mês': pd.date_range(start='2022-01-01', periods=12, freq='M'),
            'Índice de Satisfação do Cliente (%)': np.random.rand(12) * 100 + np.arange(0, 12) * 10# Percentual de satisfação
        })
        return credit_risk_data, operational_risk_data, reputation_risk_data

    elif unit_selection == 'Unidade Investimentos':
        Mêss = pd.date_range(start='2021-01-01', periods=12, freq='M')
        # Simulação de dados de risco de mercado
        market_risk_data = pd.DataFrame({
            'Mês': Mêss,
            'Variação do Preço de Mercado (%)': np.random.uniform(-0.1, 0.1, size=12)  + np.arange(0, 12) * 0.01  # Flutuações de preço como percentual
        })

        # Simulação de dados de risco de crédito
        credit_risk_data = pd.DataFrame({
            'Mês': Mêss,
            'Falhas da contraparte': np.random.randint(0, 10, size=12)  # Número de falhas de contraparte
        })

        # Simulação de dados de risco de liquidez
        liquidity_risk_data = pd.DataFrame({
            'Mês': Mêss,
            'Taxa de Liquidez de Ativos': np.random.uniform(0.5, 1.5, size=12)  # Razão de liquidez de ativos
        })

        return market_risk_data, credit_risk_data, liquidity_risk_data

def toggle_action(control):
    # Se a chave não existe no estado da sessão, ou seja, o botão nunca foi pressionado,
    # o estado é inicialmente configurado para False (texto não mostrado).
    # Se a chave existe, invertemos o estado.
    st.session_state[control] = not st.session_state.get(control, False)


# Adicionar visão geral e avaliação ao dashboard
def create_controls_overview(controls_data, unit_selection):

    actions_dict = {
        'Crédito': """
        - **Análise de Dados:** Intensifique o uso de análise preditiva para identificar clientes com alto risco de inadimplência.
        - **Revisão de Política de Crédito:** Reavalie a política de concessão de créditos.
        - **Programas de Negociação:** Desenvolva programas de renegociação de dívidas para clientes em atraso.
        """,

        'Operacional': """
        - **Tecnologia Anti-fraude:** Implemente ou atualize soluções de detecção de fraude baseadas em IA.
        - **Treinamento de Funcionários:** Realize treinamentos regulares sobre práticas de prevenção de fraude.
        - **Processos de Verificação:** Fortaleça os processos de verificação de transações e clientes.
        """,

        'Reputação': """
        - **Feedback do Cliente:** Implemente um sistema de feedback em tempo real para avaliar a satisfação do cliente.
        - **Atendimento ao Cliente:** Melhore o treinamento da equipe de suporte para proporcionar um atendimento mais eficiente e empático.
        - **Resolução de Problemas:** Crie uma força-tarefa para resolver rapidamente as questões críticas de satisfação do cliente.
        """,

        'Política de Investimento': """
        - **Auditorias e Monitoramento:** Aumente a frequência das auditorias de conformidade e use monitoramento em tempo real.
        - **Educação e Consciência:** Reforce a importância da adesão às políticas com sessões educacionais.
        - **Sistemas de Alerta:** Estabeleça alertas automáticos para violações de políticas.
        """,

        'Análise de Crédito': """
        - **Avaliação de Risco Aprofundada:** Use modelos de risco de crédito mais sofisticados para análise de contraparte.
        - **Diversificação de Portfólio:** Revise o portfólio para garantir diversificação e minimizar riscos.
        - **Limiares de Alerta:** Configure limiares para identificar aumentos no risco de crédito.
        """,

        'Plano de Liquidação': """
        - **Análise de Liquidez:** Realize testes de estresse regulares para avaliar a robustez da liquidez.
        - **Reservas de Contingência:** Constitua ou aumente reservas de contingência para melhorar a cobertura de liquidez.
        - **Gestão de Ativos e Passivos:** Melhore a correspondência entre ativos e passivos para gerenciar a liquidez efetivamente.
        """
        }

    # Avaliar a eficácia dos controles
    controls_evaluation = evaluate_controls(controls_data)

    if unit_selection == 'Unidade de Varejo':
        # Apresentar os controles e sua eficácia
        st.subheader("Eficácia dos Controles")
        for control, status in controls_evaluation.items():
            # Verifique o estado atual deste controle específico no estado da sessão
            show_action_key = f"show_action_{control}"
        
            if status == 'Eficaz':
                st.success(f"{control}: {status}")
            elif status == 'Necessita de atenção':
                st.warning(f"{control}: {status}")
            else:
                st.error(f"{control}: {status}")
                # Adiciona um botão que, quando clicado, mostra as ações para esse controle específico
            # Crie um botão que, quando clicado, irá alternar a visibilidade das ações
            if st.button(f"Ações para corrigir {control}", key=f"btn_{control}"):
                toggle_action(show_action_key)
            
            # Se o estado de visibilidade deste controle for True, mostrar as ações
            if st.session_state.get(show_action_key):
                st.markdown(actions_dict[control])

    elif unit_selection == 'Unidade Investimentos':
        st.subheader("Eficácia dos Controles da Unidade de Investimentos")
        for control, status in controls_evaluation.items():
            control_name = ' '.join(control.split('_')).title()  # Transforma 'InvestmentPolicy' em 'Investment Policy'
            show_action_key = f"show_action_{control}"
            if status == 'Eficaz':
                st.success(f"{control_name}: {status}")
            elif status == 'Necessita de atenção':
                st.warning(f"{control_name}: {status}")
            else:
                st.error(f"{control_name}: {status}")
                # Adiciona um botão que, quando clicado, mostra as ações para esse controle específico
            # Crie um botão que, quando clicado, irá alternar a visibilidade das ações
            if st.button(f"Ações para corrigir {control}", key=f"btn_{control}"):
                toggle_action(show_action_key)
            
            # Se o estado de visibilidade deste controle for True, mostrar as ações
            if st.session_state.get(show_action_key):
                st.markdown(actions_dict[control])

# Avalia a eficácia dos controles com base em KPIs e sinaliza melhorias
def evaluate_controls(controls_data):
    # Esta é uma função fictícia para ilustrar a lógica de avaliação dos controles
    controls_evaluation = {}
    for control, data in controls_data.items():
        efficacy_scores = data['efficacy']
        # Avalia a eficácia de cada controle com base na média dos escores de eficácia
        average_efficacy = np.mean(efficacy_scores)
        if average_efficacy >= 0.75:  # Suponha que a eficácia seja medida numa escala de 0 a 1
            controls_evaluation[control] = 'Eficaz'
        elif average_efficacy >= 0.5:
            controls_evaluation[control] = 'Necessita de atenção'
        else:
            controls_evaluation[control] = 'Ineficaz'
    return controls_evaluation

def sidebar(unit_selection):
    st.sidebar.title("Opções de Visualização")
    
    if unit_selection == 'Unidade de Varejo':
        chart_options_risk = [
            "Risco de Crédito",
            "Risco Operacional",
            "Risco de Reputação"
        ]
    
        chart_options_control = [
            "Controles de Crédito",
            "Controles Operacionais",
            "Controles de Reputação"
        ]

    elif unit_selection == 'Unidade Investimentos':
        chart_options_risk = [
            "Risco de Mercado",
            "Risco de Crédito",
            "Risco de Liquidez"
        ]

        chart_options_control = [
            "Controles de Investimentos",
            "Controles de Crédito",
            "Controles de Liquidez"
        ]

    selected_charts_risk = st.sidebar.multiselect("Escolha os gráficos de Risco", chart_options_risk, default=chart_options_risk)

    selected_charts_control = st.sidebar.multiselect("Escolha os gráficos de Controle", chart_options_control, default=chart_options_control)

    selected_charts = selected_charts_risk + selected_charts_control

    return selected_charts

def plot_selected_charts(selected_charts, unit_selection):

    if unit_selection == 'Unidade de Varejo':
        # Gerar os dados
        credit_risk_data, operational_risk_data, reputation_risk_data = simulate_risk_data(unit_selection)
        credit_controls_data, operational_controls_data, reputation_controls_data = simulate_controls_data(unit_selection)

        st.title("Riscos")

        # Gráfico de inadimplência de empréstimos
        if "Risco de Crédito" in selected_charts:
            # Configurar o modelo de Suavização Exponencial
            model = ExponentialSmoothing(credit_risk_data['Taxa de Inadimplência (%)'], trend='add', seasonal=None, seasonal_periods=12)
            # Treinar o modelo
            model_fit = model.fit()
            # Fazer previsões
            prediction_len = 12  # por exemplo, prever os próximos 12 meses
            forecast = model_fit.forecast(prediction_len)
            
            # Preparar os dados para a previsão
            last_point = credit_risk_data.iloc[-1]  # último ponto do conjunto de dados histórico
            future_dates = pd.date_range(start=credit_risk_data['Mês'].iloc[-2], periods=prediction_len + 1, freq='M')[1:]
            forecast_df = pd.DataFrame({'Mês': future_dates, 'Taxa de Default Prevista (%)': forecast}).reset_index(drop=True)
            forecast_df.iloc[0, forecast_df.columns.get_loc('Taxa de Default Prevista (%)')] = last_point['Taxa de Inadimplência (%)']
            
            # Gerar o gráfico de linha com Plotly Express
            fig_credit = px.line(credit_risk_data, x='Mês', y='Taxa de Inadimplência (%)', title='Taxa de Inadimplência ao Longo do Tempo')
            
            # Adicionar a previsão de ES ao gráfico
            fig_credit.add_scatter(x=forecast_df['Mês'], y=forecast_df['Taxa de Default Prevista (%)'], mode='lines', name='Previsão',
                                   line=dict(color='red', dash='dash'))
            
            # Mostrar o gráfico no Streamlit
            st.plotly_chart(fig_credit)
            
        # Gráfico de fraudes operacionais
        if "Risco Operacional" in selected_charts:
            #st.subheader("Risco Operacional: Fraudes e Falhas de Segurança Cibernética")
            fig_operational = px.bar(operational_risk_data, x='Mês', y=['Fraudes', 'Incidentes Cibernéticos'],
                                    title='Incidentes de Fraudes e Segurança Cibernética')
            fig_operational.update_layout(
                                    yaxis_title='Valor em %',
                                )
            st.plotly_chart(fig_operational)

        # Gráfico de satisfação do cliente
        if "Risco de Reputação" in selected_charts:
            #st.subheader("Risco de Reputação: Satisfação do Cliente")
            fig_reputation = px.bar(reputation_risk_data, x='Mês', y='Índice de Satisfação do Cliente (%)',
                                    title='Satisfação do Cliente ao Longo do Tempo')
            st.plotly_chart(fig_reputation)
        
        st.title("Controles")

        # Gráfico para controles de crédito
        if "Controles de Crédito" in selected_charts:
            #st.subheader("Controles de Crédito: Utilização dos Limites de Empréstimo")
            fig_credit_controls = px.bar(credit_controls_data, x='Mês', y=['Utilização do Limite de Crédito',
                                                                            'Empreśtimos Acimo do Limite'],
                                        labels={
                                            'Utilização do Limite de Crédito': 'Utilização (%)',
                                            'Empréstimos Acima do Limite': 'Valor dos Excessos'
                                        },
                                        title='Utilização dos Limites de Empréstimo e Excessos',)
            
            fig_credit_controls.update_layout(
                                                yaxis_title='Valor em %',
                                            )
            st.plotly_chart(fig_credit_controls)

        # Gráfico para controles operacionais
        if "Controles Operacionais" in selected_charts:
            #st.subheader("Controles Operacionais: Eficácia dos Sistemas Anti-Fraude")
            fig_operational_controls = px.bar(operational_controls_data, x='Mês', y=['Taxa de Detecção de Fraudes (%)', 'Taxa de Prevenção de Fraudes (%)'],
                                            title='Desempenho dos Sistemas Anti-Fraude', barmode='group')
            
            fig_operational_controls.update_layout(
                                                yaxis_title='Valor em %',
                                            )

            st.plotly_chart(fig_operational_controls)

        # Gráfico para controles de reputação
        if "Controles de Reputação" in selected_charts:
            #st.subheader("Controles de Reputação: Atendimento ao Cliente")
            fig_reputation_controls = px.bar(reputation_controls_data, x='Mês', y=['Avaliação do Cliente', 'Tempo de Resposta'],
                                            title='Avaliação do Atendimento ao Cliente e Tempo de Resposta')
            fig_reputation_controls.update_layout(
                                                yaxis_title='Valor em %',
                                            )
            st.plotly_chart(fig_reputation_controls)

    elif unit_selection == 'Unidade Investimentos':
        # Gerar os dados
        market_risk_data, credit_risk_data, liquidity_risk_data = simulate_risk_data(unit_selection)
        investment_policy_data, credit_analysis_data, liquidity_plan_data = simulate_controls_data(unit_selection)

        st.title("Riscos")

        # Gráfico de Risco de Mercado
        if "Risco de Mercado" in selected_charts:
        # Configurar o modelo de Suavização Exponencial para a flutuação de preços de mercado
            model_market_risk = ExponentialSmoothing(market_risk_data['Variação do Preço de Mercado (%)'], trend='add', seasonal=None, seasonal_periods=12)
            # Treinar o modelo
            model_market_risk_fit = model_market_risk.fit()
            # Fazer previsões
            prediction_len = 12  # por exemplo, prever os próximos 12 meses para flutuações de preço de mercado
            market_forecast = model_market_risk_fit.forecast(prediction_len)
            
            # Preparar os dados para a previsão
            last_market_data_point = market_risk_data.iloc[-1]  # último ponto do conjunto de dados histórico
            future_market_dates = pd.date_range(start=market_risk_data['Mês'].iloc[-2], periods=prediction_len + 1, freq='M')[1:]
            market_forecast_df = pd.DataFrame({'Mês': future_market_dates, 'Flutuação de Preço Prevista': market_forecast}).reset_index(drop=True)
            market_forecast_df.iloc[0, market_forecast_df.columns.get_loc('Flutuação de Preço Prevista')] = last_market_data_point['Variação do Preço de Mercado (%)']
            
            # Gerar o gráfico de linha com Plotly Express para risco de mercado
            fig_market_risk = px.line(market_risk_data, x='Mês', y='Variação do Preço de Mercado (%)', title='Flutuações de Preço dos Investimentos ao Longo do Tempo')
            
            # Adicionar a previsão de ES ao gráfico de risco de mercado
            fig_market_risk.add_scatter(x=market_forecast_df['Mês'], y=market_forecast_df['Flutuação de Preço Prevista'], mode='lines', name='Previsão', line=dict(color='red', dash='dash'))
            
            # Mostrar o gráfico no Streamlit
            st.plotly_chart(fig_market_risk)

        # Gráfico de Risco de Crédito
        if "Risco de Crédito" in selected_charts:
            #st.subheader("Risco de Crédito: Falhas de Contraparte")
            fig_credit_risk = px.bar(credit_risk_data, x='Mês', y='Falhas da contraparte',
                                    title='Falhas de Contraparte ao Longo do Tempo')
            st.plotly_chart(fig_credit_risk)

        # Gráfico de Risco de Liquidez
        if "Risco de Liquidez" in selected_charts:
            #st.subheader("Risco de Liquidez: Razão de Liquidez de Ativos")
            fig_liquidity_risk = px.bar(liquidity_risk_data, x='Mês', y='Taxa de Liquidez de Ativos',
                                        title='Razão de Liquidez dos Ativos ao Longo do Tempo')
            st.plotly_chart(fig_liquidity_risk)

        st.title("Controle")

        # Gráfico para controles de investimentos
        if "Controles de Investimentos" in selected_charts:
            #st.subheader("Controles de Investimentos: Conformidade com a Política de Investimentos")
            fig_investment_controls = px.line(investment_policy_data, x='Mês', y='Conformidade com a Política de Investimento',
                                            title='Conformidade com a Política de Investimentos ao Longo do Tempo')
            st.plotly_chart(fig_investment_controls)

        # Gráfico para controles de crédito
        if "Controles de Crédito" in selected_charts:
            #st.subheader("Controles de Crédito: Avaliação de Risco de Crédito")
            fig_credit_controls = px.line(credit_analysis_data, x='Mês', y='Score de risco de crédito',
                                            title='Avaliação de Risco de Crédito ao Longo do Tempo')
            st.plotly_chart(fig_credit_controls)

        # Gráfico para controles de liquidez
        if "Controles de Liquidez" in selected_charts:
            #st.subheader("Controles de Liquidez: Força do Plano de Contingência de Liquidez")
            fig_liquidity_controls = px.line(liquidity_plan_data, x='Mês', y='Força do Plano de Contingência de Liquidez',
                                            title='Força do Plano de Contingência de Liquidez ao Longo do Tempo')
            st.plotly_chart(fig_liquidity_controls)

    return None

def create_dashboard():
    unit_selection = st.selectbox("Escolha a Unidade do Banco:",
                                  ('Unidade de Varejo', 'Unidade Investimentos'),
                                  placeholder='Unidade de Varejo')

    st.markdown("Os dados são gerados aleatoriamente para fins de demonstração.")

    st.title("Dashborad Riscos e Controles - " + unit_selection)

    # Obter dados de controle
    controls_data = simulate_controls_data_resume(unit_selection)

    # Incluir a função de visão geral no dashboard existente
    create_controls_overview(controls_data, unit_selection) 

    selected_charts = sidebar(unit_selection)
    plot_selected_charts(selected_charts, unit_selection)

# Executar a função para criar o dashboard
create_dashboard()