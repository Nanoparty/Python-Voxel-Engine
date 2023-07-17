#version 410 core

layout (location = 0) out vec4 fragColor;

uniform sampler2DArray crosshair_texture;

void main(){
    fragColor = texture(crosshair_texture, uv);
}