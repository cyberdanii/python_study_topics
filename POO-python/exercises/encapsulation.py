from colorama import init, Style, Fore, Back

init()
color_yellow, color_cyan, color_magenta, color_red, color_black, color_reset  = Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.RED, Fore.BLACK, Fore.RESET
back_white, back_red, back_reset = Back.WHITE, Back.RED, Back.RESET

class house_base:
    porcents = {
        "rooms": 16,
        "baths": 10,
        "floors": 11,
    }
    def __init__(
        self, 
        type = None,
        location = {
            "neightboor": None, 
            "address": None
            }, 
        outside_colors = [], 
        inside_colors = [], 
        floors = 1, 
        cost = 0.00,
        rooms = 0):
        
        self.__type = type
        self.__location = location
        self.__outside_colors = outside_colors
        self.__inside_colors = inside_colors
        self.__floors = floors
        self.__cost = cost,
        self.__rooms = rooms
    @property
    def type(self): return self.__type
    @type.setter
    def type(self, value): self.__type = value
        
    @property
    def location(self): return self.__location
    @type.setter
    def location(self, value): self.__location = value
    
    @property
    def outside_colors(self): return self.__outside_colors
    @type.setter
    def outside_colors(self, value): self.__outside_colors = value
    
    @property
    def inside_colors(self): return self.__inside_colors
    @type.setter
    def inside_colors(self, value): self.__inside_colors = value
    
    @property
    def floors(self): return self.floors
    @type.setter
    def floors(self, value): self.floors = value
    
    @property
    def cost(self): return self.cost
    @type.setter
    def cost(self, value): self.cost = value
    
    @property
    def rooms(self): return self.rooms
    @type.setter
    def rooms(self, value): self.rooms = value
    
    # this is a example about how to use one function to get a lot of variables  by his name, I think lol..
    def get_privates(self, needed: str):
        if needed=="type":
            return self.type
        elif needed=="location":
            return self.location
        elif needed=="outside_colors":
            return self.outside_colors
        elif needed=="inside_colors":
            return self.inside_colors
        elif needed=="floors":
            return self.floors
        elif needed=="cost":
            return self.__cost
        elif self.needed=="rooms":
            return self.__rooms
        else:
            return "the needed variable does not exist"

    def __repr__(
        self, 
        type = None,
        inside_colors = None, 
        outside_colors = None,
        floors = None,
        rooms = None,
        cost = None,
        location = None,
        colored = False,
        ) -> str:

        """
        TARGET:
            return details about the object or instance
        PARAMS:
            inside_colors: list, 
            outside_colors: list,
            floors: int,
            rooms: int,
            cost: float,
            location: dict
        """
        if colored == False:
            return '{' + \
                '"detail":"House Properties",' + \
                f'"type": {type},' + \
                f'"floors": {floors},' + \
                f'"rooms": {rooms},' + \
                f'"cost": {cost},' + \
                f'"location": {location},' + \
                '"colors": {' + \
                    f'"inside colors": {inside_colors},' + \
                    f'"outside colors": {outside_colors},' + \
                '}, }'
        else:
            return '{' + \
                f'{back_white}{color_black}"detail":"House Properties"{color_reset}{back_reset},' + \
                f'{color_red}"type"{color_reset}: {color_cyan}{type}{color_reset},' + \
                f'{color_red}"floors"{color_reset}: {color_cyan}{floors}{color_reset},' + \
                f'{color_red}"rooms"{color_reset}: {color_cyan}{rooms}{color_reset},' + \
                f'{color_red}"cost"{color_reset}: {color_cyan}{cost}{color_reset},' + \
                f'{color_red}"location"{color_reset}: {color_cyan}{location}{color_reset},' + \
                f'{color_red}"colors"{color_reset}:'+' {' + \
                    f'{color_red}"inside colors"{color_reset}: {color_cyan}{inside_colors}{color_reset},' + \
                    f'{color_red}"outside colors"{color_reset}: {color_cyan}{outside_colors}{color_reset},' + \
                '}, }'

    def calculate_cost_rooms(self):
        ...

h = house_base()
h.type = "apartment"
print(f"{color_magenta}{h.type} : {type(h.type)}{Fore.RESET}")

print( f"{Fore.CYAN}" + h.get_privates("type") + f"{Fore.RESET}" )

print(h.__repr__(rooms = 4, type =  h.type, colored =  True ))