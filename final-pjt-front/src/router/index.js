import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
// import HomeView from '../views/HomeView.vue'
// import LoginView from '../views/LoginView.vue'
// import SignupView from '../views/SignupView.vue'

Vue.use(VueRouter)



// const isLoggedIn = store.getters.isLoggedIn

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue'),
    beforeEnter: (to, from, next) => {
      const isLoggedIn = store.getters.isLoggedIn

      if (isLoggedIn === true) {
        // console.log('이미 로그인')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignupView.vue')
  },
  {
    path: '/first-addMovie',
    name: 'first-addMovie',
    component: () => import('../views/FirstAddMovieView.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: () => import('../views/SearchView.vue')
  },
  {
    path: '/movie/:id',
    name: 'movieDetail',
    component: () => import('../views/MovieDetail.vue')
  },
  {
    path: '/game/:gameName',
    name: 'game',
    component: () => import('../views/GameView.vue')
  },
  {
    path: '/reviewCreate/:movieId',
    name: 'reviewCreate',
    component: () => import('../views/ReviewCreateView.vue')
  },
  // {
  //   path: '/browse',
  //   name: 'browse',
  //   component: () => import('../views/BrowseView.vue')
  // },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLoggedIn

  const allowAllPages = ['login']

  //이동할 페이지(to)가 로그인이 필요한 사이트인지 확인
  const isAuthRequired = !allowAllPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
