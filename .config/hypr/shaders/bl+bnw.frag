precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {
    vec4 pixColor = texture2D(tex, v_texcoord);

    // Step 1: Reduce blue light (adjust blue component)
    pixColor.b *= 0.5;

    // Step 2: Convert to grayscale using weighted luminance formula
    float gray = 0.299 * pixColor.r + 0.587 * pixColor.g + 0.114 * pixColor.b;

    // Apply the grayscale value
    gl_FragColor = vec4(vec3(gray), pixColor.a);
}
