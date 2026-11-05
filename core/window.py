from pyray import *

class Window:
    def __init__(self, title="darcia", width=1280, height=720, fps_limit=60):
        self.title = title
        self.width = width
        self.height = height

        if fps_limit >= 121:
            print("[warning]: High FPS will be ignored. Switching to 120 FPS...")
            self.fps_limit = 120
        else:
            self.fps_limit = fps_limit

        set_trace_log_level(LOG_NONE)
        
        init_window(self.width, self.height, self.title.encode('utf-8'))
        set_target_fps(self.fps_limit)
        print("[info]: Window successfully created.")

    def run(self, draw_callback=None):
        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)

            if draw_callback:
                draw_callback()
            
            end_drawing()
        
        close_window()
