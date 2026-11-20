import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

données['chiffre_affaires'] = données['prix'] * données['qte']
ventes_par_produit = données.groupby('produit', as_index=False)['qte'].sum()
ventes_par_produit = ventes_par_produit.sort_values('qte', ascending=False)

figure_ventes_produit = px.bar(
    ventes_par_produit,
    x='produit',
    y='qte',
    text='qte',
    title='Ventes par produit',
    labels={'produit': 'Produit', 'qte': 'Quantité vendue'},
)
figure_ventes_produit.update_traces(textposition='outside')
figure_ventes_produit.update_layout(template='plotly_white', uniformtext_minsize=10)
figure_ventes_produit.write_html('ventes-par-produit.html')

ca_par_produit = données.groupby('produit', as_index=False)['chiffre_affaires'].sum()
ca_par_produit = ca_par_produit.sort_values('chiffre_affaires', ascending=False)

figure_ca_produit = px.bar(
    ca_par_produit,
    x='produit',
    y='chiffre_affaires',
    text='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    labels={'produit': 'Produit', 'chiffre_affaires': "Chiffre d'affaires"},
)
figure_ca_produit.update_traces(texttemplate='€%{text:,.0f}', textposition='outside')
figure_ca_produit.update_layout(template='plotly_white', uniformtext_minsize=10)
figure_ca_produit.write_html('chiffre-affaires-par-produit.html')

print('Les trois graphiques ont été générés avec succès !')
