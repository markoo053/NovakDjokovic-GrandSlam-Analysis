# Mitnop projekat --> Marko Stjepanovic IN59-2020


# %% Biblioteke

import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


# %% Ucitavanje i uredjivanje podataka

folder_name = "datasets"

dataframes = []

for file in os.listdir(folder_name):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_name, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)

all_matches = pd.concat(dataframes, ignore_index=True)

# Izdvajam sve Grand Slam turnire
grand_slam_matches = all_matches.loc[all_matches['tourney_level'] == 'G']

# Dodajem novu kolonu za godinu
grand_slam_matches['tourney_year'] = grand_slam_matches.tourney_date.astype(str).str[:4]
grand_slam_matches['tourney_year'] = grand_slam_matches['tourney_year'].astype(int)

# Izdvajam sve GS meceve koje je igrao
djokovic_GS_matches = grand_slam_matches.loc[
   (grand_slam_matches['winner_name'] == 'Novak Djokovic') | (grand_slam_matches['loser_name'] == 'Novak Djokovic')]

# Izdvajam sve meceve koje je dobio i izgubio
djokovic_W_matches = grand_slam_matches.loc[grand_slam_matches['winner_name'] == 'Novak Djokovic']
djokovic_L_matches = grand_slam_matches.loc[grand_slam_matches['loser_name'] == 'Novak Djokovic']

