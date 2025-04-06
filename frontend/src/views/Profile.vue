<template>

    <Wrapper>

        <Navbar/>

        <Layout>
            <Kurs v-for = "kurs in kurse" :kurs = "kurs" :key = "kurs[0]"/>
        </Layout>
        
    </Wrapper>

</template>
  
  
<script>

    import axios from 'axios'

    import Wrapper from '@/components/Wrapper.vue'
    import Layout from '@/components/Layout.vue'
    import Navbar from '@/components/Navbar.vue'
    import Kurs from '@/components/Kurs.vue'
  
    export default {
        name: 'Profile',
        components: {
            Wrapper,
            Layout,
            Navbar,
            Kurs
        },
        data() {
            return {
                kurse: []
            }
        },
        created() {
            
            axios.get("http://127.0.0.1:8000/kurs/subscribed/" + localStorage.getItem("kundenID"))
            .then(response => this.kurse = response.data)

        }
    }
  
</script>
  

<style scoped>
</style>