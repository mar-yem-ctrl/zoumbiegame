import pygame

class Inventory:
    def __init__(self, max_slots=5):
        self.max_slots = max_slots
        self.items = []  # List gha t-koun fiha l-items lli haz (مثلا: ["Pistol", "Medkit"])
        self.selected_index = 0  # L-item lli khdam bih dba (0 huwa l-wlani)
        
        # Colors & Font
        self.font = pygame.font.SysFont("Arial", 16, bold=True)
        self.WHITE = (255, 255, 255)
        self.GRAY = (80, 80, 80)
        self.DARK_GRAY = (30, 30, 30)
        self.YELLOW = (255, 215, 0) # l-lawn dyal s-sandouq lli m-selectionner dba

    def add_item(self, item):
        """Zid item jdid l-inventory ila bqat l-blasa"""
        if len(self.items) < self.max_slots:
            self.items.append(item)
            return True # T-zadd b-najah
        return False # L-inventory 3amra!

    def remove_item(self, item):
        """Hyyed item (مثلا mlli t-khdem b Medkit)"""
        if item in self.items:
            self.items.remove(item)
            # Ila khwat l-inventory aw l-index khrej 3la l-hadd, n-gaddo l-selected_index
            if self.selected_index >= len(self.items) and len(self.items) > 0:
                self.selected_index = len(self.items) - 1
            return True
        return False

    def get_active_item(self):
        """Rjja3 l-item lli haz l-player f-iddih dba"""
        if self.items and 0 <= self.selected_index < len(self.items):
            return self.items[self.selected_index]
        return None

    def next_item(self):
        """Zid l-quddam f-l-selection (mlli t-dor l-wheel dyal l-mouse)"""
        if self.items:
            self.selected_index = (self.selected_index + 1) % len(self.items)

    def prev_item(self):
        """Rje3 l-lor f-l-selection"""
        if self.items:
            self.selected_index = (self.selected_index - 1) % len(self.items)

    def draw(self, screen):
        """Rsem s-snadeq dyal l-inventory l-teht f-shasha"""
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        slot_size = 50
        spacing = 10
        # N-hesbo l-width l-kamla dyal l-inventory bsh n-jibouha f l-wasat
        total_width = (self.max_slots * slot_size) + ((self.max_slots - 1) * spacing)
        start_x = (screen_width - total_width) // 2
        y_pos = screen_height - slot_size - 20 # 20px m-l-teht dyal l-shasha

        for i in range(self.max_slots):
            x_pos = start_x + i * (slot_size + spacing)
            
            # Ila kan had s-sandouq huwa lli m-selectionner dba, n-diro lih cadre sfer
            border_color = self.YELLOW if i == self.selected_index else self.GRAY
            border_thickness = 3 if i == self.selected_index else 1
            
            # 1. Rsem s-sandouq (l-background dyalu)
            pygame.draw.rect(screen, self.DARK_GRAY, (x_pos, y_pos, slot_size, slot_size))
            pygame.draw.rect(screen, border_color, (x_pos, y_pos, slot_size, slot_size), border_thickness)
            
            # 2. Rsem l-item dakhil s-sandouq (ila kan kayn)
            if i < len(self.items):
                item_name = self.items[i]
                # Hna drna text baset, m-b3d tqder t-beddel hadchi b-tsawer (sprites)
                text_surface = self.font.render(item_name[:5], True, self.WHITE) # n-khedmo b awwel 5 hrouf bsh y-qddou
                text_rect = text_surface.get_rect(center=(x_pos + slot_size//2, y_pos + slot_size//2))
                screen.blit(text_surface, text_rect)