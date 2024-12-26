class point_data():
    def __init__(
        self, id: str, index: int, name: str, latitude: str, longitude: str, is_connecting: bool,
        titl_value: str, humidity_1: str, humidity_2: str, rain_flow_value: str
    ):
        self.id = id
        self.index = index
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.is_connecting = is_connecting
        self.titl_value = titl_value
        self.humidity_1 = humidity_1
        self.humidity_2 = humidity_2
        self.rain_flow_value = rain_flow_value
