# Solar Site Optimizer

## Overview
**Solar Site Optimizer** is a data-driven solution designed to analyze solar energy potential across multiple locations in Africa. This project utilizes data from solar radiation sensors to identify optimal sites for solar installation. The analysis includes various metrics such as Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and environmental factors like temperature, wind speed, and humidity. The goal is to determine the best sites for solar energy generation, and recommend strategies for efficiency improvements and maintenance.

The analysis is part of a project with **MoonLight Energy Solutions** aimed at optimizing solar energy investments in West Africa.

## Key Insights
- **Best Location for Solar Installation**: **Benin-Malanville** stands out as the top location for solar installation due to its high GHI levels and favorable environmental conditions.
- **Impact of Cleaning on Sensor Readings**: Regular cleaning significantly boosts solar panel efficiency, particularly in **Benin-Malanville** and **Togo-Dapaong**.
- **Environmental Factors**: High temperatures and low humidity positively correlate with better solar energy performance, especially in **Benin-Malanville**.
  
## Project Structure
The project is structured as follows:

```markdown
solar-site-optimizer/
├── app                        # Folder for Streamlit dashboard 
  ├── solar_dashboard.py       # Main Python script to run the dashboard and analysis
├── notebooks/                 # Folder for data analysis
  ├── eda.ipynb                # Exploratory Data Analysis Notebook
├── tests/                     # Folder for tests
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview and instructions
└── reports/                   # Folder for detailed reports and documentation
```

## Prerequisites

To run this project locally, ensure you have the following installed:
- **Python 3.x** or later
- **Pip** (for managing Python packages)

## Setup

Follow these steps to set up the project on your local machine:

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/solar-site-optimizer.git
cd solar-site-optimizer
```

### Step 2: Create a Virtual Environment
It is recommended to create a virtual environment for your project to manage dependencies.

```bash
python -m venv venv
```

### Step 3: Install Dependencies
Install the necessary dependencies using `pip`.

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains all the necessary libraries for data analysis, visualization, and web dashboard, including:
- `pandas`
- `dash`
- `plotly`
- `geopandas`
- `folium`
- `matplotlib`
- `scipy`
- `statsmodels`
- `scikit-learn`

### Step 4: Running the Application
Once the dependencies are installed, you can run the dashboard and analysis using the following command:

```bash
python solar_dashboard.py
```

This will start a local server (usually at `http://127.0.0.1:8050/`), where you can view the interactive dashboard showing the solar site optimization analysis.

## How It Works

### Data Ingestion
The project uses historical solar radiation data from sensors located in three West African regions:
1. **Benin-Malanville**
2. **Sierra Leone-Bumbuna**
3. **Togo-Dapaong**

This data is processed to extract key insights into solar potential across these locations, focusing on variables like GHI, DNI, ambient temperature, and cleaning effects.

### Statistical Analysis
- **T-tests** and **ANOVA tests** are applied to assess the statistical significance of differences in GHI and other metrics across the three locations.
- The **best location for solar installation** is identified based on average GHI levels, seasonal trends, and environmental factors.

### Visualizations
Data visualizations of the notebook, including:
- **GHI Trend AnalysisSolar Radiation Trends**
- **Frequency Distribution of DNI**
- **Correlation Matrices**
- **GHI Trend Analysis**
- **Impact of Cleaning on Sensor Readings**
- **Monthly GHI Trends**
- **Environmental Factors and Solar Efficiency Correlation**
are generated to provide deeper insights into the patterns and relationships between environmental factors and solar efficiency.

### Dashboard
A **Dash-based interactive dashboard** is created to visualize the findings. The dashboard allows users to:
- View trends in solar radiation across different locations.
- Explore the impact of cleaning on sensor readings.
- See correlations between environmental factors (e.g., temperature, humidity) and solar performance.

## Key Results

### Best Location for Solar Installation:
- **Benin-Malanville** emerges as the best location for solar energy generation, with the highest average GHI of **241.96 W/m²**.

### Cleaning Impact:
- Regular cleaning significantly boosts solar panel performance, with the **largest impact in Togo-Dapaong**.

### Statistical Tests:
- **T-Test**: Strong evidence of a significant difference in GHI between Benin and Sierra Leone.
- **ANOVA Test**: Confirmed significant differences in GHI across the three locations.

## Future Improvements
- **Data Expansion**: Incorporating more data points (e.g., weather data) could further enhance predictions.
- **Automation**: Automating the data collection and analysis pipeline would improve efficiency and scalability.
- **Predictive Modeling**: Implementing machine learning models to predict solar efficiency based on environmental variables could lead to more accurate forecasting.

## Acknowledgments
- **MoonLight Energy Solutions** for providing the dataset and resources to carry out this analysis.
- All contributors and collaborators who assisted in the development and refinement of this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
Author: Eyor Getachew
Date: March 25, 2025
