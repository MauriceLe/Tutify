<template>

  	<div class = "navbar" >   

      	<router-link class = "logo" to = "/">
        	Tutify
      	</router-link>

    	<div class = "nav">
			<img v-if = "type == 'user'" src = "@/assets/icons/account.svg" class = "nav-item" @click = "toProfile">
			<img v-if = "type == 'company'" src = "@/assets/icons/add.svg" class = "nav-item" @click = "toAddKurs">
			<img src = "@/assets/icons/logout.svg" class = "nav-item" @click = "toLogin"> 
    	</div>

  	</div>

</template>


<script>

  	export default {
    	name: 'Navbar',
		methods: {
			toLogin() {
				localStorage.removeItem("email");
				localStorage.removeItem("password");
				localStorage.removeItem("type");
				localStorage.removeItem("id");
				this.$router.push("/login-user");
			},
			toAddKurs() {
				this.$router.push("/add-kurs");
			},
			toWarenkorb() {
				this.$router.push("/warenkorb");
			},
			toProfile() {
				this.$router.push("/profile");
			},
			toFiliale() {
				this.$router.push("/filiale");
			}
		},
		data() {
			return {
				type: localStorage.getItem("type")
			}
		}
  	}

</script>


<style scoped>
  
  	.navbar {
    	height: var(--navbar-height); 
    	display: flex;
    	align-items: center;
    	justify-content: space-between;
  	}

  	.logo {
		font-family: var(--font);
		font-size: 37.5px;
		font-weight: 900;
		color: var(--font-primary);
  	}

  	.nav {
    	display: grid;
    	grid-template-columns: auto auto auto auto;
    	grid-gap: 10px;
  	}

  	.nav-item {
    	width: 45px;
    	height: 45px;
    	border-radius: 100%;
		object-fit: cover;
    	background: var(--background-secondary);
    	cursor: pointer;
  	}

	.nav-item:hover {
		transition: 0.5s background;
		background: var(--button-secondary);
	}

	@media (max-width: 680px) { 
        .navbar {
            flex-direction: column;
			margin-bottom: 30px;
        }
    }

	@media (max-width: 500px) { 
		.navbar {
			height: auto;
		}

		.logo {
			margin-bottom: 10px;
		}

        .nav {
			grid-template-columns: auto;
			grid-template-rows: 45px 45px 45px;
        }

		.nav-item {
			margin: 0 auto;
		}
    }

</style>
