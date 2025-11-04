# Screen Time Clustering Analysis

A comprehensive data analysis project that uses K-Means clustering to identify patterns in daily screen time behavior. This project analyzes screen time data collected from iPhone usage to understand behavioral patterns and trade-offs between social, productive, and entertainment app usage.

## Overview

This project applies unsupervised machine learning (K-Means clustering) to analyze personal screen time data collected over approximately 28 days. The analysis focuses on identifying distinct behavioral patterns by examining the ratios of three main categories:

- **Social Ratio**: Time spent on social media apps
- **Productive Ratio**: Time spent on productivity, finance, information reading, and health/fitness apps
- **Entertainment Ratio**: Time spent on games, entertainment, and shopping/food apps

The goal is to understand how daily screen time patterns cluster together and identify trade-offs between different types of app usage.

## Features

- **K-Means Clustering Analysis**: Identifies 5 distinct behavioral clusters in screen time patterns
- **Data Preprocessing**: Normalizes data and calculates usage ratios for better clustering
- **Elbow Method Visualization**: Determines optimal number of clusters
- **Cluster Visualization**: Multiple scatter plots showing relationships between usage categories
- **Heatmap Summary**: Visual representation of cluster behavior patterns
- **Weekday vs Weekend Analysis**: Compares usage patterns across different day types

## Key Findings

The analysis identified **5 distinct behavioral clusters**:

1. **Balanced Day** (Cluster 0): Moderate distribution across all categories
2. **Social-Heavy Day** (Cluster 1): High social media usage with lower productivity and entertainment
3. **Entertainment-Heavy Day** (Cluster 2): High gaming and entertainment usage with lower productivity
4. **Short Social Day** (Cluster 3): Lower overall screen time with focus on social apps
5. **Moderate Mixed Day** (Cluster 4): Moderate usage across all categories, more common on weekends

### Key Insights:

- **Inverse Relationship**: When social usage is high, productive app usage tends to decrease
- **Trade-off Pattern**: Entertainment and productivity rarely coexist at high levels on the same day
- **Weekend Behavior**: 
  - Moderate Mixed Days are significantly more common on weekends
  - Short Social Days have zero occurrence on weekends, indicating heavier social usage on weekends
- **Visual Confirmation**: Scatter plots show clear negative slopes between social and entertainment usage, confirming distinct behavioral patterns

## Project Structure

```
screentime-clustering/
│
├── data/
│   └── screentime_dataset.csv          # Main dataset with screen time data
│
├── notebook/
│   └── screentime-analysis-kmeans.ipynb # Jupyter notebook with full analysis
│
├── script/
│   ├── create_csv.py                   # Script to generate CSV from data array
│   ├── images_to_pdf.py                # Converts screenshot images to PDF
│   ├── requirements.txt                # Python dependencies
│   ├── images/                         # Screenshot images of screen time data
│   └── screentime-collection.pdf       # Compiled PDF of all screenshots
│
└── README.md                           # This file
```

## 🔧 Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip (Python package installer)
- Recommended to use Anaconda Base Environment for notebook

