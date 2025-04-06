<template>

    <button class = "btn"> 
        {{ title }}
    </button>

</template>


<script>

    export default {
        name: 'Button',
        props: ['title']
    }

</script>


<style scoped>

    .btn {
        font-family: var(--font);
        font-size: 15px;
        font-weight: 400;
        color: var(--font-primary);
        background: var(--button-primary);
        cursor: pointer;
    }

    .btn:hover {
        transition: 0.2s all;
        border: 3px solid var(--button-primary);
        background: var(--button-secondary);
    }

</style>
