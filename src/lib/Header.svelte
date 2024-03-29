<div class="root">
  <h1>{title()}</h1>
  <div class="space" />
  <!-- Github link -->
  <button class="btn">
    <a href="https://github.com/Patchethium/VV-Translation.git" target="_blank"> Github </a>
  </button>
  {#if $fileText}
    <button class="btn-primary" on:click={exportFile}>Export File</button>
  {/if}
  <div class="space-small" />
</div>

<script lang="ts">
import '../style.css';
import { fileText, J, modified, currentFile } from '../store';
function exportFile() {
  console.log('Exporting file');
  // exports the J into a file
  const data = JSON.stringify($J, null, 2);
  const blob = new Blob([data], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'translation.json';
  a.click();
  URL.revokeObjectURL(url);
  modified.set(false); // reset the modified flag since they just saved
}

$: title = () => {
  if ($currentFile) {
    return `Translation Support / ${$currentFile}`;
  } else {
    return 'Translation Support';
  }
};
</script>

<style>
.root {
  width: 100%;
  height: 1rem;
  padding: 1rem 0;
  display: flex;
  flex-direction: row;
  border-bottom: solid 2px #f0f0f0;
  justify-content: center;
  align-items: center;
}
h1 {
  font-weight: bold;
  font-weight: bold;
  margin-left: 2rem;
}

.space {
  flex-grow: 1;
}

a {
  text-decoration: none;
  color: #000000;
}

.btn {
  text-decoration: none;
  color: #000000;
  width: auto;
  height: auto;
  margin-right: 1rem;
  border: none;
  outline: none;
  background-color: #ffffff;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 0.5rem;
}

.btn:hover {
  background-color: #f0f0f0;
}

.btn:active {
  background-color: #e0e0e0;
}

.space-small {
  width: 1.5rem;
}
</style>
