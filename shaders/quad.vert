#version 410 core

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_color;

out vec2 uv;

void main() {
    uv = vec2(in_color.x, in_color.y);
    gl_Position = vec4(in_position, 1.0);
}