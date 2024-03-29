import pandas as pd
import yfinance as yf
import os

lista = ['ABEV3.SA', 'ALPA4.SA','AMER3.SA','ARZZ3.SA','ASAI3.SA',
            'AZUL4.SA','B3SA3.SA','BBAS3.SA','BBDC4.SA','BBSE3.SA',
            'BEEF3.SA','BPAC11.SA','BPAN4.SA','BRAP4.SA','BRFS3.SA',
            'BRKM5.SA','BRML3.SA','CASH3.SA','CCRO3.SA','CIEL3.SA',
            'CMIG4.SA','CMIN3.SA','COGN3.SA','CPFE3.SA','CPLE6.SA',
            'CRFB3.SA','CSNA3.SA','CVCB3.SA','CYRE3.SA','DXCO3.SA',
            'ECOR3.SA','EGIE3.SA','ELET3.SA','ELET6.SA','EMBR3.SA',
            'ENBR3.SA','ENGI11.SA','EQTL3.SA','EZTC3.SA','FLRY3.SA',
            'GGBR4.SA','GOAU4.SA','GOLL4.SA','HAPV3.SA','HYPE3.SA',
            'IGTI11.SA','ITSA4.SA','ITUB4.SA','JBSS3.SA','KLBN11.SA',
            'LREN3.SA','LWSA3.SA','MGLU3.SA','MRFG3.SA','MRVE3.SA',
            'MULT3.SA','NTCO3.SA','PCAR3.SA','PETR3.SA','PETR4.SA',
            'PETZ3.SA','PRIO3.SA','QUAL3.SA','RADL3.SA','RAIL3.SA',
            'RAIZ4.SA','RDOR3.SA','RENT3.SA','RRRP3.SA','SANB11.SA',
            'SBSP3.SA','SLCE3.SA','SMTO3.SA','SOMA3.SA','SUZB3.SA',
            'TAEE11.SA','TIMS3.SA','TOTS3.SA','UGPA3.SA','USIM5.SA',
            'VALE3.SA','VBBR3.SA','VIIA3.SA','VIVT3.SA','WEGE3.SA',
            'YDUQ3.SA']    

for i in lista:
        acao = yf.Tickers(lista).history(period='5y')

fechamento = acao['Close']
dividendos = acao['Dividends']
alta = acao['High']
baixa = acao['Low']
abertura = acao['Open']
divisao_acoes = acao['Stock Splits']
volume = acao['Volume']

with pd.ExcelWriter('ibovespa-stock.xlsx') as writer:
    fechamento.to_excel(writer, sheet_name='fechamento')
    dividendos.to_excel(writer, sheet_name='dividendos')
    alta.to_excel(writer, sheet_name='alta')
    baixa.to_excel(writer, sheet_name='baixa')
    abertura.to_excel(writer, sheet_name='abertura')
    divisao_acoes.to_excel(writer, sheet_name='divisao-acoes')
    volume.to_excel(writer, sheet_name='volume')    

