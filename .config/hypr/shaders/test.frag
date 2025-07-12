precision mediump float;

uniform sampler2D u_texture;
varying vec2 v_texcoord;

void main() {
    vec4 color = texture2D(u_texture, v_texcoord);

    // Calculate brightness (luminance)
    float brightness = dot(color.rgb, vec3(0.299, 0.587, 0.114));

    // Checkerboard pattern (based on screen coords)
    ivec2 pixel = ivec2(gl_FragCoord.xy);
    bool checker = (pixel.x % 2 == 0) != (pixel.y % 2 == 0);

    // Only modify bright pixels
    float brightThreshold = 0.85;
    if (brightness > brightThreshold && checker) {
        // Turn off or dim the pixel
        color.rgb *= 0.3; // Or set to vec3(0.0) to fully drop it
    }

    gl_FragColor = color;
}

