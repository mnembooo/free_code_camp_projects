
### README for Page Views Analysis

This Python script visualizes daily page view data from the `fcc-forum-pageviews.csv` file, focusing on filtering and displaying data through various plots.

#### Dependencies
- `matplotlib`: For plotting graphs.
- `pandas`: For data manipulation and handling.
- `seaborn`: For statistical data visualization.
- `register_matplotlib_converters`: To ensure proper date conversion.

#### Data
- The dataset `fcc-forum-pageviews.csv` should contain a `date` column and a `value` column representing the date and page views, respectively.

#### Functions

1. **draw_line_plot()**
   - Generates a line plot of daily page views.
   - Filters the data by removing outliers based on the 2.5% and 97.5% quantiles.
   - Saves the plot as `line_plot.png`.

2. **draw_bar_plot()**
   - Creates a bar plot that shows the average page views for each month over the years.
   - Saves the plot as `bar_plot.png`.

3. **draw_box_plot()**
   - Generates two box plots:
     - One for the page views by year (Year-wise Box Plot).
     - One for the page views by month (Month-wise Box Plot).
   - Saves the plot as `box_plot.png`.

#### Output
- Three plots are saved as `.png` files:
  - `line_plot.png`
  - `bar_plot.png`
  - `box_plot.png`

Make sure the dataset `fcc-forum-pageviews.csv` is available in the same directory for the script to run correctly.
