"""Chart generation utilities"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_stock_by_location_chart(df: pd.DataFrame):
    """Bar chart: Stock quantity by location"""
    location_stats = df.groupby('Location')['Stock_Qty'].sum().reset_index()
    location_stats = location_stats.sort_values('Stock_Qty', ascending=False).head(10)

    fig = px.bar(
        location_stats,
        x='Location',
        y='Stock_Qty',
        title='Top 10 Locations by Stock Quantity',
        labels={'Stock_Qty': 'Total Stock', 'Location': 'Location'},
        color='Stock_Qty',
        color_continuous_scale='Blues'
    )
    fig.update_layout(height=400, showlegend=False)
    return fig

def create_condition_pie_chart(df: pd.DataFrame):
    """Pie chart: Condition distribution"""
    condition_stats = df['Condition'].value_counts().reset_index()
    condition_stats.columns = ['Condition', 'Count']

    fig = px.pie(
        condition_stats,
        values='Count',
        names='Condition',
        title='Component Condition Distribution',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    fig.update_layout(height=400)
    return fig

def create_manufacturer_chart(df: pd.DataFrame):
    """Bar chart: Components by manufacturer"""
    mfg_stats = df['Manufacturer'].value_counts().reset_index()
    mfg_stats.columns = ['Manufacturer', 'Count']

    fig = px.bar(
        mfg_stats,
        x='Manufacturer',
        y='Count',
        title='Components by Manufacturer',
        labels={'Count': 'Number of Components'},
        color='Count',
        color_continuous_scale='Greens'
    )
    fig.update_layout(height=400, showlegend=False)
    return fig

def create_maintenance_trend_chart(df: pd.DataFrame):
    """Line chart: Maintenance tasks over time"""
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    trend = df_copy.groupby('Date').size().reset_index(name='Count')
    trend = trend.sort_values('Date')

    fig = px.line(
        trend,
        x='Date',
        y='Count',
        title='Maintenance Tasks Over Time',
        labels={'Count': 'Number of Tasks', 'Date': 'Date'},
        markers=True
    )
    fig.update_layout(height=400)
    return fig

def create_task_type_chart(df: pd.DataFrame):
    """Bar chart: Tasks by type"""
    task_stats = df['Task_Type'].value_counts().reset_index()
    task_stats.columns = ['Task_Type', 'Count']

    fig = px.bar(
        task_stats,
        x='Task_Type',
        y='Count',
        title='Tasks by Type',
        labels={'Count': 'Number of Tasks'},
        color='Task_Type',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(height=400, showlegend=False)
    return fig

def create_outcome_chart(df: pd.DataFrame):
    """Bar chart: Outcome distribution"""
    outcome_stats = df['Outcome'].value_counts().reset_index()
    outcome_stats.columns = ['Outcome', 'Count']

    colors = {'Pass': 'green', 'Fail': 'red', 'Warning': 'orange'}
    color_map = [colors.get(x, 'blue') for x in outcome_stats['Outcome']]

    fig = go.Figure(data=[
        go.Bar(
            x=outcome_stats['Outcome'],
            y=outcome_stats['Count'],
            marker_color=color_map
        )
    ])
    fig.update_layout(title='Maintenance Outcomes', height=400)
    return fig

def create_technician_workload_chart(df: pd.DataFrame):
    """Bar chart: Technician workload"""
    tech_stats = df['Technician'].value_counts().reset_index()
    tech_stats.columns = ['Technician', 'Tasks']

    fig = px.bar(
        tech_stats,
        x='Technician',
        y='Tasks',
        title='Technician Workload',
        labels={'Tasks': 'Number of Tasks'},
        color='Tasks',
        color_continuous_scale='Purples'
    )
    fig.update_layout(height=400, showlegend=False)
    return fig

def create_tool_status_chart(df: pd.DataFrame):
    """Pie chart: Tool status distribution"""
    status_stats = df['Status'].value_counts().reset_index()
    status_stats.columns = ['Status', 'Count']

    fig = px.pie(
        status_stats,
        values='Count',
        names='Status',
        title='Tool Status Distribution',
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig.update_layout(height=400)
    return fig

def create_tool_usage_chart(df: pd.DataFrame):
    """Bar chart: Tool usage by technician"""
    tech_stats = df['Assigned_To'].value_counts().reset_index()
    tech_stats.columns = ['Technician', 'Checkouts']

    fig = px.bar(
        tech_stats,
        x='Technician',
        y='Checkouts',
        title='Tool Checkouts by Technician',
        labels={'Checkouts': 'Number of Checkouts'},
        color='Checkouts',
        color_continuous_scale='Teal'
    )
    fig.update_layout(height=400, showlegend=False)
    return fig

def create_gauge_chart(value: int, total: int, title: str):
    """Gauge chart for availability"""
    percentage = (value / total * 100) if total > 0 else 0

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=percentage,
        title={'text': title},
        delta={'reference': 80},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig.update_layout(height=300)
    return fig
