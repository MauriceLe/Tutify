<template>

    <div class = "kurs">

        <div class = "header">
            <span class = "header-text"> {{ kurs[2] }} </span>
        </div>

        <div class = "info">
            <span class = "info-text">Verfügbarkeit</span>
            <span class = "info-link"> {{kurs[6]}} </span>
        </div>

        <div class = "info">
            <span class = "info-text">Preis</span>
            <span class = "info-text"> {{kurs[5]}} Euro</span>
        </div>

        <Button :title = "'Anmelden'" @click = "submitKurs"/>

    </div>

</template>


<script>

    import axios from 'axios'
    import Button from '@/components/Button.vue'

    export default {
        name: 'Kurs',
        props: ['kurs'],
        components: {
            Button
        },
        methods: {
            submitKurs() {

                axios.post("http://127.0.0.1:8000/kurs/subscribe/" + this.kurs[0]+ "?userid=" +localStorage.getItem("kundenID"));

            }   
        }
    }

</script>


<style scoped>

    .kurs {
        width: 400px;
        height: 220px;
        background: var(--background-secondary);
        padding: 15px;
        display: grid;
        grid-template-rows: 40px 40px 40px 35px;
        grid-gap: 10px;
    }

    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: solid #6C6C6C 1px;
    }

    .header-text {
        font-family: var(--font);
        color: var(--font-primary);
        font-size: 22px;
        font-weight: 500;
        overflow: hidden;
    }

    .info {
        display: grid;
        grid-template-columns: 170px auto;
    }

    .info-text {
        font-family: var(--font);
        color: var(--font-secondary);
        font-size: 20px;
        overflow: hidden;
    }

    .info-link {
        font-family: var(--font);
        color: #00A7FF;
        font-size:20px;
        overflow: hidden;
    }

</style>
