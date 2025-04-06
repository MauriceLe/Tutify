<template>

    <div class = "layout">
        <slot />
    </div>

</template>
  
  
<script>

    export default {
        name: 'Layout'
    }
  
</script>
  

<style scoped>
   
    .layout {
        display: grid;
        grid-gap: 20px;
        grid-template-columns: repeat(auto-fit, minmax(var(--module-width), var(--module-width)));
        justify-content: space-evenly;
        padding-top: 30px;
    }

</style>