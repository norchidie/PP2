import pygame as pg
import os
from sys import exit

# Function to load all mp3 files from a directory
def load_playlist(directory):
    playlist = []
    all_songs = os.listdir(directory)
    for song in all_songs:
        if song.endswith(".mp3"):
            playlist.append(os.path.join(directory, song))
    return playlist

def main():
    music_directory = r"C:\Users\TUF\Desktop\PP2\Lab7\music player\MUSICA"
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((500, 250))
    pg.display.set_caption("Music Player")

    # Load icon
    icon = pg.image.load("icon.png")
    pg.display.set_icon(icon)

    # Load playlist and initialize current song index
    playlist = load_playlist(music_directory)
    if not playlist:
        print("No MP3 files found in the specified directory.")
        return
    current_song_index = 0
    current_song = playlist[current_song_index]
    pg.mixer.init()
    pg.mixer.music.load(current_song)
    pg.mixer.music.play()

    # Load images
    bg = pg.Surface((500, 500))
    pg.Surface.fill(bg, (241, 203, 255))
    btn_play = pg.image.load("playbutton.png")
    btn_pause = pg.image.load("pausebutton.png")
    btn_next = pg.image.load("nextbutton1.png")
    btn_next2 = pg.image.load("nextbutton2.png")
    btn_prev = pg.image.load("prevbutton.png")
    btn_prev2 = pg.image.load("prevbutton2.png")

    # Flags and variables for button animation
    playing = True
    next_pressed = False
    prev_pressed = False
    next_tm = 0
    prev_tm = 0

    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.pause()
                    else:
                        pg.mixer.music.unpause()
                elif event.key == pg.K_RIGHT:
                    current_song_index = (current_song_index + 1) % len(playlist)
                    pg.mixer.music.stop()
                    current_song = playlist[current_song_index]
                    pg.mixer.music.load(current_song)
                    pg.mixer.music.play()
                    next_pressed = True
                    if not pg.mixer.music.get_busy():
                        pg.mixer.music.pause()
                elif event.key == pg.K_LEFT:
                    current_song_index = (current_song_index - 1 + len(playlist)) % len(playlist)
                    pg.mixer.music.stop()
                    current_song = playlist[current_song_index]
                    pg.mixer.music.load(current_song)
                    pg.mixer.music.play()
                    prev_pressed = True
                    if not pg.mixer.music.get_busy():
                        pg.mixer.music.pause()
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the boundaries of the buttons
                if 195 <= event.pos[0] <= 305 and 90 <= event.pos[1] <= 140:
                    if pg.mixer.music.get_busy():
                        pg.mixer.music.pause()
                    else:
                        pg.mixer.music.unpause()
                elif 295 <= event.pos[0] <= 405 and 90 <= event.pos[1] <= 140:
                    current_song_index = (current_song_index + 1) % len(playlist)
                    pg.mixer.music.stop()
                    current_song = playlist[current_song_index]
                    pg.mixer.music.load(current_song)
                    pg.mixer.music.play()
                    if not pg.mixer.music.get_busy():
                        pg.mixer.music.pause()
                elif 95 <= event.pos[0] <= 205 and 90 <= event.pos[1] <= 140:
                    current_song_index = (current_song_index - 1 + len(playlist)) % len(playlist)
                    pg.mixer.music.stop()
                    current_song = playlist[current_song_index]
                    pg.mixer.music.load(current_song)
                    pg.mixer.music.play()
                    if not pg.mixer.music.get_busy():
                        pg.mixer.music.pause()

        screen.blit(bg, (0, 0))

        # Display currently playing song
        font1 = pg.font.SysFont('calibri', 20, True)
        font2 = pg.font.SysFont('calibri', 15)
        text1 = font1.render("Currently playing:", True, (138, 25, 151))
        text2 = font2.render(os.path.basename(current_song), True, (99, 20, 108))
        screen.blit(text1, (25, 25))
        screen.blit(text2, (100, 50))

        # Display play/pause button
        if pg.mixer.music.get_busy():
            screen.blit(btn_pause, (195, 90))
        else:
            screen.blit(btn_play, (195, 90))

        # Display next and previous buttons with animation
        if next_pressed:
            screen.blit(btn_next2, (295, 90))
            next_tm += 1
        else:
            screen.blit(btn_next, (295, 90))

        if prev_pressed:
            screen.blit(btn_prev2, (95, 90))
            prev_tm += 1
        else:
            screen.blit(btn_prev, (95, 90))

        # Reset animation timers
        if next_tm >= 8:
            next_pressed = False
            next_tm = 0
        if prev_tm >= 8:
            prev_pressed = False
            prev_tm = 0

        pg.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
