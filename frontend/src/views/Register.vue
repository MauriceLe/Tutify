<template>

    <div class = "register">
    
        <h1 class = "register-text">Registriere dich bei Tutify</h1>

        <form class = "register-form" @submit.prevent="submitRegister">
           
            <input placeholder="Vorname" type = "text" class = "form-input" v-model = "vorname">

            <input placeholder="Nachname" type = "text" class = "form-input" v-model = "nachname">

            <input placeholder="Email" type = "email" class = "form-input" v-model = "email">

            <input placeholder="Telefon-Nr" type = "text" class = "form-input" v-model = "telefon">

            <input placeholder="Geburtstag" type = "date" class = "form-input">

            <input placeholder="Plz" type = "text" class = "form-input" v-model = "plz">

            <input placeholder="Straße" type = "text" class = "form-input" v-model = "strasse">

            <input placeholder="Hausnummer" type = "text" class = "form-input" v-model = "hausnummer">

            <input placeholder="Passwort" type = "password" class = "form-input" v-model = "password">

            <input placeholder="Passwort wiederholen" type = "password" class = "form-input" v-model = "password_submit">

            <Button :title = "'Register'" type= "submit" />

        </form>

        <router-link to = "/login-user">
            <h1 class = "login-text">User-Login</h1>
        </router-link>

        <router-link to = "/login-company">
            <h1 class = "login-text">Company-Login</h1>
        </router-link>
        
    </div>

</template>
  
  
<script>
    
    import axios from 'axios'
    import Button from '@/components/Button.vue'

    export default {
        name: 'Register',
        components: {
            Button
        },
        data() {
            return {
                vorname: '',
                nachname: '',
                email: '',
                telefon: '',
                geburtstag: '01-01-2001',
                plz: '',
                strasse: '',
                hausnummer: '',
                password: '',
                password_submit: ''
            }
        },
        methods: {
            submitRegister() {  
                
                if (this.password == this.password_submit) {

                    var kunde;

                    kunde = axios.post("http://127.0.0.1:8000/kunde/", {
                        "PLZ": this.plz,
                        "Nachname": this.nachname,
                        "Vorname": this.vorname,
                        "E_Mail": this.email,
                        "Telefon": this.telefon,
                        "Geburtstag": this.geburtstag,
                        "Strasse": this.strasse,
                        "Hausnummer": this.hausnummer
                    }).then(response => {
                      
                        axios.post("http://127.0.0.1:8000/account/register", {
                            "EMail": this.email,
                            "Passwort": this.password,
                            "ID_Kunde": response.data[0][0]
                        })

                        localStorage.setItem("email", this.email)
                        localStorage.setItem("password", this.password)
                        localStorage.setItem("id", response.data[0][0])
                        localStorage.setItem("type", "user")

                        this.$router.push("/");
                    })

                }

            }
        }
    }    
  
</script>
  

<style scoped>

    .register {
        position: relative;
        max-width: 450px;
        padding: 20px;
        margin: 100px auto;
        background: var(--background-secondary);
        border-radius: 5px;
    }
   
    .register-text {
        font-family: var(--font);
        color: var(--font-primary);
        font-size: 25px;
        text-align: center;
        margin-bottom: 20px;
    }

    .register-form {
        display: grid;
        grid-template-rows:50px 50px 50px 50px 50px 50px 50px 50px 50px 50px 30px;
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

    .login-text {
        font-family: var(--font);
        font-size: 15px;
        font-weight: 300;
        color: var(--button-primary);
        cursor: pointer;
        text-align: center;
        margin-top: 20px;
    }

</style>