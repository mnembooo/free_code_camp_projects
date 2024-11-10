
# Sea Level Predictor

This Python script visualizes historical sea level data and projects future sea levels using linear regression.

## Files

- `epa-sea-level.csv`: Dataset containing historical sea level measurements.
- `sea_level_plot.png`: Output plot showing historical data and projected sea levels.

## Usage

1. **Install dependencies**:  
   ```bash
   pip install pandas matplotlib scipy
   ```

2. **Run the script**:
   Execute the script to generate the plot:
   ```bash
   python sea_level_predictor.py
   ```

3. **Output**:
   - The script produces a scatter plot of the historical data.
   - Two lines of best fit:
     - **1880-2050**: Based on the full dataset.
     - **2000-2050**: Based on data from the year 2000 onwards.
   - The plot is saved as `sea_level_plot.png`.

## Functionality

- **draw_plot()**: Reads data, plots it, performs linear regressions for different periods, and saves the plot.
