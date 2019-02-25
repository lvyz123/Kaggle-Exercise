# Exercise 1
pd.set_option('max_columns', None)
pokemon = pd.read_csv("../input/pokemon/pokemon.csv")
pokemon.head(3)

pokemon['type1'].value_counts().plot.bar()

pokemon['hp'].value_counts().sort_index().plot.line()

pokemon['weight_kg'].plot.hist()

# Exercise 2
pokemon = pd.read_csv("../input/pokemon/Pokemon.csv", index_col=0)
pokemon.head()

pokemon.plot.scatter(x='Attack', y='Defense')

pokemon.plot.hexbin(x='Attack', y='Defense', gridsize=15)

pokemon_stats_legendary = pokemon.groupby(['Legendary', 'Generation']).mean()[['Attack', 'Defense']]

pokemon_stats_legendary.plot.bar(stacked=True)

pokemon_stats_by_generation = pokemon.groupby('Generation').mean()[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]

pokemon_stats_by_generation.plot.line()

# Exercise 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pokemon = pd.read_csv("../input/pokemon/Pokemon.csv")
pokemon.head(3)

pokemon.plot.scatter(x='Attack', y='Defense',
                     figsize=(12, 6),
                     title='Pokemon by Attack and Defense')
                     
ax = pokemon['Total'].plot.hist(
    figsize=(12, 6),
    fontsize=14,
    bins=50,
    color='gray'
)
ax.set_title('Pokemon by Stat Total', fontsize=20)

ax = pokemon['Type 1'].value_counts().plot.bar(
    figsize=(12, 6),
    fontsize=14
)
ax.set_title("Pokemon by Primary Type", fontsize=20)
sns.despine(bottom=True, left=True)

# Exercise 4
import pandas as pd
import matplotlib.pyplot as plt
pokemon = pd.read_csv("../input/pokemon/Pokemon.csv")
pokemon.head(3)

plt.subplots(2, 1, figsize=(8, 8))

fig, axarr = plt.subplots(2, 1, figsize=(8, 8))
pokemon['Attack'].plot.hist(ax=axarr[0], title='Pokemon Attack Ratings')
pokemon['Defense'].plot.hist(ax=axarr[1], title='Pokemon Defense Ratings')

# Exercise 5
pokemon = pd.read_csv("../input/pokemon/Pokemon.csv", index_col=0)
pokemon.head()

sns.countplot(pokemon['Generation'])

sns.distplot(pokemon['HP'])

sns.jointplot(x='Attack', y='Defense', data=pokemon)

sns.jointplot(x='Attack', y='Defense', data=pokemon, kind='hex')

sns.kdeplot(pokemon['HP'], pokemon['Attack'])

sns.boxplot(x='Legendary', y='Attack', data=pokemon)

sns.violinplot(x='Legendary', y='Attack', data=pokemon)

# Exercise 6
import pandas as pd
import seaborn as sns

pokemon = pd.read_csv("../input/pokemon/Pokemon.csv", index_col=0)
pokemon.head(3)

g = sns.FacetGrid(pokemon, row="Legendary")
g.map(sns.kdeplot, "Attack")

g = sns.FacetGrid(pokemon, col="Legendary", row="Generation")
g.map(sns.kdeplot, "Attack")

sns.pairplot(pokemon[['HP', 'Attack', 'Defense']])

# Exercise 7
pokemon = pd.read_csv("../input/pokemon/Pokemon.csv", index_col=0)
pokemon.head()

import seaborn as sns

sns.lmplot(x='Attack', y='Defense', hue='Legendary', 
           markers=['x', 'o'],
           fit_reg=False, data=pokemon)
           
sns.boxplot(x="Generation", y="Total", hue='Legendary', data=pokemon)

sns.heatmap(
    pokemon.loc[:, ['HP', 'Attack', 'Sp. Atk', 'Defense', 'Sp. Def', 'Speed']].corr(),
    annot=True
)

import pandas as pd
from pandas.plotting import parallel_coordinates

p = (pokemon[(pokemon['Type 1'].isin(["Psychic", "Fighting"]))]
         .loc[:, ['Type 1', 'Attack', 'Sp. Atk', 'Defense', 'Sp. Def']]
    )

parallel_coordinates(p, 'Type 1')