# Izdvajam sve meceve koje je dobio i izgubio na svakom GS pojedinacno
djokovic_W_AO_matches = grand_slam_matches.loc[
                            (grand_slam_matches['winner_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'Australian Open')]

djokovic_L_AO_matches = grand_slam_matches.loc[
                            (grand_slam_matches['loser_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'Australian Open')]

djokovic_W_RG_matches = grand_slam_matches.loc[
                            (grand_slam_matches['winner_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'Roland Garros')]

djokovic_L_RG_matches = grand_slam_matches.loc[
                            (grand_slam_matches['loser_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'Roland Garros')]

djokovic_W_wimbledon_matches = grand_slam_matches.loc[
                            (grand_slam_matches['winner_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'Wimbledon')]

djokovic_L_wimbledon_matches = grand_slam_matches.loc[
                            (grand_slam_matches['loser_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'Wimbledon')]

djokovic_W_US_matches = grand_slam_matches.loc[
                            (grand_slam_matches['winner_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'US Open')]

djokovic_L_US_matches = grand_slam_matches.loc[
                            (grand_slam_matches['loser_name'] == 'Novak Djokovic') & 
                            (grand_slam_matches['tourney_name'] == 'US Open')]

# Izdvajam sve meceve koje je igrao na Australian Open,Roland Garros,Wimbledon i US Open
djokovic_AO_matches = djokovic_GS_matches[(djokovic_GS_matches['tourney_name'] == 'Australian Open')]
djokovic_RG_matches = djokovic_GS_matches[(djokovic_GS_matches['tourney_name'] == 'Roland Garros')]
djokovic_wimbledon_matches = djokovic_GS_matches[(djokovic_GS_matches['tourney_name'] == 'Wimbledon')]
djokovic_US_matches = djokovic_GS_matches[(djokovic_GS_matches['tourney_name'] == 'US Open')]
   

# %% Ukupan broj osvojenih i izgubljenih meceva na Grand Slam turnirima

colors = ['cornflowerblue', 'lightcoral']

fig = plt.figure(figsize=(8,6))
plt.title("Omjer dobijenih i izgubljenih meceva na GS turnirima", fontweight='bold', fontsize=15)
plt.pie([len(djokovic_W_matches),len(djokovic_L_matches)],labels = [f'{len(djokovic_W_matches)} dobijenih',f'{len(djokovic_L_matches)} izgubljenih'],textprops={'fontsize': 20}, colors=colors)
plt.show()


# %% Ukupan broj osvojenih Australian Open titula - po godinama


AO_wins = djokovic_GS_matches[
        (djokovic_GS_matches['tourney_name'] == 'Australian Open') &
        (djokovic_GS_matches['winner_name'] == 'Novak Djokovic') &
        (djokovic_GS_matches['round'] == 'F')]

po_godinama = AO_wins.groupby('tourney_year').size()

plt.figure(figsize=(12, 6))
plt.plot(po_godinama.index,po_godinama.values, marker='o', markersize=12, color='b')
plt.title('Broj osvojenih Australian Open titula', fontweight='bold', fontsize=15)
plt.xticks(po_godinama.index, rotation=45, fontsize=15)
plt.yticks([])
plt.grid(True)
plt.show()

# %% Ukupan broj osvojenih Roland Garros titula - po godinama

RG_wins = djokovic_GS_matches[
        (djokovic_GS_matches['tourney_name'] == 'Roland Garros') &
        (djokovic_GS_matches['winner_name'] == 'Novak Djokovic') &
        (djokovic_GS_matches['round'] == 'F')]

po_godinama = RG_wins.groupby('tourney_year').size()

plt.figure(figsize=(12, 6))
plt.plot(po_godinama.index,po_godinama.values, marker='D', markersize=12, color='orange')
plt.title('Broj osvojenih Roland Garros titula', fontweight='bold', fontsize=15)
plt.xticks(po_godinama.index, rotation=0, fontsize=15)
plt.yticks([])
plt.grid(True)
plt.show()


# %% Ukupan broj osvojenih Wimbledon tituala - po godinama

wimbledon_wins = djokovic_GS_matches[
        (djokovic_GS_matches['tourney_name'] == 'Wimbledon') &
        (djokovic_GS_matches['winner_name'] == 'Novak Djokovic') &
        (djokovic_GS_matches['round'] == 'F')]

po_godinama = wimbledon_wins.groupby('tourney_year').size()

plt.figure(figsize=(12, 6))
plt.plot(po_godinama.index,po_godinama.values, marker='s', markersize=12, color='green')
plt.title('Broj osvojenih Wimbledon titula', fontweight='bold', fontsize=15)
plt.xticks(po_godinama.index, rotation=45, fontsize=15)
plt.yticks([])
plt.grid(True)
plt.show()


# %% Ukupan broj osvojenih US Open titula - po godinama

US_wins = djokovic_GS_matches[
        (djokovic_GS_matches['tourney_name'] == 'US Open') &
        (djokovic_GS_matches['winner_name'] == 'Novak Djokovic') &
        (djokovic_GS_matches['round'] == 'F')]

po_godinama = US_wins.groupby('tourney_year').size()

plt.figure(figsize=(12, 6))
plt.plot(po_godinama.index,po_godinama.values, marker='x', markersize=15, color='cornflowerblue')
plt.title('Broj osvojenih US Open titula', fontweight='bold', fontsize=15)
plt.xticks(po_godinama.index, rotation=45, fontsize=15)
plt.yticks([])
plt.grid(True)
plt.show()


# %% Najjefikasnije podloge

pobjede = djokovic_GS_matches[djokovic_GS_matches['winner_name'] == 'Novak Djokovic']
pobjede_podloge_godine = pobjede.groupby(['tourney_year', 'surface']).size().reset_index(name='Broj pobjeda')

plt.figure(figsize=(12, 6))
colors = {'Grass': 'green', 'Hard': 'cornflowerblue', 'Clay': 'orange'}
sns.stripplot(data=pobjede_podloge_godine, x='tourney_year', y='Broj pobjeda', hue='surface', dodge=True, palette=colors, jitter=True, size=12)
plt.title('Efikasnost Djokovica na podlogama', fontweight='bold', fontsize=15)
plt.grid(axis='y', linestyle='--', alpha=0.8)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title='Podloga', title_fontsize='large', loc='upper left')
plt.xticks(rotation=45, fontsize=15)
plt.show()


# %% Prosjecna duzina meceva (u minutama) Djokovica na GS

prosjecna_duzina_meceva = djokovic_GS_matches.groupby('tourney_name')['minutes'].mean().reset_index()
print(prosjecna_duzina_meceva)

plt.figure(figsize=(12, 6))
sns.swarmplot(data=djokovic_GS_matches, x='tourney_name', y='minutes', palette='Set2', size=9)
sns.pointplot(data=prosjecna_duzina_meceva, x='tourney_name', y='minutes', color='black', markers='o', scale=0, ci=None)

plt.xticks(rotation=0, fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.title('Prosjecna duzina meceva - u minutama', fontweight='bold', fontsize=15)

for i in range(prosjecna_duzina_meceva.shape[0]):
    plt.text(i, prosjecna_duzina_meceva.iloc[i]['minutes'] + 5, f"{prosjecna_duzina_meceva.iloc[i]['minutes']:.2f}",
             ha='center', va='center', fontsize=20, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# %% Ukupan broj asova po GS

djokovic_wins_aces = djokovic_W_matches.groupby('tourney_name')['w_ace'].sum().reset_index()
djokovic_loses_aces = djokovic_L_matches.groupby('tourney_name')['l_ace'].sum().reset_index()

djokovic_total_aces = pd.concat([djokovic_wins_aces, djokovic_loses_aces], ignore_index=True)
djokovic_total_aces['total_aces'] = djokovic_total_aces['w_ace'].fillna(0) + djokovic_total_aces['l_ace'].fillna(0)

djokovic_total_aces.sort_values(by='total_aces', ascending=False, inplace=True)

plt.figure(figsize=(12, 6))
plt.barh(djokovic_total_aces['tourney_name'], djokovic_total_aces['total_aces'], color='cornflowerblue', linewidth=0.01)

plt.title('Broj asova', fontweight='bold', fontsize=15)
plt.show()

# %% Ukupan broj duplih servis gresaka po GS

djokovic_wins_df = djokovic_W_matches.groupby('tourney_name')['w_df'].sum().reset_index()
djokovic_losses_df = djokovic_L_matches.groupby('tourney_name')['l_df'].sum().reset_index()

djokovic_total_df = pd.concat([djokovic_wins_df, djokovic_losses_df], ignore_index=True)
djokovic_total_df['total_df'] = djokovic_total_df['w_df'].fillna(0) + djokovic_total_df['l_df'].fillna(0)

djokovic_total_df.sort_values(by='total_df', ascending=False, inplace=True)

plt.figure(figsize=(12, 6))
plt.barh(djokovic_total_df['tourney_name'], djokovic_total_df['total_df'], color='#FF5252', linewidth=0.01)

plt.title('Broj duplih servis gresaka', fontweight='bold', fontsize=15)
plt.show()


# %% Odnos procenata asova i duplih servis gresaka na Australian Open - po godinama

br_asova = djokovic_W_AO_matches.groupby('tourney_year')['w_ace'].sum() + djokovic_L_AO_matches.groupby('tourney_year')['l_ace'].sum()
br_duplih_gresaka = djokovic_W_AO_matches.groupby('tourney_year')['w_df'].sum() + djokovic_L_AO_matches.groupby('tourney_year')['l_df'].sum()

ukupno_svpt = djokovic_W_AO_matches.groupby('tourney_year')['w_svpt'].sum() + djokovic_L_AO_matches.groupby('tourney_year')['l_svpt'].sum()

procenat_asova = (br_asova / ukupno_svpt) * 100
procenat_duplih_gresaka = (br_duplih_gresaka / ukupno_svpt) * 100

plt.figure(figsize=(12, 6))
sns.lineplot(x=djokovic_W_AO_matches['tourney_year'].unique(), y=procenat_asova, marker='o', label='Procenat asova', color='cornflowerblue')
sns.lineplot(x=djokovic_W_AO_matches['tourney_year'].unique(), y=procenat_duplih_gresaka, marker='o', label='Procenat duplih servis gresaka', color='#FF5252')

plt.title('Odnos procenata asova i duplih servis gresaka na Australian Open', fontweight='bold', fontsize=15)
plt.legend()
plt.xticks(fontsize=15)
plt.grid(True)
plt.show()


# %% Odnos procenata asova i duplih servis gresaka na Roland Garros - po godinama

br_asova = djokovic_W_RG_matches.groupby('tourney_year')['w_ace'].sum() + djokovic_L_RG_matches.groupby('tourney_year')['l_ace'].sum()
br_duplih_gresaka = djokovic_W_RG_matches.groupby('tourney_year')['w_df'].sum() + djokovic_L_RG_matches.groupby('tourney_year')['l_df'].sum()

ukupno_svpt = djokovic_W_RG_matches.groupby('tourney_year')['w_svpt'].sum() + djokovic_L_RG_matches.groupby('tourney_year')['l_svpt'].sum()

procenat_asova = (br_asova / ukupno_svpt) * 100
procenat_duplih_gresaka = (br_duplih_gresaka / ukupno_svpt) * 100

plt.figure(figsize=(12, 6))
sns.lineplot(x=djokovic_W_RG_matches['tourney_year'].unique(), y=procenat_asova, marker='o', label='Procenat asova', color='cornflowerblue')
sns.lineplot(x=djokovic_W_RG_matches['tourney_year'].unique(), y=procenat_duplih_gresaka, marker='o', label='Procenat duplih servis gresaka', color='#FF5252')

plt.title('Odnos procenata asova i duplih servis gresaka na Roland Garros', fontweight='bold', fontsize=15)
plt.legend()
plt.xticks(fontsize=15)
plt.grid(True)
plt.show()


# %% Odnos procenata asova i duplih servis gresaka na Wimbledon - po godinama

br_asova = djokovic_W_wimbledon_matches.groupby('tourney_year')['w_ace'].sum() + djokovic_L_wimbledon_matches.groupby('tourney_year')['l_ace'].sum()
br_duplih_gresaka = djokovic_W_wimbledon_matches.groupby('tourney_year')['w_df'].sum() + djokovic_L_wimbledon_matches.groupby('tourney_year')['l_df'].sum()

ukupno_svpt = djokovic_W_wimbledon_matches.groupby('tourney_year')['w_svpt'].sum() + djokovic_L_wimbledon_matches.groupby('tourney_year')['l_svpt'].sum()

procenat_asova = (br_asova / ukupno_svpt) * 100
procenat_duplih_gresaka = (br_duplih_gresaka / ukupno_svpt) * 100

plt.figure(figsize=(12, 6))
sns.lineplot(x=djokovic_W_wimbledon_matches['tourney_year'].unique(), y=procenat_asova, marker='o', label='Procenat asova', color='cornflowerblue')
sns.lineplot(x=djokovic_W_wimbledon_matches['tourney_year'].unique(), y=procenat_duplih_gresaka, marker='o', label='Procenat duplih servis gresaka', color='#FF5252')

plt.title('Odnos procenata asova i duplih servis gresaka na Wimbledon', fontweight='bold', fontsize=15)
plt.legend()
plt.xticks(fontsize=15)
plt.grid(True)
plt.show()


# %% Odnos procenata asova i duplih servis gresaka na US Open - po godinama

br_asova = djokovic_W_US_matches.groupby('tourney_year')['w_ace'].sum() + djokovic_L_US_matches.groupby('tourney_year')['l_ace'].sum()
br_duplih_gresaka = djokovic_W_US_matches.groupby('tourney_year')['w_df'].sum() + djokovic_L_US_matches.groupby('tourney_year')['l_df'].sum()

ukupno_svpt = djokovic_W_US_matches.groupby('tourney_year')['w_svpt'].sum() + djokovic_L_US_matches.groupby('tourney_year')['l_svpt'].sum()

procenat_asova = (br_asova / ukupno_svpt) * 100
procenat_duplih_gresaka = (br_duplih_gresaka / ukupno_svpt) * 100

plt.figure(figsize=(12, 6))
sns.lineplot(x=djokovic_W_US_matches['tourney_year'].unique(), y=procenat_asova, marker='o', label='Procenat asova', color='cornflowerblue')
sns.lineplot(x=djokovic_W_US_matches['tourney_year'].unique(), y=procenat_duplih_gresaka, marker='o', label='Procenat duplih servis gresaka', color='#FF5252')

plt.title('Odnos procenata asova i duplih servis gresaka na US Open', fontweight='bold', fontsize=15)
plt.legend()
plt.xticks(fontsize=15)
plt.grid(True)
plt.show()


# %% Odnos procenata ubacenog prvog servisa i osvajanja poena na osnovu prvog servisa

djokovic_matches = pd.concat([djokovic_W_matches, djokovic_L_matches], ignore_index=True)

djokovic_matches['1stIn_perc'] = (djokovic_matches['w_1stIn'].fillna(0) + djokovic_matches['l_1stIn'].fillna(0)) / (djokovic_matches['w_svpt'].fillna(0) + djokovic_matches['l_svpt'].fillna(0)) * 100
djokovic_matches['1stWon_perc'] = (djokovic_matches['w_1stWon'].fillna(0) + djokovic_matches['l_1stWon'].fillna(0)) / (djokovic_matches['w_1stIn'].fillna(0) + djokovic_matches['l_1stIn'].fillna(0)) * 100

sns.set_theme(style="whitegrid", palette="Blues_r")
plt.figure(figsize=(12, 6))
sns.regplot(data=djokovic_matches, x='1stIn_perc', y='1stWon_perc', scatter_kws={'s': 80}, line_kws={'color': 'red'})

plt.title('Odnos prvih servisa u teren i osvojenih poena na osnovu prvog servisa', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.show()


# %% Odnos procenata osvojenih poena na drugom servisu i osvojenih servis gemova

djokovic_matches = pd.concat([djokovic_W_matches, djokovic_L_matches], ignore_index=True)

djokovic_matches['2ndWon'] = djokovic_matches['w_2ndWon'].fillna(0) + djokovic_matches['l_2ndWon'].fillna(0)
djokovic_matches['SvGms'] = djokovic_matches['w_SvGms'].fillna(0) + djokovic_matches['l_SvGms'].fillna(0)

grouped_data = djokovic_matches.groupby('tourney_name').agg({
    '2ndWon': 'sum',
    'SvGms': 'sum',
})

grouped_data['percentage_2ndWon'] = (grouped_data['2ndWon'] / grouped_data['2ndWon'].sum()) * 100
grouped_data['percentage_SvGms'] = (grouped_data['SvGms'] / grouped_data['SvGms'].sum()) * 100

sns.set(style="whitegrid", palette="Blues")
plt.figure(figsize=(12, 6))
ax = sns.kdeplot(data=grouped_data, x='percentage_2ndWon', y='percentage_SvGms', fill=True, cmap='Blues')

ax.xaxis.grid(True, linestyle='--', which='both', color='lightgrey', alpha=0.5)
ax.yaxis.grid(True, linestyle='--', which='both', color='lightgrey', alpha=0.5)

plt.title('Odnos osvojenih drugih servisa i servis gemova', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)

ax.tick_params(axis='both', which='major', labelsize=10)
plt.show()


# %% Odnos suocenih brejk lopti i spasenih brejk lopti

djokovic_matches = pd.concat([djokovic_W_matches, djokovic_L_matches], ignore_index=True)

djokovic_matches['bpFaced'] = djokovic_matches['w_bpFaced'].fillna(0) + djokovic_matches['l_bpFaced'].fillna(0)
djokovic_matches['bpSaved'] = djokovic_matches['w_bpSaved'].fillna(0) + djokovic_matches['l_bpSaved'].fillna(0)

data = djokovic_matches[['tourney_name', 'bpFaced', 'bpSaved']]

data = data.melt(id_vars='tourney_name', value_vars=['bpFaced', 'bpSaved'],
                 var_name='Brejk Lopte', value_name='Broj Lopti')

plt.figure(figsize=(12, 6))
sns.set_theme(style="darkgrid")

sns.violinplot(data=data, x='tourney_name', y='Broj Lopti', hue='Brejk Lopte', split=True, inner='quartile',
               palette={'bpFaced': 'cyan', 'bpSaved': '#fc8d59'}, linewidth=1, linewidth_scale=0.5)

sns.despine(left=True)
plt.title('Odnos suocenih i spasenih brejk lopti', fontweight='bold', fontsize=15)
plt.legend(title='Brejk Lopte', loc='center left', bbox_to_anchor=(0, 1))
plt.xticks(fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.show()


# %% Protivnici koje je Djokovic najvise pobjedjivao na GS

pobjede = djokovic_GS_matches[djokovic_GS_matches['winner_name'] == 'Novak Djokovic']
pobjede_p = pobjede['loser_name'].value_counts()

top_4 = pobjede_p.head(4)

plt.figure(figsize=(12, 6))
ax = sns.countplot(x='loser_name', data=pobjede, order=top_4.index, palette='viridis')
plt.title('Top 4 protivnika koje je Djokovic najvise puta pobjedio na Grand Slam turnirima', fontweight='bold', fontsize=15)
plt.xticks(rotation=0, fontsize=15)
plt.xlabel(None)
plt.ylabel(None)

for i in range(len(top_4)):
    plt.text(i, top_4[i]//2, str(top_4[i]), ha='center', fontweight='bold', fontsize=25)

plt.show()

# %% Poredjenje asova Djokovica i Federera

federer_W_matches = grand_slam_matches.loc[
   (grand_slam_matches['winner_name'] == 'Roger Federer')]

federer_L_matches =  grand_slam_matches.loc[
   (grand_slam_matches['loser_name'] == 'Roger Federer')]

djokovic_wins_aces = djokovic_W_matches.groupby('tourney_name')['w_ace'].sum().reset_index()
djokovic_losses_aces = djokovic_L_matches.groupby('tourney_name')['l_ace'].sum().reset_index()
djokovic_total_aces = pd.concat([djokovic_wins_aces, djokovic_losses_aces], ignore_index=True)
djokovic_total_aces['total_aces'] = djokovic_total_aces['w_ace'].fillna(0) + djokovic_total_aces['l_ace'].fillna(0)
djokovic_total_aces['player'] = 'Djokovic'

federer_wins_aces = federer_W_matches.groupby('tourney_name')['w_ace'].sum().reset_index()
federer_losses_aces = federer_L_matches.groupby('tourney_name')['l_ace'].sum().reset_index()
federer_total_aces = pd.concat([federer_wins_aces, federer_losses_aces], ignore_index=True)
federer_total_aces['total_aces'] = federer_total_aces['w_ace'].fillna(0) + federer_total_aces['l_ace'].fillna(0)
federer_total_aces['player'] = 'Federer'

total_aces = pd.concat([djokovic_total_aces, federer_total_aces], ignore_index=True)
total_aces = total_aces.groupby(['tourney_name', 'player'])['total_aces'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.stripplot(data=total_aces, x='tourney_name', y='total_aces', hue='player', palette=['cornflowerblue', 'yellowgreen'], size=14)
plt.title('Broj asova: Djokovic vs Federer', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title='Igrac', title_fontsize='large', loc='upper left')
plt.xticks(rotation=0, fontsize=15)
plt.show()


# %% Poredjenje asova Djokovica i Nadala

nadal_W_matches = grand_slam_matches.loc[
   (grand_slam_matches['winner_name'] == 'Rafael Nadal')]

nadal_L_matches =  grand_slam_matches.loc[
   (grand_slam_matches['loser_name'] == 'Rafael Nadal')]

djokovic_wins_aces = djokovic_W_matches.groupby('tourney_name')['w_ace'].sum().reset_index()
djokovic_losses_aces = djokovic_L_matches.groupby('tourney_name')['l_ace'].sum().reset_index()
djokovic_total_aces = pd.concat([djokovic_wins_aces, djokovic_losses_aces], ignore_index=True)
djokovic_total_aces['total_aces'] = djokovic_total_aces['w_ace'].fillna(0) + djokovic_total_aces['l_ace'].fillna(0)
djokovic_total_aces['player'] = 'Djokovic'

nadal_wins_aces = nadal_W_matches.groupby('tourney_name')['w_ace'].sum().reset_index()
nadal_losses_aces = nadal_L_matches.groupby('tourney_name')['l_ace'].sum().reset_index()
nadal_total_aces = pd.concat([nadal_wins_aces, nadal_losses_aces], ignore_index=True)
nadal_total_aces['total_aces'] = nadal_total_aces['w_ace'].fillna(0) + nadal_total_aces['l_ace'].fillna(0)
nadal_total_aces['player'] = 'Nadal'

total_aces = pd.concat([djokovic_total_aces, nadal_total_aces], ignore_index=True)
total_aces = total_aces.groupby(['tourney_name', 'player'])['total_aces'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.stripplot(data=total_aces, x='tourney_name', y='total_aces', hue='player', palette=['cornflowerblue', 'dimgrey'], size=14)
plt.title('Broj asova: Djokovic vs Nadal', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(loc='upper center')
plt.xticks(rotation=0, fontsize=15)
plt.show()


# %% Poredjenje duplih servis gresaka Djokovica i Federera

djokovic_wins_df = djokovic_W_matches.groupby('tourney_name')['w_df'].sum().reset_index()
djokovic_losses_df = djokovic_L_matches.groupby('tourney_name')['l_df'].sum().reset_index()
djokovic_total_df = pd.concat([djokovic_wins_df, djokovic_losses_df], ignore_index=True)
djokovic_total_df['total_df'] = djokovic_total_df['w_df'].fillna(0) + djokovic_total_df['l_df'].fillna(0)
djokovic_total_df['player'] = 'Djokovic'

federer_wins_df = federer_W_matches.groupby('tourney_name')['w_df'].sum().reset_index()
federer_losses_df = federer_L_matches.groupby('tourney_name')['l_df'].sum().reset_index()
federer_total_df = pd.concat([federer_wins_df, federer_losses_df], ignore_index=True)
federer_total_df['total_df'] = federer_total_df['w_df'].fillna(0) + federer_total_df['l_df'].fillna(0)
federer_total_df['player'] = 'Federer'

total_df = pd.concat([djokovic_total_df, federer_total_df], ignore_index=True)

plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.boxplot(data=total_df, x='tourney_name', y='total_df', hue='player', palette=['cornflowerblue', 'yellowgreen'])
plt.title('Broj duplih servis gresaka: Djokovic vs Federer', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(loc='upper right')
plt.xticks(rotation=0, fontsize=15)
plt.show()


# %% Poredjenje duplih servis gresaka Djokovica i Nadala

djokovic_wins_df = djokovic_W_matches.groupby('tourney_name')['w_df'].sum().reset_index()
djokovic_losses_df = djokovic_L_matches.groupby('tourney_name')['l_df'].sum().reset_index()
djokovic_total_df = pd.concat([djokovic_wins_df, djokovic_losses_df], ignore_index=True)
djokovic_total_df['total_df'] = djokovic_total_df['w_df'].fillna(0) + djokovic_total_df['l_df'].fillna(0)
djokovic_total_df['player'] = 'Djokovic'

nadal_wins_df = nadal_W_matches.groupby('tourney_name')['w_df'].sum().reset_index()
nadal_losses_df = nadal_L_matches.groupby('tourney_name')['l_df'].sum().reset_index()
nadal_total_df = pd.concat([nadal_wins_df, nadal_losses_df], ignore_index=True)
nadal_total_df['total_df'] = nadal_total_df['w_df'].fillna(0) + nadal_total_df['l_df'].fillna(0)
nadal_total_df['player'] = 'Nadal'

total_df = pd.concat([djokovic_total_df, nadal_total_df], ignore_index=True)

plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.boxplot(data=total_df, x='tourney_name', y='total_df', hue='player', palette=['cornflowerblue', 'dimgrey'])
plt.title('Broj duplih servis gresaka: Djokovic vs Nadal', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(loc='upper right')
plt.xticks(rotation=0, fontsize=15)
plt.show()


# %% Poredjenje spasenih brejk lopti Djokovica i Federera

djokovic_wins_bps = djokovic_W_matches.groupby('tourney_name')['w_bpSaved'].sum().reset_index()
djokovic_losses_bps = djokovic_L_matches.groupby('tourney_name')['l_bpSaved'].sum().reset_index()
djokovic_total_bps = pd.concat([djokovic_wins_bps, djokovic_losses_bps], ignore_index=True)
djokovic_total_bps['total_bps'] = djokovic_total_bps['w_bpSaved'].fillna(0) + djokovic_total_bps['l_bpSaved'].fillna(0)
djokovic_total_bps['player'] = 'Djokovic'

federer_wins_bps = federer_W_matches.groupby('tourney_name')['w_bpSaved'].sum().reset_index()
federer_losses_bps = federer_L_matches.groupby('tourney_name')['l_bpSaved'].sum().reset_index()
federer_total_bps = pd.concat([federer_wins_bps, federer_losses_bps], ignore_index=True)
federer_total_bps['total_bps'] = federer_total_bps['w_bpSaved'].fillna(0) + federer_total_bps['l_bpSaved'].fillna(0)
federer_total_bps['player'] = 'Federer'

total_bps = pd.concat([djokovic_total_bps, federer_total_bps], ignore_index=True)
total_bps = total_bps.groupby(['tourney_name', 'player'])['total_bps'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.pointplot(data=total_bps, x='tourney_name', y='total_bps', hue='player', palette=['cornflowerblue', 'yellowgreen'])
plt.title('Broj spasenih brejk lopti: Djokovic vs Federer', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(loc='upper right')
plt.xticks(rotation=0, fontsize=15)
plt.show()


# %% Poredjenje spasenih brejk lopti Djokovica i Nadala

djokovic_wins_bps = djokovic_W_matches.groupby('tourney_name')['w_bpSaved'].sum().reset_index()
djokovic_losses_bps = djokovic_L_matches.groupby('tourney_name')['l_bpSaved'].sum().reset_index()
djokovic_total_bps = pd.concat([djokovic_wins_bps, djokovic_losses_bps], ignore_index=True)
djokovic_total_bps['total_bps'] = djokovic_total_bps['w_bpSaved'].fillna(0) + djokovic_total_bps['l_bpSaved'].fillna(0)
djokovic_total_bps['player'] = 'Djokovic'

nadal_wins_bps = nadal_W_matches.groupby('tourney_name')['w_bpSaved'].sum().reset_index()
nadal_losses_bps = nadal_L_matches.groupby('tourney_name')['l_bpSaved'].sum().reset_index()
nadal_total_bps = pd.concat([nadal_wins_bps, nadal_losses_bps], ignore_index=True)
nadal_total_bps['total_bps'] = nadal_total_bps['w_bpSaved'].fillna(0) + nadal_total_bps['l_bpSaved'].fillna(0)
nadal_total_bps['player'] = 'Nadal'

total_bps = pd.concat([djokovic_total_bps, nadal_total_bps], ignore_index=True)
total_bps = total_bps.groupby(['tourney_name', 'player'])['total_bps'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.pointplot(data=total_bps, x='tourney_name', y='total_bps', hue='player', palette=['cornflowerblue', 'dimgrey'])
plt.title('Broj spasenih brejk lopti: Djokovic vs Nadal', fontweight='bold', fontsize=15)
plt.xlabel(None)
plt.ylabel(None)
plt.legend(loc='upper right')
plt.xticks(rotation=0, fontsize=15)
plt.show()






