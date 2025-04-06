<template>

    <div class = "wrapper">
        <slot/>
    </div>

</template>
  
  
<script>

    export default {
        name: 'Wrapper'
    }
  
</script>
  

<style scoped>
   
    .wrapper {
        padding: 0 var(--layout-padding);
    }

    @media (max-width:1150px) { 
        .wrapper {
            padding: 0 10px;
        }
    }

</style>