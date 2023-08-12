from settings import *
from world import World
from world_objects.voxel_marker import VoxelMarker
from world_objects.crosshair import Crosshair
from meshes.quad_mesh import QuadMesh
from world_objects.hotbar import HotBar
from world_objects.inventory import Inventory
from meshes.underwater_mesh import UnderwaterMesh

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        self.quad_mesh = QuadMesh(self.app)
        self.hotbar = HotBar(self.world.voxel_handler)
        self.inventory = Inventory(self.world.voxel_handler)
        self.underwater = UnderwaterMesh(self.app)

    def update(self):
        self.world.update()
        self.voxel_marker.update()
        self.hotbar.update()
        self.inventory.update()
        player_pos = glm.ivec3(int(self.app.player.position.x),int(self.app.player.position.y), int(self.app.player.position.z))
        voxel_id = self.get_voxel_id(player_pos)
        if voxel_id[0] == WATER:
            self.app.player.underwater = True
        else:
            self.app.player.underwater = False

    def render(self):
        self.world.render()
        self.voxel_marker.render()
        self.underwater.render(self.app.player)
        self.inventory.render()
        self.quad_mesh.render()
        self.hotbar.render()

    def get_voxel_id(self, voxel_world_pos):
        cx, cy, cz = chunk_pos = voxel_world_pos / CHUNK_SIZE

        if 0 <= cx < WORLD_W and 0 <= cy < WORLD_H and 0 <= cz < WORLD_D:
            chunk_index = int(cx + WORLD_W * cz + WORLD_AREA * cy)
            chunk = self.world.chunks[chunk_index]

            lx, ly, lz = voxel_local_pos = voxel_world_pos - chunk_pos * CHUNK_SIZE

            voxel_index = lx + CHUNK_SIZE * lz + CHUNK_AREA * ly
            voxel_id = chunk.voxels[voxel_index]

            return voxel_id, voxel_index, voxel_local_pos, chunk
        return 0, 0, 0, 0
        
        
        