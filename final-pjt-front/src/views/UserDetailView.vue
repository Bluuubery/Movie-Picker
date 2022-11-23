<template>
  <div class="UserDetail">
  <!-- <input type="file" @change="uploadAvatar"> -->
    <div class="header">
      <div class="user-info">
        <div class="user-info__img" :style="`background-image: url(${this.$store.state.API_URL}${this.$store.state.avatar})`">
  
        </div>
        <div class="user-info__text">
          <h1 class="user-info__text__username">{{ this.username }}</h1>
          <div class="user-info__text__sub">
            <p>팔로워 <span>541</span></p>
            <p>팔로잉 <span>200</span></p>
          </div>
        </div>
      </div>
    </div>
    <div class="wrapper">
      <div class="movies">
        <div class="link">
          <div @click.prevent="switchTab($event)" id="tab_button" class="link__button active" data-tab="watched">
            <h3 data-tab="watched">봤어요</h3>
            <div id="link-active" class="link__button__line active-line"></div>
          </div>
          <div @click.prevent="switchTab($event)" id="tab_button" class="link__button" data-tab="toWatch">
            <h3 data-tab="toWatch">보고싶어요</h3>
            <div id="link-active" class="link__button__line"></div>
          </div>
        </div>
        <div class="movies__list">
          <MovieItem v-for="(movie, key) in movies" :key="key" :movie="movie"/>
        </div>
      </div>
      <div class="records">
        <div class="records__title">
          <h3>내가 쓴 코멘트</h3>
        </div>
        <div class="records__list">
          <UserReviewItem v-for="(review, key) in reviews" :key="key" :review="review"/>
        </div>
      </div>
    </div>
    <MovieItem/>
  </div>
</template>

<script>
import axios from "axios";
import MovieItem from '@/components/MovieItem.vue';
import UserReviewItem from '@/components/UserReviewItem.vue';


export default {
  name: "UserDetailView",
  components: {
    MovieItem,
    UserReviewItem,
  },
  data() {
    return {
      user_pk: this.$route.params.userId,
      username: null,

      watched_movies: [],
      to_watch_movies: [],
      best_movie: null,

      // tab에 보여질 영화들
      movies: [],

      reviews: [],
    };
  },

  created() {
    this.getMovies()
    this.getReviews()
  },
  
  mounted() {
    // this.setHeaderImg()
  },

  methods: {
    setHeaderImg() {
      
      if (this.best_movie) {
        console.log('here')
        document.querySelector('.header').style.backgroundImage = `linear-gradient(to bottom, rgba(20, 18, 23, 1), rgba(20, 18, 23, 0.8)), url(https://image.tmdb.org/t/p/original/${this.best_movie.movie.backdrop_path})`
      } else {
        document.querySelector('.header').style.backgroundImage = `linear-gradient(to bottom, rgba(20, 18, 23, 1), rgba(20, 18, 23, 0.8)), url(${'@/assets/img/default_user_backdrop.jpg'})`

      }
    },
    getMovies() {
      const API_URL = this.$store.state.API_URL;
      // watched
      axios({
        method: "get",
        url: `${API_URL}/api/accounts/${this.user_pk}/watched/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        // console.log(res.data)
        this.watched_movies = res.data.watched_movies
        this.movies = this.watched_movies
      })
      // .catch((err) => console.log(err))
      
      // to watch
      axios({
        method: "get",
        url: `${API_URL}/api/accounts/${this.user_pk}/to_watch/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log(res.data)
        this.to_watch_movies = res.data.to_watch_movies
      })
      // .catch((err) => console.log(err))
      
      // best movie
      axios({
        method: "get",
        url: `${API_URL}/api/accounts/${this.user_pk}/best/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log('best_movie', res.data)
        const all_best_movies = res.data
        this.best_movie = all_best_movies[all_best_movies.length - 1]
        this.setHeaderImg()
      })
      .catch((err) => console.log('best movie',err))
    },

    // 내가 쓴 리뷰 받아오기
    getReviews() {
      const API_URL = this.$store.state.API_URL;
      axios({
        method: "get",
        url: `${API_URL}/api/articles/${this.user_pk}/review_user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        this.reviews = res.data;
        console.log(res.data)
      })
      .catch((err) => console.log(err))
    },

    // tab 바꾸기
    switchTab(event) {
      const tabId = event.currentTarget.dataset.tab
      const tab_contents = document.querySelectorAll('#tab_content')
      const tab_buttons = document.querySelectorAll('#tab_button')
      
      tab_contents.forEach((tab) => {
        if (tab.dataset.tab === tabId) {
          tab.classList.remove('hidden')
        } else {
          tab.classList.add('hidden')
        }
      })
      tab_buttons.forEach((btn) => {
        const line = btn.querySelector('div')
        if (btn.dataset.tab === tabId) {
          btn.classList.add('active')
          line.classList.add('active-line')
        } else {
          btn.classList.remove('active')
          line.classList.remove('active-line')
        }
      })

      // movies 바꾸기
      if (tabId === 'watched') this.movies = this.watched_movies
      else this.movies = this.to_watch_movies
    },

    // 다른 유저의 정보 가져오기(id, username, message, avatar, followings, followers)
    getOtherUser() {
      const API_URL = this.$store.state.API_URL;
      const otherUserPk = 6 // 임시로 설정한 다른 유저의 pk 값입니다. 이후 적절한 데이터로 수정해주세요
      axios({
        method: "get",
        url: `${API_URL}/api/accounts/accounts/get_profile/${otherUserPk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        console.log(res.data) // 확인용 콘솔 로그입니다.
        // ??? = res.data     // 이후 요청받은 데이터를 적절하게 활용해주세요
        // 데이터는 아래와 같은 형태로 주어집니다. (otherUserPk로 요청한 값)
        // {
            // "id": 6,
            // "followers": [
                // 2
            // ],
            // "username": "eunsung",
            // "message": null,
            // "avatar": "/images/default_avatar_2.svg",
            // "followings": [
                // 2,
                // 3,
                // 4
            // ]
        // }
      })
      .catch((err) => console.log(err))
    }

    // // 프사 업로드
    // uploadAvatar(event) {
    //   const formdata = new formdata()
    //   formdata.append('file')
    // }
  },
};
</script>

<style lang="scss" scoped>
@import '@/assets/scss/UserDetailView.scss';
</style>
