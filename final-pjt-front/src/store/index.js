import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

// const API_URL = 'http://127.0.0.1:8000';



const store = new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    // API_URL
    API_URL: 'http://127.0.0.1:8000',
    // auth
    token: null,
    username: null,
    user_pk: null,
    avatar: null,

    // 인생영화
    best_movie: {},
    // 모든 인생영화 기록들
    all_best_movies: [],

    // 영화 검색 기록
    search_result: [],
    // 봤어요
    watched_movies: [],
    // 보고 싶어요
    to_watch_movies: [],

    // 팔로잉
    followings: [],
    // 팔로워
    followers: [],
  },
  getters: {
    // 로그인 여부 확인
    isLoggedIn(state) {
      return state.token ? true : false
    },
    followingsCount(state) {
      return state.followings.length
    },
    followersCount(state) {
      return state.followers.length
    }
  },
  mutations: {
    // auth
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'home'}).catch(() => {})
    },

    // best_movie(인생영화), all_best_movies(명에의 전당) 저장
    GET_USER(state, data) {
      // console.log(data)

      // 유저 정보 받아오기
      state.username = data['username']
      state.user_pk = data['id']
      state.avatar = data['avatar']

      // 본 영화랑 볼 영화 받아오기
      state.to_watch_movies = data['to_watch_movies'],
      state.watched_movies = data['watched_movies']

      // 팔로잉/팔로우 
      state.followings = data['followings']
      state.followers = data['followers']
      
      // watched_movies 없으면 first_adddMovie로 보냄
      if (!state.watched_movies.length) {
        router.push({ name: 'first-addMovie'})
      } else {
        // watched_movies가 있으면 best_movie를 저장하고 홈으로 보낸다.
        state.all_best_movies = data['best_movies']

        const idx = state.all_best_movies.map((best_movie) => best_movie.best_of_best === true).lastIndexOf(true)
        state.best_movie = state.all_best_movies[idx]
      }
    },
    SAVE_SEARCH_RESULT(state, data) {
      state.search_result = data
    },
    LOGOUT(state) {
      state.token = null
      state.username = null
      state.user_pk = null
      state.best_movie = {}
      state.all_best_movies = [],
      state.watched_movies = [],
      state.to_watch_movies = [],
      state.followings = [],
      state.followers = []

      localStorage.clear();

      router.push({name: 'login'})
    },
    REFRESH_WATCHED_MOVIES(state, data) {
      state.watched_movies = data.watched_movies
    }
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${context.state.API_URL}/dj-rest-auth/registration/`,
        data: {
          username, password1, password2
        }
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
        this.dispatch('getUser')
      })
      .catch(err => console.log(err))
    },
    // 로그인
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${context.state.API_URL}/dj-rest-auth/login/`,
        data: {
          username, password
        }
      })
      .then(res => {
        // console.log(res.data)
        context.commit('SAVE_TOKEN', res.data.key)
        this.dispatch('getUser')
      })
      .catch(err => console.log(err))
      
      // this.state.username = username
      // this.state.password = password
      
    },

    // 로그아웃
    logout(context) {
      axios({
        method: 'POST',
        url: `${context.state.API_URL}/dj-rest-auth/logout/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then(() => {
          context.commit('LOGOUT')
        })
        .catch(err => console.log(err))
    },

    test() {
      console.log('hi')
    },


    // 유저 정보
    getUser(context) {
      // console.log('here')
      // console.log(context.state)
      axios({
        method: 'get',
        // url: `${API_URL}/api/accounts/${context.state.user_pk}`,
        url: `${context.state.API_URL}/api/accounts/profile/`,
        headers: {
          // Authorization: `Token 6023611848bfca271b0de4cb5db50064289b791d`
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then(res => {
        // console.log(res)
        context.commit('GET_USER', res.data)
      })
    },

    // 리뷰 삭제 요청
    deleteReview(context, payload) {
      const reviewId = payload.reviewId
      axios({
        method: 'DELETE',
        url: `${context.state.API_URL}/api/articles/${reviewId}/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then(() => {
        return
      })    
      .catch((err) => console.log(err))
    },
    
    // 리뷰 수정 요청
    updateReview(context, payload) {
      const reviewId = payload.reviewId
      const content = payload.content
      axios({
        method: 'PUT',
        url: `${context.state.API_URL}/api/articles/${reviewId}/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
        data: {
          content
        }
      })
      .then(() => {
        return
      })    
      .catch((err) => console.log(err))
    },
  },
  modules: {
  }
})

export default store