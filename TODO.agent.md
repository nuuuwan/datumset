# TODO

## Query Language

- [ ] Add schema and query discovery APIs: list valid entity names, dim keys per entity, cell types, and valid dim values (reusing `CategoryConcept.valid_values()` and existing metadata)
- [ ] Add friendlier query validation with parse-time error messages that name the bad token and suggest corrections
- [ ] Add a fluent Python query builder so queries can be constructed programmatically instead of as raw strings
- [ ] Add derived cell type `Bottom` (min per group) alongside the existing `Top` (max per group) in `LankaDataDerivedQueryMixin`
- [ ] Add derived cell type `Rank`: for each group key, emit a numeric rank dimension value instead of filtering to the top datum
- [ ] Add derived cell type `Share`: divide each datum's `Count` by the group total, producing a `Percent` cell
- [ ] Add derived cell type `Change`: given two `Time` values in the query, compute absolute and/or percent change between them
- [ ] Add multi-value OR filter using the existing `OPR_OR` (`,`) operator so a dim spec like `Religion=buddhist,hindu` filters to multiple values at once

## Data & Cell Types

- [ ] Replace the hard-coded `_get_y_cell_key` returning `"Count"` with dynamic selection based on the query's actual cell label, so `Percent`, `Float`, and other atom types render correctly in all visuals
- [ ] Add a `Median` derived cell type that computes weighted median across dim groups
- [ ] Add support for loading a custom local JSON/CSV file as a one-off `AbstractDB` subclass so users can visualise their own data without publishing it to GitHub

## Visuals

- [ ] Add a `LineChart` visual for time-series data (x=Time, y=Count), with one line per category value
- [ ] Add a `ScatterPlot` visual that plots two cell dimensions against each other, one point per region or category
- [ ] Add a `TreeMap` visual that tiles rectangles proportional to cell value, similar to `MekkoChart` but without the stacked axis
- [ ] Add a `WaffleChart` visual that shows share as filled unit squares, one per percent
- [ ] Add a `BubbleMap` visual: draw proportional circles on a geographic basemap instead of shading polygons
- [ ] Add a `RidgePlot` visual that overlays per-category distributions along a shared axis
- [ ] Implement `SquareMap` and `UnitSquareMap` rendering (classes exist in `VisualFactory` but appear to be stubs)
- [ ] Make `Map`, `HexMap`, and `Dorling` support `Percent` and `Float` cell types with a diverging colormap when values can be negative

## Legends & Labels

- [ ] Add an optional numeric value annotation on each bar, pie slice, and map region, toggled by a Visual parameter
- [ ] Add a color-scale bar (colorbar) to `Map` and `Cartogram` visuals when in `value` color mode
- [ ] Show percentage share next to absolute count in legends when both are available

## Output & Export

- [ ] Add SVG output alongside PNG: call `fig.savefig` with `.svg` extension and expose via `VisualPathMixin`
- [ ] Add a `to_csv(path)` method on `Datumset` that writes dim columns and cell columns as flat CSV rows
- [ ] Add a `to_dataframe()` method on `Datumset` that returns a `pandas.DataFrame` with one column per dim and cell key
- [ ] Add interactive HTML export via `mpld3` or `plotly` for at least `BarChart` and `StackedBarChart`

## Cache & Data Sources

- [ ] Add cache invalidation: accept a `max_age_hours` parameter in `AbstractDB.__class_getitem__` and re-download if the local file is stale
- [ ] Add a `prefetch_all()` class method on `LankaData` that iterates the full metadata and downloads every data file
- [ ] Add pluggable DB registration so external packages can call `LankaData.register_db(MyDB)` without modifying `LankaData.get_db_class_List`
- [ ] Add a `Census2012`↔`Census2024` cross-time datumset joiner that aligns shared dim keys across years for change analysis

## Usability

- [ ] Add a `__main__` entry point that accepts a visual query string as a CLI argument and writes the PNG to the current directory
- [ ] Add auto-generated example gallery: `ReadMe.build()` already reads a JSON list; extend it to also write an HTML index page with inline images
- [ ] Add `__repr__` and `__str__` on `Datumset` showing row count, entity type, and dim keys to ease debugging
