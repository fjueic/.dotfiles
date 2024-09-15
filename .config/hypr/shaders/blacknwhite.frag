precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {
    vec4 pixColor = texture2D(tex, v_texcoord);

    // Calculate luminance (grayscale value)
    float gray = (pixColor.r + pixColor.g + pixColor.b) / 3.0;

    // Set all color components to the grayscale value
    gl_FragColor = vec4(vec3(gray), pixColor.a);
}
