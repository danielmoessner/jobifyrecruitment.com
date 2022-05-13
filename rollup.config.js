import {nodeResolve} from '@rollup/plugin-node-resolve';

export default {
    input: 'static/js/input.js',
    output: {
        file: 'static/js/output.js',
        format: 'iife',
    },
    plugins: [nodeResolve()]
};