from flask import Flask, render_template, request, send_file
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest, Filter, FilterExpression, NumericValue
import pandas as pd
import os

def Apply_filter(set):
    if set['Filter_type'] == 'STRING_FILTER':
        if set['Match_type'] == 'EXACT':
            filter_expression = FilterExpression(
                filter=Filter(
                    field_name=set['field'],
                    string_filter=Filter.StringFilter(
                        value=set['value'],
                        match_type=Filter.StringFilter.MatchType.EXACT
                    )
                )
            )
            return filter_expression
        
        elif set['Match_type'] == 'BEGINS_WITH':
            filter_expression = FilterExpression(
                filter=Filter(
                    field_name=set['field'],
                    string_filter=Filter.StringFilter(
                        value=set['value'],
                        match_type=Filter.StringFilter.MatchType.BEGINS_WITH
                    )
                )
            )
            return filter_expression
        
        elif set['Match_type'] == 'ENDS_WITH':
            filter_expression = FilterExpression(
                filter=Filter(
                    field_name=set['field'],
                    string_filter=Filter.StringFilter(
                        value=set['value'],
                        match_type=Filter.StringFilter.MatchType.ENDS_WITH
                    )
                )
            )
            return filter_expression

        elif set['Match_type'] == 'CONTAINS':
            filter_expression = FilterExpression(
                filter=Filter(
                    field_name=set['field'],
                    string_filter=Filter.StringFilter(
                        value=set['value'],
                        match_type=Filter.StringFilter.MatchType.CONTAINS
                    )
                )
            )
            return filter_expression

        elif set['Match_type'] == 'FULL_REGEXP':
            filter_expression = FilterExpression(
                filter=Filter(
                    field_name=set['field'],
                    string_filter=Filter.StringFilter(
                        value=set['value'],
                        match_type=Filter.StringFilter.MatchType.FULL_REGEXP
                    )
                )
            )
            return filter_expression

        elif set['Match_type'] == 'PARTIAL_REGEXP':
            filter_expression = FilterExpression(
                filter=Filter(
                    field_name=set['field'],
                    string_filter=Filter.StringFilter(
                        value=set['value'],
                        match_type=Filter.StringFilter.MatchType.PARTIAL_REGEXP
                    )
                )
            )
            return filter_expression
     
    elif set['Filter_type'] == 'NUMERIC_FILTER':
        if set['Match_type'] == 'EQUAL':
            filter_expression = FilterExpression(
            filter=Filter(
            field_name=set['field'],
            numeric_filter=Filter.NumericFilter(
            operation=Filter.NumericFilter.Operation.EQUAL,
            value=NumericValue(int64_value=set['value'])
                    )
                )
            )
            return filter_expression
        
        elif set['Match_type'] == 'LESS_THAN':
            filter_expression = FilterExpression(
            filter=Filter(
            field_name=set['field'],
            numeric_filter=Filter.NumericFilter(
            operation=Filter.NumericFilter.Operation.LESS_THAN,
            value=NumericValue(int64_value=set['value'])
                    )
                )
            )
            return filter_expression
        
        elif set['Match_type'] == 'LESS_THAN_OR_EQUAL':
            filter_expression = FilterExpression(
            filter=Filter(
            field_name=set['field'],
            numeric_filter=Filter.NumericFilter(
            operation=Filter.NumericFilter.Operation.LESS_THAN_OR_EQUAL,
            value=NumericValue(int64_value=set['value'])
                    )
                )
            )
            return filter_expression

        elif set['Match_type'] == 'GREATER_THAN':
            filter_expression = FilterExpression(
            filter=Filter(
            field_name=set['field'],
            numeric_filter=Filter.NumericFilter(
            operation=Filter.NumericFilter.Operation.GREATER_THAN,
            value=NumericValue(int64_value=set['value'])
                    )
                )
            )
            return filter_expression

        elif set['Match_type'] == 'GREATER_THAN_OR_EQUAL':
            filter_expression = FilterExpression(
            filter=Filter(
            field_name=set['field'],
            numeric_filter=Filter.NumericFilter(
            operation=Filter.NumericFilter.Operation.GREATER_THAN_OR_EQUAL,
            value=NumericValue(int64_value=set['value'])
                    )
                )
            )
            return filter_expression
        
    elif set['Filter_type'] == 'BETWEEN_FILTER':
        filter_expression = FilterExpression(
        filter=Filter(
        field_name=set['field'],
        between_filter=Filter.BetweenFilter(
            from_value=NumericValue(int64_value=set['value1']),
            to_value=NumericValue(int64_value=set['value2'])
                    )
                )
            )
        return filter_expression

    elif set['Filter_type'] == 'IN_LIST_FILTER':
        filter_expression = FilterExpression(
    filter=Filter(
        field_name=set['field'],
        in_list_filter=Filter.InListFilter(
            values=set['value']
                    )
                )
            )
        return filter_expression
        
