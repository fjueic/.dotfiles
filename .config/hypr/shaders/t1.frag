precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;
uniform sampler2D blueNoiseTex;
uniform vec2 resolution;

void main() {
    vec4 color = texture2D(tex, v_texcoord);

    // Sample blue noise at pixel coords
    vec2 noiseUV = mod(floor(v_texcoord * resolution), vec2(128.0)) / 128.0; // assuming 128x128 noise texture
    float noise = texture2D(blueNoiseTex, noiseUV).r;

    float brightness = (color.r + color.g + color.b) / 3.0;

    // Threshold based on brightness and noise to turn off some pixels
    if (brightness < noise) {
        gl_FragColor = vec4(0.0, 0.0, 0.0, color.a);
    } else {
        gl_FragColor = color;
    }
}

