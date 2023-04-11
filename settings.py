class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (150, 230, 230)
        # Настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (230, 230, 230)