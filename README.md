# Project Name: Data Processing Dashboard

## Project Summary
The **Data Processing Dashboard** is a web-based tool that allows users to upload CSV files or connect to Google Sheets. Users can then select a column of interest, input custom queries to retrieve relevant data, and visualize the results. The dashboard provides a simple interface for extracting, analyzing, and exporting data efficiently.

## Key Features
- **Upload CSV or Google Sheet**: Users can upload CSV files or connect to Google Sheets to access data.
- **Column Selection**: Choose the primary column (e.g., company names) to analyze.
- **Custom Queries**: Input custom queries to retrieve specific data (e.g., retrieve emails for a specific company).
- **Data Visualization**: Plot graphs to visualize data distribution.
- **Export Data**: Download the extracted and filtered data as a CSV file.

## Setup Instructions

### Prerequisites
Before running the project, ensure that you have the following tools installed:

- Python 3.7+ (If not installed, download from [python.org](https://www.python.org/))
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/data-processing-dashboard.git
    ```

2. Navigate into the project directory:
    ```bash
    cd data-processing-dashboard
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Start the web server by running the `main.py` script:
    ```bash
    python src/main.py
    ```

2. Open a browser and navigate to `http://localhost:5000` to access the dashboard.

3. Use the dashboard to upload a CSV file, select a column, and enter custom queries. You can view and download filtered results, and plot data distributions.

## Project Structure

- `src/`: Contains the main source code for the dashboard.
- `assets/`: Contains static assets like images or icons.
- `docs/`: Additional documentation or project overviews (optional).
- `tests/`: Unit tests for the project.
- `requirements.txt`: Lists the required Python libraries.

## Dependencies

This project uses the following third-party libraries:

- **Pandas**: For data processing and manipulation.
- **Matplotlib**: For plotting graphs.
- **ipywidgets**: For interactive widgets in the UI.
- **Flask**: A web framework to serve the dashboard.
- **Google API Client**: For connecting to Google Sheets.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Third-Party Tools
- `pandas`: For data manipulation
- `ipywidgets`: For UI elements





