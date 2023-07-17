#version 410 core

// layout (location = 0) in vec2 in_tex_coord_0;
// layout (location = 1) in vec3 in_position;

// out vec2 uv;

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_color;

void main(){
    // uv = in_tex_coord_0;
    // gl_Position = vec4(in_position, 1.0);
    color = in_color;
    gl_Position = vec4(in_position, 1.0);
}