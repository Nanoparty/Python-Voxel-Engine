#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D crosshair_texture;

in vec2 uv;

void main(){
    fragColor = vec4(texture(crosshair_texture, uv).rgb, 1.0);
}