## Installation

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd screentime-clustering
```

### 2. Create a Virtual Environment (Recommended for script folder running)

**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Navigate to the `script` directory and install required packages:

```bash
cd script
pip install -r requirements.txt
```

**Note:** If you encounter issues with the KMeans memory leak warning on Windows, you can set the environment variable:
```powershell
$env:OMP_NUM_THREADS=1
```

## Usage

### Running the Analysis Notebook

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to the `notebook` folder and open `screentime-analysis-kmeans.ipynb`

3. Run all cells sequentially to:
   - Load and clean the data
   - Calculate usage ratios
   - Perform feature scaling
   - Visualize the elbow method (see which 'k' you should use if it differs)
   - Train the K-Means model with k clusters
   - Generate visualizations and insights and analyze

### Using the Helper Scripts

**Generate CSV from Data:**
```bash
cd script
python create_csv.py
```

**Convert Images to PDF:**
- Only included for others to see how they should format their screenshots
```bash
cd script
python images_to_pdf.py
```

## Data Collection Method

Due to Apple's restrictions on accessing screen time data programmatically, a manual workaround was implemented:

1. **Screenshot Collection**: Daily screenshots of iPhone screen time data were taken for approximately 28 days
2. **AI-Assisted Extraction**: Screenshots were sent to ChatGPT in batches (10 images per message) for data extraction
3. **Data Compilation**: ChatGPT generated a Python script containing the extracted data as arrays
4. **CSV Generation**: The `create_csv.py` script converts the hardcoded data array into a CSV file into the data folder (ensure it is there)

All screenshots used in the data collection process are included in `script/images/` and `script/screentime-collection.pdf` compiled in `script/screentime-collection.pdf`.

## Replicating the Analysis

### Option 1: Use Existing Dataset

The project includes a pre-processed dataset at `data/screentime_dataset.csv`. Simply run the Jupyter notebook to analyze this data.

### Option 2: Collect Your Own Data

1. **Collect Screenshots**: Take daily screenshots of your iPhone screen time data for at least 3-4 weeks (the more the better)
2. **Extract Data**: Use AI tools (like ChatGPT) to extract screen time data from screenshots:
   - Send screenshots in batches of 10
   - Ask for a Python script that contains the data as arrays
4. **Update Script**: Modify `script/create_csv.py` with your extracted data arrays
5. **Generate CSV**: Run `python create_csv.py` to create your dataset
6. **Run Analysis**: Execute the Jupyter notebook with your new dataset

### Option 3: Use Different Data Sources

If you have screen time data from other sources (Android, third-party apps, etc.), you can:

1. Format your data to match the CSV structure in `data/screentime_dataset.csv`
2. Ensure columns include:
   - `Date`, `Day_Type` (Weekday/Weekend), `Total_Screen_Time_min`, `Pickups`
   - Category minutes: `Social_min`, `Productivity_Finance_min`, `Games_min`, `Entertainment_min`, etc.
3. Run the notebook analysis on your formatted data

## Important Notes

### Data Limitations

- **Small Sample Size**: The current dataset contains ~28 days of data. More data would provide better cluster representations and more accurate insights
- **Platform Limitation**: Apple restricts programmatic access to screen time data, necessitating manual collection methods
- **Missing Work Data**: Productivity work done on non-Apple devices (Windows PC, laptop) is not captured in iPhone screen time data, potentially underrepresenting actual productivity

### Technical Notes

- **K-Means Memory Warning**: On Windows with MKL, KMeans may show memory leak warnings. Setting `OMP_NUM_THREADS=1` can resolve this
- **Optimal Clusters**: The elbow method suggested k=5 as optimal, showing diminishing returns beyond this point
- **Normalization**: Data is standardized using `StandardScaler` to ensure fair comparison across different usage categories

### Personal Note

> "Most of my productive work happens on non-Apple devices (Windows PC, laptop), which aren’t reflected here — I promise I’m more productive than this data suggests :)

## Dataset Schema

The CSV file contains the following columns:

| Column | Description |
|--------|-------------|
| `Date` | Date in YYYY-MM-DD format |
| `Day_Type` | "Weekday" or "Weekend" |
| `Total_Screen_Time_min` | Total screen time in minutes |
| `Pickups` | Number of times the phone was picked up |
| `Most_Used_Category` | Primary app category used that day |
| `Social_min` | Minutes spent on social media apps |
| `Productivity_Finance_min` | Minutes spent on productivity/finance apps |
| `Other_min` | Minutes spent on uncategorized apps |
| `Games_min` | Minutes spent on gaming apps |
| `Entertainment_min` | Minutes spent on entertainment apps |
| `Utilities_min` | Minutes spent on utility apps |
| `Information_Reading_min` | Minutes spent on information/reading apps |
| `Shopping_Food_min` | Minutes spent on shopping/food apps |
| `Creativity_min` | Minutes spent on creativity apps |
| `Travel_min` | Minutes spent on travel apps |
| `Health_Fitness_min` | Minutes spent on health/fitness apps |

## Contributing

Feel free to fork this project and adapt it for your own screen time analysis! Suggestions for improvements are welcome.

## 📄 License

This project is open source and available for personal and educational use.