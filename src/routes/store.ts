// store that stores the file text

import { writable, type Writable } from 'svelte/store';

export const fileText = writable('');
export const fileNames: Writable<string[]> = writable([]);
export const currentFile = writable('');
export const J: Writable<JsonType> = writable({});
// {filename: string, section}[]
// section = { neighbors: string[], text: string, translation: string}[]
export type JsonType = Record<
  string,
  Array<{
    neighbors: string[];
    text: string;
    translation: string;
  }>
>;

fileText.subscribe((value) => {
  try {
    if (value) {
      const j = JSON.parse(value);
      const keys = Object.keys(j);
      if (keys.length > 0) {
        fileNames.set(keys.toSorted());
      }
      J.set(j);
    }
  } catch (error) {
    console.log(error);
  }
});