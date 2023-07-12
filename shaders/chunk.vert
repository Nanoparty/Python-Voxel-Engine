#version 410 core

layout (location = 0) in ivec3 in_position;
layout (location = 1) in int voxel_id;
layout (location = 2) in int face_id;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

void main(){
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}