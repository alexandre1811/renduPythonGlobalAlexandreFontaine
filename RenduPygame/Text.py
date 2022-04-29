import pygame


def textZone(text, size, color, font):
    text_font = pygame.font.SysFont(font, size)
    return text_font.render(text, True, color)


def textShow(text, size, color, frame, pos, font="Calibri"):
    zone = textZone(text, size, color, font)
    rect = zone.get_rect()
    frame.blit(zone, (pos[0] - rect.w / 2, pos[1] - rect.h / 2))
