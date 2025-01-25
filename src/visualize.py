import plotly.graph_objs as go
import plotly.express as px

# TODO: Separate each type of graph generation into a separate function?
def analyze_vehicle_data(positions, speeds):

    # Plot position as XY coordinates
    position_graph = go.Figure()

    # Adding Position Trace
    x, y = zip(*positions)
    position_graph.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Path', line=dict(color='blue')))

    # Set title and labels for position plot
    position_graph.update_layout(
        title='Vehicle Path',
        xaxis_title='X Coordinate [m]',
        yaxis_title='Y Coordinate [m]',
        showlegend=True
    )
    # Save position plot as HTML
    position_graph.write_html("../data/vehicle_path.html")

    # Create a subplot for the speed vs time plot
    speed_graph = go.Figure()

    # Adding Speed Trace
    speed_graph.add_trace(go.Scatter(y=speeds, mode='lines', name='Speed [m/s]', line=dict(color='red')))

    # Set title and labels for speed plot
    speed_graph.update_layout(
        title='Vehicle Speed Over Time',
        xaxis_title='Time [s]',
        yaxis_title='Speed [m/s]',
        showlegend=True
    )

    # Save speed plot as HTML
    speed_graph.write_html("../data/vehicle_speed.html")
