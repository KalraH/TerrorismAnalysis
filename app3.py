"""
Created on Fri Sept 6 21:15:33 2020

@author: Hariom Kalra
"""

# Importing Libraries
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate


app = dash.Dash()  # Creating Web App


def load_data():  # Function for Loading data to be used in application
    # Making variables Global to be used all over the script
    global df, month_dict, date_dict, region_dict, attack_type_dict, types_dict
    global country_dict, state_dict, city_dict, types_dict1, year_dict, year_list

    dataset_name = "globalTerror.csv"

    pd.options.mode.chained_assignment = None # A statement to prevent errors from pandas
    df = pd.read_csv( dataset_name )  # Reafding data from CSV & saving into DataFrame
    
    # Printing first & last 5 values in Console
    print( df.head(5) )
    print( df.tail(5) )

    
    # Saving data from DataFrame and saving into dictionaries
    month_list = { "January" : 1, 
                  "February" : 2, 
                  "March" : 3, 
                  "April" : 4,
                  "May" : 5, 
                  "June" : 6, 
                  "July" : 7, 
                  "August" : 8, 
                  "September" : 9,
                  "October" : 10, 
                  "November" : 11, 
                  "December" : 12 }
    
    # Month data Dictionary
    month_dict = [{ "label" : key, "value" : values } for key,values in month_list.items() ]

    # Date data Dictionary
    date_dict = [ x for x in range(1, 32) ]

    # World Regions data Dictionary
    region_dict = [{ "label" : str(i), "value" : str(i) } for i in sorted( df[ 'region_txt' ].unique().tolist()) ]

    # World Countries data Dictionary
    country_dict = df.groupby( "region_txt" ) [ "country_txt" ].unique().apply(list).to_dict()

    # World States data Dictionary
    state_dict = df.groupby( "country_txt" ) [ "provstate" ].unique().apply(list).to_dict()

    # World Cities data Dictionary
    city_dict = df.groupby( "provstate" ) [ "city" ].unique().apply(list).to_dict()

    # Terrorist Attack Types data Dictionary
    attack_type_dict = [{ "label" : str(i), "value" : str(i) } for i in df[ 'attacktype1_txt' ].unique().tolist() ]

    # Unique Years in which attacks were done data List
    year_list = sorted( df[ 'iyear' ].unique().tolist() )
    
    # Unique Years in which attacks were done data Dictionary
    year_dict = { str(year) : str(year) for year in year_list }
    
    # Chart Dropdown data list
    type_list = { "Terrorist Organisation" : "gname", 
                 "Target Nationality" : "natlty1_txt", 
                 "Target Type" : "targtype1_txt", 
                 "Type of Attack" : "attacktype1_txt", 
                 "Weapon Type" : "weaptype1_txt", 
                 "Region" : "region_txt", 
                 "Country Attacked" : "country_txt" }
    
    # Chart Dropdown data dict
    types_dict = [{ "label" : keys, "value" : value } for keys, value in type_list.items() ]


def open_browser(): #  Function to open Web-Browser 
    webbrowser.open_new( 'http://127.0.0.1:8050/' )  # Opening Browser


