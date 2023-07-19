from settings import *
from meshes.base_mesh import BaseMesh
from array import array

class HotBarIconMesh(BaseMesh):
    def __init__(self, app, y=-0.83):
        super().__init__()

        self.app = app;
        self.ctx = app.ctx
        self.program = app.shader_program.hotbar_icon
        self.y = y

        self.vbo_format = '3f 3f'
        self.attrs = ('in_position', 'tex_coords',)
        self.vao = self.get_vao()
        

    def get_vertex_data(self):

        length = 0.06 * ASPECT_RATIO
        vertices = [
            (0.03, self.y, 0.0), (-0.03, self.y, 0.0), (-0.03, self.y - length, 0.0),
            (0.03, self.y, 0.0), (-0.03, self.y - length, 0.0), (0.03, self.y - length, 0.0)
        ]
        tex_coords = [
            (1, 1, 0), (0, 1, 0), (0, 0, 0),
            (1, 1, 0), (0, 0, 0), (1, 0, 0)
        ]

        vertex_data = np.hstack([vertices, tex_coords], dtype='float32')
        return vertex_data