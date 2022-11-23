import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)


const store = new Vuex.Store({
  plugins: [
    createPersistedState({
      key: 'vuexStore',
      storage: window.sessionStorage,
    })
  ],
  state: {
    // API_URL
    API_URL: 'http://127.0.0.1:8000',
    // auth
    token: null,
    username: null,
    user_pk: null,
    avatar: null,
    message: null,

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
      state.message = data['message']

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
      state.message = []

      // localStorage.clear();

      router.push({name: 'login'})
    },
    REFRESH_WATCHED_MOVIES(state, data) {
      state.watched_movies = data.watched_movies
    },

    // 상태메세지 변경
    UPDATE_MESSAGE(state, data) {
      state.message = data.message
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
      .catch((err) => {
        alert('아이디와 비밀번호를 다시 확인해주세요')
        console.log(err)
      })
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
      .catch((err) => {
        alert('아이디와 비밀번호를 다시 확인해주세요')
        console.log(err)
      })
      
      
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

    // 유저 정보
    getUser(context) {

      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/accounts/profile/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then(res => {
        context.commit('GET_USER', res.data)
      })
      .catch((err) => {
        console.log(err)
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

    // 팔로우 비동기
    follow(context, payload) {
      const userId = payload.userId
      console.log(userId)
      const API_URL = context.state.API_URL
      const FOLLOW_URL = `${API_URL}/api/accounts/follow/${userId}/`
      
      // 서버에도 보내고, state도 업데이트
      axios({
      method: 'post',
      url: FOLLOW_URL,
      headers: {
          Authorization: `Token ${ context.state.token }`
      }
      })
      // 이하 then() 부분의 변수명 등은 로직에 맞게 수정해주세요
      .then(() => {
        context.dispatch('getUser')
      })
    },

    // 상태 메세지 수정 요청
    updateMessage(context, payload) {
      const message = payload.message
      axios({
        method: 'PATCH',
        url: `${context.state.API_URL}/api/accounts/update_message/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
        data: {
          message
        }
      })
        .then((res) => {
          // state에 저장되어있는 상태메세지를 변경합니다. 
          context.commit('UPDATE_MESSAGE', res.data)
        })    
        .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})

export default store