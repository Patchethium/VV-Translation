<main>
  {#if sections}
    <div class="flex-row">
      <div class="title">{$currentFile}</div>
      <div class="space" />
      <button class="mark-btn" on:click={ignore_file}>Ignore File</button>
    </div>
    {#each sections as section, i}
      <section class="line-numbers">
        <div>
          <Prism language={language} source={join("\n", section.neighbors)} />
        </div>
        <h1>Original</h1>
        <h2 class="text">
          {section.text}
        </h2>
        <h1>
          Translation
          <button
            class="mark-btn"
            on:click={() => {
              mark_as_comment(i);
            }}>Mark as comment</button
          >
        </h1>
        <input
          class="translation"
          type="text"
          on:change={(e) => {
            update_translation(e, i);
          }}
          bind:value={section.translation}
        />
      </section>
    {/each}
  {/if}
</main>
<svelte:head>
  <link
    href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.22.0/themes/prism.min.css"
    rel="stylesheet"
  />
</svelte:head>

<script lang="ts">
import { J, currentFile, modified } from '../store';
import Prism from 'svelte-prism';
$: sections = $J[$currentFile];
$: language = $currentFile.split('.').pop() == 'ts' ? 'javascript' : 'html';

function join(str: string, arr: string[]) {
  const joined = arr.join(str);
  return joined;
}

function update_translation(e: Event, i: number) {
  const target = e.target as HTMLInputElement;
  const value = target.value;
  $J[$currentFile][i].translation = value;
  modified.set(true);
}

function mark_as_comment(i: number) {
  $J[$currentFile][i].translation = '//';
}

function ignore_file() {
  // this ignores the file by marking every translation as a comment
  let section = $J[$currentFile];
  section.forEach((s) => {
    s.translation = '//';
  });
  $J[$currentFile] = section;
}
</script>

<style>
/* Hey I think I just invented tailwindcss */
.flex-row {
  display: flex;
  flex-direction: row;
  align-items: center;
}
section {
  margin-bottom: 1rem;
  border: solid 1px #f0f0f0;
  padding: 0.5rem;
}
/** scrollable to prevent overflow */
main {
  overflow-y: auto;
  height: auto;
  width: 100%;
  display: relative;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
}

.text {
  padding: 0.5rem 0;
}

h1 {
  font-weight: bold;
  margin: 0.5rem 0;
}

.translation {
  width: 75%;
  padding: 0.5rem;
  border: solid 1px;
  border-radius: 0.25rem;
  outline: none;
  border-color: #f0f0f0;
  flex: 1 1 0%;
}

.translation:focus {
  border-color: #000000;
}

.title {
  font-size: 2rem;
  font-weight: bold;
  margin: 1rem 0;
}
.mark-btn {
  padding: 0.5rem;
  border-radius: 0.25rem;
  background-color: #f0f0f0;
  border: none;
  cursor: pointer;
  height: min-content;
}
.mark-btn:hover {
  background-color: #e0e0e0;
}

.mark-btn:active {
  background-color: #d0d0d0;
}

.space {
  width: 1rem;
}
</style>
