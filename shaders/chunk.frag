#version 410 core

layout (location = 0) out vec4 fragColor;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;
const vec3 bg_color = vec3(0.58, 0.83, 0.99);

uniform sampler2DArray u_texture_array_0;

in vec3 voxel_color;
in vec2 uv;
in float shading;

flat in int face_id;
flat in int voxel_id;

void main(){
    vec2 face_uv = uv;
    face_uv.x = uv.x / 3.0 - min(face_id, 2) / 3.0;

    vec3 tex_col = texture(u_texture_array_0, vec3(face_uv, voxel_id)).rgb;
    tex_col = pow(tex_col, gamma);

    // tex_col.rgb *= voxel_color;
    //tex_col = tex_col * 0.001 + vec3(1);
    tex_col *= shading;

    tex_col = pow(tex_col, inv_gamma);

    //fog
    float fog_dist = gl_FragCoord.z / gl_FragCoord.w;
    tex_col = mix(tex_col, bg_color, (1.0 - exp2(-0.000015 * fog_dist * fog_dist)));

    fragColor = vec4(tex_col, 1);

    
}