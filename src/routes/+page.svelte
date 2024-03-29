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
      <button on:click={loadTemplate}>Load Template</button>
    </div>
  {/if}
</div>

<script lang="ts">
import './reset.css';
import SidePanel from './libs/SidePanel.svelte';
import WorkSpace from './libs/WorkSpace.svelte';
import Header from './libs/Header.svelte';
import { fileText } from './store';
import * as template from './assets/template.json';

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
  fileText.set(JSON.stringify(template["default" as keyof typeof template], null, 2));
}
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
  width: max-content
}
</style>
