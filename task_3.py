import plotly.express as px
import plotly.data as pldata
import pandas as pd


# Task 3: Interactive Visualizations with Plotly

# LOAD DATA
df = pldata.wind(return_type='pandas')

# Print first 10 rows
print("=== First 10 Rows ===")
print(df.head(10))

# Print last 10 rows
print("\n=== Last 10 Rows ===")
print(df.tail(10))

# CLEAN THE DATA

# convert strength column to float using str.replace() with regex
df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# another option to convert strength column to float using str.extract() with regex
#df['strength'] = df['strength'].astype(str).str.extract('(\d+)').astype(float)

print("Data types after cleaning:")
print(df.dtypes)


# CREATE INTERACTIVE PLOT
fig = px.scatter(df, x='strength', y='frequency', color='direction', 
                 title='Wind Strength vs Frequency by Direction',
                 labels={'strength': 'Wind Strength (mph)', 'frequency': 'Frequency (%)', 'direction': 'Wind Direction'},
                 hover_data=['direction'], size='frequency', color_discrete_sequence=px.colors.qualitative.Bold)



# Improve layout
# fig.update_layout(
#     title_font_size=18,
#     xaxis_title="Wind Strength",
#     yaxis_title="Frequency",
#     legend_title="Wind Direction",
#     height=700
# )

# SAVE AS HTML
fig.write_html("wind.html")

fig.show()

print("You can now open 'wind.html' in any browser to view the interactive plot.")