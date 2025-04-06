<template>

    <div class = "login">
    
        <h1 class = "login-text">Melde dich bei Tutify an</h1>

        <form class = "login-form" @submit.prevent="submitLogin">
           
            <input placeholder="Email" type = "email" class = "form-input" v-model = "email">

            <input placeholder="Passwort" type = "password" class = "form-input" v-model = "password">

            <Button :title = "'Login'" type = "submit"/>

        </form>

        <router-link to = "/register-user">
            <h1 class = "register-text">Noch kein Konto? Regristrieren</h1>
        </router-link>

    </div>

</template>
  
  
<script>
  
    import axios from 'axios'
    import Button from '@/components/Button.vue'

    export default {
        name: 'Login',
        components: {
            Button
        },
        data() {
            return {
                email: '',
                password: ''
            }
        },
        methods: {
            submitLogin() {
                axios.post("http://127.0.0.1:8000/account/login", {
                    "EMail": this.email,
                    "Passwort": this.password
                }).then(response => {
                    localStorage.setItem("email", this.email)
                    localStorage.setItem("password", this.password)
                    localStorage.setItem("id", response.data[0][0])
                    localStorage.setItem("type", "user")
                    localStorage.setItem("kundenID", response.data[0][2])
                    this.$router.push("/");
                })
            }
        }
    }    
  
</script>
  

<style scoped>

    .login {
        position: relative;
        max-width: 450px;
        padding: 20px;
        margin: 100px auto;
        background: var(--background-secondary);
        border-radius: 5px;
    }
   
    .login-text {
        font-family: var(--font);
        color: var(--font-primary);
        font-size: 25px;
        text-align: center;
        margin-bottom: 20px;
    }

    .login-form {
        display: grid;
        grid-template-rows:50px 50px 30px;
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

    .register-text {
        font-family: var(--font);
        font-size: 15px;
        font-weight: 300;
        color: var(--button-primary);
        cursor: pointer;
        text-align: center;
        margin-top: 20px;
    }

</style>