def create_app_ui():  # Function to Create User Interface of App
    # Variables used    
    dropdown_style = { 'width' : '450px', 
                      'text-align' : 'center', 
                      'vertical-align' : 'center', 
                      'margin-left' : '400px' }
    
    tab_style = html.style = { 'borderTop' : '2px solid #18FFFF', 
                              'borderBottom': '2px solid #18FFFF', 
                              'backgroundColor': '#18FFFF', 
                              'color': '#D50000', 
                              'padding': '18px' }
    
    selected_style = html.style = { 'borderTop' : '2px solid #A7FFEB', 
                                   'borderBottom': '2px solid #A7FFEB', 
                                   'backgroundColor': '#A7FFEB', 
                                   'color': '#512DA8', 
                                   'padding': '18px' }
    
    # Main Layout of Web Page
    main_layout = html.Div( style = { 'background-color' : '#CCFF90' },
                           children = [ html.H1( 'Terrorism Analysis with Insights', 
                                                id = 'Main_title', 
                                                style = { 'textAlign' : 'center', 
                                                         'background-color' : '#80D8FF',
                                                         'color' : '#AA00FF',
                                                         'border' : '6px solid #1DE9B6', 
                                                         'padding-top' : '15px', 
                                                         'padding-bottom' : '15px' }),
                                        html.Br(),
                                        
                                        # Inserting Tabs to the UI 
                                        dcc.Tabs( id = "Tabs", 
                                                 value = "Map",
                                                 children = [ dcc.Tab( label = "Map tool",   # Map Tab
                                                                      id = "Map tool", 
                                                                      value = "Map", 
                                                                      style = tab_style, 
                                                                      selected_style = selected_style,
                                                                      children = [ dcc.Tabs( id = "subtabs",   
                                                                                            value = "WorldMap",
                                                                                            children = [ dcc.Tab( label = "World Map", # World Map Tab
                                                                                                                 id = "World", 
                                                                                                                 value = "WorldMap", 
                                                                                                                 style = tab_style, 
                                                                                                                 selected_style = selected_style ),
                                                                                                         
                                                                                                         dcc.Tab( label = "India Map", # India Map Tab
                                                                                                                 id = "India", 
                                                                                                                 value = "IndiaMap", 
                                                                                                                 style = tab_style, 
                                                                                                                 selected_style = selected_style )
                                                                                                       ]),
                                                                                    html.Br(),
                                                                                    html.Br(),
                                                                                    
                                                                                    dcc.Dropdown( id = 'month', 
                                                                                                 options = month_dict, 
                                                                                                 placeholder = 'Select Month',
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                                                                    
                                                                                    dcc.Dropdown( id = 'date', 
                                                                                                 placeholder = 'Select Day',
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                                                                    
                                                                                    dcc.Dropdown( id = 'region-dropdown', 
                                                                                                 options = region_dict, 
                                                                                                 placeholder = 'Select Region', 
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                                                                    
                                                                                    dcc.Dropdown( id = 'country-dropdown', 
                                                                                                 options = [{ 'label' : 'All', 'value' : 'All' }], 
                                                                                                 placeholder = 'Select Country', 
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                                                                    
                                                                                    dcc.Dropdown( id = 'state-dropdown', 
                                                                                                 options = [{ 'label' : 'All', 'value' : 'All' }], 
                                                                                                 placeholder = 'Select State or Province', 
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                                                                    
                                                                                    dcc.Dropdown( id = 'city-dropdown', 
                                                                                                 options = [{ 'label' : 'All', 'value' : 'All' }], 
                                                                                                 placeholder = 'Select City', 
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                                                                    
                                                                                    dcc.Dropdown( id = 'attacktype-dropdown', 
                                                                                                 options = attack_type_dict, 
                                                                                                 placeholder = 'Select Attack Type', 
                                                                                                 style = dropdown_style,
                                                                                                 multi = True ),
                                        
                                                                                    html.H3( 'Select the Year',
                                                                                            id = 'year_title',
                                                                                            style = { 'textAlign' : 'center', 
                                                                                                     'background-color' : '#80D8FF',
                                                                                                     'color' : '#AA00FF',
                                                                                                     'border' : '6px solid #1DE9B6', 
                                                                                                     'padding-top' : '10px', 
                                                                                                     'padding-bottom' : '10px' }
                                                                                            ),
                                                                            
                                                                                    dcc.RangeSlider( id = 'year-slider', 
                                                                                                    min = min(year_list), 
                                                                                                    max = max(year_list), 
                                                                                                    value = [ min(year_list), max(year_list) ], 
                                                                                                    marks = year_dict, 
                                                                                                    step = None ),
                                                                                    html.Br(),
                                                                                    html.Br(),             
                                                                                  ]
                                                                     ),
                                                              dcc.Tab( label = "Chart Tool",   # Chart Tab
                                                                      id = "chart tool", 
                                                                      value = "Chart", 
                                                                      style = tab_style, 
                                                                      selected_style = selected_style,
                                                                      children = [ dcc.Tabs( id = "subtabs2", 
                                                                                            value = "WorldChart",
                                                                                            children = [ dcc.Tab( label = "World Chart",  # World Chart Tab
                                                                                                                 id = "WorldC", 
                                                                                                                 value = "WorldChart", 
                                                                                                                 style = tab_style, 
                                                                                                                 selected_style = selected_style, ),
                                                                                                        
                                                                                                        dcc.Tab( label = "India Chart", # India Chart Tab
                                                                                                                id = "IndiaC", 
                                                                                                                value = "IndiaChart", 
                                                                                                                style = tab_style,
                                                                                                                selected_style = selected_style, )
                                                                                                       ]),
                                                                                   html.Br(),
                                                                                   
                                                                                   dcc.Dropdown( id = 'types-dropdown', 
                                                                                                options = types_dict, 
                                                                                                placeholder = 'Select Type', 
                                                                                                value = "region_txt",
                                                                                                style = dropdown_style ),
                                                                                   html.Br(),
                                                                                   html.Hr(),
                                                                                                                                  
                                                                                   dcc.Input(id = "search_box", 
                                                                                             placeholder = "Search Filter" , 
                                                                                             style = { 'text-align' : 'center', 
                                                                                                      'width' : '440px', 
                                                                                                      'margin-left' : '800px', 
                                                                                                      'height' : '25px' }
                                                                                             ),                                          
                                                                                   html.Hr(),
                                                                                   html.Br(),
                                                                                   
                                                                                   dcc.RangeSlider( id = 'chart_year_slider',
                                                                                                   min = min(year_list),
                                                                                                   max = max(year_list),
                                                                                                   value = [ min(year_list), max(year_list) ],
                                                                                                   marks = year_dict,
                                                                                                   step = None ),
                                                                                   html.Br(),
                                                                                  ]
                                                                     )
                                                            ]
                                                ),
                                        html.Div( id = 'graph-object', children = [ "Map is loading" ])
                                        ]
                           )
    return main_layout


# Callback for updating City Dropdown Values as per State Selected
@app.callback(
    Output( 'graph-object', 'children' ),
    [
        Input( 'month', 'value' ),
        Input( 'date', 'value' ),
        Input( 'region-dropdown', 'value' ),
        Input( 'country-dropdown', 'value' ),
        Input( 'state-dropdown', 'value' ),
        Input( 'city-dropdown', 'value' ),
        Input( 'attacktype-dropdown', 'value' ),
        Input( 'year-slider', 'value' ),
        Input( "Tabs", "value" ),
        Input( "types-dropdown", "value" ),
        Input( "search_box", "value" ),
        Input( "subtabs2", "value" ),
        Input( "chart_year_slider", "value" )
        
    ]
    )
def update_app_ui( month_value, date_value, region_value, country_value, state_value, city_value, 
                  attack_value, year_value, Tab, chart_value, search_box_value, subtab2, chart_year_value ):
    figure = None
    
    if Tab == "Map":  # For Map Section
        # Industry Best Practice to Print all values and their types in Console
        print("Data Type of month value = ", str( type(month_value) ))
        print("Data of month value = ", month_value )
    
        print("Data Type of Day value = ", str( type(date_value) ))
        print("Data of Day value = ", date_value )
    
        print("Data Type of region value = ", str( type(region_value) ))
        print("Data of region value = ", region_value )
    
        print("Data Type of country value = ", str( type(country_value) ))
        print("Data of country value = ", country_value )
    
        print("Data Type of state value = ", str( type(state_value) ))
        print("Data of state value = ", state_value )
    
        print("Data Type of city value = ", str( type(city_value) ))
        print("Data of city value = ", city_value )
    
        print("Data Type of Attack value = ", str( type(attack_value) ))
        print("Data of Attack value = ", attack_value )

        print("Data Type of year value = ", str( type(year_value) ))
        print("Data of year value = ", year_value )
    
        print("Data Type of Tab value = ", str( type(Tab) ))
        print("Data of Tab value = ", Tab )

        # Year Filter
        year_range = range( year_value[0], year_value[1] + 1 )
        new_df = df[ df[ "iyear" ].isin(year_range) ]
    
        # Month Filter
        if month_value == [] or month_value is None:
            pass
        
        else:
            if date_value == [] or date_value is None:
                new_df = new_df[ new_df[ "imonth" ].isin(month_value) ]
    
            else:
                new_df = new_df[ new_df[ "imonth" ].isin(month_value) & 
                                (new_df[ "iday" ].isin(date_value) )]
    
        # Region, Country, State, City Filters
        if region_value == [] or region_value is None:
            pass
       
        else:
            if country_value == [] or country_value is None :
                new_df = new_df[ new_df[ "region_txt" ].isin(region_value) ]
            
            else:
                if state_value == [] or state_value is None:
                    new_df = new_df[( new_df[ "region_txt" ].isin(region_value) ) & 
                                    ( new_df[ "country_txt" ].isin(country_value) )]
                
                else:
                    if city_value == [] or city_value is None:
                        new_df = new_df[( new_df[ "region_txt" ].isin(region_value) ) & 
                                        ( new_df[ "country_txt" ].isin(country_value) ) & 
                                        ( new_df[ "provstate" ].isin(state_value) )]
                    
                    else:
                        new_df = new_df[( new_df[ "region_txt" ].isin(region_value) ) & 
                                        ( new_df[ "country_txt" ].isin(country_value) ) & 
                                        ( new_df[ "provstate" ].isin(state_value) ) & 
                                        ( new_df[ "city" ].isin(city_value) )]

        if attack_value == [] or attack_value is None:
            pass
       
        else:
            new_df = new_df[ new_df[ "attacktype1_txt" ].isin(attack_value) ]

        # Plotting Map
        map_figure = go.Figure()
        
        if new_df.shape[0]:
            pass
        
        else:
            new_df = pd.DataFrame( columns = [ 'iyear', 
                                              'imonth', 
                                              'iday', 
                                              'country_txt', 
                                              'region_txt', 
                                              'provstate', 
                                              'city', 
                                              'latitude',
                                              'longitude', 
                                              'attacktype1_txt',
                                              'nkill' ])

            new_df.loc[0] = [ 0, 0 , 0, None, None, None, None, None, None, None, None ]
            
        map_figure = px.scatter_mapbox( new_df, 
                                       lat = "latitude", 
                                       lon = "longitude", 
                                       color = "attacktype1_txt", 
                                       hover_name = "city", 
                                       hover_data = [ "region_txt", 
                                                     "country_txt", 
                                                     "provstate", 
                                                     "city", 
                                                     "attacktype1_txt", 
                                                     "nkill", 
                                                     "iyear", 
                                                     "imonth", 
                                                     "iday" ],
                                       zoom = 1 )
    
        map_figure.update_layout( mapbox_style = "open-street-map", 
                                 autosize = True, 
                                 margin = dict( l = 0, r = 0, t = 25, b = 20 ))
            
        figure = map_figure
    
    elif Tab == "Chart":  # For Chart Section
        figure = None
        
        print("Data Type of Chart value = ", str( type(chart_value) ))
        print("Data of month value = ", month_value )
    
        print("Data Type of Chart value = ", str( type(chart_value) ))
        print("Data of Day value = ", date_value )
    
        print("Data Type of Search Box value value = ", str( type(search_box_value) ))
        print("Data of region value = ", region_value )
    
        print("Data Type of Search Box value value = ", str( type(search_box_value) ))
        print("Data of country value = ", country_value )
        
        print("Data Type of Tab value = ", str( type(Tab) ))
        print("Data of Tab value = ", Tab )
        
        print("Data Type of SubTab value = ", str( type(subtab2) ))
        print("Data of SubTab value = ", subtab2 )
        
        chart_year_range = range( chart_year_value[0], chart_year_value[1] + 1 )
        chartDF = df[ df[ "iyear" ].isin(chart_year_range) ]
        
        if( subtab2 == "WorldChart" ):
            pass
        
        elif( subtab2 == "IndiaChart" ):
             chartDF = chartDF[( chartDF[ "region_txt" ] == "South Asia" ) & 
                               ( chartDF[ "country_txt" ] == "India" )]
        # Search Box Filter
        if chart_value is not None and chartDF.shape[0]:
            if search_box_value is not None:
                chartDF = chartDF.groupby( "iyear" ) [ chart_value ].value_counts().reset_index( name = "count" )
                chartDF  = chartDF[ chartDF[ chart_value ].str.contains( search_box_value, case = False )]
            
            else:
                chartDF = chartDF.groupby( "iyear" ) [ chart_value ].value_counts().reset_index( name = "count" )
        
        
        if chartDF.shape[0]:
            pass
        
        else: 
            chartDF = pd.DataFrame( columns = [ 'iyear', 'count', chart_value ])
            
            chartDF.loc[0] = [ 0, 0, "No data" ]
        
        chartFigure = px.area( chartDF, x = "iyear", y ="count", color = chart_value )  # Plotting Map
        figure = chartFigure
    
    return dcc.Graph( figure = figure )


# Callback for updating Types Dropdown Values as per Chart Selected { India Chart or World Chart }
@app.callback(
    Output( "types-dropdown", "Options" ),
    [
        Input( "subtabs2", "value" )
    ]
    )
def update_IC_date(tab):  # Callback Supporting function
    option = types_dict

    if tab == "WorldC":
        pass
    
    elif tab == "IndiaC":
        option = types_dict1
        
    return option


# Callback for updating Date Dropdown Values as per Month Selected
@app.callback(
    Output( "date", "options" ),
    [
        Input( "month", "value" )
    ]
    )
def update_date(month):  # Callback Supporting function
    option = []

    if month:
        option = [{ "label" : m, "value" : m } for m in date_dict ]

    return option


# Callback for updating Region Dropdown & Country Dropdown Values as per Map Selected { India Map or World Map }
@app.callback(
    [
        Output("region-dropdown", "value"),
        Output("region-dropdown", "disabled"),
        Output("country-dropdown", "value"),
        Output("country-dropdown", "disabled")
    ],
    
    [
         Input("subtabs", "value")
    ])
def update_dropdown(tab):  # Callback Supporting function
    region = None
    disabled_region = False
    country = None
    disabled_country = False
    
    if tab == "WorldMap":
        pass
    
    elif tab == "IndiaMap":
        region = ["South Asia"]
        disabled_region = True
        
        country = ["India"]
        disabled_country = True
    
    return region, disabled_region, country, disabled_country


# Callback for updating Country Dropdown Values as per Region Selected
@app.callback(
    Output( 'country-dropdown', 'options' ),
    [
        Input( 'region-dropdown', 'value' )
    ]
    )
def set_country_options(region_value):  # Callback Supporting function
    option = []

    if region_value is  None:
        raise PreventUpdate

    else:
        for a in region_value:
            if a in country_dict.keys():
                option.extend( country_dict[a] )

    return [{ 'label' : m , 'value' : m } for m in option ]


# Callback for updating State Dropdown Values as per Country Selected
@app.callback(
    Output( 'state-dropdown', 'options' ),
    [
        Input( 'country-dropdown', 'value' )
    ]
    )
def set_state_options(country_value):  # Callback Supporting function
    option = []

    if country_value is None :
        raise PreventUpdate

    else:
        for a in country_value:
            if a in state_dict.keys():
                option.extend( state_dict[a] )

    return [{ 'label' : m , 'value' : m } for m in option ]


# Callback for updating City Dropdown Values as per State Selected
@app.callback(
    Output( 'city-dropdown', 'options' ),
    [
        Input( 'state-dropdown', 'value' )
    ]
    )
def set_city_options(state_value):  # Callback Supporting function
    option = []

    if state_value is None:
        raise PreventUpdate

    else:
        for a in state_value:
            if a in city_dict.keys():
                option.extend( city_dict[a] )

    return [{ 'label' : m , 'value' : m } for m in option ]


def main():  # Main Function
    global app

    # Calling Fuctions
    load_data()
    open_browser()
    app.layout = create_app_ui()  # Creating Layout of Application
    
    app.title = "Terrorism Analysis with Insights"  # Setting title of Web-Page
    app.run_server()  # Starting / Running Server of Web-Page

    print("This would be executed only after the script is closed")
    app = None  # Industry Best Practice to make all Global variables None


if __name__ == '__main__':  # Function to call main function
    main()

