class Devices:
    def __init__(self, name, connected_by, brand):
        self.name = name
        self.connected_by = connected_by
        self.is_connected = True
        self.brand = brand
    def connect(self):
        pass

    def disconnect(self):
        self.is_connected = False
        pass



class Keyboard(Devices):
    def __init__(self, name, connected_by, brand, type, lang):
        super().__init__(name, connected_by, brand)
        self.type = type
        self.lang = lang

class Mouse(Devices):
    def __init__(self,name, connected_by, brand, dpi, wireless):
        super().__init__(name, connected_by, brand)
        self.dpi = dpi
        self.wireless = wireless

class Screen(Devices):
    def __init__(self, name, connected_by, brand, size, resolution):
        super().__init__(name, connected_by, brand)
        self.size = size
        self.resolution = resolution

class Usb(Devices):
    def __init__(self, name, connected_by, brand, capacity, usb_type):
        super().__init__(name, connected_by, brand)
        self.capacity = capacity
        self.usb_type = usb_type

class Charger(Devices):
    def __init__(self, name, connected_by, brand, power, port_type):
        super().__init__(name, connected_by, brand)
        self.power = power
        self.port_type = port_type

class Camera(Devices):
    def __init__(self, name, connected_by, brand, megapixels, cam_type):
        super().__init__(name, connected_by, brand)
        self.megapixels = megapixels
        self.cam_type = cam_type

class Headset(Devices):
    def __init__(self, name, connected_by, brand, wireless, mic):
        super().__init__(name, connected_by, brand)
        self.wireless = wireless
        self.mic = mic
        
GuysHeadset = Headset("GPheadset", "wireless", "logitech", "wireless", "has_mic")
