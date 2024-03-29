<svelte:head>
  <title>VV-Translation-helper</title>
</svelte:head>
<div class="main">
  <Header />
  {#if $fileText}
    <div class="flex-row">
      <SidePanel />
      <WorkSpace />
    </div>
  {:else}
    <div class="first">
      <h1>Upload a file to get started</h1>
      <input type="file" on:change={handleFileChange} />
      <h1>Or Start with a Template</h1>
      <button class="btn-primary" on:click={loadTemplate}>Load Template</button>
    </div>
  {/if}
</div>

<script lang="ts">
import '../style.css';
import SidePanel from '../lib/SidePanel.svelte';
import WorkSpace from '../lib/WorkSpace.svelte';
import Header from '../lib/Header.svelte';
import { fileText, modified } from '../store';
import * as template from '../assets/template.json';
import { onMount } from 'svelte';

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      fileText.set(reader.result as string);
    };
    reader.readAsText(file);
  }
}

function loadTemplate() {
  // type magic to to get rid of the "default" key
  fileText.set(JSON.stringify(template['default' as keyof typeof template], null, 2));
}

onMount(() => {
  // remind the user to save before leaving
  window.onbeforeunload = (e: BeforeUnloadEvent) => {
    if ($modified) {
      e.preventDefault();
      e.returnValue = '';
    }
  };
});
</script>

<style>
.first {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.main {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  overflow: hidden;
}
.flex-row {
  position: relative;
  display: flex;
  gap: 1rem;
  flex-direction: row;
  width: 100%;
  height: calc(100% - 2rem);
  left: 0;
  top: 0;
  overflow: hidden;
}
h1 {
  font-weight: bold;
  font-size: 1rem;
}

button {
  width: max-content;
}
</style>
