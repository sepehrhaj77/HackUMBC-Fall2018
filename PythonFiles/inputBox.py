import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
#COLOR_INACTIVE = pygame.Color('lightskyblue3')
#COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:
    FONT = pygame.font.Font(None, 32)

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.txt_surface = InputBox.FONT.render(text, True, self.color)
        self.active = True

    def handle_event(self, event):
       
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    #return the text at here
                    self.text = ''

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
     
        self.rect.w = 600

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def main():

    input_box = InputBox(100, 500, 140, 32)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            input_box.handle_event(event)

     
        input_box.update()

        screen.fill((30, 30, 30))

        input_box.draw(screen)

        pygame.display.flip()
    


if __name__ == '__main__':
    main()
    pygame.quit()