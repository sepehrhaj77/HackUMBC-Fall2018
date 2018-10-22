import pygame
pygame.init()



class Textprint(object):

    def __init__(self, text):
        self.m_text = text

    def changeText(self, text):
        self.m_text = text

    def blit_text(self, surface, pos, font=pygame.font.SysFont('Arial', 25), color=pygame.Color('black')):
        words = [word.split(' ') for word in self.m_text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = 600, 100
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

        surface.display.update()

