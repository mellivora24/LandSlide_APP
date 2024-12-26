"""
This module is responsible for connecting the GUI to the controller
and the model. It will listen to the events from the GUI and call the services
"""

def connect_gui(gui):
    """
    Connect the GUI components with functions in this module
    :param gui: the GUI object
    :return: none
    """
    pass

def on_point_box_clicked(point_id):
    """
    Show the detail of a point and place, where point located when the point box is clicked
    :param point_id: the id of the point
    :return: none
    """
    print(f'Point box {point_id} is clicked')

def on_receive_point_data(point_id, data):
    """
    Handle the event when the data of a point is received and update the GUI
    :param point_id: the id of the point
    :param data: the data of the point
    :return: none
    """
    pass
