from meshes.base_mesh import BaseMesh
from meshes.chunk_mesh_builder import build_chunk_mesh, build_sorted_chunk_mesh
from random import random


class ChunkMesh(BaseMesh):
    def __init__(self, chunk, transparent=False):
        super().__init__()
        self.app = chunk.app
        self.chunk = chunk
        self.ctx = self.app.ctx
        self.program = self.app.shader_program.chunk
        self.is_transparent = transparent

        self.vbo_format = '1u4'
        self.format_size = sum(int(fmt[:1]) for fmt in self.vbo_format.split())
        self.attrs = ('packed_data',)
        self.vao = self.get_vao()

    def rebuild(self):
        self.vao = self.get_vao()

    def rebuild_transparent(self):
        if self.is_transparent:
            self.vao = self.get_vao()

    def get_vertex_data(self):
        if self.is_transparent:
            return build_sorted_chunk_mesh(
            chunk_voxels=self.chunk.voxels,
            format_size=self.format_size,
            chunk_pos=self.chunk.position,
            world_voxels=self.chunk.world.voxels,
            player_pos=self.app.player.position
            )
        else:
            return build_chunk_mesh(
            chunk_voxels=self.chunk.voxels,
            format_size=self.format_size,
            chunk_pos=self.chunk.position,
            world_voxels=self.chunk.world.voxels,
            transparent=self.is_transparent
            )

    def render(self):
        #print("render chunk mesh", random())
        #self.rebuild_transparent()
        self.vao.render()