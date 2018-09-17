#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:54:52 2018

@author: wulala
"""

import os
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url":"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})
revenue = [1000,2000,6000,2000]
items = ["娛樂","零食","住宿費","孝親費"]
colors = ['rgba(255, 0, 0, 0.4)','rgba(201, 0, 10, 0.4)','rgba(255, 0, 30, 0.4)','rgba(255, 20, 0, 0.4)']
app.layout = html.Div(  
    [
        html.Br(),
        html.Div([
            html.Div(
                dcc.Graph(
                    id="graph-1",
                    figure=dict(
                        marker={"color":colors},
                        data=[go.Pie(values=revenue,labels=items )],
                        layout={"title":"花費比例","width":"300","height":"300"}
                    )      
                ),
                className="col" ,
                style={"margin-left":"100" }     
            ),
            html.Div(
                dcc.Graph(
                    id="graph-2",
                    figure=dict(                     
                        data=[go.Bar(x=revenue,y=items ,orientation = 'h',marker={"color":"rgba(205,0,0,0.2)"},)], 
                        layout={"title":"各項花費(元)","width":"300","height":"300"}
                    )
                ),
                className="col"
            )],
            className="row justify-content-center",
            style={"width":"760"}
        ),
        html.Div([
            dcc.Slider(min=1000,max=10000,step=500,value=revenue[i],id="slider_{}".format(i) ) for i in range(len(items))        
            ],
            style={"margin-top":"-50","width":"500","margin-left":"200"},
        )
    ],
    className="container",
    style={"height":"900","width":"1000"},
    id="demo_1"
)
@app.callback( Output('graph-1','figure'),[Input('slider_0','value'),Input('slider_1','value'),Input('slider_2','value'),Input('slider_3','value')] )
def update(value_0,value_1,value_2,value_3):
    revenue = [ value_0,value_1,value_2,value_3]
    return {
        "data":[go.Pie(values=revenue,labels=items )],
        "layout":{"title":"花費比例","width":"300","height":"300"}
    }
@app.callback( Output('graph-2','figure'),[Input('slider_0','value'),Input('slider_1','value'),Input('slider_2','value'),Input('slider_3','value')] )
def update_1(value_0,value_1,value_2,value_3):
    revenue = [value_0,value_1,value_2,value_3]
    return {
        "data":[go.Bar(x=revenue,y=items ,orientation = 'h')],
        "layout":{"title":"各項花費(元)","xaxis":{'range':[1000,10000]}}
    }
if __name__ == "__main__":
    app.run_server(debug=True)
