# Exploratory Data Analysis Report

## Variable Descriptions
- **Timestamp (yyyy-mm-dd hh:mm)**: Date and time of each observation.
- **GHI (W/m²)**: Global Horizontal Irradiance, the total solar radiation received per square meter on a horizontal surface.
- **DNI (W/m²)**: Direct Normal Irradiance, the amount of solar radiation received per square meter on a surface perpendicular to the rays of the sun.
- **DHI (W/m²)**: Diffuse Horizontal Irradiance, solar radiation received per square meter on a horizontal surface that does not arrive on a direct path from the sun.
- **ModA (W/m²)**: Measurements from a module or sensor (A), similar to irradiance.
- **ModB (W/m²)**: Measurements from a module or sensor (B), similar to irradiance.
- **Tamb (°C)**: Ambient Temperature in degrees Celsius.
- **RH (%)**: Relative Humidity as a percentage of moisture in the air.
- **WS (m/s)**: Wind Speed in meters per second.
- **WSgust (m/s)**: Maximum Wind Gust Speed in meters per second.
- **WSstdev (m/s)**: Standard Deviation of Wind Speed, indicating variability.
- **WD (°N (to east))**: Wind Direction in degrees from north.
- **WDstdev**: Standard Deviation of Wind Direction, showing directional variability.
- **BP (hPa)**: Barometric Pressure in hectopascals.
- **Cleaning (1 or 0)**: Signifying whether cleaning (possibly of the modules or sensors) occurred.
- **Precipitation (mm/min)**: Precipitation rate measured in millimeters per minute.
- **TModA (°C)**: Temperature of Module A in degrees Celsius.
- **TModB (°C)**: Temperature of Module B in degrees Celsius.

## Data Quality Check
- **Null Values**: No null values were found in any of the DataFrames.
- **Column Dropped**: The 'Comments' column was dropped from all three DataFrames.

## Statistical Tests

### T-Test: Benin vs. Sierra Leone
- **Statistic**: 61.33
- **P-value**: 0.0
- **Degrees of Freedom**: 1,051,198

The T-test indicates a significant difference in the solar radiation between Benin and Sierra Leone, with a p-value of 0.0 suggesting strong evidence against the null hypothesis.

### ANOVA Test (GHI Across All Locations)
- **Statistic**: 1977.07
- **P-value**: 0.0

The ANOVA test shows significant differences in GHI values across the three locations, confirming that at least one location differs significantly from the others.

## Best Location for Solar Installation
- **Best Location**: Benin-Malanville
- **Average GHI**: 241.96 W/m²

### Cleaning Impact on ModA
- **Benin-Malanville**: Slope = 70.71, Intercept = 236.52
- **Sierra Leone-Bumbuna**: Slope = 66.73, Intercept = 206.58
- **Togo-Dapaong**: Slope = 309.21, Intercept = 225.98

## Strategic Recommendations
- **Optimal Site**: Benin-Malanville is recommended for solar installation due to its high GHI levels.
- **Viable Option**: Togo-Dapaong also presents a promising opportunity for solar investment.

## Data Visualizations

### Solar Radiation Trends
Benin-Malanville shows consistently high GHI levels throughout the year, indicating strong solar potential. Sierra Leone-Bumbuna also maintains substantial GHI, though with slight fluctuations. Togo-Dapaong exhibits stable GHI trends, but at lower average levels compared to Benin.

### Frequency Distribution of DNI
The DNI distribution in all locations shows a significant concentration at low values, indicating limited direct solar radiation availability. Benin-Malanville and Sierra Leone-Bumbuna both exhibit similar patterns, while Togo-Dapaong shows slightly more variation. This suggests a need for enhanced solar panel efficiency measures in lower DNI regions.

### Correlation Matrices
The correlation matrix for Benin-Malanville indicates strong relationships between cleaning and solar efficiency metrics. Sierra Leone-Bumbuna shows moderate correlations, especially between humidity and solar metrics. Togo-Dapaong presents weaker correlations overall, highlighting potential areas for further investigation.

### GHI Trend Analysis
Benin-Malanville's GHI trend analysis reveals distinct seasonal patterns with peaks indicating optimal solar energy periods. Sierra Leone-Bumbuna shows less variability, while Togo-Dapaong remains relatively stable. This suggests that seasonal planning may benefit solar installations in Benin.

### Impact of Cleaning on Sensor Readings
In Benin-Malanville, cleaning significantly boosts ModA sensor readings compared to uncleaned panels. Sierra Leone-Bumbuna also shows a notable improvement, though less pronounced than in Benin. Togo-Dapaong demonstrates the largest increase in efficiency from cleaning, suggesting effective maintenance strategies.

### Monthly GHI Trends
Monthly GHI trends indicate that Benin-Malanville consistently leads in solar radiation, followed by Sierra Leone-Bumbuna and Togo-Dapaong. Seasonal variations are evident, with peaks in summer months. This highlights the importance of seasonal adjustments for solar energy strategies.

### Environmental Factors and Solar Efficiency Correlation
Benin-Malanville's correlation analysis reveals that higher temperatures and lower humidity positively affect solar efficiency. Sierra Leone-Bumbuna shows similar trends but with weaker correlations. Togo-Dapaong presents minimal correlations, indicating a need to explore additional environmental factors affecting solar performance.

## Conclusion
The analysis demonstrates that Benin-Malanville is the most promising site for solar energy investment based on GHI levels and statistical tests. Togo-Dapaong also holds potential, particularly in light of its cleaning impact on efficiency. Further studies may enhance the understanding of local environmental factors affecting solar radiation.


## Acknowledgments
- Thank you to the team at MoonLight Energy Solutions for providing the dataset and resources for this analysis.
