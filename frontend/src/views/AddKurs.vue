<template>

    <Wrapper>

        <Navbar/>

        <form class = "login-form" @submit.prevent="addKurs">
           
            <input placeholder="Name" type = "text" class = "form-input" v-model = "name">

            <input placeholder="Datum" type = "date" class = "form-input" >

            <input placeholder="Preis" type = "number" class = "form-input" v-model = "preis">

            <input placeholder="Klasse" type = "text" class = "form-input" v-model = "klasse">

            <input placeholder="Verfügbarkeit" type = "text" class = "form-input" v-model = "verfügbarkeit">

            <Button :title = "'Hinzufügen'" type = "submit"/>

        </form>
        
    </Wrapper>

</template>
  
  
<script>

    import axios from 'axios'

    import Wrapper from '@/components/Wrapper.vue'
    import Layout from '@/components/Layout.vue'
    import Navbar from '@/components/Navbar.vue'
    import Button from '@/components/Button.vue'
  
    export default {
        name: 'Add-Kurs',
        components: {
            Wrapper,
            Layout,
            Navbar,
            Button
        },
        data() {
            return {
                name: '',
                datum: '01-01-2001',
                preis: '',
                klasse: '',
                verfügbarkeit: ''
            }
        },
        methods: {
            addKurs() {

                axios.post("http://127.0.0.1:8000/kurs/", {
                    "ID_FACHBEREICH": "1",
                    "NAME": this.name,
                    "DATUM": this.datum,
                    "PREIS": this.preis,
                    "KLASSE": this.klasse,
                    "VERFUGBARKEIT": this.verfügbarkeit
                }).then(response => {
                    this.$router.push("/");
                })

            }
        }
    }
  
</script>
  

<style scoped>

    .login-form {
        display: grid;
        grid-template-rows:50px 50px 50px 50px 50px 30px;
        grid-gap: 15px;
    }

    .form-input {
        padding: 15px;
        background: #3E3E3E;
    }

    .form-input, .form-input::placeholder {
        font-family: var(--font);
        color: var(--font-primary);
        font-size: 15px;
    }

</style>