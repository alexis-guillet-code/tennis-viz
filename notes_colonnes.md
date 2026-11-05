markdown
# Notes : colonnes TML-Database (matchs ATP 2025)

## Tournoi
- tourney_name, surface, draw_size, tourney_level (G=Grand Chelem, A=ATP, D=Davis, F=Masters/Finals)
- tourney_date : format AAAAMMJJ (ex. 20250113)

## Joueurs (winner_ = gagnant, loser_ = perdant)
- name, rank, rank_points, hand (R/L), ht (taille cm), ioc (pays), age

## Match
- score (abandon = "RET"), best_of (3 ou 5), round (R32, QF, F...), minutes

## Stats de service (w_ = gagnant, l_ = perdant)
- ace, df (doubles fautes), svpt (points au service), 1stIn, 1stWon, 2ndWon
- SvGms (jeux de service), bpSaved / bpFaced (balles de break sauvées / affrontées)

## Ce que j'observe
- 2 944 matchs ATP en 2025
- Surfaces : Hard 1 860 (63 %), Clay 787 (27 %), Grass 297 (10 %)
- 193 matchs (~6,6 %) sans stats de service : à exclure des analyses de service

## Questions que je pourrais poser à ces données
1. Le % de 1res balles prédit-il la victoire sur terre ?
2. Les gauchers gagnent-ils plus souvent sur gazon ?
3. Les matchs en 5 sets favorisent-ils le mieux classé ?