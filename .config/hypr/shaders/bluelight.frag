precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {
    vec4 pixColor = texture2D(tex, v_texcoord);

    // Reduce blue component more aggressively
    pixColor[2] *= 0.5;

    // Optionally, boost the red component for a warmer effect
    pixColor[0] *= 1.1;

    // Output the adjusted color
    gl_FragColor = pixColor;
}
