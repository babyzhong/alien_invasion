class Settings:
    """class which store all settings"""

    def __init__(self):
        """init game setting"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # setting of ship
        self.ship_speed_factor = 1.5

        # setting of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
