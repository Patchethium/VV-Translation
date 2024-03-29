import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import path from 'path';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://kit.svelte.dev/docs/integrations#preprocessors
  // for more information about preprocessors
  preprocess: vitePreprocess(),
  alias: {
    $lib: path.resolve('./src/lib'),
    $store: path.resolve('./src/store'),
  },
  kit: {
    adapter: adapter()
  }
};

export default config;
