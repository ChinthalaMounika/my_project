import pandas as pd
from google.colab import files
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

# Initialize global variable to hold the dataframe and selected column
df = None
selected_column = None

# Function to handle file upload and process the CSV
def upload_and_process_file(change):
    global df, selected_column
    # Get uploaded file
    uploaded = files.upload()
    
    for filename in uploaded.keys():
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(filename)
        
        # Display a preview of the uploaded data
        print("Preview of uploaded data:")
        display(df.head())
        
        # Get list of columns and create a dropdown for selecting the primary column
        columns = df.columns.tolist()
        column_dropdown = widgets.Dropdown(
            options=columns,
            description="Select Column:",
            disabled=False
        )
        display(column_dropdown)
        
        # Text input box for custom query
        query_input = widgets.Text(
            value='',
            placeholder='Type your query here (e.g., "Get the email address of {company}")',
            description='Custom Query:',
            disabled=False
        )
        display(query_input)

        # Function to handle changes in the column dropdown
        def on_column_change(change):
            global selected_column
            selected_column = column_dropdown.value
            print(f"Selected column: {selected_column}")

            # Dynamically adjust widgets based on the column selected
            update_widgets_for_column()

        column_dropdown.observe(on_column_change, names="value")

        # Function to execute query on selected column
        def execute_query(query, column_value):
            if selected_column is not None:
                # Replace placeholder in query with the actual value
                modified_query = query.replace("{company}", column_value)
                print(f"Executing query: {modified_query}")
                # Example: display rows where the selected column matches the value
                filtered_df = df[df[selected_column] == column_value]
                display(filtered_df)
            else:
                print("Please select a column first.")

        # Function to handle changes in the query input
        def on_query_change(change):
            if selected_column is not None:
                column_value = column_dropdown.value  # Get the selected value from the dropdown
                query = query_input.value  # Get the custom query from the input
                execute_query(query, column_value)
            else:
                print("Please select a column first.")

        query_input.observe(on_query_change, names="value")

        # Function to filter the DataFrame based on column value range
        def filter_data_by_column(column_name, min_value, max_value):
            filtered_df = df[(df[column_name] >= min_value) & (df[column_name] <= max_value)]
            display(filtered_df)

        # Function to allow the user to download the filtered DataFrame
        def export_filtered_data(filtered_df):
            # Convert the filtered DataFrame to a CSV
            filtered_df.to_csv('filtered_data.csv', index=False)
            # Provide the file for download
            files.download('filtered_data.csv')

        # Function to allow the user to download the entire DataFrame as CSV
        def export_full_data():
            # Convert the full DataFrame to a CSV
            df.to_csv('full_data.csv', index=False)
            # Provide the file for download
            files.download('full_data.csv')

        # Add a button to export the filtered data
        export_button = widgets.Button(description="Export Filtered Data")
        export_button.on_click(lambda change: export_filtered_data(df))
        display(export_button)

        # Add a button to export the entire data
        full_data_export_button = widgets.Button(description="Export Full Data")
        full_data_export_button.on_click(lambda change: export_full_data())
        display(full_data_export_button)

        # Function to plot data distribution
        def plot_data(column):
            if column is not None:
                df[column].value_counts().plot(kind='bar')
                plt.title(f"Distribution of {column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.show()
            else:
                print("Please select a column to plot.")

        # Add a button to plot data from the selected column
        plot_button = widgets.Button(description="Plot Data")
        plot_button.on_click(lambda change: plot_data(selected_column) if selected_column else print("Please select a column first"))
        display(plot_button)

        # Function to update widgets based on the selected column
        def update_widgets_for_column():
            # Remove the previous slider if it exists
            if 'slider' in globals():
                slider.close()

            # Create a slider widget for numeric column filtering
            if df[selected_column].dtype in ['int64', 'float64']:  # Check if the column is numeric
                slider = widgets.FloatRangeSlider(
                    value=[df[selected_column].min(), df[selected_column].max()],
                    min=df[selected_column].min(),
                    max=df[selected_column].max(),
                    step=0.1,
                    description=f"Filter {selected_column}:",
                    continuous_update=False
                )
                slider.observe(lambda change: filter_data_by_column(selected_column, change['new'][0], change['new'][1]), names="value")
                display(slider)

# Display file upload button and call function when file is uploaded
upload_button = widgets.Button(description="Upload CSV File")
upload_button.on_click(upload_and_process_file)
display(upload_button)
