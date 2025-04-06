<template>

    <Wrapper>

        <Navbar/>

        <Layout>
            <Kurs v-for = "kurs in kurse" :kurs = "kurs" :key = "kurs[3]"/>
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
        name: 'Home',
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
        async created() {
            
            await axios.get("http://127.0.0.1:8000/kurs/")
            .then(response => this.kurse = response.data);

            console.log(this.kurse)
        }
    }
  
</script>
  

<style scoped>
</style>