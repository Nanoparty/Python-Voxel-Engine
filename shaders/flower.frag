#version 410 core

layout (location = 0) out vec4 fragColor;

in vec2 uv;

uniform sampler2D u_texture_0;

void main() {
    fragColor = texture(u_texture_0, uv);
    fragColor.a = (fragColor.r + fragColor.g + fragColor.b == 0) ? 0.0: 1.0;
}
