import pygame
import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory(title="Select a folder containing images")
files = os.listdir(folder_path)
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
file_index = 0
clock2 = 0
fps = 1
text_margin = 10
pygame.font.init()
font = pygame.font.Font(r"c:\USERS\LUCAS\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\PRODUCT SANS REGULAR.TTF", 150)
fill_screen = False
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
image = pygame.image.load(folder_path + "/" + image_files[0])
screen.blit(image, (0, 0))
def display_text(surface, text, font, color, margin):
    text_surface = font.render(text, True, color)
    text_surface.set_alpha(220)
    text_rect = text_surface.get_rect()
    text_rect.bottomright = surface.get_rect().bottomright
    text_rect.x -= margin + 30  # Adjust x-coordinate by margin
    text_rect.y -= margin + 40  # Adjust y-coordinate by margin
    surface.blit(text_surface, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    if clock2 == 3:
        clock2 = 0
        file_index += 1
        if file_index > len(image_files) - 1:
            file_index = 0
        image = pygame.image.load(folder_path + "/" + image_files[file_index])
    
    screen.fill((0,0,0))
    #groter dan 16/9 dan minder hoog
    #kleiner dan 16/9 dan minder wijd
    if not fill_screen:
        if image.get_width() / image.get_height() > 16/9:
            scaling_factor = 1920 / image.get_width()
            #image = pygame.transform.scale(image, (1920, image.get_height() * scaling_factor))
            image = pygame.transform.smoothscale_by(image, scaling_factor)
            position = (0, 1080/2 - image.get_height() / 2)
        if image.get_width() / image.get_height() < 16/9:
            scaling_factor = 1080 / image.get_height()
            #image = pygame.transform.scale(image, (image.get_width() * scaling_factor, 1080))
            image = pygame.transform.smoothscale_by(image, scaling_factor)
            position = (1920/2 - image.get_width() /2, 0)
        if image.get_width() / image.get_height() == 16/9:
            position = (0, 0)
    if fill_screen:
        if image.get_width() / image.get_height() > 16/9:
            scaling_factor = 1080 / image.get_height()
            #image = pygame.transform.scale(image, (1920, image.get_height() * scaling_factor))
            image = pygame.transform.smoothscale_by(image, scaling_factor)
            position = (1920/2 - image.get_width() / 2, 0)
        if image.get_width() / image.get_height() < 16/9:
            scaling_factor = 1920 / image.get_width()
            #image = pygame.transform.scale(image, (image.get_width() * scaling_factor, 1080))
            image = pygame.transform.smoothscale_by(image, scaling_factor)
            position = (0, 1080/2 - image.get_height() /2)
        if image.get_width() / image.get_height() == 16/9:
            position = (0, 0)
    screen.blit(image, position)
    now = datetime.now()
    formatted_time = now.strftime('%H:%M')
    
    
    
    display_text(screen, formatted_time, font, (230, 230, 230), text_margin)

    clock2 += 1
    
        
    clock.tick(fps)
    fps = 1/5