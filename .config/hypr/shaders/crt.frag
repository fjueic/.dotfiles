precision mediump float;

varying vec2 v_texcoord;
uniform sampler2D tex;
uniform float u_time;
const vec2 u_resolution = vec2(1920.0, 1080.0);

// --- Grain Noise ---
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453);
}

float grain(vec2 uv) {
    float noise = random(uv * u_resolution.xy + u_time * 0.1);
    return (noise - 0.5) * 0.03; // softer, centered grain
}

// --- Soft vignette effect ---
float vignette(vec2 uv) {
    vec2 pos = uv - 0.5;
    float len = length(pos);
    return smoothstep(0.8, 0.4, len); // soft vignette with less intensity
}

// --- Slight desaturation and warm tone ---
vec3 paperTone(vec3 color) {
    float gray = dot(color, vec3(0.3, 0.59, 0.11));
    return mix(color, vec3(gray), 0.3); // moderate desaturation (30%)
}

vec3 warmTint(vec3 color) {
    return color * vec3(1.05, 0.98, 0.92); // gentle warmth for paper effect
}

void main() {
    vec2 uv = v_texcoord;
    vec3 color = texture2D(tex, uv).rgb;

    // Slight desaturation for paper tone
    color = paperTone(color);

    // Apply warm paper-like tint
    color = warmTint(color);

    // Add subtle paper-like grain
    color += grain(uv);
    color += grain(uv);
    color += grain(uv);
    color += grain(uv);
    color += grain(uv);

    // Apply soft vignette for natural edge shadowing
    float vign = vignette(uv);
    // color *= vign;

    gl_FragColor = vec4(color, 1.0);
}

