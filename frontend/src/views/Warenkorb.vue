<template>

    <Wrapper>

        <Navbar/>

        <Layout>

        </Layout>
        <div class = "container">
            <Button :title = "'Kaufen'"/>
        </div>

    </Wrapper>

</template>
  
  
<script>

    import axios from 'axios'

    import Wrapper from '@/components/Wrapper.vue'
    import Layout from '@/components/Layout.vue'
    import Navbar from '@/components/Navbar.vue'
    import Button from '@/components/Button.vue'

    export default {
        name: 'Warenkorb',
        components: {
            Wrapper,
            Layout,
            Navbar,
            Button
        },
        data() {
            return {
                kurse: []
            }
        },
        created() {

        }
    }
  
</script>
  

<style scoped>

    .container {
        display: grid;
        grid-template-rows: 40px;
    }

</style>