# Define a function to retrieve GA4 data
def GA_run_report(property_id, dimensions, metrics, start_date, end_date, D_filterexp = None, M_filterexp=None, limit=10000, offset=0):
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=dimensions,
        metrics=metrics,
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        limit=limit,
        offset=offset,
        dimension_filter= D_filterexp,
        metric_filter = M_filterexp
    )
    response = client.run_report(request)
    return response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    key_file_path = 'key.json'
    if not os.path.isfile(key_file_path):
        print(f"Error: Key file '{key_file_path}' not found.")
        # Handle the error, raise an exception, or exit the program
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_file_path
    
    propertiesID = {
        'GA' : 250390478,
        'GU' : 254956546,
        'BR' : 290480246,
        'BC' : 290657070,
        'BG' : 290805288,
        'KV' : 290822049,
        'SH' : 290510947,
        'MB' : 255577568,
        'BP' : 290652599,
        'SP' : 290802604,
        'PC' : 290736299
    }
    brand = request.form['brand']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    selected_dimensions = request.form.getlist('selected-dimensions-list')
    selected_metrics = request.form.getlist('selected-metrics-list')
    DF_status = request.form.get('D_Filter')
    MF_status = request.form.get('M_Filter')
    # Define dimensions and metrics based on form inputs
    dimensions = [Dimension(name=dimension) for dimension in selected_dimensions]
    metrics = [Metric(name=metric) for metric in selected_metrics]
    property_id= 0
    for i in propertiesID.keys():
        if i == brand:
            property_id = propertiesID[i]
    # Call your GA data retrieval function
    limit = 10000
    offset = 0
    data_frames = []
    global response
    D_filterexp=None
    M_filterexp=None
    if DF_status:
        D_Field = request.form.get('dimensionscombo')
        D_Filter_Type = request.form.get('D_Filter_type')
        DSTR_Filter_Match = request.form.get('DSTR_MatchType')
        DNUM_Filter_Match = request.form.get('DNUM_MatchType')
        D_Filter_Value = request.form.get('D_value')
        D_Filter_Value1 = request.form.get('D_value1')
        D_Filter_Value2 = request.form.get('D_value2')
        if D_Filter_Type == 'STRING_FILTER':
            set = {'field': D_Field, 'value': D_Filter_Value, 'value1': D_Filter_Value1, 'value2': D_Filter_Value2, 'Filter_type':D_Filter_Type,'Match_type': DSTR_Filter_Match }
        elif D_Filter_Type == 'NUMERIC_FILTER':
            set = {'field': D_Field, 'value': D_Filter_Value, 'value1': D_Filter_Value1, 'value2': D_Filter_Value2, 'Filter_type':D_Filter_Type,'Match_type': DNUM_Filter_Match }
        else:
            set = {'field': D_Field, 'value': D_Filter_Value, 'value1': D_Filter_Value1, 'value2': D_Filter_Value2, 'Filter_type':D_Filter_Type,'Match_type': 'None' }
        print(set)
        D_filterexp = Apply_filter(set)
        
    if MF_status:
        M_Field = request.form.get('metricscombo')
        M_Filter_Type = request.form.get('M_Filter_type')
        MSTR_Filter_Match = request.form.get('MSTR_MatchType')
        MNUM_Filter_Match = request.form.get('MNUM_MatchType')
        M_Filter_Value = request.form.get('M_value')
        M_Filter_Value1 = request.form.get('M_value1')
        M_Filter_Value2 = request.form.get('M_value2')
        if M_Filter_Type == 'STRING_FILTER':
            set = {'field': M_Field, 'value': M_Filter_Value, 'value1': M_Filter_Value1, 'value2': M_Filter_Value2, 'Filter_type': M_Filter_Type,'Match_type': MSTR_Filter_Match }
        elif M_Filter_Type == 'NUMERIC_FILTER':
            set = {'field': M_Field, 'value': M_Filter_Value, 'value1': M_Filter_Value1, 'value2': M_Filter_Value2, 'Filter_type': M_Filter_Type,'Match_type': MNUM_Filter_Match }
        else:
            set = {'field': M_Field, 'value': M_Filter_Value, 'value1': M_Filter_Value1, 'value2': M_Filter_Value2, 'Filter_type': M_Filter_Type,'Match_type': 'None' }
        print(set)
        M_filterexp = Apply_filter(set)
    print(D_filterexp)
    print(M_filterexp)
    while True:
        try:
            response = GA_run_report(property_id, dimensions, metrics, start_date, end_date, D_filterexp, M_filterexp, limit, offset)
        except Exception as e:
            print(f"Error during API request: {e}")
        # Process the GA data
        for row in response.rows:
            dimension_values = [dimension.value for dimension in row.dimension_values]
            metric_values = [metric.value for metric in row.metric_values]
            new_row_data = {'Brand': brand}

            # Handle dimensions
            for i, dimension in enumerate(selected_dimensions):
                 if i < len(dimension_values):
                    if dimension == 'date':
                        new_row_data[dimension] = pd.to_datetime(dimension_values[i])  # type: ignore
                    else:
                        new_row_data[dimension] = dimension_values[i]
                 else:
                    new_row_data[dimension] = None # type: ignore
                 
            # Handle metrics
            for i, metric in enumerate(selected_metrics):
                if i < len(metric_values):
                    new_row_data[metric] = metric_values[i]
                else:
                    new_row_data[metric] = None  # type: ignore # Set to None if no value is available

            # Create a DataFrame for the current row and append it to the list
            row_df = pd.DataFrame([new_row_data])
            data_frames.append(row_df)

        # If there are more rows, update the offset for the next request
        if response.row_count > offset + limit:
            offset += limit
        else:
            break

    # Concatenate all DataFrames
    global GA_Export
    if data_frames:
        GA_Export = pd.concat(data_frames, ignore_index=True)
    else:
        print("Warning: No data to export.")
        # Handle the case where there is no data, raise a warning, or return an appropriate response


    # Sort the data by date
    #GA_Export = GA_Export.sort_values(by=['date'])

    # Save data to a CSV file
    csv_filename = 'GA_Data.csv'
    GA_Export.to_csv(csv_filename, index=False)

    # Send the file for download with a specific filename
    return send_file(csv_filename, as_attachment=True, download_name='GA_Data.csv')

if __name__ == '__main__':
    app.run(debug=True)
