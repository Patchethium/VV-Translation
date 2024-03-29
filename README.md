# VV-Translation helper

This is a simple web app to help you translate VOICEVOX or any other software that uses the same format for translation files.

## How to use

The quickest way is to enter the website and click "Start from Template" and you're good to go.

After you finished your translation or want to save your progress, click "Export" button on the top right corner to download the translation file.

You can clice "Choose a File" to load a translation file and continue your work.

#### Translate other software

Prepare a translation file that looks like the [template](src/routes/assets/template.json) and load it in the website.

There is a brief script I use to gather the untranslated strings from VOICEVOX [here](scripts/gather_string.py).

## Development

This project is built with [SvelteKit](https://kit.svelte.dev/).
```bash
git clone https://github.com/Patchethium/VV-Translation.git

cd VV-Translation

pnpm i

pnpm run dev -- --open
```

## Deploy

Vercel does everything and I don't know how to deploy myself. I'm spoiled.

## License

[The Unlicense](LICENSE)
