# Pitao Cocijo

Lluvia diaria y acumulada en San Pablo Villa de Mitla, Oaxaca.

![actions](https://github.com/mvillasante/pitao_cocijo/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/mvillasante/pitao_cocijo)
![languages](https://img.shields.io/github/languages/top/mvillasante/pitao_cocijo)
![commits](https://img.shields.io/github/commit-activity/y/mvillasante/pitao_cocijo)
[![codecov](https://codecov.io/gh/mvillasante/pitao_cocijo/graph/badge.svg)](https://codecov.io/gh/mvillasante/pitao_cocijo)



- **Lluvia diaria**: los milímetros que cayeron cada día, agrupados por año.
![Lluvia diaria](lluvia_diaria.png)

- **Lluvia acumulada**: la suma de la lluvia a lo largo de cada año.
![Lluvia acumulada](lluvia_acumulada.png)


Cada color representa un año distinto. La primera gráfica muestra los días con lluvia; la segunda, cuánto se ha acumulado durante el año en curso hasta la fecha.

## Resumen de cinco números

| Estadístico | Lluvia (mm) |
| --- | ---: |
| Mínimo | {{min}} |
| Cuartil 1 (25%) | {{q1}} |
| Mediana | {{median}} |
| Cuartil 3 (75%) | {{q3}} |
| Máximo | {{max}} |

El resumen de cinco números es un conjunto de estadísticas descriptivas que aporta información sobre un conjunto de datos. Consta de los cinco [percentiles](https://en.wikipedia.org/wiki/Percentile) más importantes:
- el mínimo muestral (la observación más pequeña)
- el [cuartil](https://en.wikipedia.org/wiki/Quartile) inferior o primer cuartil
- la [mediana](https://en.wikipedia.org/wiki/Median) (el valor central)
- el cuartil superior o tercer cuartil
- el máximo muestral (la observación más grande)


## Antes de empezar

Necesitas Docker. Si prefieres no usar Docker, necesitas Python 3.9 o superior.

## Ejecutar el proyecto

Con Docker, para regenerar las gráficas:

```
docker compose build main
docker compose run --rm main cocijo write-daily-rain-plot --data-path data/registro_lluvias.csv --output-path lluvia_diaria.png
docker compose run --rm main cocijo write-cumulative-rain-plot --data-path data/registro_lluvias.csv --output-path lluvia_acumulada.png
```

Para ver la versión web:

```
docker compose up streamlit
```

y abre <http://localhost:8501>.

Sin Docker:

```
pip install --editable .
cocijo write-daily-rain-plot --data-path data/registro_lluvias.csv --output-path lluvia_diaria.png
cocijo write-cumulative-rain-plot --data-path data/registro_lluvias.csv --output-path lluvia_acumulada.png
```
