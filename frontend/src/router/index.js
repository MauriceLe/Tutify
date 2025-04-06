import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue')
    },
    {
        path: '/login-user',
        name: 'Login-User',
        component: () => import('@/views/Login.vue')
    },
    {
        path: '/login-company',
        name: 'Login-Company',
        component: () => import('@/views/LoginCompany.vue')
    },
    {
        path: '/register-user',
        name: 'Register-User',
        component: () => import('@/views/Register.vue')
    },
    {
        path: '/add-kurs',
        name: 'Add-Kurs',
        component: () => import('@/views/AddKurs.vue')
    },
    {
        path: '/warenkorb',
        name: 'Warenkorb',
        component: () => import('@/views/Warenkorb.vue')
    },
    {
        path: '/profile',
        name: 'Profile',
        component: () => import('@/views/Profile.vue')
    }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

/*
router.beforeEach((to, from, next) => {
    
    const activeUser = localStorage.getItem('email')
    
    if (to.matched.some((record) => record.meta.requiresAuth) && !activeUser) {
        next('/login')
    }
    else {
        next()
    }
  
})
*/


export default router
