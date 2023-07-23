import pygame as pg
from camera import Camera
from settings import *
from world_objects.crosshair import Crosshair
from meshes.underwater_mesh import UnderwaterMesh

class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)
        #self.underwater_mesh = UnderwaterMesh(app)
        self.open_inventory = False
        self.underwater = False
        # if self.app.scene:
        #     self.chunks = self.app.scene.world.chunks
        

    def update(self, pg):
        self.keyboard_controls()
        self.mouse_control(pg)
        super().update()
        # if self.chunks:
        #     voxel_type = self.get_voxel_id(self.position)
        #     print("Voxel Type: ", voxel_type)

    def render(self):
        pass
        #self.underwater_mesh.render()

    def get_voxel_id(self, voxel_world_pos):
        cx, cy, cz = chunk_pos = voxel_world_pos / CHUNK_SIZE

        if 0 <= cx < WORLD_W and 0 <= cy < WORLD_H and 0 <= cz < WORLD_D:
            chunk_index = cx + WORLD_W * cz + WORLD_AREA * cy
            chunk = self.chunks[chunk_index]

            lx, ly, lz = voxel_local_pos = voxel_world_pos - chunk_pos * CHUNK_SIZE

            voxel_index = lx + CHUNK_SIZE * lz + CHUNK_AREA * ly
            voxel_id = chunk.voxels[voxel_index]

            return voxel_id, voxel_index, voxel_local_pos, chunk
        return 0, 0, 0, 0
    
    def handle_event(self, event, pg):
        voxel_handler = self.app.scene.world.voxel_handler
        inventory = self.app.scene.inventory

        # toggle inventory
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                inventory.toggle_visible()
                self.open_inventory = 1 - self.open_inventory
                if self.open_inventory:
                    pg.mouse.set_visible(True)
                else:
                    pg.mouse.set_visible(False)
                    pg.mouse.set_pos(WIN_RES.x / 2, WIN_RES.y / 2)
                    pg.mouse.get_rel()
        
        if event.type == pg.MOUSEBUTTONDOWN:

            # adding and removing voxels with clicks
            if event.button == 1:
                voxel_handler.set_voxel(pg, self.app.sounds)
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

        

    def mouse_control(self, pg):
        if self.open_inventory:
            return
        
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSITIVITY)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSITIVITY)

        pg.mouse.set_pos(WIN_RES.x / 2, WIN_RES.y / 2)

    def keyboard_controls(self):
        if self.open_inventory:
            return
        
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