<!-- The clickable list for the users to choose which file to view -->
<div class="sidepanel">
  <!-- a scrollable list of file names -->
  {#each $fileNames as fileName}
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div
      class={$currentFile != fileName ? 'clickable' : 'selected'}
      on:click={() => currentFile.set(fileName)}
    >
      {fileName}
    </div>
  {/each}
</div>

<script lang="ts">
import { fileNames, currentFile } from '../store';
</script>

<style>
.clickable {
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 0.25rem;
}

.clickable:hover {
  background-color: #f0f0f0;
}

.clickable:active {
  background-color: #e0e0e0;
}

.sidepanel {
  top: 0;
  left: 0;
  bottom: 0;
  width: auto;
  height: auto;
  background-color: #ffffff;
  overflow-y: auto;
  padding: 1rem;
}
.selected {
  background-color: #f0f0f0;
  padding: 0.5rem;
  border-radius: 0.25rem;
  cursor: pointer;
}
</style>
