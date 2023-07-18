import pygame as pg
from camera import Camera
from settings import *
from world_objects.crosshair import Crosshair

class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)
        

    def update(self):
        self.keyboard_controls()
        self.mouse_control()
        super().update()

    def render(self):
        pass
    
    def handle_event(self, event, pg):
        voxel_handler = self.app.scene.world.voxel_handler

        
        if event.type == pg.MOUSEBUTTONDOWN:

            # adding and removing voxels with clicks
            if event.button == 1:
                voxel_handler.set_voxel()
                print("Mouse Pos:", pg.mouse.get_pos())
                print("Voxel_id:", voxel_handler.new_voxel_id)
            if event.button == 3:
                voxel_handler.switch_mode()
        
        # changing block types
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_0:
                voxel_handler.set_voxel_id(10)
            if event.key == pg.K_1:
                voxel_handler.set_voxel_id(1)
            if event.key == pg.K_2:
                voxel_handler.set_voxel_id(2)
            if event.key == pg.K_3:
                voxel_handler.set_voxel_id(3)
            if event.key == pg.K_4:
                voxel_handler.set_voxel_id(4)
            if event.key == pg.K_5:
                voxel_handler.set_voxel_id(5)
            if event.key == pg.K_6:
                voxel_handler.set_voxel_id(6)
            if event.key == pg.K_7:
                voxel_handler.set_voxel_id(7)
            if event.key == pg.K_8:
                voxel_handler.set_voxel_id(8)
            if event.key == pg.K_9:
                voxel_handler.set_voxel_id(9)

        if event.type == pg.MOUSEWHEEL:
            print(event.x, event.y)
            if event.y == 1:
                voxel_handler.set_voxel_id(voxel_handler.new_voxel_id + 1)
            if event.y == -1:
                voxel_handler.set_voxel_id(voxel_handler.new_voxel_id - 1)

        

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSITIVITY)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSITIVITY)

    def keyboard_controls(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.delta_time
        if key_state[pg.K_w]:
            self.move_forward(vel)
        if key_state[pg.K_s]:
            self.move_back(vel)
        if key_state[pg.K_a]:
            self.move_left(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
        if key_state[pg.K_SPACE]:
            self.move_up(vel)
        if key_state[pg.K_LCTRL]:
            self.move_down(vel)