<template>
    <router-view />
</template>

<script>
 
    export default {
        name: 'App'
    }

</script>

<style>

    button, input { border: none; }
    input { background: transparent; }
    input:focus, select:focus { outline: none; }
    a { text-decoration: none; }

    * {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
    }

    body {
        background-color: var(--background-primary);
    }

    :root {
        --background-primary: #171717;
        --background-secondary: #282828;
        --button-primary: #00A7FF;
        --button-secondary: #424242;
        --layout-padding: 10rem;
        --navbar-height: 100px;
        --module-width: 400px;
        --font: Roboto;
        --font-primary: #ffffff;
        --font-secondary: #B8B8B8;
    }

</style>
